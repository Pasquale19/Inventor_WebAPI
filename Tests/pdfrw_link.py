import pdfrw
import sys
import os

from pdfrw import PdfReader, PdfWriter

path="Inventor2022ObjectModel.pdf"
outputPath="pdfrw_out.py"

pages=PdfReader(path).pages
outData=PdfWriter(outputPath)
outData.addpage(pages[0])
outData.addpage(pages[0])
x=10
y=10
page=pages[0]
word="http://example.com/word"
link_annotation = pdfrw.PdfDict(
                    Subtype="/Link",
                    Rect=[x, y, x + len(word) * 5, y + 10],
                    Border=[0, 0, 0],
                    A=pdfrw.PdfDict(
                        S="/URI",
                        URI="http://example.com/word={}".format(word)
                    ),
                    C=[139, 0, 0],
                )

page.Annots.append(link_annotation)
outData.write()
pdfrw.PdfWriter().write(outputPath, path)