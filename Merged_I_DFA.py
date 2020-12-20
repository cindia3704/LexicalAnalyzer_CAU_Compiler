import dfa_class as dfac
#1->WhiteSpace
alphabet_I={'\t','\n',' '}
states_I={0,1}
tf_I=dict()


tf_I[(0,' ')]=1
tf_I[(0,'\t')]=1
tf_I[(0,'\n')]=1

start_state_I=0
accept_states_I={1}

Merged_I = dfac.DFA(states=states_I,alphabet=alphabet_I,transition_function=tf_I,start_state=start_state_I,accept_states=accept_states_I,state_number_to_state_contents={1:'WhiteSpace'})
