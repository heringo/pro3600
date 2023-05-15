import random

class Agent:
    def __init__(self, id, initial_wealth):
        self.id = id
        self.wealth = initial_wealth
        
    def trade(self, price, trade_volume):
        if self.wealth >= trade_volume * price:
            self.wealth -= trade_volume * price
        else:
            trade_volume = self.wealth / price
            self.wealth = 0
        return trade_volume

class Market:
    def __init__(self, initial_price, initial_volume, num_agents):
        self.price = initial_price
        self.volume = initial_volume
        self.agents = [Agent(i, 1000) for i in range(num_agents)]
        
    def simulate_market(self, num_steps):
        for step in range(num_steps):
            buyer = random.choice(self.agents)
            seller = random.choice(self.agents)
            trade_volume = random.uniform(0, 100)
            trade_volume = min(trade_volume, buyer.wealth / self.price, seller.wealth * self.price)
            buyer.wealth -= trade_volume * self.price
            seller.wealth += trade_volume * self.price
            self.volume += trade_volume
            self.price = (self.price * self.volume + trade_volume * self.price) / (self.volume + trade_volume)

market = Market(100, 1000, 1000)
market.simulate_market(10000)
print("Final Price: ", market.price)