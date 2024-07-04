import pymupdf # imports the pymupdf library
import re

path="Inventor2022ObjectModel.pdf"
doc = pymupdf.open(path) # open a document
doc2=doc
# Open the PDF file
#doc = fitz.open(path)

# Specify the text you want to search for
search_text = 'Application'

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

def addUrl(path:str):


# Iterate through each page in the PDF
for count,page in enumerate(doc):

    # Use the `search_for` method to find instances of the search text on the page
    text_instances = page.search_for(search_text)

    # Iterate through each instance and print the bounding box coordinates
    for text_instance in text_instances:
        x0 = text_instance.x0
        x1=text_instance.x1
        y0=text_instance.y0
        y1=text_instance.y1
        print(f"Page {count + 1}:")
        print(f"Text: {search_text}")
        print(f"Bounding Box: ({x0}, {y0}) - ({x1}, {y1})")
        box=page.get_textbox(text_instance)
        try:
            box=box.split('\n')[0]
        except:
            print(f'no split')
        print(f"textbox{page.get_textbox(text_instance)}")
        if box==search_text:
            new_page=doc2[0]
            new_page.draw_rect(text_instance,  color = (0, 1, 0), width = 6)
            pypdf.add_uri("www.Google.com")
doc2.save('result.pdf')
