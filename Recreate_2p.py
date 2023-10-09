import pygame.display
from pygame import display
from Haracter import *
#wszystkie dane sa w infostart dzieki temu ponizej ze importyje je z tamtat
from info_start import *

pygame.init()
title = pygame.display.set_caption("ReCreates", "fast")
scren = pygame.display.set_mode((1100,1025))
icon  = pygame.image.load("files/PIC_M/M_Grass.png")
pygame.display.set_icon(icon)


###################################-----Wyswietlanie_Wszystkiego
def back_ground():
    scren.blit(pygame.image.load("files/PIC_M/M_BackG.png"), (0, 0))
    scren.blit(pygame.image.load("files/PIC_M/M_BackG.png"), (550, 0))
def players_stats():
    scren.blit(pygame.image.load("files/PIC_M/W_stats_1.png"), (0, -125))
    scren.blit(pygame.image.load("files/PIC_M/W_stats_1.png"), (500, -125))
    scren.blit(pygame.image.load("files/PIC_M/W_stats_hp.png"), (0 + P2_HP * 5, -125))
    scren.blit(pygame.image.load("files/PIC_M/W_stats_hp.png"), (-500 + P1_HP * 5, -125))
    scren.blit(pygame.image.load("files/PIC_M/W_stats_2.png"), (0, -125))
    scren.blit(pygame.image.load("files/PIC_M/W_stats_2.png"), (500, -125))

def player_1():
    scren.blit(P1_Hand2,(B1X + 50 - int(P1_Hand2.get_width() / 2), B1Y  + 50 - HandY - int(P1_Hand2.get_height() / 2)))
    scren.blit(P1_Leg2,(B1X + 50 - int(P1_Leg2.get_width() / 2), B1Y + 50 + LegY - int(P1_Leg2.get_height() / 2)))

    scren.blit(P1_Shadow,(P1X,P1Y))
    scren.blit(P1_Body,(B1X,B1Y + 0))
    scren.blit(P1_Head,(B1X + 50 - int(P1_Head.get_width() / 2), B1Y  + 50 - HeadY - int(P1_Head.get_height() / 2)))
    scren.blit(P1_Hand,(B1X + 50 - int(P1_Hand.get_width() / 2), B1Y  + 50 - HandY - int(P1_Hand.get_height() / 2)))
    scren.blit(P1_Leg,(B1X + 50 - int(P1_Leg.get_width() / 2), B1Y + 50 + LegY - int(P1_Leg.get_height() / 2)))
    scren.blit(pygame.transform.rotate(P1_Magic, 0), (M_X + Magiaspeed, M_Y ), ((ATic + 1) * 100 + 1, 1, 98, 98,))
def player_2():
    scren.blit(P2_Hand2,(B2X + 50 - int(P2_Hand2.get_width() / 2), B2Y  + 50 - HandY_p2 - int(P2_Hand2.get_height() / 2)))
    scren.blit(P2_Leg2,(B2X + 50 - int(P2_Leg2.get_width() / 2), B2Y + 50 + LegY_p2 - int(P2_Leg2.get_height() / 2)))

    scren.blit(P2_Shadow,(P2X,P2Y))
    scren.blit(P2_Body,(B2X,B2Y + 0))
    scren.blit(P2_Head,(B2X + 50 - int(P2_Head.get_width() / 2), B2Y  + 50 - HeadY_p2 - int(P2_Head.get_height() / 2)))
    scren.blit(P2_Hand,(B2X + 50 - int(P2_Hand.get_width() / 2), B2Y  + 50 - HandY_p2 - int(P2_Hand.get_height() / 2)))
    scren.blit(P2_Leg,(B2X + 50 - int(P2_Leg.get_width() / 2), B2Y + 50 + LegY_p2 - int(P2_Leg.get_height() / 2)))
    scren.blit(pygame.transform.rotate(P2_Magic, 0), (M_X_p2 + Magiaspeed_p2, M_Y_p2), ((ATic_p2 + 1) * 100 + 1, 1, 98, 98,))    

