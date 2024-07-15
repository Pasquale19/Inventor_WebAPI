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
