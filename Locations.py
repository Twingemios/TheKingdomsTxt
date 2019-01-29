#codes[0][0] - Type ID
#codes[0][1] - Event ID
#codes[0][2] - Event ID
#codes[0][3] - Memory
#codes[0][4] - Memory
#codes[0][5] - Up
#codes[0][6] - Down
#codes[0][6] - Left
#codes[0][6] - Right

class Forest:
    A_1 = ['0', 0, 0, 0, 0, 0, 1, 0, 0]
    B_1 = ['0', 0, 0, 0, 0, 0, 1, 0, 0]
    C_1 = ['0', 0, 0, 0, 0, 0, 0, 0, 0]
    D_1 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    E_1 = ['+', 0, 0, 0, 0, 0, 1, 0, 1]
    F_1 = ['@', 0, 0, 0, 0, 0, 0, 1, 0]
    G_1 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    H_1 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    I_1 = ['#', 0, 0, 0, 0, 0, 1, 0, 1]
    J_1 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    K_1 = ['!', 0, 0, 0, 0, 0, 0, 1, 0]
    A_2 = ['+', 0, 0, 0, 0, 0, 0, 0, 1]
    B_2 = ['#', 0, 0, 0, 0, 0, 1, 1, 0]
    C_2 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    D_2 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    E_2 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    F_2 = ['0', 0, 0, 0, 0, 1, 1, 1, 0]
    G_2 = ['0', 0, 0, 0, 0, 0, 0, 0, 0]
    H_2 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    I_2 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    J_2 = ['0', 0, 0, 0, 0, 1, 0, 1, 0]
    K_2 = ['0', 0, 0, 0, 0, 1, 0, 0, 0]
    A_3 = ['0', 0, 0, 0, 0, 1, 0, 0, 1]
    B_3 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    C_3 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    D_3 = ['0', 0, 0, 0, 0, 0, 1, 0, 1]
    E_3 = ['#', 0, 0, 0, 0, 1, 0, 0, 1]
    F_3 = ['#', 0, 0, 0, 0, 0, 1, 1, 0]
    G_3 = ['0', 0, 0, 0, 0, 0, 1, 1, 0]
    H_3 = ['0', 0, 0, 0, 0, 0, 1, 0, 1]
    I_3 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    J_3 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    K_3 = ['0', 0, 0, 0, 0, 0, 0, 0, 0]
    A_4 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    B_4 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    C_4 = ['0', 0, 0, 0, 0, 0, 0, 1, 1]
    D_4 = ['+', 0, 0, 0, 0, 0, 1, 0, 0]
    E_4 = ['0', 0, 0, 0, 0, 1, 0, 1, 1]
    F_4 = ['#', 0, 0, 0, 0, 1, 0, 0, 1]
    G_4 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    H_4 = ['#', 0, 0, 0, 0, 0, 1, 1, 1]
    I_4 = ['$', 0, 0, 0, 0, 1, 0, 1, 0]
    J_4 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    K_4 = ['0', 0, 0, 0, 0, 0, 0, 0, 0]
    A_5 = ['0', 0, 0, 0, 0, 0, 1, 0, 1]
    B_5 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    C_5 = ['0', 0, 0, 0, 0, 0, 1, 1, 1]
    D_5 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    E_5 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    F_5 = ['0', 0, 0, 0, 0, 1, 1, 0, 0]
    G_5 = ['0', 0, 0, 0, 0, 1, 1, 0, 1]
    H_5 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    I_5 = ['0', 0, 0, 0, 0, 1, 0, 1, 0]
    J_5 = ['0', 0, 0, 0, 0, 0, 1, 0, 0]
    K_5 = ['0', 0, 0, 0, 0, 0, 1, 0, 0]
    A_6 = ['@', 0, 0, 0, 0, 0, 0, 0, 1]
    B_6 = ['#', 0, 0, 0, 0, 1, 0, 1, 1]
    C_6 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    D_6 = ['#', 0, 0, 0, 0, 1, 1, 1, 0]
    E_6 = ['0', 0, 0, 0, 0, 0, 0, 1, 1]
    F_6 = ['#', 0, 0, 0, 0, 0, 1, 0, 1]
    G_6 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    H_6 = ['#', 0, 0, 0, 0, 1, 0, 1, 0]
    I_6 = ['0', 0, 0, 0, 0, 0, 0, 1, 1]
    J_6 = ['#', 0, 0, 0, 0, 0, 1, 0, 1]
    K_6 = ['@', 0, 0, 0, 0, 0, 0, 1, 0]
    A_7 = ['0', 0, 0, 0, 0, 1, 0, 0, 0]
    B_7 = ['0', 0, 0, 0, 0, 1, 0, 0, 0]
    C_7 = ['0', 0, 0, 0, 0, 1, 0, 0, 1]
    D_7 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    E_7 = ['0', 0, 0, 0, 0, 0, 0, 1, 1]
    F_7 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    G_7 = ['0', 0, 0, 0, 0, 1, 0, 1, 0]
    H_7 = ['0', 0, 0, 0, 0, 1, 0, 0, 0]
    I_7 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    J_7 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    K_7 = ['0', 0, 0, 0, 0, 1, 0, 1, 0]
    A_8 = ['0', 0, 0, 0, 0, 0, 0, 0, 0]
    B_8 = ['0', 0, 0, 0, 0, 0, 1, 0, 0]
    C_8 = ['0', 0, 0, 0, 0, 0, 1, 0, 1]
    D_8 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    E_8 = ['0', 0, 0, 0, 0, 0, 1, 1, 1]
    F_8 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    G_8 = ['0', 0, 0, 0, 0, 0, 1, 1, 0]
    H_8 = ['0', 0, 0, 0, 0, 0, 1, 0, 0]
    I_8 = ['0', 0, 0, 0, 0, 0, 1, 0, 1]
    J_8 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    K_8 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    A_9 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    B_9 = ['#', 0, 0, 0, 0, 0, 1, 0, 1]
    C_9 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    D_9 = ['#', 0, 0, 0, 0, 1, 0, 1, 1]
    E_9 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
