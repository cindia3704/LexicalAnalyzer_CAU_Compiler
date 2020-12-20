import dfa_class as dfac

#1->LCurly
#2->RCurly

alphabet_G={'{','}'}
states_G={0,1,2}
tf_G=dict()

tf_G[(0,'{')]=1
tf_G[(0,'}')]=2

start_state_G=0
accept_states_G={1,2}

Merged_G = dfac.DFA(states=states_G,alphabet=alphabet_G,transition_function=tf_G,start_state=start_state_G,accept_states=accept_states_G,state_number_to_state_contents={1:'LBracket',2:'RBracket'})
