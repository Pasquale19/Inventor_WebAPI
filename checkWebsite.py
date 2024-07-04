from ctypes.wintypes import BOOLEAN
import requests #https://pypi.org/project/requests/
import json

def validateUrl(url,debug:BOOLEAN=False)->bool:
    response = requests.get(url)
    code=response.status_code
    if code!=200:
        if debug: print("code!=200")
        return False
    #try:
    #    jsonStr=response.json()
    #except:
    #    print("json failed")

    text={response.text}
    try:
        text=text.pop()
    except:
        print("text kein set")
    #print(f"txttype{type(text)}")
    #print(f"text={text}")
    #jsonStr=response.json()
    #print(f"jsontype={type(jsonStr)}")
    #try:
    #    status=jsonStr["status"]
    #    print(f"""status_completed={status}""")
    #except:
    #    print("eror")

    #print('\n')
    return code




if __name__=="__main__":
    name1="AnalysisManager"
    name2="AnalysisManager2"
    urls = ["https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/bookmark/?p=INVNTOR&v=2022&l=ENU&guid="+name1,
            "https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/bookmark/?p=INVNTOR&v=2022&l=ENU&guid="+name2,
            "https://origin-beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/bookmark/?p=INVNTOR&v=2022&l=ENU&guid="+name1,
            "https://origin-beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/bookmark/?p=INVNTOR&v=2022&l=ENU&guid="+name2,
            "https://help.autodesk.com/view/INVNTOR/2022/ENU/?guid="+name1,
            "https://help.autodesk.com/view/INVNTOR/2022/ENU/?guid="+name2
            ]
    for count,url in enumerate(urls):
        if count<0:continue
        print(f"url{count}={str(validateUrl(url))}")
        print("\n")

    
