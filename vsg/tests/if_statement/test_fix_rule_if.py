import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg.tests import utils
from vsg import rule_list

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))
oFileCompress = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'if_compressed_line_test_input.vhd'))


class testFixRuleIfMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = if_statement.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = if_statement.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = if_statement.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = if_statement.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = if_statement.rule_005()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = if_statement.rule_006()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006_case(self):
        oRule = if_statement.rule_006()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = if_statement.rule_007()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = if_statement.rule_008()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008_case(self):
        oRule = if_statement.rule_008()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = if_statement.rule_009()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = if_statement.rule_010()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010_case(self):
        oRule = if_statement.rule_010()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = if_statement.rule_011()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011_case(self):
        oRule = if_statement.rule_011()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_024(self):
        oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oRule = if_statement.rule_024()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[107].line, '    if (a = 2) then')
        self.assertEqual(oFile.lines[108].line, ' b <= \'1\'; else b <= \'0\'; end if;')
        self.assertEqual(oFile.lines[108].indentLevel, oFile.lines[107].indentLevel + 1)
        self.assertFalse(oFile.lines[107].isEndIfKeyword)
        self.assertFalse(oFile.lines[107].isElseKeyword)

    def test_fix_rule_021(self):
        oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oRule = if_statement.rule_021()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[105].line, '    if (a = 2) then b <= \'1\'; ')
        self.assertEqual(oFile.lines[106].line, 'else b <= \'0\'; end if;')
        self.assertEqual(oFile.lines[106].indentLevel, oFile.lines[105].indentLevel)


    def test_fix_rule_020(self):
        oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oRule = if_statement.rule_020()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_015(self):
        oRule = if_statement.rule_015()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_022(self):
        oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oRule = if_statement.rule_022()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[102].line, '    else')
        self.assertEqual(oFile.lines[103].line, ' g <= x;')
        self.assertEqual(oFile.lines[103].indentLevel, oFile.lines[102].indentLevel + 1)

    def test_fix_compressed_line(self):
        oRuleList = rule_list.list(oFileCompress)
        oRuleList.fix()
#        utils.debug_lines(oFileCompress, 9, 10)
        self.assertEqual(oFileCompress.lines[10].line, '    if (A = \'1\' and B = \'1\') then')
        self.assertEqual(oFileCompress.lines[11].line, '      X <= \'1\';')
        self.assertEqual(oFileCompress.lines[12].line, '    elsif (C = \'0\') then')
        self.assertEqual(oFileCompress.lines[13].line, '      Y <= \'0\';')
        self.assertEqual(oFileCompress.lines[14].line, '    else')
        self.assertEqual(oFileCompress.lines[15].line, '      W <= \'0\';')

        self.assertEqual(oFileCompress.lines[18].line, '    if (A = \'1\' and B = \'1\') then')
        self.assertEqual(oFileCompress.lines[19].line, '      X <= \'1\';')
        self.assertEqual(oFileCompress.lines[20].line, '    elsif (C = \'0\') then')
        self.assertEqual(oFileCompress.lines[21].line, '      Y <= \'0\';')
        self.assertEqual(oFileCompress.lines[22].line, '    else')
        self.assertEqual(oFileCompress.lines[23].line, '      W <= \'0\';')


