import pygame
import datetime
from random import sample
algus = datetime.datetime.now()
pygame.init()
# Ekraani suurus
laius = 1200
kõrgus = 650
mäng = pygame.display.set_mode((laius, kõrgus))

# Laeb taustapildi
taustapilt = pygame.image.load('taustapilt.png')
taustapilt = pygame.transform.scale(taustapilt, (laius, kõrgus))

#Saad valida nuppudest mitu kaarti tahad sisestada
kaart2_valik = pygame.image.load('2kaarti.png')
kaart2_valik = pygame.transform.scale(kaart2_valik, (250, 70))

#Taust kirjale
taust_kirjale = pygame.image.load('taustaks.png')
objekt_suurus_taust_kirjale = (700, 500)
objekt_x_taust_kirjale, objekt_y_taust_kirjale = 270, 100
taust_kirjale = pygame.transform.scale(taust_kirjale, (objekt_suurus_taust_kirjale))

#Restart nupp
restartnupp = pygame.image.load('restart.png')
objekt_suurus_restartnupp = (200, 150)
objekt_x_restartnupp, objekt_y_restartnupp = 600, 500
restartnupp = pygame.transform.scale(restartnupp, (objekt_suurus_restartnupp))

#Arvuta nupp
arvutanupp = pygame.image.load('arvuta.png')
objekt_suurus_arvutanupp = (200, 150)
objekt_x_arvutanupp, objekt_y_arvutanupp = 300, 500
arvutanupp = pygame.transform.scale(arvutanupp, (objekt_suurus_arvutanupp))

#Millist font programm kasutab
font = pygame.font.Font(None, 30)
laius = mäng.get_width()
kõrgus = mäng.get_width()

