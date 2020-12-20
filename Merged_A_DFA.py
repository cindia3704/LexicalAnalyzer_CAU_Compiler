import dfa_class as dfac
#1,3,5,6,7,9,10,11,13,14,15,17,18,19,21,22,23,24,26,27,28,29,30,32,33,34,35,37,38,39,41,43 -> ID
#4,8,12,36 -> Var_Type
#16,40 -> Bool_String
#2,20,25,31,42->Special_Statement

All_input=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
All_alphabet_with_underscore=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_']
alphabet_A={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_'}

states_A={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43}
tf_A=dict()

#T0
for le in All_alphabet_with_underscore:
    if (le=='i'):
        tf_A[(0, le)] = 1
    elif(le=='c'):
        tf_A[(0, le)] = 5
    elif (le == 'b'):
        tf_A[(0, le)] = 9
    elif (le == 't'):
        tf_A[(0, le)] = 13
    elif (le == 'e'):
        tf_A[(0, le)] = 17
    elif (le == 'w'):
        tf_A[(0, le)] = 21
    elif (le == 'r'):
        tf_A[(0, le)] = 26
    elif (le=='f'):
        tf_A[(0, le)] = 32
    else:
        tf_A[(0, le)] = 43

#T1
for le in All_input:
    if(le=='f'):
        tf_A[(1, le)] = 2
    elif(le=='n'):
        tf_A[(1, le)] = 3
    else:
        tf_A[(1, le)] = 43
#T2
for le in All_input:
    tf_A[(2,le)]=43

#T3
for le in All_input:
    if(le=='t'):
        tf_A[(3, le)] = 4
    else:
        tf_A[(3, le)] = 43
#T4
for le in All_input:
    tf_A[(4, le)] = 43

#T5
for le in All_input:
    if(le=='h'):
        tf_A[(5,le)]=6
    else:
        tf_A[(5, le)] = 43
#T6
for le in All_input:
    if(le=='a'):
        tf_A[(6, le)] = 7
    else:
        tf_A[(6, le)] = 43
#T7
for le in All_input:
    if(le=='r'):
        tf_A[(7, le)] = 8
    else:
        tf_A[(7, le)] = 43
#T8
for le in All_input:
    tf_A[(8, le)] = 43
#T9
for le in All_input:
    if(le=='o'):
        tf_A[(9, le)] = 10
    else:
        tf_A[(9, le)] = 43
#T10
for le in All_input:
    if(le=='o'):
        tf_A[(10, le)] = 11
    else:
        tf_A[(10, le)] = 43
#T11
for le in All_input:
    if(le=='l'):
        tf_A[(11, le)] = 12
    else:
        tf_A[(11, le)] = 43
#T12
for le in All_input:
    tf_A[(12, le)] = 43

#T13
for le in All_input:
    if(le=='r'):
        tf_A[(13, le)] = 14
    else:
        tf_A[(13, le)] = 43
#T14
for le in All_input:
    if(le=='u'):
        tf_A[(14, le)] = 15
    else:
        tf_A[(14, le)] = 43
#T15
for le in All_input:
    if(le=='e'):
        tf_A[(15, le)] = 16
    else:
        tf_A[(15, le)] = 43
#T16
for le in All_input:
    tf_A[(16, le)] = 43

#T17
for le in All_input:
    if(le=='l'):
        tf_A[(17, le)] = 18
    else:
        tf_A[(17, le)] = 43

#T18
for le in All_input:
    if(le=='s'):
        tf_A[(18, le)] = 19
    else:
        tf_A[(18, le)] = 43

#T19
for le in All_input:
    if(le=='e'):
        tf_A[(19, le)] = 20
    else:
        tf_A[(19, le)] = 43

#T20
for le in All_input:
    tf_A[(20, le)] = 43

#T21
for le in All_input:
    if(le=='h'):
        tf_A[(21, le)] = 22
    else:
        tf_A[(21, le)] = 43
#T22
for le in All_input:
    if(le=='i'):
        tf_A[(22, le)] = 23
    else:
        tf_A[(22, le)] = 43
#T23
for le in All_input:
    if(le=='l'):
        tf_A[(23, le)] = 24
    else:
        tf_A[(23, le)] = 43
#T24
for le in All_input:
    if(le=='e'):
        tf_A[(24, le)] = 25
    else:
        tf_A[(24, le)] = 43

#T25
for le in All_input:
    tf_A[(25, le)] = 43

#T26
for le in All_input:
    if(le=='e'):
        tf_A[(26, le)] = 27
    else:
        tf_A[(26, le)] = 43
#T27
for le in All_input:
    if(le=='t'):
        tf_A[(27, le)] = 28
    else:
        tf_A[(27, le)] = 43

#T28
for le in All_input:
    if(le=='u'):
        tf_A[(28, le)] = 29
    else:
        tf_A[(28, le)] = 43

#T29
for le in All_input:
    if(le=='r'):
        tf_A[(29, le)] = 30
    else:
        tf_A[(29, le)] = 43

#T30
for le in All_input:
    if(le=='n'):
        tf_A[(30, le)] = 31
    else:
        tf_A[(30, le)] = 43

#T31
for le in All_input:
    tf_A[(31, le)] = 43

#T32
for le in All_input:
    if(le=='l'):
        tf_A[(32, le)] = 33
    elif(le=='a'):
        tf_A[(32, le)] = 37
    elif(le=='o'):
        tf_A[(32, le)] = 41
    else:
        tf_A[(32, le)] = 43
#T33
for le in All_input:
    if(le=='o'):
        tf_A[(33, le)] = 34
    else:
        tf_A[(33, le)] = 43

#T34
for le in All_input:
    if(le=='a'):
        tf_A[(34, le)] = 35
    else:
        tf_A[(34, le)] = 43

#T35
for le in All_input:
    if(le=='t'):
        tf_A[(35, le)] = 36
    else:
        tf_A[(35, le)] = 43

#T36
for le in All_input:
    tf_A[(36, le)] = 43

#T37
for le in All_input:
    if(le=='l'):
        tf_A[(37, le)] = 38
    else:
        tf_A[(37, le)] = 43

#T38
for le in All_input:
    if(le=='s'):
        tf_A[(38, le)] = 39
    else:
        tf_A[(38, le)] = 43

#T39
for le in All_input:
    if(le=='e'):
        tf_A[(39, le)] = 40
    else:
        tf_A[(39, le)] = 43

#T40
for le in All_input:
    tf_A[(40, le)] = 43

#T41
for le in All_input:
    if(le=='r'):
        tf_A[(41, le)] = 42
    else:
        tf_A[(41, le)] = 43
#T42
for le in All_input:
    tf_A[(42, le)] = 43

#T43
for le in All_input:
    tf_A[(43, le)] = 43

start_state_A=0
accept_states_A={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43}

Merged_A = dfac.DFA(states=states_A,alphabet=alphabet_A,transition_function=tf_A,start_state=start_state_A,accept_states=accept_states_A,state_number_to_state_contents={1:'ID',2:'Special_Statement',3:'ID',4:'Var_Type',5:'ID',6:'ID',7:'ID',8:'Var_Type',9:'ID',10:'ID',11:'ID',12:'Var_Type',13:'ID',14:'ID',15:'ID',16:'Bool_String',17:'ID',18:'ID',19:'ID',20:'Special_Statement',21:'ID',22:'ID',23:'ID',24:'ID',25:'Special_Statement',26:'ID',27:'ID',28:'ID',29:'ID',30:'ID',31:'Special_Statement',32:'ID',33:'ID',34:'ID',35:'ID',36:'Var_Type',37:'ID',38:'ID',39:'ID',40:'Bool_String',41:'ID',42:'Special_Statement',43:'ID'})




