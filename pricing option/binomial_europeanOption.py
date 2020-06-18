import numpy as np
import math
from decimal import Decimal
from StockOption import StockOption


class BinomialEuropeanOption(StockOption):

    def parameter_setup(self):
        # number of terminal nodes
        self.M = self.N + 1
        # 1 + probability of price going up
        self.up = 1 + self.pu
        # 1 - probability of price going down
        self.down = 1 - self.pd
        # probability * discount factor
        self.qu = (math.exp(self.rf - self.div) * self.dt()-self.down)/(self.up-self.down)
        self.qd = 1 - self.qu

    def init_stock_price_tree(self):
        # price at leaf nodes, from up to down
        self.Sts = np.zeros(self.M)
        for i in range(self.M):
            self.Sts[i] = self.s0 * (self.up ** (self.N - i)) * self.down**i

    def init_payoffs_tree(self):
        # Determine whether it is an call option or put option
        # Define payoff function according to which
        if self.is_call:
            return np.maximum(0, self.Sts - self.k)
        else:
            return np.maximum(0, self.k - self.Sts)

    def travers_tree(self, payoffs):
        # Starting from the last layer
        # Traverse the tree
        # and calculating payoff at each layer.
        for i in range(self.N):
            payoffs = (payoffs[:-1] * self.qu + payoffs[1:] * self.qd) * self.df()
        return payoffs

    def begin_traverse_tree(self):
        # payoffs at terminal nodes
        payoffs = self.init_payoffs_tree()
        return self.travers_tree(payoffs)

    def price(self):
        # Return: the pricing of the option
        # Call the above functions accordingly
        self.parameter_setup()
        self.init_stock_price_tree()
        payoffs = self.begin_traverse_tree()
        return payoffs[0]


# Usage:
# eu = BinomialEuropeanOption(50, 52, pu=0.2, pd=0.2, rf=0.05, T=2, N=3, is_put=True)
# print("The price of this option is :", eu.price())






