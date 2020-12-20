import dfa_class
import Merged_A_DFA as MgD_A
import Merged_B_DFA as MgD_B
import Merged_C_DFA as MgD_C
import Merged_D_DFA as MgD_D
import Merged_E_DFA as MgD_E
import Merged_F_DFA as MgD_F
import Merged_G_DFA as MgD_G
import Merged_H_DFA as MgD_H
import Merged_I_DFA as MgD_I
is_in_DFA=0 #지금 DFA에 있는지를 확인하는 변수
current_TOKEN="" #현재 DFA의 State의 내용이 담긴 변수
prior_TOKEN="" #이전 DFA의 state의 내용이 담긴 변수(arithmetic 하고 floating 검사 위함) (ERRHAN) (단 whitespace는 저장안함)
what_DFA="" #어떤 DFA에 있는지 저장하는 변수이다. (Merged_A~에 있는지)
buffer_string=''#들어온 input들을 저장해주는 변수이다.
current_state=0 #현재의 state 번호를 저장
is_DFA_Over=0 #DFA가 끝났는지, 다음 input이 들어갔을때 DFA에 들어가지 않고 그 state가 accept 일때
number_of_line=1
#세가지 경우
#input이 들어갔을때 DFA에는 들어갔으나 마지막 state가 accept일때(아직모름)(뒤에꺼까지 확인필요)
#input이 들어갔을때 DFA에는 들어갔으나 마지막 state가 accept가 아닐때(ERRHAN)
#input이 들어갔을때 DFA에 안들어갔는데 마지막 state가 accept가 아닐때(ERRHAN)
##pythonfiddle.com/dfa-simple-implementation/

#what_DFA(어디 DFA를 참조해야하는 가)와 is_in_DFA(지금 DFA에 들어있다를 알려줌)
def Start_DFA(a):
    global what_DFA
    global buffer_string
    global is_in_DFA

    if (a=='a'or a=='A'or a=='b'or a=='B'or a=='c'or a=='C'or a=='d'or a=='D'or a=='e'or a=='E'or a=='f'or a=='F'or a=='g'or a=='G'or a=='h'or a=='H'or a=='i'or a=='I'or a=='j'or a=='J'or a=='k'or a=='K'or a=='l'or a=='L'or a=='m'or a=='M'or a=='n'or a=='N'or a=='o'or a=='O'or a=='p'or a=='P'or a=='q'or a=='Q'or a=='r'or a=='R'or a=='s'or a=='S'or a=='t'or a=='T'or a=='u'or a=='U'or a=='v'or a=='V'or a=='w'or a=='W'or a=='x'or a=='X'or a=='y'or a=='Y'or a=='z'or a=='Z'or a=='_' ):
        what_DFA = 'A'
        is_in_DFA=1
    elif(a=='"'):
        what_DFA = 'B'
        is_in_DFA = 1
    elif(a=='+' or a=='-'or a=='*' or a=='/' or a=='0' or a=='1' or a=='2' or a=='3' or a=='4' or a=='5' or a=='6' or a=='7' or a=='8' or a=='9'):
        what_DFA = 'C'
        is_in_DFA = 1
    elif(a=='=' or a=='!' or a=='<' or a=='>' or a=='&' or a=='|'):
        what_DFA = 'D'
        is_in_DFA = 1
    elif(a==';'):
        what_DFA = 'E'
        is_in_DFA = 1
    elif(a=='(' or a==')'):
        what_DFA = 'F'
        is_in_DFA = 1
    elif(a=='{' or a=='}'):
        what_DFA = 'G'
        is_in_DFA = 1
    elif(a==','):
        what_DFA = 'H'
        is_in_DFA = 1
    elif(a.isspace()):
        what_DFA = 'I'
        is_in_DFA = 1
    else:
        print("Undefined Symbols!")
        what_DFA = 'ERROR'
        exit()


print("Enter File Name to Lexical Analysis")
file_name=input()
f=open(file_name,'r',encoding='Utf_8')

s=f.read()
fw=open('output.txt','w')

