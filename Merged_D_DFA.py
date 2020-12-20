import dfa_class as dfac

alphabet_D={'=','!','<','>','&','|'}
states_D={0,1,2,3,4,5,6,7,8,9,10,11,12}
tf_D=dict()

tf_D[(0,'=')]=1
tf_D[(0,'!')] =2
tf_D[(0,'<')] =3
tf_D[(0,'>')] =4
tf_D[(0,'&')] =5
tf_D[(0,'|')] =6
tf_D[(1,'=')] =7
tf_D[(2,'=')] =8
tf_D[(3,'<')] =9
tf_D[(3,'=')] =10
tf_D[(4,'>')] =11
tf_D[(4,'=')] =12

start_state_D=0
accept_states_D={1,3,4,5,6,7,8,9,10,11,12}

Merged_D = dfac.DFA(states=states_D,alphabet=alphabet_D,transition_function=tf_D,start_state=start_state_D,accept_states=accept_states_D,state_number_to_state_contents={1:'AssignMent_Operator',3:'Comparison_Operator',4:'Comparison_Operator',5:'Bitwise_Operator',6:'Bitwise_Operator',7:'Comparison_Operator',8:'Comparison_Operator',9:'Bitwise_Operator',10:'Comparison_Operator',11:'Bitwise_Operator',12:'Comparison_Operator'})

#1->AssignMent_Operator
#3,4,7,8,10,12->Comparison_Operator
#5,6,9,11->Bitwise_Operator
