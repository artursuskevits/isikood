
from re import S


def pikkus(ikood:str)->bool:
    """Funktsioon tagastab True; kui pikkus on 11 sümbolid
    :param str ikood: Inimese isikukood
    rtype: bool
    """
    if len(ikood)==11:
        flag=True
    else:
        flag=False
    return flag

def sugu (ikood:str)->str:
    """Kui esmine tät on [1,2,3,4,5,6] siis määramesugu
    :param str ikood: Isikukood
    rtype: str
    """
    ikood_list=list(map(int,ikood))
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s = "viga"
    return s

def kuud (ikood:str)->bool:
    """Kui kolm täht on 0 or 1 see on õige
    :param bool ikood: Isikukood
    rtype:bool
    """
    ikood_list=list(map(int,ikood))
    if ikood_list[3] in [0,1]:
        k=True
    else:
        k=False
    return k

def päev (ikood:str)->bool:
    """Kui viis täht on [0,1,2,3] see on õige
    :param bool ikood: Isikukood
    rtype:bool
    """
    ikood_list=list(map(int,ikood))
    if ikood_list[5] in [0,1,2,3]:
        p=True
    else:
        p=False
    return p

def sunnipaev (ikood:str)->str:
    ikood_list=list(map(int,ikood))
    y=str(ikood_list[1])+str(ikood_list[2])
    m=str(ikood_list[3])+str(ikood_list[4])
    d=str(ikood_list[5])+str(ikood_list[6])

    if(int(m)>0 and int(m)<13) and (int(d)>0 and int(d)<32):
        if ikood_list[0] in [1,2]:
            yy="18"
        elif ikood_list[0] in [3,4]:
            yy="19"
        elif ikood_list[0] in [5,6]:
            yy="20"
        spaev = d+"."+m+"."+yy+y
    else:
        spaev="viga"
    return spaev
        
def sunnikoht (ikood:str)->str:
    ikood_list=list(ikood)
    tahed_8910=ikood_list[7]+ikood_list[8]+ikood_list[9]
    t=int(tahed_8910)
    if 1 <t<10:
        haigla="Kuresaare Haigla"
    elif 11<t<19:
        haigla ="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<t<220:
        haigla ="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221<t<270:
        haigla ="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi"
    elif 271<t<370:
        haigla = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<t<420:
        haigla = "Narva Haigla"
    elif 421<t<470: 
        haigla = "Pärnu Haigla"
    elif 471<t<490:
        haigla = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491<t<520:
        haigla = "Järvamaa Haigla (Paide)"
    elif 521<t<570:
        haigla= "Rakvere, Tapa haigla"
    elif 571<t<600:
        haigla  = "Valga Haigla"
    elif 601<t<650:
        haigla = "Viljandi Haigla"
    elif 651<t<700:
        haigla= "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        haigla = "Ei ole sündinud Eestis"
    return haigla


def viiamne(ikood:str)->int:
    astme = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    astme2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    summa=0
    ikood_list=list(ikood)
    ikood_list=list(map(int,ikood_list))
    for i in range(0,10):
        summa+=ikood_list[i]*astme[i]
    s=(summa//11)*11
    jaak=summa-s
    if 1<=jaak<=9 :
        return jaak
    else:
        summa=0
        for i in range(0,10,1):
            summa+ikood_list[i]*astme2[i]
        s=(summa//11)*11
        jaak=summa-s
        if jaak != 10:
            return jaak
        else:
            jaak = 0
            return jaak



def naised_mehed(ikood:list)->list:
    naised=[] 
    mehed=[]
    for kood in range in ikoodid:
        kood_=list(kood)
        if int(kood_[0])%2==0:
            naised.append(kood)
        else:
            mehed.append(kood)
    naised.extend(mehed) 
    ikoodid=naised 
    return naised



def arvus_sorted(arvud:list)-> list:
    arvud = list(map(int,arvud))
    arvud.sort()
    return arvud
     #sum2= 0
    #sum3= 0
    #for i in range(len(ikood) - 1):
    #    sum2 += int(ikood[i]) * astme[i]
    #    jääk = sum2 // 11
    #if jääk ==10:
    #    for ii in range(len(ikood) - 1):
    #        sum3 += int(ikood[ii]) * astme2[ii]
    #        jääk2 = sum3 // 11
            
    #    if jääk2 ==10:
    #        ln= 0
    #    else:
    #        u=jääk2*11
    #        uu=sum3-u
    #        ln=uu     
    #else:
    #    u=jääk*11
    #    uu=sum2-u
    #    ln=uu
    #return ln
