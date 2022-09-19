x=int(input("scrie un nr- "))
y=int(input("scrie un nr- "))
#a
def suma(a,b):
    return a+b
print("suma=", suma(x,y))
#b
def produs(a,b):
    return a*b
print("produs=", produs(x,y))
#c
def medaritmetica(a,b):
    return (a+b)/2
print("medaritmetica=", medaritmetica(x,y))
#d,#e
def cmmadc(a,b):
    while a!=b:
        if a>b:a=a-b
        else: b=b-a
    return a
print("cmmadc=", cmmadc(x,y))
def cmmicmc(a,b):
    mult=(a*b)// cmmadc(a,b)
    return mult
print("cmmicmc=", cmmicmc(x,y))
#f
def nrmin(a,b):
    return min([a,b])
print("nrmin=", nrmin(x,y))
#g
def nrmax(a,b):
    return max([a,b])
print("nrmax=", nrmax(x,y))
#h
def sumnrcitite():
    a=int(input("a- "))
    b=int(input("b- "))
    return a+b
print("suma ab=", sumnrcitite())
#i
def prodnrcitite():
    a=int(input("a- "))
    b=int(input("b- "))
    return a*b
print("produsul ab=", prodnrcitite())
#j
def divcom(a,b):
    list=[]
    n=cmmadc(a,b)
    for i in range(1, n+1):
        if n%i==0:
            list.append(i)
    return list
print("divcom=", divcom(x,y))
#k
def multcom(a,b):
    list1=[]
    for i in range(1, 6):
        list1.append(cmmicmc(a,b)*i)
    return list1
print("multcom=", multcom(x,y))
#l
def cifrecom(a,b):
    cifa=[int(i)for i in str(a)]
    cifb=[int(i)for i in str(b)]
    return list(set(cifa) & set(cifb))
print("cifrecom=", cifrecom(x,y))
#m
def cifredif(a,b):
    cifa=[int(i)for i in str(a)]
    cifb=[int(i)for i in str(b)]
    return list(set(cifa) - set(cifb))
print("cifredif=", cifredif(x,y))