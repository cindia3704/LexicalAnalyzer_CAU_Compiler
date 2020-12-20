class DFA:
    current_state=None #수정
    #nextIsArith_Op=0

    def __init__(self,states,alphabet,transition_function,start_state,accept_states,state_number_to_state_contents):
        self.states=states
        self.alphabet=alphabet
        self.transition_function=transition_function
        self.start_state=start_state
        self.accept_states=accept_states
        self.current_state=start_state
        self.state_number_to_state_contents=state_number_to_state_contents
        return
    def in_accept_state(self,a):
        return a in self.accept_states

    def emission_state_contents(self):
        return self.state_number_to_state_contents

    def transition_to_state_with_input(self,input_value):

        if((self.current_state,input_value) not in self.transition_function.keys()): #다음 키 값이 들어가지 않을때

            if(self.current_state in self.accept_states):
                last_state=self.current_state
                self.current_state=self.start_state

                return 0,"",last_state
            else:
                last_state=self.current_state
                print("Last State is not acceptable! ")
                return 0,"",last_state
        else:                                                                       #다음 키 값이 들어갈때(순회가 될때)
            self.current_state=self.transition_function[(self.current_state,input_value)]

            return 1,input_value,self.current_state

    def go_to_initial_state(self):
        self.current_state=self.start_state
        return
    pass
