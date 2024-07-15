from __future__ import unicode_literals
from searchDoc2023 import searchForDoc
import pymupdf
from APIObject import APIObject
import re
import json
from Utilities import savelist,saveDict




if __name__=='__main__':
    path="Pdf/Inventor2023ObjectModel.pdf"
    doc = pymupdf.open(path)  # or pymupdf.Document(filename)
    page = doc[0]
    words=page.get_text('words')#https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_text
    wrong_list=[]
    API_list=[]
    for count, t in enumerate(words):
        x0, y0, x1, y1, txt, block_no, line_no, word_no=t
        if count>20000:
            continue
        processed=txt.rstrip().lstrip() #strip off empty space at start and end
        processed2=processed.split(' ')
        if (type(processed2)==list):
            processed2=processed2[0]
        processed2=processed2.strip()
        if processed2.startswith('(') or processed2.startswith('['):
            print(f"skipped over word that starts with ( => {processed2}")
            continue
        if len(processed2)<3: #'BOM is the shortest word
            print(f"skipped over to short word or word that starts with ( ={processed2}")
            continue
        correct_url=searchForDoc(processed2,addObject=True)
        if correct_url!='None':
            o=APIObject(processed2,correct_url,x0,y0,x1,y1)
            cont=repr(o)
            API_list.append(cont)
            print(f"{count}\t", processed2,'\t',correct_url)
        else:
            wrong_list.append(processed2)
            print("fail\t",processed2)

    savelist(API_list,"output/API_list2023.txt")
    print(len(API_list),f" correct words found")
    savelist(wrong_list,"output/wrong_dict2023.txt")
    print(len(wrong_list),f" wrong words found")
