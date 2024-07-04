import pymupdf
from pymupdf import Rect,Point
path="Inventor2022ObjectModel.pdf"
print(pymupdf.__doc__)
doc = pymupdf.open(path)  # or pymupdf.Document(filename)

page1=doc[0]
doc.fullcopy_page(0)
page = doc.new_page(-1, # insertion point: end of document
                    width = 595, # page dimension: A4 portrait
                    height = 842)
page2=doc[1]
#https://pymupdf.readthedocs.io/en/latest/page.html#link-dict-description
linkdict = {'kind': 1, 'xref': 121, 'from': Rect(112.31999969482422, 54.909912109375, 136.7917938232422, 68.35308837890625), 'page': 1, 'to': Point(108.0, 460.0), 'zoom': 4.0, 'id': 'VLRQFKMMYAYEKJIV'}
#2 LINK_URI
url="https://www.google.de/"
lftTopCorner=Point(112.31999969482422, 54.909912109375)
rightBotCorner=Point(136.7917938232422, 68.35308837890625)
RectLink=Rect(lftTopCorner,rightBotCorner )
linkdict2 = {'kind': 2, 'xref': 121, 'from': RectLink, 'page': 1, 'to': Point(108.0, 460.0),'uri': url}
#page.insert_text(pt,  # anywhere, but outside all redaction rectangles
#    "something",  # some non-empty string
#    fontname="newname",  # new, unused reference name
#    render_mode=3  # makes the text invisible
#)
page.draw_line(lftTopCorner,Point(rightBotCorner.x,lftTopCorner.y)) #https://pymupdf.readthedocs.io/en/latest/page.html#Page.draw_line
page.draw_rect(RectLink) #https://pymupdf.readthedocs.io/en/latest/shape.html#Shape.draw_rect
page.insert_link(linkdict)
page.insert_link(linkdict2)

#write text
bottomLeftPt=Point(lftTopCorner.x,rightBotCorner.y)
#https://pymupdf.readthedocs.io/en/latest/shape.html#Shape.insert_textbox
page.insert_text(bottomLeftPt, "google", fontsize=11, fontname='helv', fontfile=None, set_simple=False)
for count,link in enumerate(page2.links()):
    print(f"link{count}= {link}")

#for count,annot in enumerate(page1.annots()):
#    print(f"annot{count}= {annot}")

#for field in page1.widgets():
#    print(f"field{count}= {field}")

doc.save("pymupdf.pdf")