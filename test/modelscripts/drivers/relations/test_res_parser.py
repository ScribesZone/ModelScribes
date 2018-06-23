# coding=utf-8
from __future__ import print_function

from modelscripts.metamodels import relations
from modelscripts.scripts.megamodels.printer.megamodels import \
    MegamodelPrinter
from test.modelscripts.drivers.assertions import (
    checkAllAssertionsForDirectory,
    checkValidIssues,
)

EXPECTED_ISSUES={
}

def testGenerator_Assertions():
    res = checkAllAssertionsForDirectory(
        relTestcaseDir='res',
        extension=['.res'])

    for (file , expected_issue_map, expected_metrics_map) in res:
        yield (
            checkValidIssues,
            file,
            relations.METAMODEL,
            expected_issue_map,
            expected_metrics_map)

def testFinalMegamodel():
    MegamodelPrinter().display()