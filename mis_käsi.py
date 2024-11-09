#mõte, et kasutaja sisestab lihtsalt mis käsi tal on preflop ning siis tagastatakse kui
#suurest hulgast kätest ta käsi parem on.
mastide_sõnastik = {
    "risti" : "\u2663",
    "clubs" : "\u2663",
    "c" : "\u2663",
    "ri" : "\u2663",
    "ärtu" : "\u2665",
    "hearts" : "\u2665",
    "h" : "\u2665",
    "är" : "\u2665",
    "ruutu" : "\u2666",
    "diamonds" : "\u2666",
    "d" : "\u2666",
    "ru" : "\u2666",
    "poti" : "\u2660",
    "spades" : "\u2660",
    "s" : "\u2660",
    "po" : "\u2660",
}
kaartide_väärtused = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

kaartide_väärtused_sõnastik = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}

kaardid = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']

def kaartide_järjestus(kaart):
    järjestus = {"A":13, "K":12, "Q":11, "J":10, "10":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
    return järjestus[kaart]


def hand_ranking(käsi): #erineva tugevusega käte võrdlemiseks
    käed = ["kõrge", "paar", "kaks paari", "kolmik", "rida", "mast", "maja", "mastirida", "kuninglik mastirida"]
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
    return "Kõrge"


def mast(laua_järjend):
    laua_mastid = [laua_järjend[i][-1] for i in range(7)]
    for mast in laua_mastid:
        if laua_mastid.count(mast) >= 5:
            return "mast"
    return False


def rida(laua_järjend):
    laua_väärtused = [laua_järjend[i][:-1] for i in range(7)]
    laua_väärtused = sorted(laua_väärtused, key=kaartide_järjestus)
    luger = 0
    if "A" in laua_väärtused and "2" in laua_väärtused and "3" in laua_väärtused and "4" in laua_väärtused and "5" in laua_väärtused:
        print("AAA")
        return "rida"
    for i in range(6):
        if kaartide_väärtused_sõnastik[laua_väärtused[i+1]]-kaartide_väärtused_sõnastik[laua_väärtused[i]] == 1:
            luger += 1
            if luger == 4:
                return "rida"
        else:
            luger = 0
    return False


def main(): #põhiprogramm mis võtab kõik kokku ning väljastab (ja ka tagastab) mis käsi on
    käsi = input("Sisesta käsi: ")
    käsi = käsi.split()
    if mitmik_maja(käsi) in ["maja", "nelik"]:
        print(mitmik_maja(käsi))
        return mitmik_maja(käsi)
    if mast(käsi) == "mast":
        print("mast")
        return "mast"
    if rida(käsi) == "rida":
        print("rida")
        return "rida"
    else:
        print(mitmik_maja(käsi))
        return mitmik_maja(käsi)


if __name__ == "__main__": #lihtsalt proovimiseks tehtud - saab mistahes käe sisse panna kujul 2x 7y 3x Kx Ax 5y Jz ning tagastab mis väärtus on
    while True:
        main()
