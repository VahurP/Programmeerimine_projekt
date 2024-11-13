import pygame
################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Pokkerimängu abivahend
#
#
# Autorid:(Vahur paist), Tristan Imala
#
#
##################################################
pygame.init()
# Setting game window dimensions
laius = 1200
kõrgus = 650
game_display = pygame.display.set_mode((laius, kõrgus))
# Loading the image
taustapilt = pygame.image.load('tasut.jpg')
taustapilt = pygame.transform.scale(taustapilt, (laius, kõrgus))
#Taust kirjale
taust_kirjale = pygame.image.load('taustaks.png')
object_size_taust_kirjale = (700, 500)
object_x_taust_kirjale, object_y_taust_kirjale = 270, 100
taust_kirjale = pygame.transform.scale(taust_kirjale, (object_size_taust_kirjale))
#Sama masti nupp
mastinupp = pygame.image.load('mastinupp.png')
object_size_mastinupp = (200, 150)
object_x_mastinupp, object_y_mastinupp = 900, 500
mastinupp = pygame.transform.scale(mastinupp, (object_size_mastinupp))
mastinuppvärv = 'valge'
#Restart nupp
restartnupp = pygame.image.load('restart.png')
object_size_restartnupp = (200, 150)
object_x_restartnupp, object_y_restartnupp = 600, 500
restartnupp = pygame.transform.scale(restartnupp, (object_size_restartnupp))
#Arvuta nupp
arvutanupp = pygame.image.load('arvuta.png')
object_size_arvutanupp = (200, 150)
object_x_arvutanupp, object_y_arvutanupp = 300, 500
arvutanupp = pygame.transform.scale(arvutanupp, (object_size_arvutanupp))
font = pygame.font.Font(None, 30)
timer = pygame.time.Clock()
laius = game_display.get_width()
kõrgus = game_display.get_width()

