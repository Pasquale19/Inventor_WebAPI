#https://proxiesapi.com/articles/working-with-query-parameters-in-python-requests#:~:text=Query%20parameters%20allow%20you,using%20the%20excellent%20Requests%20library.
from ctypes.wintypes import BOOLEAN
import requests
import json
import urllib.request 



def searchForDoc(term:str,addObject:BOOLEAN=True)->str:
    if addObject: 
        search_term=term+'%20Object'
    else:
        search_term=term
    url:str="https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/search/?origin=upi&p=INVNTOR&knowledgeSource=Product%20Documentation&cg=Developer%27s%20Documentation&v=2023&l=ENU&maxresults=5&source=all&q="+search_term
    base_url:str='https://help.autodesk.com/view/INVNTOR/2023/ENU/'
    response1=requests.get(url, params=None)
    error_message:str='None'
    if response1.status_code!=200: return error_message
    try:
        json1=response1.json()
    except:
        #print(f"json not possible")
        return error_message
    status=json1['status']
    #print(f'status={status}')
    if status!='Completed':
        return error_message
    entries=json1['entries']
    #print(f'entries={entries}\n')
    items=entries['item']
    #print(f'item={items}\n')
    for count,i in enumerate(items):
        if i['source']=='CloudHelp':
            topicId=i['topicId']
            title=i['title'].split(' ')
            if type(title) ==list:
                title=title[0]
            if title!=term:
                continue
            full_url=base_url+'?guid='+topicId
            response_found=requests.get(full_url)
            if response_found.status_code==200:
                #print(f'API Documentation found under {full_url}')
                return full_url
    return error_message

def checkLink(url:str):
    if url=='None': return
    # Using urlopen() function with url in it
    print(f"{url=}")
    webUrl = urllib.request.urlopen(url)

if __name__ == '__main__':
    search_term='AngularGeneralDimension'
    search_term2='AngularGeneralDimension%20Object'
    search_term3="Model"
    result3:str=searchForDoc(search_term3)
    print(f'{result3=}')
    if result3=='None':
        print('None')
    result=searchForDoc(search_term)
    checkLink(result)
    result=searchForDoc(search_term)
    checkLink(result)
         


