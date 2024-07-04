from addLinkToText import addLink
import pymupdf
import timeit
import json 

if __name__ =="__main__":
    outputPath='output/result2.pdf'
    start=start = timeit.default_timer()
    dic=json.load(open('output/dict2.txt','r'))     
    path="Pdf/Inventor2022ObjectModel.pdf"
    doc = pymupdf.open(path) # open a document
    doc2=doc
    len1=len(dic)
    
    for count,(word,url) in enumerate(dic.items()):
        addLink(doc2[0],word,url)
        print(f"from dic1 {count}/{len1}\tadded {word}")
        if count % 100==0:
            save_file=f"output/result{count}.pdf"
            doc2.save(save_file)
            doc2 = pymupdf.open(save_file)
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