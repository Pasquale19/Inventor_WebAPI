#https://proxiesapi.com/articles/working-with-query-parameters-in-python-requests#:~:text=Query%20parameters%20allow%20you,using%20the%20excellent%20Requests%20library.
import requests
import json


search_term='AngularGeneralDimension%20Object'
search_term2='AngularGeneralDimension%20Object'
str_req_full="https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/search/?origin=upi&p=INVNTOR&knowledgeSource=Product%20Documentation&cg=Developer%27s%20Documentation&v=2023&l=ENU&maxresults=16&source=all&q="+search_term
#str_req_full="https://help.autodesk.com/view/INVNTOR/2023/ENU/?query=AnalysisManager%20Object&knowledgeSource=Product%20Documentation"

url_beginning="https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/search/"
response1=requests.get(str_req_full)
base_url='https://help.autodesk.com/view/INVNTOR/2023/ENU/'
url2=base_url+"?q="+search_term

#params = {'origin':'upi', 'p':'INVNTOR','v':'2023','l':'ENU','maxresults': '16','cg':'Developer%27s%20Documentation','source':'all'}
params = {'origin':'upi', 'p':'INVNTOR','v':'2023','l':'ENU','maxresults': '16','cg':'Developer%27s%20Documentation','source':'all','knowledgeSource':'Product Documentation'}
#del params['q']
#del params['cg']
url_beginning=url_beginning+"?q="+search_term


response2=requests.get(url2, params=params)
print(f"{1} full_url={response1.url}")
print(f"{2} full_url={response2.url}")
print('\n')
def checkResponse(response1,path='data1'):
    
    if response1.status_code==200:
        print(f"response {path}\n")
        #print(f"{response1.json()}\n\n")
        try:
            json1=response1.json()
            with open(path+'.json', 'w', encoding='utf-8') as f:
                json.dump(json1, f, ensure_ascii=False, indent=4)
                print(f'json written to {path}')
        except:
            print(f"json not possible")
    try:
        params1=response1.request.params
        print(f'parameter1\n{params1}')
    except:
        print(f"{path} has no parameter")
    status=json1['status']
    print(f'status={status}')
    if status=='Completed':
        entries=json1['entries']
        #print(f'entries={entries}\n')
        items=entries['item']
        #print(f'item={items}\n')
        for count,i in enumerate(items):
            if i['source']=='CloudHelp':
                topicId=i['topicId']
                full_url=base_url+'?guid='+topicId
                response_found=requests.get(full_url)
                if response_found.status_code==200:
                    print(f'API Documentation found under {full_url}')

                #print(f'item{count}={i}\n')

    else:
        print(f"response {path} failed")

checkResponse(response1)
checkResponse(response2,'data2')
checkResponse(response3,'data3')
#if response1.status_code==200:
#    print("response1\n")
#    print(f"{response1.json()}\n\n")
#    json1=response1.json()
#    with open('data1.json', 'w', encoding='utf-8') as f:
#        json.dump(json1, f, ensure_ascii=False, indent=4)
#    try:
#        params1=response1.request.params
#        print(f'parameter1\n{params1}')
#    except:
#        print("response 1 has no parameter")
#else:
#    print(f"response1 failed")


#if response2.status_code==200:
#    print("response2")
#    print(f"{response2.json()}\n\n")
#    json2=response2.json()
#    with open('data2.json', 'w', encoding='utf-8') as f:
#        json.dump(json2, f, ensure_ascii=False, indent=4)
#    try:
#        params1=response1.request.params
#        print(f'parameter1\n{params1}')
#    except:
#        print("response 1 has no parameter")
#else:
#    print(f"response1 failed")

def getParams(str:str):
    split=[str.split()]