#Defineerib objektide alguskohad. Samuti pärast restart nuppu otsib üles need väärtused ja viib kaardid sinna.
def algus():
    #Ruutuässa info
    global ruutuäss, objekt_x_ruutuäss, objekt_y_ruutuäss, objekt_suurus_ruutuäss
    ruutuäss = pygame.image.load('ruutuäss.png')
    objekt_suurus_ruutuäss = (70, 100)
    objekt_x_ruutuäss, objekt_y_ruutuäss = 5, 10  #Stardipositsioon
    
    #Ruutu2 info
    global ruutu2, objekt_suurus_ruutu2, objekt_x_ruutu2, objekt_y_ruutu2
    ruutu2 = pygame.image.load('ruutu2.png')
    objekt_suurus_ruutu2 = (70, 100)
    objekt_x_ruutu2, objekt_y_ruutu2 = 5, 10
    
    #Ruutu3 info
    global ruutu3, objekt_suurus_ruutu3, objekt_x_ruutu3, objekt_y_ruutu3
    ruutu3 = pygame.image.load('ruutu3.png')
    objekt_suurus_ruutu3 = (70, 100)
    objekt_x_ruutu3, objekt_y_ruutu3 = 5, 10
    
    #Ruutu4 info
    global ruutu4, objekt_suurus_ruutu4, objekt_x_ruutu4, objekt_y_ruutu4
    ruutu4 = pygame.image.load('ruutu4.png')
    objekt_suurus_ruutu4 = (70, 100)
    objekt_x_ruutu4, objekt_y_ruutu4 = 5, 10
    
    #Ruutu5 info
    global ruutu5, objekt_suurus_ruutu5, objekt_x_ruutu5, objekt_y_ruutu5
    ruutu5 = pygame.image.load('ruutu5.png')
    objekt_suurus_ruutu5 = (70, 100)
    objekt_x_ruutu5, objekt_y_ruutu5 = 5, 10
    
    #Ruutu6 info
    global ruutu6, objekt_suurus_ruutu6, objekt_x_ruutu6, objekt_y_ruutu6
    ruutu6 = pygame.image.load('ruutu6.png')
    objekt_suurus_ruutu6 = (70, 100)
    objekt_x_ruutu6, objekt_y_ruutu6 = 5, 10
    
    #Ruutu7 info
    global ruutu7, objekt_suurus_ruutu7, objekt_x_ruutu7, objekt_y_ruutu7
    ruutu7 = pygame.image.load('ruutu7.png')
    objekt_suurus_ruutu7 = (70, 100)
    objekt_x_ruutu7, objekt_y_ruutu7 = 5, 10
    
    #Ruutu8 info
    global ruutu8, objekt_suurus_ruutu8, objekt_x_ruutu8, objekt_y_ruutu8
    ruutu8 = pygame.image.load('ruutu8.png')
    objekt_suurus_ruutu8 = (70, 100)
    objekt_x_ruutu8, objekt_y_ruutu8 = 5, 10
    
    #Ruutu9 info
    global ruutu9, objekt_suurus_ruutu9, objekt_x_ruutu9, objekt_y_ruutu9
    ruutu9 = pygame.image.load('ruutu9.png')
    objekt_suurus_ruutu9 = (70, 100)
    objekt_x_ruutu9, objekt_y_ruutu9 = 5, 10
    
    #Ruutu10 info
    global ruutu10, objekt_suurus_ruutu10, objekt_x_ruutu10, objekt_y_ruutu10
    ruutu10 = pygame.image.load('ruutu10.png')
    objekt_suurus_ruutu10 = (70, 100)
    objekt_x_ruutu10, objekt_y_ruutu10 = 5, 10
    
    #RuutuJ info
    global ruutuJ, objekt_suurus_ruutuJ, objekt_x_ruutuJ, objekt_y_ruutuJ
    ruutuJ = pygame.image.load('ruutuJ.png')
    objekt_suurus_ruutuJ = (70, 100)
    objekt_x_ruutuJ, objekt_y_ruutuJ = 5, 10
    
    #RuutuQ info
    global ruutuQ, objekt_suurus_ruutuQ, objekt_x_ruutuQ, objekt_y_ruutuQ
    ruutuQ = pygame.image.load('ruutuQ.png')
    objekt_suurus_ruutuQ = (70, 100)
    objekt_x_ruutuQ, objekt_y_ruutuQ = 5, 10
    
    #RuutuK info
    global ruutuK, objekt_suurus_ruutuK, objekt_x_ruutuK, objekt_y_ruutuK
    ruutuK = pygame.image.load('ruutuK.png')
    objekt_suurus_ruutuK = (70, 100)
    objekt_x_ruutuK, objekt_y_ruutuK = 5, 10
    
    #Potiässa info
    global potiäss, objekt_x_potiäss, objekt_y_potiäss, objekt_suurus_potiäss
    potiäss = pygame.image.load('potiäss.png')
    objekt_suurus_potiäss = (70, 100)
    objekt_x_potiäss, objekt_y_potiäss = 5, 110
    
    #Poti2 info
    global poti2, objekt_suurus_poti2, objekt_x_poti2, objekt_y_poti2
    poti2 = pygame.image.load('poti2.png')
    objekt_suurus_poti2 = (70, 100)
    objekt_x_poti2, objekt_y_poti2 = 5, 110
    
    #Poti3 info
    global poti3, objekt_suurus_poti3, objekt_x_poti3, objekt_y_poti3
    poti3 = pygame.image.load('poti3.png')
    objekt_suurus_poti3 = (70, 100)
    objekt_x_poti3, objekt_y_poti3 = 5, 110
    
    #Poti4 info
    global poti4, objekt_suurus_poti4, objekt_x_poti4, objekt_y_poti4
    poti4 = pygame.image.load('poti4.png')
    objekt_suurus_poti4 = (70, 100)
    objekt_x_poti4, objekt_y_poti4 = 5, 110
    
    #Poti5 info
    global poti5, objekt_suurus_poti5, objekt_x_poti5, objekt_y_poti5
    poti5 = pygame.image.load('poti5.png')
    objekt_suurus_poti5 = (70, 100)
    objekt_x_poti5, objekt_y_poti5 = 5, 110
    
    #Poti6 info
    global poti6, objekt_suurus_poti6, objekt_x_poti6, objekt_y_poti6
    poti6 = pygame.image.load('poti6.png')
    objekt_suurus_poti6 = (70, 100)
    objekt_x_poti6, objekt_y_poti6 = 5, 110
    
    #Poti7 info
    global poti7, objekt_suurus_poti7, objekt_x_poti7, objekt_y_poti7
    poti7 = pygame.image.load('poti7.png')
    objekt_suurus_poti7 = (70, 100)
    objekt_x_poti7, objekt_y_poti7 = 5, 110
    
    #Poti8 info
    global poti8, objekt_suurus_poti8, objekt_x_poti8, objekt_y_poti8
    poti8 = pygame.image.load('poti8.png')
    objekt_suurus_poti8 = (70, 100)
    objekt_x_poti8, objekt_y_poti8 = 5, 110
    
    #Poti9 info
    global poti9, objekt_suurus_poti9, objekt_x_poti9, objekt_y_poti9
    poti9 = pygame.image.load('poti9.png')
    objekt_suurus_poti9 = (70, 100)
    objekt_x_poti9, objekt_y_poti9 = 5, 110
    
    #Poti10 info
    global poti10, objekt_suurus_poti10, objekt_x_poti10, objekt_y_poti10
    poti10 = pygame.image.load('poti10.png')
    objekt_suurus_poti10 = (70, 100)
    objekt_x_poti10, objekt_y_poti10 = 5, 110
    
    #PotiJ info
    global potiJ, objekt_suurus_potiJ, objekt_x_potiJ, objekt_y_potiJ
    potiJ = pygame.image.load('potiJ.png')
    objekt_suurus_potiJ = (70, 100)
    objekt_x_potiJ, objekt_y_potiJ = 5, 110
    
    #PotiQ info
    global potiQ, objekt_suurus_potiQ, objekt_x_potiQ, objekt_y_potiQ
    potiQ = pygame.image.load('potiQ.png')
    objekt_suurus_potiQ = (70, 100)
    objekt_x_potiQ, objekt_y_potiQ = 5, 110
    
    #PotiK info
    global potiK, objekt_suurus_potiK, objekt_x_potiK, objekt_y_potiK
    potiK = pygame.image.load('potiK.png')
    objekt_suurus_potiK = (70, 100)
    objekt_x_potiK, objekt_y_potiK = 5, 110
    
    #Ristiiässa info
    global ristiäss, objekt_x_ristiäss, objekt_y_ristiäss, objekt_suurus_ristiäss
    ristiäss = pygame.image.load('ristiäss.png')
    objekt_suurus_ristiäss = (70, 100)
    objekt_x_ristiäss, objekt_y_ristiäss = 5, 210
    
    #Risti2 info
    global risti2, objekt_suurus_risti2, objekt_x_risti2, objekt_y_risti2
    risti2 = pygame.image.load('risti2.png')
    objekt_suurus_risti2 = (70, 100)
    objekt_x_risti2, objekt_y_risti2 = 5, 210
    
    #Risti3 info
    global risti3, objekt_suurus_risti3, objekt_x_risti3, objekt_y_risti3
    risti3 = pygame.image.load('risti3.png')
    objekt_suurus_risti3 = (70, 100)
    objekt_x_risti3, objekt_y_risti3 = 5, 210
    
    #Risti4 info
    global risti4, objekt_suurus_risti4, objekt_x_risti4, objekt_y_risti4
    risti4 = pygame.image.load('risti4.png')
    objekt_suurus_risti4 = (70, 100)
    objekt_x_risti4, objekt_y_risti4 = 5, 210
    
    #Risti5 info
    global risti5, objekt_suurus_risti5, objekt_x_risti5, objekt_y_risti5
    risti5 = pygame.image.load('risti5.png')
    objekt_suurus_risti5 = (70, 100)
    objekt_x_risti5, objekt_y_risti5 = 5, 210
    
    #Risti6 info
    global risti6, objekt_suurus_risti6, objekt_x_risti6, objekt_y_risti6
    risti6 = pygame.image.load('risti6.png')
    objekt_suurus_risti6 = (70, 100)
    objekt_x_risti6, objekt_y_risti6 = 5, 210
    
    #Risti7 info
    global risti7, objekt_suurus_risti7, objekt_x_risti7, objekt_y_risti7
    risti7 = pygame.image.load('risti7.png')
    objekt_suurus_risti7 = (70, 100)
    objekt_x_risti7, objekt_y_risti7 = 5, 210
    
    #Risti8 info
    global risti8, objekt_suurus_risti8, objekt_x_risti8, objekt_y_risti8
    risti8 = pygame.image.load('risti8.png')
    objekt_suurus_risti8 = (70, 100)
    objekt_x_risti8, objekt_y_risti8 = 5, 210
    
    #Risti9 info
    global risti9, objekt_suurus_risti9, objekt_x_risti9, objekt_y_risti9
    risti9 = pygame.image.load('risti9.png')
    objekt_suurus_risti9 = (70, 100)
    objekt_x_risti9, objekt_y_risti9 = 5, 210
    
    #Risti10 info
    global risti10, objekt_suurus_risti10, objekt_x_risti10, objekt_y_risti10
    risti10 = pygame.image.load('risti10.png')
    objekt_suurus_risti10 = (70, 100)
    objekt_x_risti10, objekt_y_risti10 = 5, 210
    
    #RistiJ info
    global ristiJ, objekt_suurus_ristiJ, objekt_x_ristiJ, objekt_y_ristiJ
    ristiJ = pygame.image.load('ristiJ.png')
    objekt_suurus_ristiJ = (70, 100)
    objekt_x_ristiJ, objekt_y_ristiJ = 5, 210
    
    #RistiQ info
    global ristiQ, objekt_suurus_ristiQ, objekt_x_ristiQ, objekt_y_ristiQ
    ristiQ = pygame.image.load('ristiQ.png')
    objekt_suurus_ristiQ = (70, 100)
    objekt_x_ristiQ, objekt_y_ristiQ = 5, 210
    
    #RistiK info
    global ristiK, objekt_suurus_ristiK, objekt_x_ristiK, objekt_y_ristiK
    ristiK = pygame.image.load('ristiK.png')
    objekt_suurus_ristiK = (70, 100)
    objekt_x_ristiK, objekt_y_ristiK = 5, 210
    
    #Ärtuässa info
    global ärtuäss, objekt_x_ärtuäss, objekt_y_ärtuäss, objekt_suurus_ärtuäss
    ärtuäss = pygame.image.load('ärtuäss.png')
    objekt_suurus_ärtuäss = (70, 100)
    objekt_x_ärtuäss, objekt_y_ärtuäss = 5, 310
    
    #Ärtu2 info
    global ärtu2, objekt_suurus_ärtu2, objekt_x_ärtu2, objekt_y_ärtu2
    ärtu2 = pygame.image.load('ärtu2.png')
    objekt_suurus_ärtu2 = (70, 100)
    objekt_x_ärtu2, objekt_y_ärtu2 = 5, 310
    
    #Ärtu3 info
    global ärtu3, objekt_suurus_ärtu3, objekt_x_ärtu3, objekt_y_ärtu3
    ärtu3 = pygame.image.load('ärtu3.png')
    objekt_suurus_ärtu3 = (70, 100)
    objekt_x_ärtu3, objekt_y_ärtu3 = 5, 310
    
    #Ärtu4 info
    global ärtu4, objekt_suurus_ärtu4, objekt_x_ärtu4, objekt_y_ärtu4
    ärtu4 = pygame.image.load('ärtu4.png')
    objekt_suurus_ärtu4 = (70, 100)
    objekt_x_ärtu4, objekt_y_ärtu4 = 5, 310
    
    #Ärtu5 info
    global ärtu5, objekt_suurus_ärtu5, objekt_x_ärtu5, objekt_y_ärtu5
    ärtu5 = pygame.image.load('ärtu5.png')
    objekt_suurus_ärtu5 = (70, 100)
    objekt_x_ärtu5, objekt_y_ärtu5 = 5, 310
    
    #Ärtu6 info
    global ärtu6, objekt_suurus_ärtu6, objekt_x_ärtu6, objekt_y_ärtu6
    ärtu6 = pygame.image.load('ärtu6.png')
    objekt_suurus_ärtu6 = (70, 100)
    objekt_x_ärtu6, objekt_y_ärtu6 = 5, 310
    
    #Ärtu7 info
    global ärtu7, objekt_suurus_ärtu7, objekt_x_ärtu7, objekt_y_ärtu7
    ärtu7 = pygame.image.load('ärtu7.png')
    objekt_suurus_ärtu7 = (70, 100)
    objekt_x_ärtu7, objekt_y_ärtu7 = 5, 310
    
    #Ärtu8 info
    global ärtu8, objekt_suurus_ärtu8, objekt_x_ärtu8, objekt_y_ärtu8
    ärtu8 = pygame.image.load('ärtu8.png')
    objekt_suurus_ärtu8 = (70, 100)
    objekt_x_ärtu8, objekt_y_ärtu8 = 5, 310
    
    #Ärtu9 info
    global ärtu9, objekt_suurus_ärtu9, objekt_x_ärtu9, objekt_y_ärtu9
    ärtu9 = pygame.image.load('ärtu9.png')
    objekt_suurus_ärtu9 = (70, 100)
    objekt_x_ärtu9, objekt_y_ärtu9 = 5, 310
    
    #Ärtu10 info
    global ärtu10, objekt_suurus_ärtu10, objekt_x_ärtu10, objekt_y_ärtu10
    ärtu10 = pygame.image.load('ärtu10.png')
    objekt_suurus_ärtu10 = (70, 100)
    objekt_x_ärtu10, objekt_y_ärtu10 = 5, 310
    #ÄrtuJ info
    global ärtuJ, objekt_suurus_ärtuJ, objekt_x_ärtuJ, objekt_y_ärtuJ
    ärtuJ = pygame.image.load('ärtuJ.png')
    objekt_suurus_ärtuJ = (70, 100)
    objekt_x_ärtuJ, objekt_y_ärtuJ = 5, 310
    
    #ÄrtuQ info
    global ärtuQ, objekt_suurus_ärtuQ, objekt_x_ärtuQ, objekt_y_ärtuQ
    ärtuQ = pygame.image.load('ärtuQ.png')
    objekt_suurus_ärtuQ = (70, 100)
    objekt_x_ärtuQ, objekt_y_ärtuQ = 5, 310
    
    #ÄrtuK info
    global ärtuK, objekt_suurus_ärtuK, objekt_x_ärtuK, objekt_y_ärtuK
    ärtuK = pygame.image.load('ärtuK.png')
    objekt_suurus_ärtuK = (70, 100)
    objekt_x_ärtuK, objekt_y_ärtuK = 5, 310

