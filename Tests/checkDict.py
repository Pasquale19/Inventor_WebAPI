#import json
#word_dict=json.load(open('output/dict2.txt','r'))
#txt="ModelAnnotation"
#try:
    
#    print(f"ModelAnnotation= {word_dict[txt]}")
#except:
#    print("word not found")

if __name__ =="__main__":
    txt="Application"
    f=open("output/API_List.txt",'r')
    lines=f.read().split('\n')
    for count,l in enumerate(lines):
        items=l.split('\t')
        if items[0]==txt:
            print(f"{count} found ", l)

