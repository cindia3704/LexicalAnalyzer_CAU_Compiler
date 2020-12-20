import dfa_class as dfac
#1->Terminating Symbol

alphabet_E={'j'}
states_E={0,1}
tf_E=dict()

tf_E[(0,';')]=1

start_state_E=0
accept_states_E={1}

Merged_E = dfac.DFA(states=states_E,alphabet=alphabet_E,transition_function=tf_E,start_state=start_state_E,accept_states=accept_states_E,state_number_to_state_contents={1:'Termingating_Symbol'})