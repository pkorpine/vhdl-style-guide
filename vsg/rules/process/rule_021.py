
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.token import process_statement as token

from vsg.vhdlFile import utils


class rule_021(rule.Rule):
    '''
    Checks for blank lines before the begin keyword if there are no process declarative items.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'process', '021')
        self.solution = 'Remove blank lines above begin keyword'
        self.phase = 1
        self.style = 'no_blank_line_line'
        self.configuration.append('style')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(token.process_keyword, token.begin_keyword)

    def _analyze(self, lToi):
        if self.style == 'no_blank_line':
            _analyze_no_blank_line(self, lToi)
        elif self.style == 'require_blank_line':
            _analyze_require_blank_line(self, lToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.style == 'no_blank_line':
            lTokens.reverse()
            lNewTokens = []
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.blank_line):
                    lNewTokens.pop()
                    continue
                lNewTokens.append(oToken)
            lNewTokens.reverse()
            oViolation.set_tokens(lNewTokens)
        elif self.style == 'require_blank_line':
            if isinstance(lTokens[-2], parser.whitespace):
                lTokens.insert(-3, parser.blank_line())
                lTokens.insert(-3, parser.carriage_return())
            else:
                lTokens.insert(-2, parser.blank_line())
                lTokens.insert(-2, parser.carriage_return())

            oViolation.set_tokens(lTokens)


def _analyze_no_blank_line(self, lToi):
    sSolution = 'Remove blank lines above begin keyword'
    dAction = {}
    dAction['action'] = 'Remove'
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        iLine = oToi.get_line_number() + utils.count_carriage_returns(lTokens)
        for iToken, oToken in enumerate(lTokens):
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.process_keyword, token.begin_keyword], iToken, lTokens):
                if blank_lines_exist(iToken, lTokens):
                    oViolation = violation.New(iLine, oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                    break
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.close_parenthesis, token.begin_keyword], iToken, lTokens):
                if blank_lines_exist(iToken, lTokens):
                    oViolation = violation.New(iLine, oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                    break
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.is_keyword, token.begin_keyword], iToken, lTokens):
                if blank_lines_exist(iToken, lTokens):
                    oViolation = violation.New(iLine, oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                    break

def _analyze_require_blank_line(self, lToi):
    sSolution = 'Add blank line above begin keyword'
    dAction = {}
    dAction['action'] = 'Insert'
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        iLine = oToi.get_line_number() + utils.count_carriage_returns(lTokens)
        for iToken, oToken in enumerate(lTokens):
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.process_keyword, token.begin_keyword], iToken, lTokens):
                if not blank_lines_exist(iToken, lTokens):
                    oViolation = violation.New(iLine, oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                    break
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.close_parenthesis, token.begin_keyword], iToken, lTokens):
                if not blank_lines_exist(iToken, lTokens):
                    oViolation = violation.New(iLine, oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                    break
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.is_keyword, token.begin_keyword], iToken, lTokens):
                if not blank_lines_exist(iToken, lTokens):
                    oViolation = violation.New(iLine, oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                    break


def blank_lines_exist(iToken, lTokens):
    for iIndex in range(iToken, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.blank_line):
            return True
    return False
