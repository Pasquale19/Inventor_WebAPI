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

def first_difference(str1, str2):
    z=zip(str1, str2)
    for a, b in z:
        if a != b:
            return a+b
    return 'no difference'

if __name__=='__main__':
    path="Pdf/Inventor2022ObjectModel.pdf"
    doc = pymupdf.open(path)  # or pymupdf.Document(filename)
    doc2=doc
    page = doc2[0]
    search_text="PresentationDocument"
    search_text="ModelAnnotation"
    search_text="Application"
    text_instances=page.search_for(search_text)
    len_search_text=len(search_text)
    if text_instances is None:
        print(f"{search_text} not found")
        #break
    #print(f"search_Text: {search_text}")
    # Iterate through each instance and print the bounding box coordinates
    for text_instance in text_instances:
        x0=text_instance.x0
        x1=text_instance.x1
        y0=text_instance.y0
        y1=text_instance.y1
        
        #print(f"Bounding Box: ({x0}, {y0}) - ({x1}, {y1})")
        box=page.get_textbox(text_instance).strip()
        
        try:
            box=box.split('\n')[0]
        except:
            print(f'no split')
        box=box.split(' ')[0]
        len_box=len(box)
        len_differnce=len_box-len_search_text
        #print(f"found_text={page.get_textbox(text_instance)}")
        

        if box==search_text:
            page.draw_rect(text_instance,  color = (0, 1, 0), width = 2)
            print(f"{search_text} found")
            print(f"found at {text_instance}")
            #linkdict2 = {'kind': 2, 'xref': 121, 'from': text_instance, 'page': 1, 'to': Point(108.0, 460.0),'uri': url}
            #page.insert_link(linkdict2)
        else:
            dif=first_difference(search_text,box)
            #if len_differnce!=0:
            #    print("length differs")
            #    continue
            print("different words: ",box,'\tvs\t',search_text, 'first difference is ',dif, 'length difference is ',len_differnce)
    doc2.save(f"output/found_{search_text}.pdf")