counter=0
for a in s:                     #한글자씩 읽음
    if (is_in_DFA==0):
        Start_DFA(a)
    if (is_in_DFA==1):  #처음에 어느 Merged_DFA에 들어가는지 판별이 되면 그 값을 Merged에 넣어줌/다음것도 계속
        if(what_DFA=='A'):
            is_in_DFA,input_value,current_state=MgD_A.Merged_A.transition_to_state_with_input(a)
            if(input_value==""): #이때는 언제냐! DFA_class의 정의상 DFA에 다음인풋이 안들어갈때임
                if(MgD_A.Merged_A.in_accept_state(current_state)):
                    fw.write("<"+MgD_A.Merged_A.emission_state_contents()[current_state]+","+buffer_string+">")
                    buffer_string="" #버퍼스트링 초기화
                    prior_TOKEN=MgD_A.Merged_A.emission_state_contents()[current_state]
                    is_in_DFA=0    #DFA를 벗어났음을 나타냄
                    is_DFA_Over=1  #DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line "+str(number_of_line))
                    exit()
            else: #이떄는 DFA_class의 정상 DFA에 다음인풋이 잘 들어갈때임
                buffer_string=buffer_string+input_value #버퍼스트링에 잘 저장
                is_DFA_Over=0
        elif (what_DFA == 'B'):
            is_in_DFA, input_value, current_state = MgD_B.Merged_B.transition_to_state_with_input(a)
            if (input_value == ""):
                if (MgD_B.Merged_B.in_accept_state(current_state)):
                    fw.write("<" + MgD_B.Merged_B.emission_state_contents()[current_state] + "," + buffer_string + ">")
                    prior_TOKEN = MgD_B.Merged_B.emission_state_contents()[current_state]
                    buffer_string = ""  # 버퍼스트링 초기화
                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()
            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
        elif (what_DFA == 'C'):
            is_in_DFA, input_value, current_state = MgD_C.Merged_C.transition_to_state_with_input(a)
            if (input_value == ""):
                if(MgD_C.Merged_C.in_accept_state(current_state)):
                    if (current_state == 7 or current_state == 9 or current_state == 11):  # 앞이 숫자일때
                        if (prior_TOKEN == 'Sign_Integer' or prior_TOKEN == 'Floating_Point' or prior_TOKEN=='ID'):
                            if (buffer_string[0] == '-'):
                                fw.write("<Arithmetic_Operator,"+buffer_string[0]+">")
                                fw.write("<"+MgD_C.Merged_C.emission_state_contents()[current_state]+","+buffer_string[1:]+">")
                                prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                                buffer_string = ""  # 버퍼스트링 초기화
                                is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                                is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                            else:
                                fw.write("<"+MgD_C.Merged_C.emission_state_contents()[current_state]+","+buffer_string+">")
                                prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                                buffer_string = ""  # 버퍼스트링 초기화
                                is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                                is_DFA_Over = 1  # DFA가 끝났음을 나타냄

                        else:
                            fw.write("<"+MgD_C.Merged_C.emission_state_contents()[current_state]+","+buffer_string+">")
                            prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                            buffer_string = ""  # 버퍼스트링 초기화
                            is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                            is_DFA_Over = 1  # DFA가 끝났음을 나타냄


                    elif(current_state==10):  #0.00000 이나 5.0000
                        counter=0
                        if(a=='.'):
                            for k in buffer_string:
                                counter=counter+1
                                if(k=='.'):
                                    fw.write("<Floating_Point,"+buffer_string[0:counter+1]+">")
                                    break
                            for number_integer in range(len(buffer_string)-counter-2):
                                fw.write("<Sign_Integer,0>")
                                prior_TOKEN="Sign_Integer"
                            buffer_string='0.'
                            MgD_C.Merged_C.go_to_initial_state()
                            MgD_C.Merged_C.transition_to_state_with_input('0')
                            MgD_C.Merged_C.transition_to_state_with_input('.')
                            current_state=8
                            what_DFA='C'
                            is_in_DFA=1
                            is_DFA_Over=0
                        else:
                            for k in buffer_string:
                                counter=counter+1
                                if(k=='.'):
                                    fw.write("<Floating_Point,"+buffer_string[0:counter+1]+">")
                                    break
                            for number_integer in range(len(buffer_string)-counter-1):
                                fw.write("<Sign_Integer,0>")
                                prior_TOKEN="Sign_Integer"
                            buffer_string = ""  # 버퍼스트링 초기화
                            is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                            is_DFA_Over = 1  # DFA가 끝났음을 나타냄

                    elif(current_state==12):   #81.1541000
                        counter=0
                        if(a=='.'):
                            for k in buffer_string[::-1]:
                                if(k =='0'):
                                    counter=counter+1
                                elif(k!='0'):
                                    break
                            fw.write("<Floating_Point,"+buffer_string[0:-(counter)]+">")
                            for number_integer in range(counter-1):
                                fw.write("<Sign_Integer,0>")
                                prior_TOKEN = "Sign_Integer"
                            buffer_string = '0.'
                            MgD_C.Merged_C.go_to_initial_state()
                            MgD_C.Merged_C.transition_to_state_with_input('0')
                            MgD_C.Merged_C.transition_to_state_with_input('.')
                            what_DFA = 'C'
                            current_state = 8
                            is_in_DFA = 1
                            is_DFA_Over = 0
                        else:
                            for k in buffer_string[::-1]:
                                if(k =='0'):
                                    counter=counter+1
                                elif(k!='0'):
                                    break
                            fw.write("<Floating_Point,"+buffer_string[0:-(counter)]+">")
                            for number_integer in range(counter):
                                fw.write("<Sign_Integer,0>")
                                prior_TOKEN = "Sign_Integer"

                            buffer_string = ""  # 버퍼스트링 초기화
                            is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                            is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("<"+MgD_C.Merged_C.emission_state_contents()[current_state]+","+buffer_string+">")
                        prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()

            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
                #C부분은 추가적으로 설명 필요
        elif (what_DFA == 'D'):
            is_in_DFA, input_value, current_state = MgD_D.Merged_D.transition_to_state_with_input(a)
            if (input_value == ""):
                if (MgD_D.Merged_D.in_accept_state(current_state)):
                    fw.write("<" +  MgD_D.Merged_D.emission_state_contents()[current_state] + "," +buffer_string+ ">")
                    prior_TOKEN = MgD_D.Merged_D.emission_state_contents()[current_state]
                    buffer_string = ""  # 버퍼스트링 초기화
                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()
            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
        elif (what_DFA == 'E'):
            is_in_DFA, input_value, current_state = MgD_E.Merged_E.transition_to_state_with_input(a)
            if (input_value == ""):
                if (MgD_E.Merged_E.in_accept_state(current_state)):
                    fw.write("<" + MgD_E.Merged_E.emission_state_contents()[current_state] + "," + buffer_string + ">")
                    prior_TOKEN = MgD_E.Merged_E.emission_state_contents()[current_state]
                    buffer_string = ""  # 버퍼스트링 초기화
                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()
            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
        elif (what_DFA == 'F'):
            is_in_DFA, input_value, current_state = MgD_F.Merged_F.transition_to_state_with_input(a)
            if (input_value == ""):
                if (MgD_F.Merged_F.in_accept_state(current_state)):
                    fw.write("<" +  MgD_F.Merged_F.emission_state_contents()[current_state] + "," +buffer_string+ ">")
                    prior_TOKEN = MgD_F.Merged_F.emission_state_contents()[current_state]
                    buffer_string = ""  # 버퍼스트링 초기화
                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()
            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
        elif (what_DFA == 'G'):
            is_in_DFA, input_value, current_state = MgD_G.Merged_G.transition_to_state_with_input(a)
            if (input_value == ""):
                if (MgD_G.Merged_G.in_accept_state(current_state)):
                    fw.write("<" + MgD_G.Merged_G.emission_state_contents()[current_state] + "," + buffer_string + ">")
                    prior_TOKEN = MgD_G.Merged_G.emission_state_contents()[current_state]
                    buffer_string = ""  # 버퍼스트링 초기화
                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()
            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
        elif (what_DFA == 'H'):
            is_in_DFA, input_value, current_state = MgD_H.Merged_H.transition_to_state_with_input(a)
            if (input_value == ""):
                if (MgD_H.Merged_H.in_accept_state(current_state)):
                    fw.write("<" +MgD_H.Merged_H.emission_state_contents()[current_state]+ "," + buffer_string + ">")
                    prior_TOKEN = MgD_H.Merged_H.emission_state_contents()[current_state]
                    buffer_string = ""  # 버퍼스트링 초기화
                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()
            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
        elif (what_DFA == 'I'):
            is_in_DFA, input_value, current_state = MgD_I.Merged_I.transition_to_state_with_input(a)
            if (input_value == ""):
                if (MgD_I.Merged_I.in_accept_state(current_state)):
                    if (buffer_string=="\n"):
                        number_of_line = number_of_line + 1
                        prior_TOKEN = MgD_I.Merged_I.emission_state_contents()[current_state]
                        fw.write("<"+ MgD_I.Merged_I.emission_state_contents()[current_state] + ",\\n>")
                    elif(buffer_string=="\t"):
                        fw.write("<"+ MgD_I.Merged_I.emission_state_contents()[current_state] + ",\\t>")
                    else:
                        fw.write("<" + MgD_I.Merged_I.emission_state_contents()[current_state] + ", >")
                    buffer_string = ""  # 버퍼스트링 초기화
                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                else:
                    if (buffer_string=="\n"):
                        number_of_line = number_of_line + 1
                    fw.write("There is error in Line " + str(number_of_line))
                    exit()
            else:
                buffer_string = buffer_string + input_value
                is_DFA_Over = 0
        else:
            if (a == '\n'):
                number_of_line = number_of_line + 1
            fw.write("There is error in Line "+str(number_of_line))
            exit()

    if(is_in_DFA==0 and is_DFA_Over==1): #여기는 뭐냐면 인제 마지막 으로 들어간 인풋이 안들어갔을때임 -> 이 인풋도 다시 어딘가에 넣어줘야하자너? #근데 이게 하나가 오고 또 바로 잘못될수가 있단말이지(엥 while을 쓸 필요가 있나?) (if만 써도 뭔가 같은값이 나올듯) (ERRHAN)
        Start_DFA(a)
        if (is_in_DFA == 1):  # 처음에 어느 Merged_DFA에 들어가는지 판별이 되면 그 값을 Merged에 넣어줌/다음것도 계속
            if (what_DFA == 'A'):
                is_in_DFA, input_value, current_state = MgD_A.Merged_A.transition_to_state_with_input(a)
                if (input_value == ""):  # 이때는 언제냐! DFA_class의 정의상 DFA에 다음인풋이 안들어갈때임
                    if (MgD_A.Merged_A.in_accept_state(current_state)):
                        fw.write("<"+MgD_A.Merged_A.emission_state_contents()[current_state]+","+buffer_string+">")
                        prior_TOKEN = MgD_A.Merged_A.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line "+str(number_of_line))
                        exit()
                else:  # 이떄는 DFA_class의 정상 DFA에 다음인풋이 잘 들어갈때임
                    buffer_string = buffer_string + input_value  # 버퍼스트링에 잘 저장
                    is_DFA_Over = 0
            elif (what_DFA == 'B'):
                is_in_DFA, input_value, current_state = MgD_B.Merged_B.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_B.Merged_B.in_accept_state(current_state)):
                        fw.write("<" + MgD_B.Merged_B.emission_state_contents()[current_state] + "," + buffer_string + ">")
                        prior_TOKEN = MgD_B.Merged_B.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()
                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            elif (what_DFA == 'C'):
                is_in_DFA, input_value, current_state = MgD_C.Merged_C.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_C.Merged_C.in_accept_state(current_state)):
                        if (current_state == 7 or current_state == 9 or current_state == 11):  # 앞이 숫자일때
                            if (
                                    prior_TOKEN == 'Sign_Integer' or prior_TOKEN == 'Floating_Point' or prior_TOKEN == 'ID'):
                                if (buffer_string[0] == '-'):
                                    fw.write("<Arithmetic_Operator," + buffer_string[0] + ">")
                                    fw.write("<" + MgD_C.Merged_C.emission_state_contents()[
                                        current_state] + "," + buffer_string[1:] + ">")
                                    prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                                    buffer_string = ""  # 버퍼스트링 초기화
                                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                                else:
                                    fw.write("<" + MgD_C.Merged_C.emission_state_contents()[
                                        current_state] + "," + buffer_string + ">")
                                    prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                                    buffer_string = ""  # 버퍼스트링 초기화
                                    is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                                    is_DFA_Over = 1  # DFA가 끝났음을 나타냄

                            else:
                                fw.write("<" + MgD_C.Merged_C.emission_state_contents()[
                                    current_state] + "," + buffer_string + ">")
                                prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                                buffer_string = ""  # 버퍼스트링 초기화
                                is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                                is_DFA_Over = 1  # DFA가 끝났음을 나타냄


                        elif (current_state == 10):  # 0.00000 이나 5.0000
                            counter = 0
                            if (a == '.'):
                                for k in buffer_string:
                                    counter = counter + 1
                                    if (k == '.'):
                                        fw.write("<Floating_Point," + buffer_string[0:counter + 1] + ">")
                                        break
                                for number_integer in range(len(buffer_string) - counter - 2):
                                    fw.write("<Sign_Integer,0>")
                                    prior_TOKEN = "Sign_Integer"
                                buffer_string = '0.'
                                MgD_C.Merged_C.go_to_initial_state()
                                MgD_C.Merged_C.transition_to_state_with_input('0')
                                MgD_C.Merged_C.transition_to_state_with_input('.')
                                current_state = 8
                                what_DFA = 'C'
                                is_in_DFA = 1
                                is_DFA_Over = 0
                            else:
                                for k in buffer_string:
                                    counter = counter + 1
                                    if (k == '.'):
                                        fw.write("<Floating_Point," + buffer_string[0:counter + 1] + ">")
                                        break
                                for number_integer in range(len(buffer_string) - counter - 1):
                                    fw.write("<Sign_Integer,0>")
                                    prior_TOKEN = "Sign_Integer"
                                buffer_string = ""  # 버퍼스트링 초기화
                                is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                                is_DFA_Over = 1  # DFA가 끝났음을 나타냄

                        elif (current_state == 12):  # 81.1541000
                            counter = 0
                            if (a == '.'):
                                for k in buffer_string[::-1]:
                                    if (k == '0'):
                                        counter = counter + 1
                                    elif (k != '0'):
                                        break
                                fw.write("<Floating_Point," + buffer_string[0:-(counter)] + ">")
                                for number_integer in range(counter - 1):
                                    fw.write("<Sign_Integer,0>")
                                    prior_TOKEN = "Sign_Integer"
                                buffer_string = '0.'
                                MgD_C.Merged_C.go_to_initial_state()
                                MgD_C.Merged_C.transition_to_state_with_input('0')
                                MgD_C.Merged_C.transition_to_state_with_input('.')
                                current_state = 8
                                what_DFA = 'C'
                                is_in_DFA = 1
                                is_DFA_Over = 0
                            else:
                                for k in buffer_string[::-1]:
                                    if (k == '0'):
                                        counter = counter + 1
                                    elif (k != '0'):
                                        break
                                fw.write("<Floating_Point," + buffer_string[0:-(counter)] + ">")
                                for number_integer in range(counter):
                                    fw.write("<Sign_Integer,0>")
                                    prior_TOKEN = "Sign_Integer"

                                buffer_string = ""  # 버퍼스트링 초기화
                                is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                                is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                        else:
                            fw.write("<" + MgD_C.Merged_C.emission_state_contents()[
                                current_state] + "," + buffer_string + ">")
                            prior_TOKEN = MgD_C.Merged_C.emission_state_contents()[current_state]
                            buffer_string = ""  # 버퍼스트링 초기화
                            is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                            is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()

                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            elif (what_DFA == 'D'):
                is_in_DFA, input_value, current_state = MgD_D.Merged_D.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_D.Merged_D.in_accept_state(current_state)):
                        fw.write("<" +  MgD_D.Merged_D.emission_state_contents()[current_state] + "," +buffer_string+ ">")
                        prior_TOKEN = MgD_D.Merged_D.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()
                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            elif (what_DFA == 'E'):
                is_in_DFA, input_value, current_state = MgD_E.Merged_E.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_E.Merged_E.in_accept_state(current_state)):
                        fw.write("<" + MgD_E.Merged_E.emission_state_contents()[current_state] + "," + buffer_string + ">")
                        prior_TOKEN = MgD_E.Merged_E.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()
                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            elif (what_DFA == 'F'):
                is_in_DFA, input_value, current_state = MgD_F.Merged_F.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_F.Merged_F.in_accept_state(current_state)):
                        fw.write("<" +  MgD_F.Merged_F.emission_state_contents()[current_state] + "," +buffer_string+ ">")
                        prior_TOKEN = MgD_F.Merged_F.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()
                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            elif (what_DFA == 'G'):
                is_in_DFA, input_value, current_state = MgD_G.Merged_G.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_G.Merged_G.in_accept_state(current_state)):
                        fw.write("<" + MgD_G.Merged_G.emission_state_contents()[current_state] + "," + buffer_string + ">")
                        prior_TOKEN = MgD_G.Merged_G.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()
                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            elif (what_DFA == 'H'):
                is_in_DFA, input_value, current_state = MgD_H.Merged_H.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_H.Merged_H.in_accept_state(current_state)):
                        fw.write("<" +MgD_H.Merged_H.emission_state_contents()[current_state]+ "," + buffer_string + ">")
                        prior_TOKEN = MgD_H.Merged_H.emission_state_contents()[current_state]
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()
                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            elif (what_DFA == 'I'):
                is_in_DFA, input_value, current_state = MgD_I.Merged_I.transition_to_state_with_input(a)
                if (input_value == ""):
                    if (MgD_I.Merged_I.in_accept_state(current_state)):
                        if (buffer_string == "\n"):
                            number_of_line = number_of_line + 1
                            prior_TOKEN = MgD_I.Merged_I.emission_state_contents()[current_state]
                            fw.write("<" + MgD_H.Merged_I.emission_state_contents()[current_state] + ",\\n>")
                        elif (buffer_string == "\t"):
                            fw.write("<" + MgD_H.Merged_I.emission_state_contents()[current_state] + ",\\t>")
                        else:
                            fw.write("<" + MgD_H.Merged_I.emission_state_contents()[current_state] + ", >")
                        buffer_string = ""  # 버퍼스트링 초기화
                        is_in_DFA = 0  # DFA를 벗어났음을 나타냄
                        is_DFA_Over = 1  # DFA가 끝났음을 나타냄
                    else:
                        if (buffer_string == "\n"):
                            number_of_line = number_of_line + 1
                        fw.write("There is error in Line " + str(number_of_line))
                        exit()
                else:
                    buffer_string = buffer_string + input_value
                    is_DFA_Over = 0
            else:
                if (a == '\n'):
                    number_of_line = number_of_line + 1
                fw.write("There is error in Line "+str(number_of_line))
                exit()

