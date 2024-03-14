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
    aranir

    [abc] => a : 1 match
            ac : 2 match
            Python: no mathces
           

    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39]=>[012..39]
    

    [^abc] => abc disindaki karakterler.
    [^0-9] => rakam olmayan karakterler.

'''
result=re.findall("[abc]",str)
result=re.findall("[sat]",str)
result=re.findall("[a-e]",str)
result=re.findall("[0-9]",str)
result=re.findall("[^abc]",str)

'''
    . -Her hangi bir tek karakteri belirtirr.

        .. => a: no match
              ab : 1 match
              abc : 1match
              abc:1match
              abcd:2match
'''
result=re.findall("..",str)
result =re.findall("Py..on",str)

'''
    ^ - belirtilen karakterle basliyor mu

    ^a => a: 1 match
          abc:1 match
          bac:no match
'''
result=re.findall("^P",str)

'''
    $ - belitrilen karakter ile bitiyor mu
    a$ =>a :1 match
        lamba :1match
'''
result=re.findall("t$",str)

print(result)