#Käivitab funktsiooni
algus()

#Ekraani paremal poolel on kõik sama masti kaardid mängu alguses genereeritud samasse asukohta. See rida aitab programmil mängu loopis aru saada, milline mast valiti
rida_äss = ['ärtuäss', 'potiäss', 'ruutuäss', 'ristiäss']

#Siin on reana kõik risti masti kaardid.
rida_risti = ['ristiäss', 'risti2', 'risti3', 'risti4', 'risti5', 'risti6', 'risti7', 'risti8', 'risti9', 'risti10', 'ristiJ', 'ristiQ', 'ristiK']

#Siin on reana kõik ruutu masti kaardid.
rida_ruutu = ['ruutuäss', 'ruutu2', 'ruutu3', 'ruutu4', 'ruutu5', 'ruutu6', 'ruutu7', 'ruutu8', 'ruutu9', 'ruutu10', 'ruutuJ', 'ruutuQ', 'ruutuK']

#Siin on reana kõik poti masti kaardid.
rida_poti = ['potiäss', 'poti2', 'poti3', 'poti4', 'poti5', 'poti6', 'poti7', 'poti8', 'poti9', 'poti10', 'potiJ', 'potiQ', 'potiK']

#Siin on reana kõik ärtu masti kaardid.
rida_ärtu = ['ärtuäss', 'ärtu2', 'ärtu3', 'ärtu4', 'ärtu5', 'ärtu6', 'ärtu7', 'ärtu8', 'ärtu9', 'ärtu10', 'ärtuJ', 'ärtuQ', 'ärtuK']