if (is_in_DFA==1):                #마지막은 그냥 잘 저장되고 끝난다는 가정하에 아무런 출력도 하지않아서 마지막을 출력하기 위한 코드
    #print(buffer_string)         #여기서도 뭔가 accept가 잘 안되면(아마 MgD_A->emission에서 처리가 한번에 될듯)(ERRHAN)
    if(what_DFA=='A'):
        if (MgD_A.Merged_A.in_accept_state(current_state)):
            fw.write("<"+MgD_A.Merged_A.emission_state_contents()[current_state]+","+buffer_string+">")
        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif(what_DFA=='B'):
        if (MgD_B.Merged_B.in_accept_state(current_state)):
            fw.write("<"+MgD_B.Merged_B.emission_state_contents()[current_state]+","+buffer_string+">")
        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif (what_DFA == 'C'):
        if (MgD_C.Merged_C.in_accept_state(current_state)):
            if (current_state == 7 or current_state == 9 or current_state == 11):  # 앞이 숫자일때
                if (prior_TOKEN == 'Sign_Integer' or prior_TOKEN == 'Floating_Point'):
                    if (buffer_string[0] == '-'):
                        fw.write("<Arithmetic_Operator," + buffer_string[0] + ">")
                        fw.write("<" + MgD_C.Merged_C.emission_state_contents()[current_state] +"," +buffer_string[1:] + ">")
                    else:
                        fw.write("<" + MgD_C.Merged_C.emission_state_contents()[current_state] + "," + buffer_string + ">")
                else:
                    fw.write("<" + MgD_C.Merged_C.emission_state_contents()[current_state] + "," + buffer_string + ">")

            elif (current_state == 10):  # 0.00000 이나 5.0000
                counter = 0
                for k in buffer_string:
                    counter = counter + 1
                    if (k == '.'):
                        fw.write("<Floating_Point," + buffer_string[0:counter+1] + ">")
                        break
                for number_integer in range(len(buffer_string) - counter - 1):
                    fw.write("<Sign_Integer,0>")

            elif (current_state == 12):  # 81.1541000
                counter = 0
                for k in buffer_string[::-1]:
                    if (k == '0'):
                        counter = counter + 1
                    elif (k != '0'):
                        break
                fw.write("<Floating_Point," + buffer_string[0:-(counter)] + ">")
                for number_integer in range(counter):
                    fw.write("<Sign_Integer,0>")


            else:
                fw.write("<" + MgD_C.Merged_C.emission_state_contents()[current_state] + "," + buffer_string + ">")

        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif (what_DFA == 'D'):
        if (MgD_D.Merged_D.in_accept_state(current_state)):
            fw.write("<"+MgD_D.Merged_D.emission_state_contents()[current_state]+","+buffer_string+">")
        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif (what_DFA == 'E'):
        if (MgD_E.Merged_E.in_accept_state(current_state)):
            fw.write("<" + MgD_E.Merged_E.emission_state_contents()[current_state] + "," + buffer_string + ">")
        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif (what_DFA == 'F'):
        if (MgD_F.Merged_F.in_accept_state(current_state)):
            fw.write("<"+MgD_F.Merged_F.emission_state_contents()[current_state]+","+buffer_string+">")
        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif (what_DFA == 'G'):
        if (MgD_G.Merged_G.in_accept_state(current_state)):
            fw.write("<"+MgD_G.Merged_G.emission_state_contents()[current_state]+","+buffer_string+">")
        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif (what_DFA == 'H'):
        if (MgD_H.Merged_H.in_accept_state(current_state)):
            fw.write("<"+MgD_H.Merged_H.emission_state_contents()[current_state]+","+buffer_string+">")
        else:
            fw.write("There is error in Line " + str(number_of_line))
            exit()
    elif (what_DFA == 'I'):
        if (MgD_I.Merged_I.in_accept_state(current_state)):
            if (buffer_string == "\n"):
                number_of_line = number_of_line + 1
                prior_TOKEN = MgD_I.Merged_I.emission_state_contents()[current_state]
                fw.write("<" + MgD_I.Merged_I.emission_state_contents()[current_state] + ",\\n>")
            elif (buffer_string == "\t"):
                fw.write("<" + MgD_I.Merged_I.emission_state_contents()[current_state] + ",\\t>")
            else:
                fw.write("<" + MgD_I.Merged_I.emission_state_contents()[current_state] + ", >")
        else:
            if (buffer_string=="\n"):
                number_of_line = number_of_line + 1
            fw.write("There is error in Line " + str(number_of_line))
            exit()


f.close()
fw.close()
