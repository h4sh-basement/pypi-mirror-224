###############################################################################
# (c) Copyright 2022 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
"""Run a local test job for based on a production request YAML specification"""
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from textwrap import dedent
from typing import Optional

import yaml

from DIRAC import gLogger
from DIRAC.ConfigurationSystem.Client.Helpers import CSGlobals
from DIRAC.Core.Base.Script import Script
from DIRAC.Core.Utilities.ReturnValues import returnValueOrRaise, convertToReturnValue
from LHCbDIRAC.ProductionManagementSystem.Utilities.Models import (
    parse_obj,
    ProductionBase,
    SimulationProduction,
    DataProduction,
    ProductionStep,
)


def parseArgs():
    useCfgOverride = True
    inputFiles = None
    inputFileType = None

    @convertToReturnValue
    def disableCfgOverride(_):
        nonlocal useCfgOverride
        useCfgOverride = False

    @convertToReturnValue
    def setInputFiles(s: str):
        nonlocal inputFiles
        inputFiles = s.split(",")

    @convertToReturnValue
    def setOutputFileType(s: str):
        nonlocal inputFileType
        inputFileType = s

    switches = [
        ("", "input-files=", "Comma separated list of input files (Data only)", setInputFiles),
        ("", "no-cfg-override", "Internal implementation detail", disableCfgOverride),
        ("", "input-file-type=", "Limit the file type for generic merge steps", setOutputFileType),
    ]
    Script.registerSwitches(switches)
    Script.registerArgument("yaml_path: Path to the YAML file containing productions to submit")
    Script.registerArgument("name: Name of the production to submit", mandatory=False)
    Script.registerArgument("event_type: The event type to generate (Simulation only)", mandatory=False)
    Script.parseCommandLine(ignoreErrors=False)
    yaml_path, name, eventType = Script.getPositionalArgs(group=True)

    from DIRAC.ConfigurationSystem.Client.ConfigurationClient import ConfigurationClient

    if not ConfigurationClient().ping()["OK"]:
        gLogger.fatal("Failed to contact CS, do you have a valid proxy?")
        sys.exit(1)

    return Path(yaml_path), name, eventType, inputFiles, useCfgOverride, inputFileType


def _runWithConfigOverride(argv):
    """Relaunch the process with DIRACSYSCONFIG overridden for local tests"""
    cfg_content = f"""
    DIRAC
    {{
        Setup={CSGlobals.getSetup()}
    }}
    LocalSite
    {{
        Site = DIRAC.LocalProdTest.local
        GridCE = jenkins.cern.ch
        CEQueue = jenkins-queue_not_important
        LocalSE = CERN-DST-EOS
        LocalSE += CERN-HIST-EOS
        LocalSE += CERN-RAW
        LocalSE += CERN-FREEZER-EOS
        LocalSE += CERN-SWTEST
        Architecture = x86_64-centos7
        SharedArea = /cvmfs/lhcb.cern.ch/lib
        CPUTimeLeft = 123456
    }}
    """
    with tempfile.NamedTemporaryFile(mode="wt") as tmp:
        tmp.write(dedent(cfg_content))
        tmp.flush()

        env = dict(os.environ)
        env["DIRACSYSCONFIG"] = ",".join([tmp.name] + env.get("DIRACSYSCONFIG", "").split(","))

        gLogger.always("Overriding DIRACSYSCONFIG to", env["DIRACSYSCONFIG"])
        gLogger.always("Restarting process with", argv)
        proc = subprocess.run(argv, env=env, check=False)
    sys.exit(proc.returncode)


@Script()
def main():
    yamlPath, name, eventType, inputFiles, useCfgOverride, inputFileType = parseArgs()

    if useCfgOverride:
        return _runWithConfigOverride(sys.argv + ["--no-cfg-override"])

    productionRequests = defaultdict(list)
    for spec in yaml.safe_load(yamlPath.read_text()):
        productionRequest = parse_obj(spec)
        productionRequests[productionRequest.name] += [productionRequest]

    if name is None:
        if len(productionRequests) == 1:
            name = list(productionRequests)[0]
        else:
            gLogger.fatal(
                "Multiple production requests available, please specify a name. Available options are:\n",
                "   * " + "\n    * ".join(map(shlex.quote, productionRequests)),
            )
            sys.exit(1)
    if name not in productionRequests:
        gLogger.fatal(
            "Unrecognised production request name. Available options are:\n",
            "   * " + "\n    * ".join(map(shlex.quote, productionRequests)),
        )
        sys.exit(1)
    if len(productionRequests[name]) > 1:
        gLogger.fatal("Ambiguous production requests found with identical names", shlex.quote(name))
        sys.exit(1)
    productionRequest = productionRequests[name][0]

    numTestEvents = None
    if isinstance(productionRequest, SimulationProduction):
        availableEventTypes = {e.id: e.num_test_events for e in productionRequest.event_types}
        if eventType is None and isinstance(productionRequest, SimulationProduction):
            if len(productionRequest.event_types) == 1:
                eventType = productionRequest.event_types[0].id
            else:
                gLogger.fatal(
                    "Multiple event types available, please specify a one.\nAvailable options are:\n",
                    "   * " + "\n    * ".join(availableEventTypes),
                )
                sys.exit(1)
        if eventType not in availableEventTypes:
            gLogger.fatal(f"Invalid event type passed ({eventType}), available options are: {availableEventTypes!r}")
            sys.exit(1)
        numTestEvents = availableEventTypes[eventType]
    elif eventType is not None:
        gLogger.fatal(f"{eventType!r} but this is not a simulation production!")
        sys.exit(1)

    testProductionRequest(
        productionRequest,
        eventType=eventType,
        numTestEvents=numTestEvents,
        inputFiles=inputFiles,
        inputFileType=inputFileType,
    )


