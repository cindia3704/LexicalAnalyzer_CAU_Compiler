import dfa_class as dfac
#1,2,3,4->Arithmetic_Operator
#5,6,7->Sign_Integer
#9,11->Floating_Point

alphabet_C={'*','/','+','-','0','1','2','3','4','5','6','7','8','9','.'}
states_C={0,1,2,3,4,5,6,7,8,9,10,11,12}
tf_C=dict()

state_number_to_state_contents={1,2,3,4,5,6,7,9,11}

tf_C[(0,'*')]=1
tf_C[(0,'/')]=2
tf_C[(0,'+')]=3
tf_C[(0,'-')]=4
tf_C[(0,'1')]=5
tf_C[(0,'2')]=5
tf_C[(0,'3')]=5
tf_C[(0,'4')]=5
tf_C[(0,'5')]=5
tf_C[(0,'6')]=5
tf_C[(0,'7')]=5
tf_C[(0,'8')]=5
tf_C[(0,'9')]=5
tf_C[(0,'0')]=6

tf_C[(4,'1')]=7
tf_C[(4,'2')]=7
tf_C[(4,'3')]=7
tf_C[(4,'4')]=7
tf_C[(4,'5')]=7
tf_C[(4,'6')]=7
tf_C[(4,'7')]=7
tf_C[(4,'8')]=7
tf_C[(4,'9')]=7

tf_C[(5,'1')]=5
tf_C[(5,'2')]=5
tf_C[(5,'3')]=5
tf_C[(5,'4')]=5
tf_C[(5,'5')]=5
tf_C[(5,'6')]=5
tf_C[(5,'7')]=5
tf_C[(5,'8')]=5
tf_C[(5,'9')]=5
tf_C[(5,'0')]=5
tf_C[(5,'.')]=8

tf_C[(6,'.')]=8

tf_C[(7,'1')]=7
tf_C[(7,'2')]=7
tf_C[(7,'3')]=7
tf_C[(7,'4')]=7
tf_C[(7,'5')]=7
tf_C[(7,'6')]=7
tf_C[(7,'7')]=7
tf_C[(7,'8')]=7
tf_C[(7,'9')]=7
tf_C[(7,'0')]=7
tf_C[(7,'.')]=8

tf_C[(8,'0')]=9
tf_C[(8,'1')]=11
tf_C[(8,'2')]=11
tf_C[(8,'3')]=11
tf_C[(8,'4')]=11
tf_C[(8,'5')]=11
tf_C[(8,'6')]=11
tf_C[(8,'7')]=11
tf_C[(8,'8')]=11
tf_C[(8,'9')]=11

tf_C[(9,'0')]=10
tf_C[(9,'1')]=11
tf_C[(9,'2')]=11
tf_C[(9,'3')]=11
tf_C[(9,'4')]=11
tf_C[(9,'5')]=11
tf_C[(9,'6')]=11
tf_C[(9,'7')]=11
tf_C[(9,'8')]=11
tf_C[(9,'9')]=11

tf_C[(10,'0')]=10
tf_C[(10,'1')]=11
tf_C[(10,'2')]=11
tf_C[(10,'3')]=11
tf_C[(10,'4')]=11
tf_C[(10,'5')]=11
tf_C[(10,'6')]=11
tf_C[(10,'7')]=11
tf_C[(10,'8')]=11
tf_C[(10,'9')]=11

tf_C[(11,'0')]=12
tf_C[(11,'1')]=11
tf_C[(11,'2')]=11
tf_C[(11,'3')]=11
tf_C[(11,'4')]=11
tf_C[(11,'5')]=11
tf_C[(11,'6')]=11
tf_C[(11,'7')]=11
tf_C[(11,'8')]=11
tf_C[(11,'9')]=11

tf_C[(12,'0')]=12
tf_C[(12,'1')]=11
tf_C[(12,'2')]=11
tf_C[(12,'3')]=11
tf_C[(12,'4')]=11
tf_C[(12,'5')]=11
tf_C[(12,'6')]=11
tf_C[(12,'7')]=11
tf_C[(12,'8')]=11
tf_C[(12,'9')]=11

start_state_C=0
accept_states_C={1,2,3,4,5,6,7,9,10,11,12}

#1,2,3,4->Arithmetic_Operator
#5,6,7->Sign_Integer
#9,11->Floating_Point


Merged_C = dfac.DFA(states=states_C,alphabet=alphabet_C,transition_function=tf_C,start_state=start_state_C,accept_states=accept_states_C,state_number_to_state_contents={1:'Arithmetic_Operator',2:'Arithmetic_Operator',3:'Arithmetic_Operator',4:'Arithmetic_Operator',5:'Sign_Integer',6:'Sign_Integer',7:'Sign_Integer',9:'Floating_Point',10:'Handling_0',11:'Floating_Point',12:'Handling_0'})