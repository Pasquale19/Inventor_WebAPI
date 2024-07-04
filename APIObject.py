import pymupdf
from pymupdf import Point,Rect


class APIObject:
    def __init__(self, name, url,x0,x1,y0,y1):
        self.name = name
        self.url = url
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
    def __str__(self):
        return f"{self.name}\t{self.url}\t{self.x0}\t{self.y0}\t{self.x1}\t{self.y1}"
    def __repr__(self): 
        return f"{self.name}\t{self.url}\t{self.x0}\t{self.y0}\t{self.x1}\t{self.y1}"

    def box(self)->Rect:
        p1=Point(self.x0,self.y0)
        p2=Point(self.x1,self.y1)
        return Rect(p1,p2)

    @staticmethod
    def load(txt:str):
        sp=txt.split('\t')
        name=sp[0]
        url=sp[1]
        x0=sp[2]
        y0=sp[3]
        x1=sp[4]
        y1=sp[5]
        return APIObject(name,url,x0,y0,x1,y1)

    @staticmethod
    def loadAPIObjects(path:str)->list:
        f=open(path,'r')
        txt=f.read()
        items=txt.split('\n')
        l=[]
        for item in items:
            if len(item)<8: continue
            a=APIObject.load(item)
            l.append(a)
        f.close()
        return l

if __name__ =="__main__":
    t="ModelAnnotation\turl\t0\t0\t100\t100"
    x=APIObject.load(t)
    print(x)
    print(repr(x))
    