#Siin on reana kõik võimalikud kaardid.
rida_kaardid = ['risti2', 'risti3', 'risti4', 'risti5', 'risti6', 'risti7', 'risti8', 'risti9', 'risti10', 'ristiJ', 'ristiQ', 'ristiK','ristiäss', 'ruutu2', 'ruutu3', 'ruutu4', 'ruutu5', 'ruutu6', 'ruutu7', 'ruutu8', 'ruutu9', 'ruutu10', 'ruutuJ', 'ruutuQ', 'ruutuK','ruutuäss', 'poti2', 'poti3', 'poti4', 'poti5', 'poti6', 'poti7', 'poti8', 'poti9', 'poti10', 'potiJ', 'potiQ', 'potiK','potiäss', 'ärtu2', 'ärtu3', 'ärtu4', 'ärtu5', 'ärtu6', 'ärtu7', 'ärtu8', 'ärtu9', 'ärtu10', 'ärtuJ', 'ärtuQ', 'ärtuK', 'ärtuäss']



###
kaartide_väärtused = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

kaartide_väärtused_sõnastik = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}

kaardid = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',]

kaardipaarid_kõik = [] #lisame kõik võimalikud kahekaardilised käed pokkeris
for i in range(51):
    for j in range(i+1,52):
        kaardipaarid_kõik.append(kaardid[i] + " " + kaardid[j])
