
def pageCount(n, p):
    # p son sayfa n istenen
    c1=1
    c2=1
    firstPage=1
    while True:
        if p-n==1 or n-p==1:
            print('0')
            break
        if p!=n-1 and p!=n-2:
            c1=c1+1

        if p!=firstPage+1 and p!=firstPage+2:
            c2=c2+1 

        if c1!=c2:
            print(min(c1,c2))
            break
        firstPage+=2
        n-=2

            
        
pageCount(6,2)