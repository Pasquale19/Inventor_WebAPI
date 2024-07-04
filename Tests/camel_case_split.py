
# Python3 program Split camel case 
# string to individual strings
import timeit
import random
import string
# code snippet to be executed only once
input = "Es gibt zwei Möglichkeiten, mehrere Codezeilen in timeit.timeit() auszuführen: ein Semikolon oder indem der Code in dreifache Anführungszeichen eingeschlossen als Zeichenfolge gespeichert wird."
input=input+"Mangel an Originalität sagten alle: »Da ist Shaitana, dieser verdammte"
input=input+"Anschließend verwendet die Funktion join(), um die Elemente in modified_string zu einem einzigen String zusammenzufügen, wobei die Unterstriche als Trennzeichen dienen. Der resultierende String wird dann mit split() an den Unterstrichen geteilt und die resultierende Liste in split_string gespeichert.Schließlich verwendet die Funktion filter() und eine Lambda-Funktion, um alle leeren Zeichenfolgen aus split_string zu entfernen, und gibt dann die resultierende Liste zurück."
input=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1000000))
print(f'{input=}')
def camel_case_split1(str):
    words = [[str[0]]]
 
    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)
 
    return [''.join(word) for word in words]

import re
 
def camel_case_split2(str):
     
    start_idx = [i for i, e in enumerate(str)
                 if e.isupper()] + [len(str)]
 
    start_idx = [0] + start_idx
    return [str[x: y] for x, y in zip(start_idx, start_idx[1:])]

def camel_case_split3(str):
 
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

def camel_case_split4(str:str):
    new_string=""
    for i in str:
        if(i.isupper()):
            new_string+="*"+i
        else:
            new_string+=i
    x=new_string.split("*")
    x.remove('')
    return x


def camel_case_split5(s):
    # use map to add an underscore before each uppercase letter
    modified_string = list(map(lambda x: '_' + x if x.isupper() else x, s))
    # join the modified string and split it at the underscores
    split_string = ''.join(modified_string).split('_')
    # remove any empty strings from the list
    split_string = list(filter(lambda x: x != '', split_string))
    return split_string

dic={}     
start = timeit.default_timer()
camel_case_split1(input)
t1=timeit.default_timer() - start
dic['t1']=t1
print('Variante 1\t',  t1   )

start = timeit.default_timer()
camel_case_split2(input)
t2=timeit.default_timer() - start
dic['t2']=t2
print('Variante 2\t',  t2   )

start = timeit.default_timer()
camel_case_split3(input)
t3=timeit.default_timer() - start
dic['t3']=t3
print('Variante 3\t',  t3  )

start = timeit.default_timer()
camel_case_split4(input)
t4=timeit.default_timer() - start
dic['t4']=t4
print('Variante 4\t',  t4   )

start = timeit.default_timer()
camel_case_split5(input)
t5=timeit.default_timer() - start
dic['t5']=t5
print('Variante 5\t',  t5   )

result=dict(sorted(dic.items(), key=lambda item: item[1]))
print(result)