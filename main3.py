from addLinkToText import addLink
import pymupdf
from pymupdf import Point
from APIObject import APIObject
import timeit
import json 

if __name__ =="__main__":
    outputPath='output/resultAPI2.pdf'
    start=start = timeit.default_timer()
    APIObjects=APIObject.loadAPIObjects("output/API_list.txt")    
    path="Pdf/Inventor2022ObjectModel.pdf"
    doc = pymupdf.open(path) # open a document
    doc2=doc
    len1=len(APIObjects)
    page=doc2[0]

    #layers
    oc_link = doc.add_ocg("links")
    oc_box = doc.add_ocg("boxes")

    for count,item in enumerate(APIObjects):
        box=item.box()
        area=box.get_area()
        if item.name=='Application':
            print("Application")
        if area>1600: continue
        page.draw_rect(box,  color = (1, 1, 0), width = 2,oc=oc_box)
        linkdict2 = {'kind': 2, 'xref': 121, 'from': box, 'page': 1, 'to': Point(108.0, 460.0),'uri': item.url}
        page.insert_link(linkdict2)
        print(f"from dic1 {count+1}/{len1}\tadded {item.name} with ")
        if count % 100==0:
            save_file=f"output/resultAPI{count}.pdf"
            doc2.save(save_file)
            #doc2 = pymupdf.open(save_file)
            print(f"saved\t",save_file)
    
    doc2.save(outputPath)
    print("finished first dict after ",(timeit.default_timer()-start)/60,' min and saved to: ',outputPath)
    #doc2 = pymupdf.open(outputPath) # open a document
    #dic2=json.load(open('output/corrected_dic.txt','r'))
    #len2=len(dic2)
    #for count,(word,url) in enumerate(dic2.items()):
    #    addLink(doc2[0],word,url)
    #    print(f"from dic2 {count}/{len2}\tadded {word}")
    #doc2.save('output/result3.pdf')
    #print(f'finished second dict after ',timeit.default_timer()-start,' s')