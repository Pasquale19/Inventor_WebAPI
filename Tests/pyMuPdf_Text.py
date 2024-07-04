import pymupdf
from pymupdf import Rect,Point
import json

def saveDict(d:dict,path:str="dict.txt"):
    #with open(path, 'w') as f:
    #    print(d, file=f)
    json.dump(d, open(path,'w'))
 
def camel_case_split(str):
### https://www.geeksforgeeks.org/python-split-camelcase-string-to-individual-strings/
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

#def checkWord(word:str):
#    url_start="https://help.autodesk.com/view/INVNTOR/2022/ENU/?guid="
#    request_url="https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/bookmark/?p=INVNTOR&v=2022&l=ENU&guid="
#    full_url=request_url+word
#    valid_url=validateUrl(full_url)
#    if valid_url:
#        correct_url=url_start + word
#        #result=word+'\t'+str(valid_url)+'\t'+correct_url
#        return correct_url
#    else: return "None"

if __name__=='__main__':
    path="Pdf/Inventor2022ObjectModel.pdf"
    doc = pymupdf.open(path)  # or pymupdf.Document(filename)
    page = doc[0]
    txt=page.get_text('text') #https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_text
    words=page.get_text('words')

    lines=txt.split('\n')
    word_dict={}
    wrong_dict={}
    for count, t in enumerate(lines):
        if count>2000:
            continue
        processed=t.rstrip().lstrip() #strip off empty space at start and end
        #processed2=processed.split('(c)')
        processed2=processed.split(' ')
        print(processed2)
        #processed2=processed2[0].split('(k)')
        #print(processed2)
    
        if (type(processed2)==list):
            processed2=processed2[0]
        processed2=processed2.strip()
        #processed2=processed[0]
        #print(f"{count}\t {processed2}")

        #correct_url=checkWord(processed2)
        #if correct_url!="None":
        #    word_dict[processed2]=correct_url
        #    print(f"{count}\t", processed2,'\t',correct_url)
        #else:
        #    wrong_dict[processed2]=processed2
        #    print("fail\t",processed2)

saveDict(word_dict,"output/dict2_pymupdf.txt")
saveDict(wrong_dict,"output/wrong_pymupdf.txt")