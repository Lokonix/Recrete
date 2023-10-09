from Haracter import *

######################################################################-----Dane Poczontkowe Gracza 1

###################################-----Dane Tick-u oraz Magi Anim oraz w ktora strona
Tick, ATic, ATic_P_M, MAGI_P_M = 0, 0, 1, 1
###################################-----Player 1 Dane Location speed itp
P1X, P1Y, Speed1, Speed2, S_ANIM, R_L, P1_DEAD = 100, 500, 0, 0, 0, 0, 0
###################################-----Animacje Wybory w [1]- pzyklad
A_L = [0,48,96,144,192,240,288,336] #TO NIE JEST GDZIE SIE ZACZYNA TYLKO ILE DODAJE DO haracter, by byla nastempna animacja
###################################-----Buttons
B_W, B_S, B_A, B_D, X2_A, X2_D, B_TAB, B_SHIFT = 0, 0, 0, 0, 0, 0, 0, 0
###################################-----Magic_Dane
M_X, M_Y, MAGIC, M_PIC, M_SPED, Magiaspeed = 0, 0, 0, 0, 0, 0


######################################################################-----Dane Poczontkowe Gracza 2
###################################-----Dane Tick-u oraz Magi Anim oraz w ktora strona
Tick_p2, ATic_p2, ATic_P_M_p2, MAGI_P_M_p2 = 0, 0, 1, 1
###################################-----Player 1 Dane Location speed itp
P2X, P2Y, Speed1_p2, Speed2_p2, S_ANIM_p2, R_L_p2, P2_DEAD = 100, 100, 0, 0, 0, 0, 0
###################################-----Animacje Wybory w [1]- pzyklad
A_L_p2 = [0,48,96,144,192,240,288,336] #TO NIE JEST GDZIE SIE ZACZYNA TYLKO ILE DODAJE DO haracter, by byla nastempna animacja
###################################-----Buttons
B_W_p2, B_S_p2, B_A_p2, B_D_p2, X2_A_p2, X2_D_p2, B_J, B_L = 0, 0, 0, 0, 0, 0, 0, 0
###################################-----Magic_Dane
M_X_p2, M_Y_p2, MAGIC_p2, M_PIC_p2, M_SPED_p2, Magiaspeed_p2 = 0, 0, 0, 0, 0, 0


######################################################################-----Hp graczy oraz jaka magia ma ile damage 
P1_HP = 100
P2_HP = 100
DAM_P1 = 0
DAM_P2 = 0
######################################################################-----Hp graczy- widgety lokalizacja dane
hp_p1_widgetX = 100
hp_p2_widgetX = 300
