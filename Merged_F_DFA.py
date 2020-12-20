import dfa_class as dfac
#1->lparen
#2->rparen

alphabet_F={'(',')'}
states_F={0,1,2}
tf_F=dict()

tf_F[(0,'(')]=1
tf_F[(0,')')]=2

start_state_F=0
accept_states_F={1,2}

Merged_F = dfac.DFA(states=states_F,alphabet=alphabet_F,transition_function=tf_F,start_state=start_state_F,accept_states=accept_states_F,state_number_to_state_contents={1:'LParen',2:'RParen'})
#눈 검정 완료