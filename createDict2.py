from __future__ import unicode_literals
from concurrent.futures import process
from checkWebsite import validateUrl
import pymupdf
from APIObject import APIObject
import re
import json

def saveDict(d:dict,path:str="dict.txt"):
    #with open(path, 'w') as f:
    #    print(d, file=f)
    json.dump(d, open(path,'w'))

def savelist(d:list,path:str="list.txt"):
    f= open(path, 'w')
    for item in d:
        f.write(f"{item}\n")
    f.close()
 
def camel_case_split(str):
### https://www.geeksforgeeks.org/python-split-camelcase-string-to-individual-strings/
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

def checkWord(word:str):
    url_start="https://help.autodesk.com/view/INVNTOR/2022/ENU/?guid="
    request_url="https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/bookmark/?p=INVNTOR&v=2022&l=ENU&guid="
    full_url=request_url+word
    valid_url=validateUrl(full_url)
    if valid_url:
        correct_url=url_start + word
        #result=word+'\t'+str(valid_url)+'\t'+correct_url
        return correct_url
    else: return "None"

if __name__=='__main__':
    path="Pdf/Inventor2023ObjectModel.pdf"
    doc = pymupdf.open(path)  # or pymupdf.Document(filename)
    page = doc[0]
    words=page.get_text('words')#https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_text
    word_dict={}
    wrong_dict={}
    API_list=[]
    for count, t in enumerate(words):
        x0, y0, x1, y1, txt, block_no, line_no, word_no=t
        if count>20000:
            continue
        processed=txt.rstrip().lstrip() #strip off empty space at start and end
        #processed2=processed.split('(c)')
        processed2=processed.split(' ')
        #print(processed2)
        #processed2=processed2[0].split('(k)')
        #print(processed2)
    
        if (type(processed2)==list):
            processed2=processed2[0]
        processed2=processed2.strip()
        #processed2=processed[0]
        #print(f"{count}\t {processed2}")

        correct_url=checkWord(processed2)
        if correct_url!="None":
            o=APIObject(processed2,correct_url,x0,y0,x1,y1)
            cont=repr(o)
            API_list.append(cont)
            print(f"{count}\t", processed2,'\t',correct_url)
        else:
            wrong_dict[processed2]=processed2
            print("fail\t",processed2)

    savelist(API_list,"output/API_list.txt")
    saveDict(wrong_dict,"output/wrong_dict.txt")
