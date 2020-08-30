from math import exp as e


class StockOption(object):
    def __init__(self, s0, K, rf=0.05, T=1,
                 N=2, pu=0, pd=0, div=0,
                 sigma=0, is_put=False, is_am=False):
        self.s0 = s0        # stock price at time 0
        self.k = K          # strike price of the option
        self.rf = rf        # risk free interest rate
        self.T = T          # time to maturity
        self.N = max(1, N)   # number of time steps
        self.pu = pu        # probability that s0 will go up
        self.pd = pd        # probability that s0 will go down
        self.div = div      # dividend yield
        self.sigma = sigma      # risk
        self.is_put = is_put    # whether it is a put option or not
        self.is_am = is_am      # whether it is an American option or not
        self.is_call = not is_put   # whether it is a call option or not
        self.is_euro = not is_am    # whether it is a European option or not
        self.Sts = []       # stock price tree

    def dt(self):
        # It returns how long a single time step is in years
        return self.T/float(self.N)

    def df(self):
        # df: discount factor
        # e^(-rt)
        return e(-(self.rf - self.div) * self.dt())

    

s = StockOption()
print(s.rf)
s1 = StockOption(rf = 0.08)
print(s1.rf)