def kaartide_järjestus(kaart):
    järjestus = {"A":13, "K":12, "Q":11, "J":10, "10":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
    return järjestus[kaart]
sisend1 = 'n'
def algus():
    #Ruutuässa info
    global ruutuäss, object_x_ruutuäss, object_y_ruutuäss, object_size_ruutuäss
    ruutuäss = pygame.image.load('ruutuäss.png')
    object_size_ruutuäss = (70, 100)
    object_x_ruutuäss, object_y_ruutuäss = 5, 10  # Start position
    #Ruutu2 info
    global ruutu2, object_size_ruutu2, object_x_ruutu2, object_y_ruutu2
    ruutu2 = pygame.image.load('ruutu2.png')
    object_size_ruutu2 = (70, 100)
    object_x_ruutu2, object_y_ruutu2 = 5, 110
    #Ruutu3 info
    global ruutu3, object_size_ruutu3, object_x_ruutu3, object_y_ruutu3
    ruutu3 = pygame.image.load('ruutu3.png')
    object_size_ruutu3 = (70, 100)
    object_x_ruutu3, object_y_ruutu3 = 5, 210    
    #Ruutu4 info
    global ruutu4, object_size_ruutu4, object_x_ruutu4, object_y_ruutu4
    ruutu4 = pygame.image.load('ruutu4.png')
    object_size_ruutu4 = (70, 100)
    object_x_ruutu4, object_y_ruutu4 = 5, 310
    #Ruutu5 info
    global ruutu5, object_size_ruutu5, object_x_ruutu5, object_y_ruutu5
    ruutu5 = pygame.image.load('ruutu5.png')
    object_size_ruutu5 = (70, 100)
    object_x_ruutu5, object_y_ruutu5 = 5, 410
    #Ruutu6 info
    global ruutu6, object_size_ruutu6, object_x_ruutu6, object_y_ruutu6
    ruutu6 = pygame.image.load('ruutu6.png')
    object_size_ruutu6 = (70, 100)
    object_x_ruutu6, object_y_ruutu6 = 5, 510
    #Ruutu7 info
    global ruutu7, object_size_ruutu7, object_x_ruutu7, object_y_ruutu7
    ruutu7 = pygame.image.load('ruutu7.png')
    object_size_ruutu7 = (70, 100)
    object_x_ruutu7, object_y_ruutu7 = 85, 10
    #Ruutu8 info
    global ruutu8, object_size_ruutu8, object_x_ruutu8, object_y_ruutu8
    ruutu8 = pygame.image.load('ruutu8.png')
    object_size_ruutu8 = (70, 100)
    object_x_ruutu8, object_y_ruutu8 = 85, 110
    #Ruutu9 info
    global ruutu9, object_size_ruutu9, object_x_ruutu9, object_y_ruutu9
    ruutu9 = pygame.image.load('ruutu9.png')
    object_size_ruutu9 = (70, 100)
    object_x_ruutu9, object_y_ruutu9 = 85, 210
    #Ruutu10 info
    global ruutu10, object_size_ruutu10, object_x_ruutu10, object_y_ruutu10
    ruutu10 = pygame.image.load('ruutu10.png')
    object_size_ruutu10 = (70, 100)
    object_x_ruutu10, object_y_ruutu10 = 85, 310
    #RuutuJ info
    global ruutuJ, object_size_ruutuJ, object_x_ruutuJ, object_y_ruutuJ
    ruutuJ = pygame.image.load('ruutuJ.png')
    object_size_ruutuJ = (70, 100)
    object_x_ruutuJ, object_y_ruutuJ = 85, 410
    #RuutuQ info
    global ruutuQ, object_size_ruutuQ, object_x_ruutuQ, object_y_ruutuQ
    ruutuQ = pygame.image.load('ruutuQ.png')
    object_size_ruutuQ = (70, 100)
    object_x_ruutuQ, object_y_ruutuQ = 85, 510
    #RuutuK info
    global ruutuK, object_size_ruutuK, object_x_ruutuK, object_y_ruutuK
    ruutuK = pygame.image.load('ruutuK.png')
    object_size_ruutuK = (70, 100)
    object_x_ruutuK, object_y_ruutuK = 165, 10
    
    global tekst1, tekst2, object_x_tekst1, object_y_tekst1, object_x_tekst2, object_y_tekst2
    tekst1 = pygame.image.load('tühi.jpg')
    tekst2 = pygame.image.load('tühi.jpg')
    object_x_tekst1, object_y_tekst1 = 10000, 10000
    object_x_tekst2, object_y_tekst2 = 10000, 10000
algus()

mitmes = 0 #See aitab programmil meelde jätta, mitmes kaart on valitud, et ta viiks ta õigele kohta ja ei stakiks kõiki üksteise otsa
# Main game loop
running = True
while running:
    kaardi_koht_vajutades = 900 + mitmes*100, 10 #Arvutab välja kaardi kordinaadi paremal poolel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mitmes < 2:
                if object_x_ruutuäss <= mouse[0] <= object_x_ruutuäss + object_size_ruutuäss[0] and object_y_ruutuäss <= mouse[1] <= object_y_ruutuäss + object_size_ruutuäss[1] and object_x_ruutuäss < 670:
                    object_x_ruutuäss, object_y_ruutuäss = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = 'A'
                    elif mitmes == 2:
                        sisend3 = 'A'
                if object_x_ruutu2 <= mouse[0] <= object_x_ruutu2 + object_size_ruutu2[0] and object_y_ruutu2 <= mouse[1] <= object_y_ruutu2 + object_size_ruutu2[1] and object_x_ruutu2 < 670:
                    object_x_ruutu2, object_y_ruutu2 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '2'
                    elif mitmes == 2:
                        sisend3 = '2'
                if object_x_ruutu3 <= mouse[0] <= object_x_ruutu3 + object_size_ruutu3[0] and object_y_ruutu3 <= mouse[1] <= object_y_ruutu3 + object_size_ruutu3[1] and object_x_ruutu3 < 670:
                    object_x_ruutu3, object_y_ruutu3 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '3'
                    elif mitmes == 2:
                        sisend3 = '3'
                if object_x_ruutu4 <= mouse[0] <= object_x_ruutu4 + object_size_ruutu4[0] and object_y_ruutu4 <= mouse[1] <= object_y_ruutu4 + object_size_ruutu4[1] and object_x_ruutu4 < 670:
                    object_x_ruutu4, object_y_ruutu4 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '4'
                    elif mitmes == 2:
                        sisend3 = '4'
                if object_x_ruutu5 <= mouse[0] <= object_x_ruutu5 + object_size_ruutu5[0] and object_y_ruutu5 <= mouse[1] <= object_y_ruutu5 + object_size_ruutu5[1] and object_x_ruutu5 < 670:
                    object_x_ruutu5, object_y_ruutu5 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '5'
                    elif mitmes == 2:
                        sisend3 = '5'
                if object_x_ruutu6 <= mouse[0] <= object_x_ruutu6 + object_size_ruutu6[0] and object_y_ruutu6 <= mouse[1] <= object_y_ruutu6 + object_size_ruutu6[1] and object_x_ruutu6 < 670:
                    object_x_ruutu6, object_y_ruutu6 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '6'
                    elif mitmes == 2:
                        sisend3 = '6'
                if object_x_ruutu7 <= mouse[0] <= object_x_ruutu7 + object_size_ruutu7[0] and object_y_ruutu7 <= mouse[1] <= object_y_ruutu7 + object_size_ruutu7[1] and object_x_ruutu7 < 670:
                    object_x_ruutu7, object_y_ruutu7 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '7'
                    elif mitmes == 2:
                        sisend3 = '7'
                if object_x_ruutu8 <= mouse[0] <= object_x_ruutu8 + object_size_ruutu8[0] and object_y_ruutu8 <= mouse[1] <= object_y_ruutu8 + object_size_ruutu8[1] and object_x_ruutu8 < 670:
                    object_x_ruutu8, object_y_ruutu8 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '8'
                    elif mitmes == 2:
                        sisend3 = '8'
                if object_x_ruutu9 <= mouse[0] <= object_x_ruutu9 + object_size_ruutu9[0] and object_y_ruutu9 <= mouse[1] <= object_y_ruutu9 + object_size_ruutu9[1] and object_x_ruutu9 < 670:
                    object_x_ruutu9, object_y_ruutu9 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '9'
                    elif mitmes == 2:
                        sisend3 = '9'
                if object_x_ruutu10 <= mouse[0] <= object_x_ruutu10 + object_size_ruutu10[0] and object_y_ruutu10 <= mouse[1] <= object_y_ruutu10 + object_size_ruutu10[1] and object_x_ruutu10 < 670:
                    object_x_ruutu10, object_y_ruutu10 = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = '10'
                    elif mitmes == 2:
                        sisend3 = '10'
                if object_x_ruutuJ <= mouse[0] <= object_x_ruutuJ + object_size_ruutuJ[0] and object_y_ruutuJ <= mouse[1] <= object_y_ruutuJ + object_size_ruutuJ[1] and object_x_ruutuJ < 670:
                    object_x_ruutuJ, object_y_ruutuJ = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = 'J'
                    elif mitmes == 2:
                        sisend3 = 'J'
                if object_x_ruutuQ <= mouse[0] <= object_x_ruutuQ + object_size_ruutuQ[0] and object_y_ruutuQ <= mouse[1] <= object_y_ruutuQ + object_size_ruutuQ[1] and object_x_ruutuQ < 670:
                    object_x_ruutuQ, object_y_ruutuQ = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = 'Q'
                    elif mitmes == 2:
                        sisend3 = 'Q'
                if object_x_ruutuK <= mouse[0] <= object_x_ruutuK + object_size_ruutuK[0] and object_y_ruutuK <= mouse[1] <= object_y_ruutuK + object_size_ruutuK[1] and object_x_ruutuK < 670:
                    object_x_ruutuK, object_y_ruutuK = kaardi_koht_vajutades
                    mitmes += 1
                    if mitmes == 1:
                        sisend2 = 'K'
                    elif mitmes == 2:
                        sisend3 = 'K'
            if object_x_mastinupp <= mouse[0] <= object_x_mastinupp + object_size_mastinupp[0] and object_y_mastinupp <= mouse[1] <= object_y_mastinupp + object_size_mastinupp[1]:
                if mastinuppvärv == 'valge':
                    mastinupp = pygame.image.load('mastinuppR.png')
                    mastinuppvärv = 'roheline'
                    sisend1 = 'y'
                elif mastinuppvärv == 'roheline':
                    mastinupp = pygame.image.load('mastinupp.png')
                    mastinuppvärv = 'valge'
                    sisend1 = 'n'
                mastinupp = pygame.transform.scale(mastinupp, (object_size_mastinupp))
            if object_x_restartnupp <= mouse[0] <= object_x_restartnupp + object_size_restartnupp[0] and object_y_restartnupp <= mouse[1] <= object_y_restartnupp + object_size_restartnupp[1]:
                algus()
                mitmes = 0
            if object_x_arvutanupp <= mouse[0] <= object_x_arvutanupp + object_size_arvutanupp[0] and object_y_arvutanupp <= mouse[1] <= object_y_arvutanupp + object_size_arvutanupp[1] and mitmes == 2:
                if kaartide_järjestus(sisend2) >= kaartide_järjestus(sisend3):
                    if sisend1 == "y":
                        sisend = sisend3 + "♥ " + sisend2 + "♥"
                    else:
                        sisend = sisend3 + "♣ " + sisend2 + "♥"
                else:
                    if sisend1 == "y":
                        sisend = sisend2 + "♥ " + sisend3 + "♥"
                    else:
                        sisend = sisend2 + "♣ " + sisend3 + "♥"
                sõnastik = {'A♣ A♥': 8632, 'K♣ K♥': 8465, 'Q♣ Q♥': 8422, 'J♣ J♥': 8397, '10♣ 10♥': 8229, '9♣ 9♥': 7989, '8♣ 8♥': 7887, '7♣ 7♥': 7527, '6♣ 6♥': 7278, '5♣ 5♥': 7003, 'K♥ A♥': 6742, 'J♥ K♥': 6716, 'Q♥ A♥': 6688, 'J♥ A♥': 6681, '4♣ 4♥': 6678, '10♥ A♥': 6653, 'Q♥ K♥': 6653, 'J♥ Q♥': 6583, 'K♣ A♥': 6528, '9♥ A♥': 6505, '7♥ A♥': 6462, 'J♣ A♥': 6461, 'Q♣ A♥': 6434, '10♥ Q♥': 6433, 'Q♣ K♥': 6431, '10♥ K♥': 6422, 'J♣ Q♥': 6413, '3♣ 3♥': 6406, '8♥ A♥': 6404, 'J♣ K♥': 6389, '10♣ A♥': 6370, '5♥ A♥': 6351, '9♥ K♥': 6340, '3♥ A♥': 6317, '4♥ A♥': 6302, '10♥ J♥': 6301, '2♥ A♥': 6283, '9♣ A♥': 6262, '10♣ K♥': 6244, '5♣ A♥': 6225, '8♣ A♥': 6218, '9♥ Q♥': 6211, '10♣ J♥': 6175, '6♥ A♥': 6168, '10♣ Q♥': 6162, '9♣ K♥': 6133, '4♣ A♥': 6129, '7♣ A♥': 6127, '8♥ K♥': 6122, '9♥ J♥': 6117, '9♥ 10♥': 6087, '8♥ Q♥': 6073, '3♣ A♥': 6060, '7♥ K♥': 6053, '2♣ 2♥': 6026, '6♣ A♥': 6019, '6♥ K♥': 6002, '2♣ A♥': 5970, '8♥ J♥': 5959, '5♥ K♥': 5924, '8♣ K♥': 5917, '4♥ K♥': 5911, '9♣ Q♥': 5909, '9♣ J♥': 5880, '8♥ 10♥': 5858, '7♣ K♥': 5850, '2♥ K♥': 5841, '9♣ 10♥': 5826, '7♥ Q♥': 5815, '3♥ K♥': 5801, '8♣ Q♥': 5794, '8♥ 9♥': 5770, '6♣ K♥': 5766, '5♣ K♥': 5758, '6♥ Q♥': 5732, '8♣ J♥': 5702, '7♥ J♥': 5698, '5♥ Q♥': 5688, '3♣ K♥': 5680, '4♣ K♥': 5679, '8♣ 10♥': 5618, '4♥ Q♥': 5605, '3♥ Q♥': 5597, '2♣ K♥': 5596, '7♥ 10♥': 5586, '7♣ Q♥': 5581, '6♣ Q♥': 5549, '6♥ J♥': 5487, '2♥ Q♥': 5459, '8♣ 9♥': 5453, '7♥ 9♥': 5441, '5♣ Q♥': 5439, '5♥ J♥': 5410, '7♣ J♥': 5397, '4♣ Q♥': 5365, '3♣ Q♥': 5358, '4♥ J♥': 5354, '3♥ J♥': 5318, '7♣ 10♥': 5304, '6♥ 10♥': 5281, '7♥ 8♥': 5266, '2♥ J♥': 5263, '7♣ 9♥': 5254, '2♣ Q♥': 5241, '6♣ J♥': 5225, '6♥ 9♥': 5224, '5♥ 10♥': 5138, '4♣ J♥': 5095, '5♣ J♥': 5087, '3♥ 10♥': 5056, '4♥ 10♥': 5045, '7♣ 8♥': 5037, '6♥ 8♥': 5029, '2♣ J♥': 5019, '6♣ 10♥': 5009, '6♣ 9♥': 4992, '5♥ 9♥': 4991, '3♣ J♥': 4971, '2♥ 10♥': 4952, '6♥ 7♥': 4932, '5♣ 10♥': 4865, '6♣ 8♥': 4841, '4♣ 10♥': 4818, '5♥ 8♥': 4792, '4♥ 9♥': 4733, '5♥ 7♥': 4725, '3♥ 9♥': 4717, '2♥ 9♥': 4696, '3♣ 10♥': 4689, '6♣ 7♥': 4660, '5♥ 6♥': 4634, '5♣ 9♥': 4630, '2♣ 10♥': 4621, '5♣ 8♥': 4578, '3♣ 9♥': 4494, '4♥ 7♥': 4469, '4♣ 9♥': 4437, '4♥ 8♥': 4434, '2♥ 8♥': 4431, '4♥ 6♥': 4419, '3♥ 8♥': 4414, '2♣ 9♥': 4397, '5♣ 7♥': 4395, '3♥ 6♥': 4308, '3♥ 7♥': 4307, '4♣ 8♥': 4290, '4♥ 5♥': 4283, '5♣ 6♥': 4220, '4♣ 7♥': 4210, '3♥ 5♥': 4207, '2♥ 7♥': 4175, '3♣ 8♥': 4156, '3♥ 4♥': 4124, '2♣ 8♥': 4093, '2♥ 6♥': 4052, '4♣ 5♥': 4034, '2♥ 4♥': 4017, '3♣ 7♥': 3996, '4♣ 6♥': 3952, '2♥ 5♥': 3941, '2♣ 7♥': 3854, '2♥ 3♥': 3815, '3♣ 6♥': 3779, '3♣ 4♥': 3772, '3♣ 5♥': 3755, '2♣ 6♥': 3734, '2♣ 5♥': 3636, '2♣ 4♥': 3526, '2♣ 3♥': 3317}
                võtmed = list(sõnastik.keys())
                must = (0, 0, 0)
                try:
                    tekst1 = font.render(f"Suvalise käe vastu mängides on võidu võimalus: {round(sõnastik[sisend]/100, 3)}%, ", True, must)              
                    tekst2 = font.render(f"Sinu käsi on parem {round((169 - võtmed.index(sisend))/169*100,3)}% kätest.", True, must)
                except:
                    tekst1 = font.render('Samasugused kaardid ei saa olla samast mastist', True, must)
                object_x_tekst1, object_y_tekst1 = 300, 300
                object_x_tekst2, object_y_tekst2 = 300, 400
                
    mouse = pygame.mouse.get_pos()
    # Drawing image at position (0,0)
    game_display.blit(taustapilt, (0, 0))
    game_display.blit(taust_kirjale, (object_x_taust_kirjale, object_y_taust_kirjale, * object_size_taust_kirjale))
    game_display.blit(ruutuäss, (object_x_ruutuäss, object_y_ruutuäss, * object_size_ruutuäss))
    game_display.blit(mastinupp, (object_x_mastinupp, object_y_mastinupp, * object_size_mastinupp))
    game_display.blit(ruutu2, (object_x_ruutu2, object_y_ruutu2, * object_size_ruutu2))
    game_display.blit(ruutu3, (object_x_ruutu3, object_y_ruutu3, * object_size_ruutu3))
    game_display.blit(restartnupp, (object_x_restartnupp, object_y_restartnupp, * object_size_restartnupp))
    game_display.blit(ruutu4, (object_x_ruutu4, object_y_ruutu4, * object_size_ruutu4))
    game_display.blit(ruutu5, (object_x_ruutu5, object_y_ruutu5, * object_size_ruutu5))
    game_display.blit(ruutu6, (object_x_ruutu6, object_y_ruutu6, * object_size_ruutu6))
    game_display.blit(ruutu7, (object_x_ruutu7, object_y_ruutu7, * object_size_ruutu7))
    game_display.blit(ruutu8, (object_x_ruutu8, object_y_ruutu8, * object_size_ruutu8))
    game_display.blit(ruutu9, (object_x_ruutu9, object_y_ruutu9, * object_size_ruutu9))
    game_display.blit(ruutu10, (object_x_ruutu10, object_y_ruutu10, * object_size_ruutu10))
    game_display.blit(ruutuJ, (object_x_ruutuJ, object_y_ruutuJ, * object_size_ruutuJ))
    game_display.blit(ruutuQ, (object_x_ruutuQ, object_y_ruutuQ, * object_size_ruutuQ))
    game_display.blit(ruutuK, (object_x_ruutuK, object_y_ruutuK, * object_size_ruutuK))
    game_display.blit(arvutanupp, (object_x_arvutanupp, object_y_arvutanupp, * object_size_arvutanupp))
    game_display.blit(tekst1, (object_x_tekst1, object_y_tekst1 ))
    game_display.blit(tekst2, (object_x_tekst2, object_y_tekst2))
    pygame.display.update()
pygame.quit()