windowstart = True
while windowstart:
    # importuje dane do dalszych animacji
    from info_after import *
    #########################################################################-----Ticki animacji oby dwuch graczy
    Tick = Tick + T_R
    if Tick >= 160: Tick = 0
    Tick1 = str(Tick / 20)[0]
    ATic = int(Tick1)
    #Player 2 Animation Tick
    Tick_p2 = Tick_p2 + T_R
    if Tick_p2 >= 160: Tick_p2 = 0
    Tick2 = str(Tick_p2 / 20)[0]
    ATic_p2 = int(Tick2)

    #########################################################################-----Animacaj oraz Tick animacji teraz 7-Tick
    #print(ATic) to jest do sprawdzenia jaki tick teraz jest 7 tickowy - 7 fps
    Z_Body, Rot_Head, Rot_Hand = Haracter[26 + S_ANIM + ATic], Haracter[34 + S_ANIM + ATic], Haracter[42 + S_ANIM + ATic]
    Rot_Leg, Rot_Hand2, Rot_Leg2 = Haracter[50 + S_ANIM + ATic], Haracter[58 + S_ANIM + ATic], Haracter[66 + S_ANIM + ATic] 
    RHE, RHA, RLE, RHA2, RLE2 = Rot_Head * ATic_P_M, Rot_Hand * ATic_P_M, Rot_Leg * ATic_P_M, Rot_Hand2 * ATic_P_M, Rot_Leg2 * ATic_P_M
    #222222222222222222222222222222222222222222222222222222222222222222222222
    Z_Body_p2, Rot_Head_p2, Rot_Hand_p2 = Haracter_p2[26 + S_ANIM_p2 + ATic_p2], Haracter_p2[34 + S_ANIM_p2 + ATic_p2], Haracter_p2[42 + S_ANIM_p2 + ATic_p2]
    Rot_Leg_p2, Rot_Hand2_p2, Rot_Leg2_p2 = Haracter_p2[50 + S_ANIM_p2 + ATic_p2], Haracter_p2[58 + S_ANIM_p2 + ATic_p2], Haracter_p2[66 + S_ANIM_p2 + ATic_p2] 
    RHE_p2, RHA_p2, RLE_p2, RHA2_p2, RLE2_p2 = Rot_Head_p2 * ATic_P_M_p2, Rot_Hand_p2 * ATic_P_M_p2, Rot_Leg_p2 * ATic_P_M_p2, Rot_Hand2_p2 * ATic_P_M_p2, Rot_Leg2_p2 * ATic_P_M_p2
    
    DAMAGE_P1, DAMAGE_P2 = Haracter[15 + DAM_P1], Haracter_p2[15 + DAM_P2]

    #########################################################################-----dane jaki obraz sie ma generowac
    P1_Shadow = pygame.image.load("files/PIC_P/P_T/T_Shadow.png") #####-----To jest cien-zawsze ten sam dla wszystkich postaci
    P1_Body = pygame.image.load(Haracter[0 + R_L])
    P1_Head, P1_Magic = pygame.transform.rotate(pygame.image.load(Haracter[1 + R_L]), RHE), pygame.image.load(Haracter[16 + M_PIC])
    P1_Hand, P1_Hand2 = pygame.transform.rotate(pygame.image.load(Haracter[2 + R_L]), RHA), pygame.transform.rotate(pygame.image.load(Haracter[2 + R_L]), RHA2)
    P1_Leg, P1_Leg2 = pygame.transform.rotate(pygame.image.load(Haracter[3 + R_L]), RLE), pygame.transform.rotate(pygame.image.load(Haracter[3 + R_L]), RLE2)
    #222222222222222222222222222222222222222222222222222222222222222222222222
    P2_Shadow = pygame.image.load("files/PIC_P/P_T/T_Shadow.png") #####-----To jest cien-zawsze ten sam dla wszystkich postaci
    P2_Body = pygame.image.load(Haracter_p2[0 + R_L_p2])
    P2_Head, P2_Magic = pygame.transform.rotate(pygame.image.load(Haracter_p2[1 + R_L_p2]), RHE_p2), pygame.image.load(Haracter_p2[16 + M_PIC_p2])
    P2_Hand, P2_Hand2 = pygame.transform.rotate(pygame.image.load(Haracter_p2[2 + R_L_p2]), RHA_p2), pygame.transform.rotate(pygame.image.load(Haracter_p2[2 + R_L_p2]), RHA2_p2)
    P2_Leg, P2_Leg2 = pygame.transform.rotate(pygame.image.load(Haracter_p2[3 + R_L_p2]), RLE_p2), pygame.transform.rotate(pygame.image.load(Haracter_p2[3 + R_L_p2]), RLE2_p2)
    

    #########################################################################-----Lokalizacja Player1,2 and dane do ciala i cienia
    P1X, P1Y, B1X, B1Y = P1X + Speed1, P1Y + Speed2, P1X, P1Y - BodyY - Z_Body
    #222222222222222222222222222222222222222222222222222222222222222222222222
    P2X, P2Y, B2X, B2Y = P2X + Speed1_p2, P2Y + Speed2_p2, P2X, P2Y - BodyY_p2 - Z_Body_p2
    #########################################################################-----player1,2 dobble click na D,A,->,<-
    if X2_D > 0: X2_D = X2_D -1
    if X2_D > 80: X2_D = 0
    if X2_A > 0: X2_A = X2_A -1
    if X2_A > 80: X2_A = 0
    #222222222222222222222222222222222222222222222222222222222222222222222222
    if X2_D_p2 > 0: X2_D_p2 = X2_D_p2 -1
    if X2_D_p2 > 80: X2_D_p2 = 0
    if X2_A_p2 > 0: X2_A_p2 = X2_A_p2 -1
    if X2_A_p2 > 80: X2_A_p2 = 0


    #########################################################################-----Event na close window
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            windowstart = False
    #########################################################################-----Kiedy Dane guziki sa Docisniente
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: B_W = 1
            if event.key == pygame.K_s: B_S = 1
            if event.key == pygame.K_a: X2_A, B_A, R_L, ATic_P_M = X2_A + 30, 1, 4, -1
            if X2_A > 30: B_A = 2
            if event.key == pygame.K_d: X2_D, B_D, R_L, ATic_P_M = X2_D + 30, 1, 0, 1
            if X2_D > 30: B_D = 2
            if event.key == pygame.K_TAB: B_TAB, Tick = 1, 0
            if event.key == pygame.K_LSHIFT: B_SHIFT, Tick = 1, 0
            #222222222222222222222222222222222222222222222222222222222222222222222222
            if event.key == pygame.K_UP: B_W_p2 = 1
            if event.key == pygame.K_DOWN: B_S_p2 = 1
            if event.key == pygame.K_LEFT: X2_A_p2, B_A_p2, R_L_p2, ATic_P_M_p2 = X2_A_p2 + 30, 1, 4, -1
            if X2_A_p2 > 30: B_A_p2 = 2
            if event.key == pygame.K_RIGHT: X2_D_p2, B_D_p2, R_L_p2, ATic_P_M_p2 = X2_D_p2 + 30, 1, 0, 1
            if X2_D_p2 > 30: B_D_p2 = 2
            if event.key == pygame.K_j: B_J, Tick_p2 = 1, 0
            if event.key == pygame.K_l: B_L, Tick_p2 = 1, 0
            #testowe\/
            if event.key == pygame.K_t: S_ANIM, M_X, M_Y, MAGIC, Magiaspeed = A_L[6], Haracter[10] + B1X, Haracter[10] + B1Y, 1, 0

    #########################################################################-----Kiedy Dane guziki sa Odcisniente
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: S_ANIM, B_W, Speed2 = A_L[0], 0, 0
            if event.key == pygame.K_s: S_ANIM, B_S, Speed2 = A_L[0], 0, 0   
            if event.key == pygame.K_a: S_ANIM, B_A, Speed1 = A_L[0], 0, 0
            if event.key == pygame.K_d: S_ANIM, B_D, Speed1 = A_L[0], 0, 0
            if event.key == pygame.K_LSHIFT: S_ANIM, B_SHIFT = A_L[0], 0
            #222222222222222222222222222222222222222222222222222222222222222222222222
            if event.key == pygame.K_UP: S_ANIM_p2, B_W_p2, Speed2_p2 = A_L_p2[0], 0, 0
            if event.key == pygame.K_DOWN: S_ANIM_p2, B_S_p2, Speed2_p2 = A_L_p2[0], 0, 0   
            if event.key == pygame.K_LEFT: S_ANIM_p2, B_A_p2, Speed1_p2 = A_L_p2[0], 0, 0
            if event.key == pygame.K_RIGHT: S_ANIM_p2, B_D_p2, Speed1_p2 = A_L_p2[0], 0, 0
            if event.key == pygame.K_l: S_ANIM_p2, B_L = A_L_p2[0], 0

    #########################################################################-----Odczyt Guzikow Nieskonczony czas odczytywania, Kolejnosc jest wazna
    #########################################################################-----to co na samej guze jest najmniej wazne jako animacja oraz poruszanie
    if B_W >0: S_ANIM, Speed2 = A_L[1], -T_R / 4
    if B_S >0: S_ANIM, Speed2 = A_L[1], T_R / 4 # Predkosc
    if B_A == 1: S_ANIM, Speed1 = A_L[1], -T_R / 4
    elif B_A == 2: S_ANIM, Speed1 = A_L[2], -T_R / 2
    if B_D == 1: S_ANIM, Speed1 = A_L[1], T_R / 4
    elif B_D == 2: S_ANIM, Speed1 = A_L[2], T_R / 2
    if B_TAB == 1: ##########-----tak dziala jednorazowe
        S_ANIM = A_L[3]
        if Tick >= 155: S_ANIM, B_TAB = A_L[0], 0
    if B_SHIFT == 1: S_ANIM, Speed1 = A_L[4], 0
    if M_X_p2 >= B1X - Haracter[24] and M_X_p2 <= B1X + Haracter[24] and M_Y_p2 >= B1Y - Haracter[25] and M_Y_p2 <= B1Y + Haracter[25]:
        M_X_p2, M_Y_p2, MAGIC = -1000, -1000, 0
        if B_SHIFT != 1: P1_DEAD, TIME, B_A, B_D, P1_HP = 1, 0, 0, 0, P1_HP - DAMAGE_P2
    #222222222222222222222222222222222222222222222222222222222222222222222222
    if B_W_p2 >0: S_ANIM_p2, Speed2_p2 = A_L_p2[1], -T_R / 4
    if B_S_p2 >0: S_ANIM_p2, Speed2_p2 = A_L_p2[1], T_R / 4 # Predkosc
    if B_A_p2 == 1: S_ANIM_p2, Speed1_p2 = A_L_p2[1], -T_R / 4
    elif B_A_p2 == 2: S_ANIM_p2, Speed1_p2 = A_L_p2[2], -T_R / 2
    if B_D_p2 == 1: S_ANIM_p2, Speed1_p2 = A_L_p2[1], T_R / 4
    elif B_D_p2 == 2: S_ANIM_p2, Speed1_p2 = A_L_p2[2], T_R / 2
    if B_J == 1: ##########-----tak dziala jednorazowe
        S_ANIM_p2 = A_L_p2[3]
        if Tick_p2 >= 155: S_ANIM_p2, B_J = A_L_p2[0], 0
    if B_L == 1: S_ANIM_p2, Speed1_p2 = A_L_p2[4], 0
    if M_X >= B2X - Haracter_p2[24] and M_X <= B2X + Haracter_p2[24] and M_Y >= B2Y - Haracter_p2[25] and M_Y <= B2Y + Haracter_p2[25]:
        M_X, M_Y, MAGIC_p2 = -1000, -1000, 0
        if B_L != 1: P2_DEAD, TIME_p2, B_A_p2, B_D_p2, P2_HP = 1, 0, 0, 0, P2_HP - DAMAGE_P1


    #########################################################################-----Dzialanie Magii
    if B_TAB == 1 and B_D == 2:     #MAGIA1 PRAWO
        Speed1, S_ANIM, DAM_P1 = 0, A_L[5], 0
        if Tick >= 156: S_ANIM, B_TAB, X2_D, B_D = A_L[0], 0, 1, 1
        elif 78 < Tick < 82: M_X, M_Y, M_SPED, MAGIC, MAGI_P_M, M_PIC = Haracter[12] + B1X, Haracter[13] + B1Y, Haracter[14], 1, 1, 0
    elif B_TAB == 1 and B_A == 2:   #MAGIA1 LEWO
        Speed1, S_ANIM, DAM_P1 = 0, A_L[5], 0
        if Tick >= 156: S_ANIM, B_TAB, X2_A, B_A = A_L[0], 0, 1, 1
        elif 78 < Tick < 82: M_X, M_Y, M_SPED, MAGIC, MAGI_P_M, M_PIC = Haracter[12] + B1X, Haracter[13] + B1Y, Haracter[14], 1, -1, 1
    elif B_SHIFT == 1 and B_D == 2: #MAGIA2 PRAWO
        Speed1, S_ANIM, DAM_P1 = 0, A_L[5], 6
        if Tick >= 156: S_ANIM, B_SHIFT, X2_d, B_D = A_L[0], 0, 1, 1
        elif 78 < Tick < 82: M_X, M_Y, M_SPED, MAGIC, MAGI_P_M, M_PIC = Haracter[18] + B1X, Haracter[19] + B1Y, Haracter[20], 1, 1, 6
    elif B_SHIFT == 1 and B_A == 2: #MAGIA2 LEWO
        Speed1, S_ANIM, DAM_P1 = 0, A_L[5], 6
        if Tick >= 156: S_ANIM, B_SHIFT, X2_A, B_A = A_L[0], 0, 1, 1
        elif 78 < Tick < 82: M_X, M_Y, M_SPED, MAGIC, MAGI_P_M, M_PIAaC = Haracter[18] + B1X, Haracter[19] + B1Y, Haracter[20], 1, -1, 7
    if P1_DEAD == 1:                #HIT MAGIA
        S_ANIM, Speed1, Speed2, B_TAB, B_SHIFT = A_L[6], 0, 0, 0, 0
        if TIME <= 350: TIME += 1
        else: P1_DEAD, S_ANIM = 0, A_L[0]
    if MAGIC == 1: M_X += M_SPED * MAGI_P_M         #SEND MAGIA
    #222222222222222222222222222222222222222222222222222222222222222222222222
    if B_J == 1 and B_D_p2 == 2:    #MAGIA1 PRAWO_P2
        Speed1_p2, S_ANIM_p2, DAM_P2 = 0, A_L_p2[5], 0
        if Tick_p2 >= 156: S_ANIM_p2, B_J, X2_D_p2, B_D_p2 = A_L_p2[0], 0, 1, 1
        elif 78 < Tick_p2 < 82: M_X_p2, M_Y_p2, M_SPED_p2, MAGIC_p2, MAGI_P_M_p2, M_PIC_p2 = Haracter_p2[12] + B2X, Haracter_p2[13] + B2Y, Haracter_p2[14], 1, 1, 0
    elif B_J == 1 and B_A_p2 == 2:  #MAGIA1 LEWO_P2
        Speed1_p2, S_ANIM_p2, DAM_P2 = 0, A_L_p2[5], 0
        if Tick_p2 >= 156: S_ANIM_p2, B_J, X2_A_p2, B_A_p2 = A_L_p2[0], 0, 1, 1
        elif 78 < Tick_p2 < 82: M_X_p2, M_Y_p2, M_SPED_p2, MAGIC_p2, MAGI_P_M_p2, M_PIC_p2 = Haracter_p2[12] + B2X, Haracter_p2[13] + B2Y, Haracter_p2[14], 1, -1, 1
    elif B_L == 1 and B_D_p2 == 2:  #MAGIA2 PRAWO_P2
        Speed1_p2, S_ANIM_p2, DAM_P2 = 0, A_L_p2[5], 6
        if Tick_p2 >= 156: S_ANIM_p2, B_L, X2_d, B_D_p2 = A_L_p2[0], 0, 1, 1
        elif 78 < Tick_p2 < 82: M_X_p2, M_Y_p2, M_SPED_p2, MAGIC_p2, MAGI_P_M_p2, M_PIC_p2 = Haracter_p2[18] + B2X, Haracter_p2[19] + B2Y, Haracter_p2[20], 1, 1, 6
    elif B_L == 1 and B_A_p2 == 2:  #MAGIA2 LEWO_P2
        Speed1_p2, S_ANIM_p2, DAM_P2 = 0, A_L_p2[5], 6
        if Tick_p2 >= 156: S_ANIM_p2, B_L, X2_A_p2, B_A_p2 = A_L_p2[0], 0, 1, 1
        elif 78 < Tick_p2 < 82: M_X_p2, M_Y_p2, M_SPED_p2, MAGIC_p2, MAGI_P_M_p2, M_PIAaC = Haracter_p2[18] + B2X, Haracter_p2[19] + B2Y, Haracter_p2[20], 1, -1, 7
    if P2_DEAD == 1:                #HIT MAGIA_P2
        S_ANIM_p2, Speed1_p2, Speed2_p2, B_J, B_L = A_L_p2[6], 0, 0, 0, 0
        if TIME_p2 <= 350: TIME_p2 += 1
        else: P2_DEAD, S_ANIM_p2 = 0, A_L_p2[0]
    if MAGIC_p2 == 1:  M_X_p2 += M_SPED_p2 * MAGI_P_M_p2    #SEND MAGIA_P2

    # print(P1_HP, P2_HP)
    back_ground()
    if P1Y < P2Y: #to robi ze kto jest wyzej od kogo gracz 1 czy gracz 2
        player_1()
        player_2()
    else:
        player_2()
        player_1()
    # players_stats()

    pygame.display.update()