def testProductionRequest(
    productionRequest: ProductionBase,
    *,
    eventType: str | None = None,
    numTestEvents: int = 10,
    inputFiles: list[str] | None = None,
    inputFileType: str | None = None,
):
    from LHCbDIRAC.ProductionManagementSystem.Utilities.ModelCompatibility import production_to_legacy_dict
    from LHCbDIRAC.ProductionManagementSystem.Client.ProductionRequest import ProductionRequest

    pr = ProductionRequest()
    kwargs = {}
    legacy_dict, _ = production_to_legacy_dict(productionRequest)
    pr.prodGroup = json.loads(legacy_dict["ProDetail"])["pDsc"]
    if isinstance(productionRequest, SimulationProduction):
        pr.configName = "MC"
        pr.configVersion = productionRequest.mc_config_version
        pr.dataTakingConditions = productionRequest.sim_condition
        pr.eventType = eventType

        kwargs |= dict(
            events=numTestEvents,
            multicore=False,
            prodType="MCSimulation" if productionRequest.fast_simulation_type == "None" else "MCFastSimulation",
        )
    elif isinstance(productionRequest, DataProduction):
        if not inputFiles:
            raise ValueError("No input files specified")

        kwargs |= dict(
            inputDataList=inputFiles,
            prodType=productionRequest.type,
            inputDataPolicy="download",
        )
    else:
        raise NotImplementedError(type(productionRequest))

    pr.outConfigName = "validation"
    pr.outputSEs = ["Tier1-Buffer"]

    stepsInProd = _steps_to_production_dict(productionRequest.steps, inputFileType)
    outputSE = {t["FileType"]: "Tier1-Buffer" for step in stepsInProd for t in step["visibilityFlag"]}

    # TODO: pr._buildProduction eats stepsInProd
    prod = pr._buildProduction(stepsInProd=stepsInProd, outputSE=outputSE, priority=0, cpu=100, **kwargs)

    return returnValueOrRaise(prod.runLocal())


def _steps_to_production_dict(steps: list[ProductionStep], inputFileType: str | None) -> list[dict]:
    """Convert steps into list of dictionaries expected by ProductionRequest._buildProduction

    Normally this is handled by ProductionRequest.resolveSteps however this only
    supports reading from the bookkeeping.

    TODO: The ProductionRequest class should be refactored.
    """
    from LHCbDIRAC.ProductionManagementSystem.Utilities.ModelCompatibility import step_to_step_manager_dict

    stepsInProd = []
    for i, dirac_step in enumerate(steps):
        result = step_to_step_manager_dict(i + 1, dirac_step)
        step_dict = result["Step"]
        step_dict["StepId"] = step_dict.get("StepId", 12345)
        if len(dirac_step.input) > 1 and inputFileType is None:
            raise NotImplementedError(
                f"Multiple input file types found, pick one of with --input-file-type:"
                f" {' '.join(repr(f.type) for f in dirac_step.input)}"
            )
        step_dict["fileTypesIn"] = [
            f.type for f in dirac_step.input if inputFileType is None or f.type == inputFileType
        ]
        if len(dirac_step.input) > 1:
            print(f"Assuming that step {i+1} is a merging step and reducing output filetypes to {inputFileType}")
            step_dict["fileTypesOut"] = [f.type for f in dirac_step.output if f.type == inputFileType]
            if len(step_dict["fileTypesOut"]) != 1:
                raise NotImplementedError(step_dict["fileTypesOut"])
        else:
            step_dict["fileTypesOut"] = [f.type for f in dirac_step.output]
        step_dict["ExtraPackages"] = ";".join([f"{d.name}.{d.version}" for d in dirac_step.data_pkgs])
        step_dict.setdefault("OptionsFormat", "")
        step_dict.setdefault("SystemConfig", "")
        step_dict.setdefault("mcTCK", "")
        step_dict["ExtraOptions"] = ""
        step_dict["visibilityFlag"] = result["OutputFileTypes"]
        # Normally ProductionRequest.resolveSteps will set these but that only supports getting IDs from the bookkeeping
        for field in ["CONDDB", "DDDB", "DQTag"]:
            if step_dict[field] == "fromPreviousStep":
                step_dict[field] = stepsInProd[i - 1][field]
        stepsInProd.append(step_dict)
    return stepsInProd


if __name__ == "__main__":
    main()
