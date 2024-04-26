class BuyLowSellHighAlgorithm(QCAlgorithm):
    
    def Initialize(self):
        self.SetStartDate(2024, 1, 1)
        self.SetEndDate(2024, 1, 31)
        self.SetCash(10000)
        self.AddEquity("BIL", Resolution.Daily)
        
        self.buy_price = 91.42
        self.sell_price = 91.62
        self.current_holdings = 0
        
        self.Schedule.On(self.DateRules.EveryDay("BIL"), self.TimeRules.AfterMarketOpen("BIL", 30), self.Trade)
        
    def OnData(self, data):
        pass
    
    def Trade(self):
        price = self.Securities["BIL"].Price
        
        if price <= self.buy_price - 0.02 and self.current_holdings == 0:
            self.SetHoldings("BIL", 1)
            self.current_holdings = 1
            self.Log("Buying 1 share of BIL at price: {}".format(price))
        
        if price >= self.sell_price + 0.02 and self.current_holdings == 1:
            self.Liquidate("BIL")
            self.current_holdings = 0
            self.Log("Selling 1 share of BIL at price: {}".format(price))
