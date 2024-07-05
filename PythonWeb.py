# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io
import pypdf
from pypdf import PdfReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import requests

def validateUrl(url)->bool:
    response = requests.get(url)
    valid=response.status_code == 200
    if valid:
        print('Web site exists')
    else:
        print('Web site does not exist')
    return valid

def validateUrlName(url:str)->bool:
    response = requests.get(url)
    code=response.status_code
    if code!=200:
        return False
    try:
        jsonStr=response.json()
    except:
        print("json failed")
        return False
    try:
        status=jsonStr["status"]
        print(f"{status=}")
        if status=="Failed":
            return False
        else:
            return True
    except:
        return False

path = "D:\090_Programmiersandbox\001_python\PythonWeb\Inventor2022ObjectModel.pdf"
path="Inventor2022ObjectModel.pdf"
reader=PdfReader(path)
page = reader.pages[0]
txt=page.extract_text()
print(f"type={type(txt)}")

lines=txt.split('\n')

#print(txt)
for count, t in enumerate(lines):
    if count>10:
        continue
    #print(t)
    processed=t.rstrip().lstrip()
    #print(processed)
    processed2=processed.split('(c)')
    #print(processed2)
    #processed2=processed2[0].split('(k)')
    #print(processed2)
    
    if (type(processed2)==list):
        processed2=processed2[0]
    processed2=processed2.strip()
    #processed2=processed[0]

    url_start="https://help.autodesk.com/view/INVNTOR/2022/ENU/?guid="
    full_url=url_start+processed2
    valid_url=validateUrl(full_url)
    if valid_url:
        result=processed2+'\t'+str(valid_url)+'\t'+full_url
        print(count, result)



if __name__ == "__main__":
    validateUrl("https://help.autodesk.com/view/INVNTOR/2027/ENU/?guid=AssemblyWorkPointDefBOM")
