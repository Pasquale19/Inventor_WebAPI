import pymupdf # imports the pymupdf library
from pymupdf import Rect,Point
from pymupdf import Page
import re



def isExactMatch(page, term, clip, fullMatch=False, caseSensitive=False):
# clip is an item from page.search_for(term, quads=True)

    termLen = len(term)
    termBboxLen = max(clip.height, clip.width)
    termfontSize = termBboxLen/termLen
    f = termfontSize*2

    #clip = clip.rect

    validate = page.get_text("blocks", clip = clip + (-f, -f, f, f), flags=0)[0][4]
    
    flag = 0
    if not caseSensitive:
        flag = re.IGNORECASE

    matches = len(re.findall(f'{term}', validate, flags=flag)) > 0
    if fullMatch:
        matches = len(re.findall(f'\\b{term}\\b', validate))>0
    return matches