#EID 2
    F_9 = ['#', 0, 2, 0, 0, 1, 1, 1, 1]
    G_9 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    H_9 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    I_9 = ['#', 0, 0, 0, 0, 0, 0, 1, 1]
    J_9 = ['$', 0, 0, 0, 0, 1, 1, 1, 0]
    K_9 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    A_10 = ['0', 0, 0, 0, 0, 0, 1, 0, 1]
    B_10 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    C_10 = ['0', 0, 0, 0, 0, 1, 0, 1, 0]
    D_10 = ['0', 0, 0, 0, 0, 1, 0, 0, 0]
    E_10 = ['0', 0, 0, 0, 0, 1, 0, 0, 1]
#EID 1
    F_10 = ['+', 0, 1, 0, 0, 1, 1, 0, 0]
    G_10 = ['0', 0, 0, 0, 0, 1, 0, 1, 0]
    H_10 = ['0', 0, 0, 0, 0, 1, 0, 0, 0]
    I_10 = ['0', 0, 0, 0, 0, 1, 0, 0, 1]
    J_10 = ['#', 0, 0, 0, 0, 1, 1, 0, 0]
    K_10 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    A_11 = ['#', 0, 0, 0, 0, 0, 0, 0, 1]
    B_11 = ['#', 0, 0, 0, 0, 1, 0, 1, 0]
    C_11 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    D_11 = ['0', 0, 0, 0, 0, 0, 0, 0, 0]
    E_11 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    F_11 = ['@', 0, 0, 0, 0, 1, 0, 0, 0]
    G_11 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    H_11 = ['0', 0, 0, 0, 0, 0, 0, 0, 0]
    I_11 = ['0', 0, 0, 0, 0, 0, 0, 0, 1]
    J_11 = ['#', 0, 0, 0, 0, 1, 0, 0, 0]
    K_11 = ['0', 0, 0, 0, 0, 0, 0, 1, 0]
    allForest = [A_1, B_1, C_1, D_1, E_1, F_1, G_1, H_1, I_1, J_1, K_1, A_2, B_2, C_2, D_2, E_2, F_2, G_2, H_2, I_2, J_2, K_2, A_3, B_3, C_3, D_3, E_3, F_3, G_3, H_3, I_3, J_3, K_3, A_4, B_4, C_4, D_4, E_4, F_4, G_4, H_4, I_4, J_4, K_4, A_5, B_5, C_5, D_5, E_5, F_5, G_5, H_5, I_5, J_5, K_5, A_6, B_6, C_6, D_6, E_6, F_6, G_6, H_6, I_6, J_6, K_6, A_7, B_7, C_7, D_7, E_7, F_7, G_7, H_7, I_7, J_7, K_7, A_8, B_8, C_8, D_8, E_8, F_8, G_8, H_8, I_8, J_8, K_8, A_9, B_9, C_9, D_9, E_9, F_9, G_9, H_9, I_9, J_9, K_9, A_10, B_10, C_10, D_10, E_10, F_10, G_10, H_10, I_10, J_10, K_10, A_11, B_11, C_11, D_11, E_11, F_11, G_11, H_11, I_11, J_11, K_11]
    allForestText = [['A_1'], ['B_1'], ['C_1'], ['D_1'], ['E_1'], ['F_1'], ['G_1'], ['H_1'], ['I_1'], ['J_1'], ['K_1'], ['A_2'], ['B_2'], ['C_2'], ['D_2'], ['E_2'], ['F_2'], ['G_2'], ['H_2'], ['I_2'], ['J_2'], ['K_2'], ['A_3'], ['B_3'], ['C_3'], ['D_3'], ['E_3'], ['F_3'], ['G_3'], ['H_3'], ['I_3'], ['J_3'], ['K_3'], ['A_4'], ['B_4'], ['C_4'], ['D_4'], ['E_4'], ['F_4'], ['G_4'], ['H_4'], ['I_4'], ['J_4'], ['K_4'], ['A_5'], ['B_5'], ['C_5'], ['D_5'], ['E_5'], ['F_5'], ['G_5'], ['H_5'], ['I_5'], ['J_5'], ['K_5'], ['A_6'], ['B_6'], ['C_6'], ['D_6'], ['E_6'], ['F_6'], ['G_6'], ['H_6'], ['I_6'], ['J_6'], ['K_6'], ['A_7'], ['B_7'], ['C_7'], ['D_7'], ['E_7'], ['F_7'], ['G_7'], ['H_7'], ['I_7'], ['J_7'], ['K_7'], ['A_8'], ['B_8'], ['C_8'], ['D_8'], ['E_8'], ['F_8'], ['G_8'], ['H_8'], ['I_8'], ['J_8'], ['K_8'], ['A_9'], ['B_9'], ['C_9'], ['D_9'], ['E_9'], ['F_9'], ['G_9'], ['H_9'], ['I_9'], ['J_9'], ['K_9'], ['A_10'], ['B_10'], ['C_10'], ['D_10'], ['E_10'], ['F_10'], ['G_10'], ['H_10'], ['I_10'], ['J_10'], ['K_10'], ['A_11'], ['B_11'], ['C_11'], ['D_11'], ['E_11'], ['F_11'], ['G_11'], ['H_11'], ['I_11'], ['J_11'], ['K_11']]
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K']
    dumbList = []
    
#Enemies----------------------------------------------------------------------------
    #0- Strength
    #1- Magic
    #2- Defence
    #3- Speed
    #4- Luck
    #5- HP
    #6- Name
    #7- Item Table
    #8 Attack1
    #9 Attack2
    #10 Attack3
    #11 Attack4
    #12 Attack5
    #13 Exp Points Reward
    #14 Level
    default = [1,1,1,1,1,1,'Test',[0,0,0,0],'1','2','3','4','5',100,0]
    slime = [1,1,1,1,1]
    rat = []
    enemiesList = [default]










    #for n in range(1, 12):
        #for i in range(len(alphabet)):
            #t = alphabet[i]
            #dumbList.append([str(t)#"_"#str(n)])
            #print(dumbList)
    

    