
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rule_utils


class insert_token_left_of_token_if_it_does_not_exist_between_tokens(rule.Rule):
    '''
    Checks for the existence of a token and will insert it if it does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    insert_token : token object
       token to insert if it does not exist.

    anchor_token : token object type
       token to check if insert_token exists to the right of

    end_token : token object type
       token that bounds the search for the insert_token
    '''

    def __init__(self, name, identifier, insert_token, anchor_token, start_token, end_token):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.start_token = start_token
        self.end_token = end_token
        self.action = 'add'
        self.configuration.append('action')

    def _get_tokens_of_interest(self, oFile):
        if self.action == 'add':
            return oFile.get_tokens_bounded_by(self.start_token, self.end_token)
        else:
            return oFile.get_token_and_n_tokens_before_it([self.insert_token], 1)

    def _analyze(self, lToi):
        if self.action == 'remove':
            for oToi in lToi:
                sSolution = self.action.capitalize() + ' ' + self.solution
                self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))
            return

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bFound = False
            dAction = {}
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, type(self.insert_token)):
                    break
                if isinstance(oToken, self.anchor_token):
                    dAction['index'] = iToken - 1
            else:
                if dAction == {}:
                    continue
                sSolution = self.action.capitalize() + ' ' + self.solution
                oViolation  = violation.New(oToi.get_line_number(), oToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.action == 'remove':
            rule_utils.remove_optional_item(lTokens, oViolation, self.insert_token)
        else:
            dAction = oViolation.get_action()
            lTokens.insert(dAction['index'], self.insert_token)
            lTokens.insert(dAction['index'], parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
