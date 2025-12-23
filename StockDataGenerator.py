import random
from OHLCModel import OHLCData
from datetime import datetime


def StockPriceGenerator(PricingData: OHLCData, PriceChange)-> OHLCData:
    
    price_change_close = random.uniform(-PriceChange, PriceChange)
    new_close = round(PricingData.Close + price_change_close, 2)

    price_change_high = random.uniform(-PriceChange, PriceChange)
    new_high = round(PricingData.Close + price_change_close, 2)
    
    price_change_low = random.uniform(-PriceChange, PriceChange)
    new_low = round(PricingData.Close + price_change_low, 2)

    
    if new_high < PricingData.Low:
        new_high = round(PricingData.Low + abs(price_change_high),2)
    if new_low > PricingData.High:
        new_low = round(PricingData.High - abs(price_change_low),2)
    PricingData.High = new_high
    PricingData.Low = new_low

    
    if new_close > PricingData.High:
        PricingData.High = new_close
    if new_close < PricingData.Low:
        PricingData.Low = new_close
    
    
    PricingData.Open = PricingData.Close
    PricingData.Close = new_close
    
    
    PricingData.Volume = random.randint(500, 1500)
    
    
    PricingData.timestamp = datetime.now()
    return PricingData