kaardipaar = ['2♣ 2♥', '2♣ 3♥', '2♣ 4♥', '2♣ 5♥', '2♣ 6♥', '2♣ 7♥', '2♣ 8♥', '2♣ 9♥', '2♣ 10♥', '2♣ J♥', '2♣ Q♥', '2♣ K♥', '2♣ A♥', '3♣ 3♥', '3♣ 4♥', '3♣ 5♥', '3♣ 6♥', '3♣ 7♥', '3♣ 8♥', '3♣ 9♥', '3♣ 10♥', '3♣ J♥', '3♣ Q♥', '3♣ K♥', '3♣ A♥', '4♣ 4♥', '4♣ 5♥', '4♣ 6♥', '4♣ 7♥', '4♣ 8♥', '4♣ 9♥', '4♣ 10♥', '4♣ J♥', '4♣ Q♥', '4♣ K♥', '4♣ A♥', '5♣ 5♥', '5♣ 6♥', '5♣ 7♥', '5♣ 8♥', '5♣ 9♥', '5♣ 10♥', '5♣ J♥', '5♣ Q♥', '5♣ K♥', '5♣ A♥', '6♣ 6♥', '6♣ 7♥', '6♣ 8♥', '6♣ 9♥', '6♣ 10♥', '6♣ J♥', '6♣ Q♥', '6♣ K♥', '6♣ A♥', '7♣ 7♥', '7♣ 8♥', '7♣ 9♥', '7♣ 10♥', '7♣ J♥', '7♣ Q♥', '7♣ K♥', '7♣ A♥', '8♣ 8♥', '8♣ 9♥', '8♣ 10♥', '8♣ J♥', '8♣ Q♥', '8♣ K♥', '8♣ A♥', '9♣ 9♥', '9♣ 10♥', '9♣ J♥', '9♣ Q♥', '9♣ K♥', '9♣ A♥', '10♣ 10♥', '10♣ J♥', '10♣ Q♥', '10♣ K♥', '10♣ A♥', 'J♣ J♥', 'J♣ Q♥', 'J♣ K♥', 'J♣ A♥', 'Q♣ Q♥', 'Q♣ K♥', 'Q♣ A♥', 'K♣ K♥', 'K♣ A♥', 'A♣ A♥', '2♥ 3♥', '2♥ 4♥', '2♥ 5♥', '2♥ 6♥', '2♥ 7♥', '2♥ 8♥', '2♥ 9♥', '2♥ 10♥', '2♥ J♥', '2♥ Q♥', '2♥ K♥', '2♥ A♥', '3♥ 4♥', '3♥ 5♥', '3♥ 6♥', '3♥ 7♥', '3♥ 8♥', '3♥ 9♥', '3♥ 10♥', '3♥ J♥', '3♥ Q♥', '3♥ K♥', '3♥ A♥', '4♥ 5♥', '4♥ 6♥', '4♥ 7♥', '4♥ 8♥', '4♥ 9♥', '4♥ 10♥', '4♥ J♥', '4♥ Q♥', '4♥ K♥', '4♥ A♥', '5♥ 6♥', '5♥ 7♥', '5♥ 8♥', '5♥ 9♥', '5♥ 10♥', '5♥ J♥', '5♥ Q♥', '5♥ K♥', '5♥ A♥', '6♥ 7♥', '6♥ 8♥', '6♥ 9♥', '6♥ 10♥', '6♥ J♥', '6♥ Q♥', '6♥ K♥', '6♥ A♥', '7♥ 8♥', '7♥ 9♥', '7♥ 10♥', '7♥ J♥', '7♥ Q♥', '7♥ K♥', '7♥ A♥', '8♥ 9♥', '8♥ 10♥', '8♥ J♥', '8♥ Q♥', '8♥ K♥', '8♥ A♥', '9♥ 10♥', '9♥ J♥', '9♥ Q♥', '9♥ K♥', '9♥ A♥', '10♥ J♥', '10♥ Q♥', '10♥ K♥', '10♥ A♥', 'J♥ Q♥', 'J♥ K♥', 'J♥ A♥', 'Q♥ K♥', 'Q♥ A♥', 'K♥ A♥']

