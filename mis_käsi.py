################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Pokkerimängu abivahend
#
#
# Autorid:Vahur paist, (Tristan Imala)
#
#
##################################################
import datetime
from random import sample
algus = datetime.datetime.now()

kaartide_väärtused = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

kaartide_väärtused_sõnastik = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}

kaardid = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']

kaardipaar = [] #loome sellise faili kus on minimaalne arv kaardipaare, et programm lõpus jookseks kordades kiiremini (pole mõtet eraldi vaadelda näiteks käte 7♣8♥ ja 7♦8♥ tugevusi kui nad on täiesti sümmetrilised igat moodi (nii saame sisendite arvu ca 1300 pealt 169-le)
kaardid_risti = kaardid[:13]
kaardid_ärtu = kaardid[13:26]
for i in range(13):
    for j in range(i,13):
        kaardipaar.append(kaardid_risti[i] + " " + kaardid_ärtu[j])
for i in range(12):
    for j in range(i+1,13):
        kaardipaar.append(kaardid_ärtu[i] + " " + kaardid_ärtu[j])
def kaartide_järjestus(kaart):
    järjestus = {"A":13, "K":12, "Q":11, "J":10, "10":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
    return järjestus[kaart[:-1]]


def hand_ranking(käsi): #erineva tugevusega käte võrdlemiseks
    käed = ["kõrge", "paar", "kaks paari", "kolmik", "rida", "mast", "maja","nelik", "mastirida", "kuninglik mastirida"]
    return käed.index(käsi)


#Defineerime funktsioonid millega saame tuvastada mis käsi kasutajal on

def mitmik_maja(laua_järjend): #paar, kaks paari kolmiku ja neliku funktsioon (annad seitse kaarti ning tagastab mis on)
    luger = 0 #loeme palju paare on (kolmikud j anelikud pole paarid)
    tagastus = []
    ilma_mastita = [] #kui sisendis on ka mastid siis oleks hea kuikood selle pärast katki ei läheks, standardne esitus kaartidele on kaart_mast (kokkukirjutatuna) inglisekeeles nt ace of hearts ehk A♥
    for i in range(7):
        ilma_mastita.append(laua_järjend[i][:-1])
    for kaart in kaartide_väärtused:
        if ilma_mastita.count(kaart) == 4:
            return "nelik"
        elif ilma_mastita.count(kaart) == 3:
            tagastus += ["kolmik"]
        elif ilma_mastita.count(kaart) == 2:
            luger += 1
    if luger >= 2:
        if "kolmik" in tagastus:
            return "maja"
        else:
            return "kaks paari"
    if luger == 1:
        if "kolmik" in tagastus:
            return "maja"
        else:
            return "paar"
    if "kolmik" in tagastus:
        if tagastus.count("kolmik") >= 2:
            return "maja"
        return "kolmik"
    return "kõrge"


def mast(laua_järjend):
    laua_mastid = [laua_järjend[i][-1] for i in range(7)]
    for mast in laua_mastid:
        if laua_mastid.count(mast) >= 5:
            return "mast"
    return False


def rida(laua_järjend):
    laua_väärtused = sorted(laua_järjend, key=kaartide_järjestus)
    laua_väärtused = [laua_väärtused[i][:-1] for i in range(7)]
    if "A" in laua_väärtused and "2" in laua_väärtused and "3" in laua_väärtused and "4" in laua_väärtused and "5" in laua_väärtused:
        return "rida"
    for j in range(3):
        luger = 0
        for i in range(4):
            if kaartide_väärtused_sõnastik[laua_väärtused[i+j+1]]-kaartide_väärtused_sõnastik[laua_väärtused[i+j]] == 1:
                luger += 1
                if luger == 4:
                    return "rida"
            else:
                luger = 0
    return False


def mis_käsi(käsi): #põhiprogramm mis võtab kõik kokku ning tagastab mis käsi on
    if mitmik_maja(käsi) in ["maja", "nelik"]:
        return mitmik_maja(käsi)
    if mast(käsi) == "mast":
        return "mast"
    if rida(käsi) == "rida":
        return "rida"
    else:
        return mitmik_maja(käsi)

def viis_kaarti(käsi): #programm mis tagastab viis kaarti millest käsi koosneb
    viisik = []
    käsi = sorted(käsi, key=kaartide_järjestus, reverse=True)
    käsi1 = [käsi[i][:-1] for i in range(7)]
    väärtus = mis_käsi(käsi)
    if väärtus == "mast":
        mastid = [käsi[i][-1] for i in range(7)]
        for el in mastid:
            if mastid.count(el) >= 5:
                mast = el
                break
        for el in käsi:
            if el[-1] == mast:
                viisik.append(el)
                if len(viisik) == 5:
                    return viisik
    if väärtus == "maja":
        c = 0
        for i in range(7):
            if käsi1.count(käsi1[i]) == 3 and c == 0:
                viisik.append(käsi[i])
                if len(viisik) == 3:
                    c = 1
        for i in range(7):
            if käsi1.count(käsi1[i]) == 2:
                viisik.append(käsi[i])
                if len(viisik) == 5:
                    return viisik
    if väärtus == "nelik":
        for i in range(7):
            if käsi1.count(käsi1[i]) == 4:
                viisik.append(käsi[i])
        for i in range(7):
            if käsi1.count(käsi1[i]) != 4:
                viisik.append(käsi[i])
                return viisik
    if väärtus == "rida":
        if "A" in käsi1 and "2" in käsi1 and "3" in käsi1 and "4" in käsi1 and "5" in käsi1:
            viisik.append(käsi[käsi1.index("5")])
            viisik.append(käsi[käsi1.index("4")])
            viisik.append(käsi[käsi1.index("3")])
            viisik.append(käsi[käsi1.index("2")])
            viisik.append(käsi[käsi1.index("A")])
            return viisik
        for i in range(3):
            luger = 0
            viisik = [käsi[i]]
            for j in range(4):
                if kaartide_väärtused_sõnastik[käsi1[i + j]] - kaartide_väärtused_sõnastik[käsi1[i + j + 1]] == 1:
                    viisik.append(käsi[i + j + 1])
                    luger += 1
                    if luger == 4:
                        return viisik
    if väärtus == "kolmik":
        for i in range(7):
            if käsi1.count(käsi1[i]) == 3:
                viisik.append(käsi[i])
        for i in range(7):
            if käsi1.count(käsi1[i]) == 1:
                viisik.append(käsi[i])
                if len(viisik) == 5:
                    return viisik
    if väärtus == "paar" or väärtus == "kaks paari":
        for i in range(7):
            if käsi1.count(käsi1[i]) == 2:
                viisik.append(käsi[i])
                if len(viisik) == 4:
                    break
        for i in range(7):
            if käsi1.count(käsi1[i]) == 1:
                viisik.append(käsi[i])
                if len(viisik) == 5:
                    return viisik
    else:
        return [käsi[i] for i in range(5)]


def kumb_võidab(kaardid1, kaardid2): #funktsioon mis võtab sisendiks kaks kätt ning tagastab kas "Esimene", "Teine" või "Viik" vastavalt kaartidevahelisele rankingule
    if mis_käsi(kaardid1) != mis_käsi(kaardid2):
        if hand_ranking(mis_käsi(kaardid1)) > hand_ranking(mis_käsi(kaardid2)):
            return "Esimene"
        else:
            return "Teine"
    else:
        for i in range(5):
            if kaartide_järjestus(viis_kaarti(kaardid1)[i]) > kaartide_järjestus(viis_kaarti(kaardid2)[i]):
                return "Esimene"
        for i in range(5):
            if kaartide_järjestus(viis_kaarti(kaardid1)[i]) < kaartide_järjestus(viis_kaarti(kaardid2)[i]):
                return "Teine"
    return "Viik"

def main():
    väljund = {}
    for i in range(len(kaardipaar)):
        luger = 0
        järjend = kaardipaar[i].split()
        kaart1 = järjend[0]
        kaart2 = järjend[1]
        kaardid1 = kaardid.copy()
        kaardid1.remove(kaart1)
        kaardid1.remove(kaart2)
        for k in range(500000):
            seitse = sample(kaardid1,7)
            laud = sample(seitse, 5)
            laud.append(kaart1)
            laud.append(kaart2)
            tulemus = kumb_võidab(laud, seitse)
            if tulemus == "Esimene":
                luger += 1
            elif tulemus == "Viik":
                luger += 0.5

        väljund[kaardipaar[i]] = luger
    sorteeritud_väljund = dict(sorted(väljund.items(), key=lambda item: item[1], reverse=True))
    print(sorteeritud_väljund)
    return(sorteeritud_väljund)



if __name__ == "__main__":
    main()
print(datetime.datetime.now()-algus)

