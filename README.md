[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)

# Background 
Suppose an online business which is planing to maximize its revenue.
To maximize the revenue the company creates 10 subscription plan with different special deals. Afterwards, company wants to find the plan which attracts more user or which of the plan has highest conversion rate.They want to figure it out as soon as possible, and by saving the maximum costs, which one has the highest
conversion rate, because they know how finding and deploying that best strategy can significantly maximize
the revenues.

Then the company plans to show pop-up add to 1% of its user to choose between the 10 different subscription strategies.<br>

Lets assume that it had the rewrads matrix as :<br>

![alt](Capture.png)

Here row indicates the number of selected users and column indicates the number of strategies.<br>From the table we can see that user 0 was convinced by the strategy 4 and 8 and user 1 was convinced by strategy 7.
Now using Thompson Sampling, we have to find the best strategy that will have maximum convesion rate.<br>

For each round n, repeat, over 1000 rounds, the following three steps:<br>
1. Step 1. For each strategy i, we take a random draw from the following distribution:
θi(n) ∼ β(Ni1(n) + 1; Ni0(n) + 1)<br>
where:
 Ni1(n) is the number of times the strategy "i" has received a 1 reward up to round "n".<br>
  Ni0(n) is the number of times the strategy "i" has received a 0 reward up to round "n" 

2. Step 2. We select the strategy s(n) that has the highest θi(n):
s(n) = argmax
i2f1;:::;9g
(θi(n))

3. Step 3. We update Ns1(n)(n) and Ns0(n)(n) according to the following conditions:
<br>
• If the strategy selected s(n) received a 1 reward:
N1
s(n)(n) := Ns1(n)(n) + 1 <br>
• If the strategy selected s(n) received a 0 reward:
N0
s(n)(n) := Ns0(n)(n) + 1

Each strategy has its own beta distribution. Over the rounds, the beta distribution of the
strategy with the highest conversion rate will be progressively shifted to the right, and the beta distributions
of the strategies with lower conversion rates will be progressively shifted to the left (Steps 1 and 3). Therefore,
because of Step 2, the strategy with the highest conversion rate will be more and more selected.
To know more about beta distribution click [HERE](https://towardsdatascience.com/beta-distribution-intuition-examples-and-derivation-cf00f4db57af)

# Implemetation:
Lets assume that the company got the conversion rates as:<br>
conversion_rates = [0.05,0.13,0.09,0.16,0.11,0.04,0.20,0.08,0.01,0.21]<br>
By using this conversion rates we can easily form the 
rewrads matrix for 10,000 user as : 
```
d = 10 # total no of strategies 
N = 10000 # total number of users

#SIMULATION: 
conversion_rates = [0.05,0.13,0.09,0.16,0.11,0.04,0.20,0.08,0.01,0.21]
X = np.array(np.zeros([N,d]))

for i in range(N):
    for j in range(d):

        if np.random.rand() <= conversion_rates[j]:
            X[i,j] = 1 
```
So if we apply Thompson Sampling to this reward matrix, the sampling must select strategy 10 as we already know it has the highest conversion rate. In the implementation part we are also comapring Thompson with Random Strategy.

 