kaardid_risti = kaardid[:13]
kaardid_ärtu = kaardid[13:26]

def kaartide_järjestus(kaart):
    järjestus = {"A":13, "K":12, "Q":11, "J":10, "10":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
    return järjestus[kaart[:-1]]


def hand_ranking(käsi): #erineva tugevusega käte võrdlemiseks
    käed = ["kõrge", "paar", "kaks paari", "kolmik", "rida", "mast", "maja","nelik", "mastirida", "kuninglik mastirida"]
    return käed.index(käsi)
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
            a = kaartide_järjestus(viis_kaarti(kaardid1)[i])
            b = kaartide_järjestus(viis_kaarti(kaardid2)[i])
            if a > b:
                return "Esimene"
            if a < b:
                return "Teine"
    return "Viik"

def preflop():
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

#Eestikeelesetes sõnastikes uurides leidsin, et kõige sagedasemani kasutatakse eestikeeles ingliskeerlseid väljendeid preflop, flop, turn, river (sellest inspireeritune ka nimed funktsioonidele)
def flop(a, b, c, d, e):
    luger = 0
    kaart1 = kaardid[a] #Valime kaartide nimistust suvalised kaardid mis võiks olla laual
    kaart2 = kaardid[b]
    flop1 = kaardid[c]
    flop2 = kaardid[d]
    flop3 = kaardid[e]
    print(kaart1, kaart2, flop1, flop2, flop3)
    kaardid1 = kaardid.copy()
    kaardid1.remove(kaart1)
    kaardid1.remove(kaart2)
    kaardid1.remove(flop1)
    kaardid1.remove(flop2)
    kaardid1.remove(flop3)
    for k in range(10000):
        neli = sample(kaardid1, 4)
        laud = sample(neli, 2)
        neli.extend([flop1, flop2, flop3])
        laud.extend([kaart1, kaart2, flop1, flop2, flop3])
        tulemus = kumb_võidab(laud, neli)
        if tulemus == "Esimene":
            luger += 1
        elif tulemus == "Viik":
            luger += 0.5
    return luger

def turn(a, b, c, d, e, f):
    luger = 0
    kaart1 = kaardid[a] #Valime kaartide nimistust suvalised kaardid mis võiks olla laual
    kaart2 = kaardid[b]
    flop1 = kaardid[c]
    flop2 = kaardid[d]
    flop3 = kaardid[e]
    turn = kaardid[f]
    print(kaart1, kaart2, flop1, flop2, flop3, turn)
    kaardid1 = kaardid.copy()
    kaardid1.remove(kaart1)
    kaardid1.remove(kaart2)
    kaardid1.remove(flop1)
    kaardid1.remove(flop2)
    kaardid1.remove(flop3)
    kaardid1.remove(turn)
    for k in range(10000):
        kolm = sample(kaardid1, 3)
        laud = sample(kolm, 1)
        kolm.extend([flop1, flop2, flop3, turn])
        laud.extend([kaart1, kaart2, flop1, flop2, flop3, turn])
        tulemus = kumb_võidab(laud, kolm)
        if tulemus == "Esimene":
            luger += 1
        elif tulemus == "Viik":
            luger += 0.5
    return luger


def river(a, b, c, d, e, f, g):
    luger = 0
    kaart1 = kaardid[a] #Valime kaartide nimistust suvalised kaardid mis võiks olla laual
    kaart2 = kaardid[b]
    flop1 = kaardid[c]
    flop2 = kaardid[d]
    flop3 = kaardid[e]
    turn = kaardid[f]
    river = kaardid[g]
    print(kaart1, kaart2, flop1, flop2, flop3, turn, river)
    kaardid1 = kaardid.copy()
    kaardid1.remove(kaart1)
    kaardid1.remove(kaart2)
    kaardid1.remove(flop1)
    kaardid1.remove(flop2)
    kaardid1.remove(flop3)
    kaardid1.remove(turn)
    kaardid1.remove(river)
    for k in range(10000):
        kaks = sample(kaardid1, 2)
        kaks.extend([flop1, flop2, flop3, turn, river])
        laud = [kaart1, kaart2, flop1, flop2, flop3, turn, river]
        tulemus = kumb_võidab(laud, kaks)
        if tulemus == "Esimene":
            luger += 1
        elif tulemus == "Viik":
            luger += 0.5
    return luger

###




#Alguses tühi sõnastik, mis hiljem salvestab nende kaartide infod, mis on valitud mänguks
asukohad = {}

#Mängus kasutuses olevaid kaarte saab valida, kui selle väärtus on True
kaardid_valitud = False

#Mitmes mängus olev kaart on valitud
mitmes = 0

kaart1 = ''
kaart2 = ''
programm_käib = True
while programm_käib:
    
    #Aitab visuaalselt paremini eristada, millised kaardid on mängijal endal käes ning millised on mängulaual
    if mitmes < 2:
        kaardi_koht_vajutades = 300 + mitmes*75, 150
    else:
        kaardi_koht_vajutades = 400 + mitmes*75, 150
        
    hiir = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                programm_käib = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #See on restartnupp, mis põhimõtteliselt taastab mängu sarnasesse olekusse nagu ta on, kui programm käivitada
            if objekt_x_restartnupp <= hiir[0] <= objekt_x_restartnupp + objekt_suurus_restartnupp[0] and objekt_y_restartnupp <= hiir[1] <= objekt_y_restartnupp + objekt_suurus_restartnupp[1]:
                algus()
                kaardid_valitud = False
                mitmes = 0
                asukohad = {}
            if mitmes == 2 or mitmes == 5 or mitmes == 6 or mitmes == 7:
                if objekt_x_arvutanupp <= hiir[0] <= objekt_x_arvutanupp + objekt_suurus_arvutanupp[0] and objekt_y_arvutanupp <= hiir[1] <= objekt_y_arvutanupp + objekt_suurus_arvutanupp[1]:
                    if mitmes == 2:
                        
                        
            
            #See programmilõik kontrollib, milline mast on valitud
            for i in rida_äss:
                if globals()[f'objekt_x_{i}'] <= hiir[0] <= globals()[f'objekt_x_{i}'] + 70 and globals()[f'objekt_y_{i}'] <= hiir[1] <= globals()[f'objekt_y_{i}'] + 100:
                    
                    #Arvutab kaartide kohad mastikaarti valides
                    arvuta_koht = [130, 5]
                    
                    #Kui mast on ärtu
                    if rida_äss.index(i) == 0:
                        
                        #Funktsiooni väljakutsumine on vajalik, kuna programm laob kõik sama väärtustega kaardid(erinevad mastid) samasse kohta ekraanil. Valides teistsugune mast, viib funktsioon kaardid oma algesse positsiooni, et neid ei pandaks üksteise otsa.
                        algus()
                        for ärtu in rida_ärtu:
                            globals()[f'objekt_x_{ärtu}'], globals()[f'objekt_y_{ärtu}'] = arvuta_koht
                            
                            #Iga uus kaart viiakse natukene parenale
                            arvuta_koht[0] += 75
                            kaardid_valitud = True
                    
                    #Kui mast on poti
                    if rida_äss.index(i) == 1:
                        algus()
                        for poti in rida_poti:
                            globals()[f'objekt_x_{poti}'], globals()[f'objekt_y_{poti}'] = arvuta_koht
                            arvuta_koht[0] += 75
                            kaardid_valitud = True
                            
                    #Kui mast on ruutu
                    if rida_äss.index(i) == 2:
                        algus()
                        for ruutu in rida_ruutu:
                            globals()[f'objekt_x_{ruutu}'], globals()[f'objekt_y_{ruutu}'] = arvuta_koht
                            arvuta_koht[0] += 75
                            kaardid_valitud = True
                            
                    #Kui mast on risti
                    if rida_äss.index(i) == 3:
                        algus()
                        for risti in rida_risti:
                            globals()[f'objekt_x_{risti}'], globals()[f'objekt_y_{risti}'] = arvuta_koht
                            arvuta_koht[0] += 75
                            kaardid_valitud = True
            
            #Kui mastikaart on valitud, hakkab see programmilõik alles tööle
            if kaardid_valitud == True:
                
                #Programmilõik käib läbi kõik võimalikud kaardid ning vajutades kaardi asukohale, transpordib see selle allapoole
                for kaart in rida_kaardid:
                    
                    #Rohkem kui 7 kaarti ei saa valida ning kui y väärtus on liiga suur, ehk kaardid on juba valitud ning transporditud allapoole, siis ei saa neid allpool aktiveerida
                    if globals()[f'objekt_x_{kaart}'] <= hiir[0] <= globals()[f'objekt_x_{kaart}'] + 70 and globals()[f'objekt_y_{kaart}'] <= hiir[1] <= globals()[f'objekt_y_{kaart}'] + 100 and mitmes < 7 and globals()[f'objekt_x_{kaart}'] > 100:
                        globals()[f'objekt_x_{kaart}'], globals()[f'objekt_y_{kaart}'] = kaardi_koht_vajutades
                        
                        #Lisab sõnastikku kaardi nime ja selle kordinaadid
                        asukohad[kaart] = kaardi_koht_vajutades
                        mitmes += 1
                        
                        if mitmes == 1:
                            kaart1_index = rida_kaardid.index(kaart)
                            kaart1 = kaardid[kaart1_index]
                        if mitmes == 2:
                            kaart2_index = rida_kaardid.index(kaart)
                            kaart2 = kaardid[kaart1_index]
            #Kuna iga kord kui masti vahetatakse, kutsutakse välja algus(), siis aitab sõnastik meelde jätta millised kaardid on valitud ja transpordib nad nende kohtadele koguaeg tagasi.
            for kaart in rida_kaardid:
                if kaart in asukohad:
                    globals()[f'objekt_x_{kaart}'], globals()[f'objekt_y_{kaart}'] = asukohad[kaart]
                    
                    
    # Pärast iga tsükklit värskendab asukohtasid
    #Teised nupud ja taustapilt
    mäng.blit(taustapilt, (0, 0))
    mäng.blit(restartnupp, (objekt_x_restartnupp, objekt_y_restartnupp, * objekt_suurus_restartnupp))
    mäng.blit(arvutanupp, (objekt_x_arvutanupp, objekt_y_arvutanupp, * objekt_suurus_arvutanupp))
    mäng.blit(taust_kirjale, (objekt_x_taust_kirjale, objekt_y_taust_kirjale, * objekt_suurus_taust_kirjale))
    
    #Värskendab iga kaardi asukohta
    for kaart in rida_kaardid:
        mäng.blit(globals()[f'{kaart}'], (globals()[f'objekt_x_{kaart}'], globals()[f'objekt_y_{kaart}'], * globals()[f'objekt_suurus_{kaart}']))

    pygame.display.update()
pygame.quit()