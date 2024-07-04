import json
word_dict=json.load(open('output/dict2.txt','r'))
txt="ModelAnnotation"
try:
    
    print(f"ModelAnnotation= {word_dict[txt]}")
except:
    print("word not found")
