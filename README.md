I developed this project to gain hands-on experience with Apache Cassandra, one of the most widely adopted databases in the financial technology sector.

**The following steps outline my approach to data generation, storage, and visualization:**
1. Set up a local Cassandra instance using Docker to host the timeseries database
2. Build a stock pricing generator to randomly simulate price changes over a defined number of days
3. Integrate TradingView's `lightweight_charts` library to visualize the generated stock data
4. Connect the pricing generator to Cassandra to store the timeseries data
5. Create charts from the stored Cassandra data using the lightweight_charts visualization

<img width="1306" height="668" alt="Screenshot 2025-12-23 at 11 14 41 AM" src="https://github.com/user-attachments/assets/ed9a1acb-acb0-4dcf-b036-d6b02318d35a" />


<img width="764" height="931" alt="Screenshot 2025-12-23 at 11 20 13 AM" src="https://github.com/user-attachments/assets/2d891a92-997c-4763-8cf4-a9792ff56f41" />
