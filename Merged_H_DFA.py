import dfa_class as dfac
#1->Comma
alphabet_H={','}
states_H={0,1}
tf_H=dict()


tf_H[(0,',')]=1

start_state_H=0
accept_states_H={1}

Merged_H = dfac.DFA(states=states_H,alphabet=alphabet_H,transition_function=tf_H,start_state=start_state_H,accept_states=accept_states_H,state_number_to_state_contents={1:'Comma'})
