import re

result=dir(re)
#re module

str= "Python Kursu: Python Programlama Rehberiniz | 40 saat"

result=re.findall("Python",str)
result=len(result)

result= re.split(" ",str)#bosluklardan itibaren ayir
result= re.sub(" ","-",str)#bosluklari cizgiyle degistir /s=bosluk
#result= re.search("Python",str)
#result= result.span() #burada result match objesi oldugu icin sadec spani gosterir
#result= result.string()

#regular expression
'''
    [] - K6seli parantezler arasina yazilan bitin karakterler
    aranır

    [abc] => a : 1 match
            ac : 2 match
            Python: no mathces
           

    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39]=>[012..39]
    

    [^abc] => abc disindaki karakterler.
    [^0-9] => rakam olmayan karakterler.

'''
print(result)