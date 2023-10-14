#Haracter list H_?
#0 = Body / 1 = Head / 2 = Hands / 3 = Legs, BodyL HeadL itp do 7 / 8 do 10 = Lokacja HeadZ,HandsZ,LegsZ /

H_T = ["files/PIC_P/P_T/T_Body.png","files/PIC_P/P_T/T_Head.png","files/PIC_P/P_T/T_Hand.png","files/PIC_P/P_T/T_Leg.png","files/PIC_P/P_T/T_Body2.png","files/PIC_P/P_T/T_Head2.png","files/PIC_P/P_T/T_Hand2.png","files/PIC_P/P_T/T_Leg2.png"
       ,30,18,8,11                                                      #Haracter-----(Body from Shadow),(Head from Body),(Legs from Body),(Hands from Body)
       ,4,2,2,10,"files/PIC_P/P_T/T_Magi_1.png","files/PIC_P/P_T/T_Magi_1.png"          #Magia1-----(MagiaX-spawn)--(MagiaY)--(Speed)--(Damage)--(Template R,L)   start 12
       ,8,8,5,20,"files/PIC_P/P_T/T_Magi_1.png","files/PIC_P/P_T/T_Magi_1.png"          #Magia2-----(Magiax)--(MagiaY)--(Speed)--(Damage)--(Template R,L)   start 18
       ,25,35                                                           #Body-----(Scala-Hitboxa ciala w stosunku do magi)--(X,Y)
       #animacja swobodna kun glowa od 25 do 35
        ,0,0,0,0,0,0,0,0                # BodyY    24 - 31
        ,0,2.5,5,2.5,0,-2.5,-5,-2.5     # Head     32 - 
        ,0,2.5,5,2.5,0,-2.5,-5,-2.5     # Hand1
        ,0,0,0,0,0,0,0,0                # Leg1
        ,0,-2.5,-5,-2.5,0,2.5,5,2.5     # Hand2
        ,0,0,0,0,0,0,0,0                # Leg2
        #animacja Walk
        ,0,1,0,0,0,1,0,0                #BodyY
        ,0,5,10,5,0,-5,-10,-5           # Head     
        ,0,10,15,10,0,-10,-15,-10       # Hand1    
        ,0,-10,-15,-10,0,10,15,10       # Leg1     
        ,0,10,15,10,0,-10,-15,-10       # Hand2
        ,0,10,15,10,0,-10,-15,-10       # Leg2    
        #animacja Run
        ,0,1,0,1,0,1,0,1                #BodyY
        ,0,5,10,5,0,-5,-10,-5           # Head 
        ,0,15,30,15,0,-15,-30,-15       # Hand1
        ,0,15,30,15,0,-15,-30,-15       # Leg1
        ,0,-15,-30,-15,0,15,30,15       #Hand2
        ,0,-15,-30,-15,0,15,30,15       #Leg2
        #animacja jump
        ,-2.5,-5,30,30,20,10,0,0        #BodyY
        ,0,-15,30,35,30,15,0,-5         # Head 
        ,0,15,30,50,0,-15,-30,-15       # Hand1
        ,-15,-30,-30,-15,-15,-5,0,0     # Leg1
        ,0,-15,-30,-15,0,15,30,15       #Hand2
        ,15,30,30,15,15,5,0,0           #Leg2
        #animacja Block
        ,0,0,0,0,0,0,0,0                #BodyY
        ,0,5,10,5,0,-5,-10,-5           # Head     
        ,80,80,80,80,80,80,80,80        # Hand1    
        ,0,0,0,0,0,0,0,0                # Leg1     
        ,0,10,15,10,0,-10,-15,-10       # Hand2
        ,0,0,0,0,0,0,0,0                # Leg2  
        #animacja Send Magic
        ,0,0,0,0,0,0,0,0                # BodyY
        ,-10,-40,-60,10,30,10,5,0       # Head     
        ,0,-80,-30,80,80,30,10,0        # Hand1    
        ,-15,-30,-30,-15,-15,-5,0,0     # Leg1     
        ,0,-80,-30,80,80,30,10,0        # Hand2
        ,15,30,30,15,15,5,0,0           # Leg2
        #animacja get damage with magic
        ,-2.5,-2.5,-2.5,-2.5,0,0,0,0    # BodyY
        ,5,10,12,10,8,5,2,0             # Head     
        ,140,140,145,140,120,60,30,0    # Hand1    
        ,-15,-30,-30,-15,-15,-5,0,0     # Leg1     
        ,130,130,135,130,110,50,20,0    # Hand2
        ,15,30,30,15,15,5,0,0]          # Leg2



