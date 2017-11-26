
from vsg.rules.entity import entity_rule
from vsg import line

class rule_003(entity_rule):
    '''
    Entity rule 003 checks for a blank line above the entity keyword.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above entity keyword.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                self._is_blank_line_before(oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.insert(iLineNumber, line.blank_line()) 