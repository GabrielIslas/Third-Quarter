import numpy as np
import matplotlib.pyplot as plt


# Parameters, this are constant
n_years = 5
n_months = 12*n_years
r_bank = 0.005   # bank rate
r_stock = 0.05   # stock rate


# Initial state
C = 1000.0      # account balance
S = 100.0       # Stock price
n_stocks = 0.0  # how many stocks do I have


def sim_run(C, S, n_stocks):
    C_list = [C]
    S_list = [S]
    n_stocks_list = [n_stocks]

    for month in range(n_months):
        # Add interest to my account
        C = (1 + r_bank)*C
        C_list.append(C)

        # Change the stock price
        u = np.random.uniform(0, 1)
        if u < 0.25:
            S = (1 + r_stock)*S
        elif u < 0.5:
            S = (1 - r_stock)*S
        S_list.append(S)

        # Determine what to do
        if S < 95 and C > 0:
            n_stocks = C/S
            C = 0
        elif S > 110 and C == 0:
            C = n_stocks*S
            n_stocks = 0
        n_stocks_list.append(n_stocks)

    net_worth = C + S*n_stocks

    if 1340 < net_worth < 1360 and False:
        plt.subplot(311)
        plt.plot(C_list, label="Account balance")
        plt.legend()
        plt.subplot(312)
        plt.plot(S_list, label="Stock price")
        plt.legend()
        plt.plot(95*np.ones(len(S_list)))
        plt.plot(110*np.ones(len(S_list)))
        plt.subplot(313)
        plt.plot(n_stocks_list, label="Stocks")
        plt.legend()
        plt.show()

    return(net_worth)


n_sims = 10000  # How many sims to run
net_worth_list = []
for i in range(n_sims):
    net_worth_list.append(sim_run(C, S, n_stocks))

net_worth_list = np.array(net_worth_list)
print(net_worth_list.mean(), np.sqrt(net_worth_list.var()))
plt.hist(net_worth_list, bins=100)
plt.show()
