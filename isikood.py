from omamoodul import *
ikoodid = []
arvud = ["100","1001","211"]
ikood=""
while True:
    ikood=input("Sisesta isikukood")
    if ikood == "-" : break
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
        arvud.append(ikood)
    else:
        print("11 sümbolid")
        s=sugu(ikood)
        print(ikood[10])
        if s =="viga":
            print("Esimine täht ei ole õige")
            arvud.append(ikood)
            print(arvud)
        else:
            if kuud(ikood) == False:
                print("viga neli number")
                arvud.append(ikood)
                print(arvud)
            else:
                if päev(ikood)==False:
                    print("viga kuus number")
                    arvud.append(ikood)
                    print(arvud)
                else:
                    ss=sunnipaev
                    if sunnipaev(ikood)=="viga":
                        print("2-7 tähed on valesti sisestatud")
                        arvud.append(ikood)
                        print(arvud)
                    else:
                        viiamne
                        if viiamne(ikood) != int((ikood[10])):
                            print("viga viimane number")
                            print(viiamne(ikood))
                            arvud.append(ikood)
                            print(arvud)
                        else:
                            sunnipaev1=(sunnipaev(ikood))
                            sunnikoht1= sunnikoht(ikood)
                            print(f"See on {s}, tema sünnipäev {sunnipaev1} ja sünnikoht {sunnikoht1}.")
                            ikoodid.append(ikood)
                            print(ikoodid)

print()
naised_mehed(ikoodid)
print(ikoodid)
arvud=arvus_sorted(arvud)
print(arvud)


