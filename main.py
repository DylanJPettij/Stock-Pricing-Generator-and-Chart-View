import StockDataGenerator
from cassandra.cluster import Cluster
import pandas as pd
from lightweight_charts import Chart
import datetime
import random

def generateStockData(symbol: str, daysback: int, session: Cluster):
    stock = StockDataGenerator.OHLCData(100,90,95,98,1000,"2024-01-01T00:00:00Z")
    dateCounter = daysback
    for _ in range(100):
        trade_date = datetime.date.today()-pd.Timedelta(days=dateCounter)
        
        #the price change parameter controls the volatility of the stock price changes
        stock = StockDataGenerator.StockPriceGenerator(stock,PriceChange=random.randint(1,5))
        session.execute('INSERT INTO stock_data (symbol, trade_date, close, dt, high, low, open, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                        (symbol, trade_date, stock.Close, stock.timestamp, stock.High, stock.Low, stock.Open, stock.Volume))
        dateCounter -= 1


def connectCassandra():
    cluster = Cluster(['0.0.0.0'], port=9042)
    session = cluster.connect("test_keyspace")
    return session
    

def chartData(session: Cluster):
    results = session.execute("SELECT * FROM stock_data")
    cols = results.column_names
    data = results.all()
    df = pd.DataFrame(data, columns=cols)
    df2 = pd.DataFrame()
    #open high low close volume
    df2['date'] = df['trade_date'].astype(str)
    df2['open'] = df['open'].astype(float)
    df2['high'] = df['high'].astype(float)
    df2['low'] = df['low'].astype(float)
    df2['close'] = df['close'].astype(float)
    df2['volume'] = df['volume'].astype(float)
    

    chart = Chart()
    chart.set(df=df2)
    chart.show(block=True)


def clearDatabase(session: Cluster):
    print("Clearing the stock_data table...")
    session.execute("TRUNCATE stock_data")
    

def main():
    choice = ''
    while choice != '4':
        print("what would you like to do?")
        print("1. Generate Stock Data")
        print("2. Visualize Stock Data")
        print("3. Clear Database")
        print("4. Exit")
        session = connectCassandra()
        choice = input("Enter your choice: ")
        if choice == '1':
    
            symbol = input("Enter the stock symbol to generate data for: ")
            daysback = int(input("Enter the number of days back to generate data for: "))
            generateStockData(symbol, daysback, session)
            print("Stock data generated and inserted into Cassandra.")
            return
        
        elif choice == '2':
            chartData(session)
        elif choice == '3':
            clearDatabase(session)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try Again.")
            return
    
if __name__ == '__main__':
    main()