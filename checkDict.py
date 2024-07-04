from addLinkToText import addLink
from checkWebsite import validateUrl
import pymupdf
import json 
import re
from createDict import saveDict,checkWord


def camel_case_split(str):
### https://www.geeksforgeeks.org/python-split-camelcase-string-to-individual-strings/
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

if __name__ =="__main__":

    dic=json.load(open('output/wrong_dict.txt','r')) 
    corrected_dic={}
    notFound_dic={}
    for count,(failed_word,url) in enumerate(dic.items()):
        words=camel_case_split(failed_word)
        limit=len(words)
        got_corrected=False
        for i in range(limit):
            word=words[i]
            correct_url=checkWord(word)
            if correct_url!="None":
                print(f"is correct\t {word}")
                corrected_dic[word]=correct_url
                got_corrected=True
                break
            else:
                if i<limit-1:
                    words[i+1]=word+words[i+1]
                print(f'failed\t{word}')
        if got_corrected==False:
            notFound_dic[failed_word]=failed_word
    print("finished")
    print(f"corrected\t{corrected_dic}")
    saveDict(corrected_dic,path='output/corrected_dic.txt')
    saveDict(notFound_dic,path='output/notFound_dic.txt')