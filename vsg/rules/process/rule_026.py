
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.token import process_statement as token

from vsg.vhdlFile import utils


class rule_026(rule.Rule):
    '''
    Process rule 026 checks for blank lines between the end of the sensitivity list and process declarative lines.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'process', '026')
        self.solution = 'Insert blank line below'
        self.phase = 3
        self.style = 'require_blank_line'
        self.configuration.append('style')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(token.process_keyword, token.begin_keyword)

    def _analyze(self, lToi):
        if self.style == 'require_blank_line':
            _analyze_require_blank_line(self, lToi)
        elif self.style == 'no_blank_line':
            _analyze_no_blank_line(self, lToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction['action'] == 'Insert':
            lTokens.insert(dAction['index'], parser.carriage_return())
            lTokens.insert(dAction['index'], parser.blank_line())
            oViolation.set_tokens(lTokens)
        else:
            iStart = dAction['start']
            iEnd = dAction['end']
            lNewTokens = lTokens[:iStart]
            lNewTokens.extend(lTokens[iEnd:])
            oViolation.set_tokens(lTokens[:iStart] + lTokens[iEnd:])


def _analyze_require_blank_line(self, lToi):
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if not are_there_process_declarative_items(lTokens):
            continue
        iLine, iSearch = find_beginning_of_process_declarative_region(oToi.get_line_number(), lTokens)

        if does_a_blank_line_exist(iSearch, lTokens):
            continue

        dAction = {}
        dAction['action'] = 'Insert'
        dAction['index'] = find_carriage_return(iSearch, lTokens) + 1

        oViolation = violation.New(iLine, oToi, self.solution)
        oViolation.set_action(dAction)
        self.add_violation(oViolation)

def _analyze_no_blank_line(self, lToi):
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if not are_there_process_declarative_items(lTokens):
            continue
        iLine, iSearch = find_beginning_of_process_declarative_region(oToi.get_line_number(), lTokens)

        if not does_a_blank_line_exist(iSearch, lTokens):
            continue

        dAction = {}
        dAction['action'] = 'Remove'
        dAction['start'] = iSearch
        for iToken, oToken in enumerate(lTokens[iSearch:]):
            if isinstance(oToken, parser.carriage_return):
                if not isinstance(lTokens[iSearch + iToken + 1], parser.blank_line):
                    dAction['end'] = iSearch + iToken - 1
                    break

        oViolation = violation.New(iLine, oToi, self.solution)
        oViolation.set_action(dAction)
        self.add_violation(oViolation)

def are_there_process_declarative_items(lTokens):
    for iToken, oToken in enumerate(lTokens):

        if utils.are_next_consecutive_token_types_ignoring_whitespace([token.process_keyword, token.begin_keyword], iToken, lTokens):
            return False
        if utils.are_next_consecutive_token_types_ignoring_whitespace([token.close_parenthesis, token.begin_keyword], iToken, lTokens):
            return False
        if utils.are_next_consecutive_token_types_ignoring_whitespace([token.is_keyword, token.begin_keyword], iToken, lTokens):
            return False

    return True


def find_beginning_of_process_declarative_region(iLine, lTokens):
    iReturn = 1
    iMyLine = iLine
    iReturnLine = iLine
    for iToken, oToken in enumerate(lTokens):
        iMyLine = utils.increment_line_number(iMyLine, oToken)
        if isinstance(oToken, token.close_parenthesis):
            iReturnLine = iMyLine
            iReturn = iToken + 1
        if isinstance(oToken, token.is_keyword):
            iReturnLine = iMyLine
            iReturn = iToken + 1
            break
    return iReturnLine, iReturn


def does_a_blank_line_exist(iToken, lTokens):
    if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return, parser.blank_line], iToken, lTokens):
        return True
    if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return, parser.blank_line], iToken, lTokens):
        return True
    if utils.are_next_consecutive_token_types([parser.carriage_return, parser.blank_line], iToken, lTokens):
        return True
    return False


def find_carriage_return(iToken, lTokens):
    for iIndex in range(iToken, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.carriage_return):
            return iIndex
    return None
