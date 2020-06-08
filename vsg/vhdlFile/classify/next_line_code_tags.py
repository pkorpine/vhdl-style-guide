import re
import copy


def next_line_code_tags(dVars, oLine, oLinePrevious):
    '''
    Searches for the following string at the beginning of the previous line:

       -- vsg-disable-next-line

    and disables the rule given for the current line.
    '''

    if re.match('^\s*--\s*vsg-disable-next-line\s+\w', oLinePrevious.line):
        oLine.hasNextLineCodeTag = True
        lRules = oLinePrevious.line.split()[2::]
        oLine.nextLineCodeTags = oLinePrevious.nextLineCodeTags
        oLine.nextLineCodeTags.extend(lRules)
