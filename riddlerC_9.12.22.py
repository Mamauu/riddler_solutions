import random
import numpy as np

def get_quality():
    teams =	{
        "a": random.random(),
        "b": random.random(),
        "c": random.random(),
        "d": random.random()
            }
    print(teams)
    return teams

def play(name1,name2):  
    q1 = teams[name1]
    q2 = teams[name2]
    win_percentage = q1/(q1+q2)
    if random.random() < win_percentage:
        return name1
    else:
        return name2

winner_q_list = list()
sample_size = 100000
for i in range(sample_size):

    teams = get_quality() #inital random qualities
    
    #semifinal 1
    winner1 = play("a","b")
    #print("semi1:", winner1)
    
    #semifinal 1
    winner2 = play("c","d")
    #print("semi2:", winner2)
    
    #final
    winner3 = play(winner1,winner2)
    winner_q_list.append(teams[winner3]) #write winning quality in list
    #print("final:", winner3, teams[winner3])

avq = np.average(winner_q_list)
print(avq)

#answer = 0.655085829092286
