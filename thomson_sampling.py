import random
import numpy as np
import matplotlib.pyplot as plt 

d = 10 # total no of strategies 
N = 10000 # total number of users

#SIMULATION: 
conversion_rates = [0.05,0.13,0.09,0.16,0.11,0.04,0.20,0.08,0.01,0.21]
X = np.array(np.zeros([N,d]))

for i in range(N):
    for j in range(d):

        if np.random.rand() <= conversion_rates[j]:
            X[i,j] = 1 
    

# IMPLEMENTING RANDOM STARTEGY AND THOMSON SAMPLING
# VARIBALES FOR R.S and T.S 

strategies_selected_rs = [] 
strategies_selected_ts = []

total_reward_rs = 0
total_reward_ts = 0 

# number of times startegy 'i' has received a reward 1 up to round 'n'.
numbers_of_rewards_1 = [0] * d
# number of times startegy 'i' has received a reward 1 up to round 'n'.
numbers_of_rewards_0 = [0] * d

for n in range (0,N):
    # lets do it randomly first:
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs =  X[n,strategy_rs]
    total_reward_rs += reward_rs 

    # Lets do it using thomson sampling:
    #SETP 1:
    max_random = 0
    strategy_ts = 0
    for i in range(0,d):
        random_beta = random.betavariate(numbers_of_rewards_1[i]+1,numbers_of_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta 
            strategy_ts = i
    #SETP 2:
    reward_ts = X[n, strategy_ts]
    #SETEP 3:
    if reward_ts == 1: 
        numbers_of_rewards_1[strategy_ts] +=1 
    else:
        numbers_of_rewards_0[strategy_ts] +=1

    strategies_selected_ts.append(strategy_ts)
    total_reward_ts += reward_ts

# COMPUTE THE ABSOULTE AND RELATIVE REWARDS.
Absolute_Return =(total_reward_ts - total_reward_rs)*100
relative_Retrun = (total_reward_ts - total_reward_rs) / total_reward_rs * 100

print("Absolute Return :{:.0f} RS".format(Absolute_Return))
print("Relative_Return:{:.0f} %".format(relative_Retrun))

# LETS SEE IT VISUALLY:
plt.hist(strategies_selected_ts)
plt.title("HISTOGRAM OF SELECTIONS")
plt.xlabel('Strategy')
plt.ylabel('Number of times strategy was selected')
plt.show()
    
         