H_Neit = ["files/PIC_P/P_1/N_Body.png","files/PIC_P/P_1/N_Head.png","files/PIC_P/P_1/N_Hand.png","files/PIC_P/P_1/N_Leg.png","files/PIC_P/P_1/N_Body2.png","files/PIC_P/P_1/N_Head2.png","files/PIC_P/P_1/N_Hand2.png","files/PIC_P/P_1/N_Leg2.png"
       ,30,18,8,11                                                      #Haracter-----(Body from Shadow),(Head from Body),(Legs from Body),(Hands from Body)
       ,4,2,2,10,"files/PIC_P/P_T/T_Magi_1.png","files/PIC_P/P_T/T_Magi_1.png"          #Magia1-----(MagiaX-spawn)--(MagiaY)--(Speed)--(Damage)--(Template R,L)   start 12
       ,8,8,5,20,"files/PIC_P/P_T/T_Magi_1.png","files/PIC_P/P_T/T_Magi_1.png"          #Magia2-----(Magiax)--(MagiaY)--(Speed)--(Damage)--(Template R,L)   start 18
       ,25,35                                                           #Body-----(Scala-Hitboxa ciala w stosunku do magi)--(X,Y)
       #animacja swobodna kun glowa od 25 do 35
        ,0,0,0,0,0,0,0,0                # BodyY    24 - 31
        ,0,2.5,5,2.5,0,-2.5,-5,-2.5     # Head     32 - 
        ,0,2.5,5,2.5,0,-2.5,-5,-2.5     # Hand1
        ,0,0,0,0,0,0,0,0                # Leg1
        ,0,-2.5,-5,-2.5,0,2.5,5,2.5     # Hand2
        ,0,0,0,0,0,0,0,0                # Leg2
        #animacja Walk
        ,0,1,0,0,0,1,0,0                #BodyY
        ,0,5,10,5,0,-5,-10,-5           # Head     
        ,0,10,15,10,0,-10,-15,-10       # Hand1    
        ,0,-10,-15,-10,0,10,15,10       # Leg1     
        ,0,10,15,10,0,-10,-15,-10       # Hand2
        ,0,10,15,10,0,-10,-15,-10       # Leg2    
        #animacja Run
        ,0,1,0,1,0,1,0,1                #BodyY
        ,0,5,10,5,0,-5,-10,-5           # Head 
        ,0,15,30,15,0,-15,-30,-15       # Hand1
        ,0,15,30,15,0,-15,-30,-15       # Leg1
        ,0,-15,-30,-15,0,15,30,15       #Hand2
        ,0,-15,-30,-15,0,15,30,15       #Leg2
        #animacja jump
        ,-2.5,-5,30,30,20,10,0,0        #BodyY
        ,0,-15,30,35,30,15,0,-5         # Head 
        ,0,15,30,50,0,-15,-30,-15       # Hand1
        ,-15,-30,-30,-15,-15,-5,0,0     # Leg1
        ,0,-15,-30,-15,0,15,30,15       #Hand2
        ,15,30,30,15,15,5,0,0           #Leg2
        #animacja Block
        ,0,0,0,0,0,0,0,0                #BodyY
        ,0,5,10,5,0,-5,-10,-5           # Head     
        ,80,80,80,80,80,80,80,80        # Hand1    
        ,0,0,0,0,0,0,0,0                # Leg1     
        ,0,10,15,10,0,-10,-15,-10       # Hand2
        ,0,0,0,0,0,0,0,0                # Leg2  
        #animacja Send Magic
        ,0,0,0,0,0,0,0,0                # BodyY
        ,-10,-40,-60,10,30,10,5,0       # Head     
        ,0,-80,-30,80,80,30,10,0        # Hand1    
        ,-15,-30,-30,-15,-15,-5,0,0     # Leg1     
        ,0,-80,-30,80,80,30,10,0        # Hand2
        ,15,30,30,15,15,5,0,0           # Leg2
        #animacja get damage with magic
        ,-2.5,-2.5,-2.5,-2.5,0,0,0,0    # BodyY
        ,5,10,12,10,8,5,2,0             # Head     
        ,140,140,145,140,120,60,30,0    # Hand1    
        ,-15,-30,-30,-15,-15,-5,0,0     # Leg1     
        ,130,130,135,130,110,50,20,0    # Hand2
        ,15,30,30,15,15,5,0,0]          # Leg2