import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Global variable for the ticker symbol
TICKER_SYMBOL = "^GSPC"

# Function to fetch historical data for a given ticker
def fetch_historical_data(ticker_symbol, years=10):
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365.25 * years)  # Approximate, considering leap years

        ticker = yf.Ticker(ticker_symbol)
        historical_data = ticker.history(start=start_date.strftime('%Y-%m-%d'),
                                          end=end_date.strftime('%Y-%m-%d'))
        
        # Check if data was returned
        if historical_data.empty:
            print(f"No data returned for {ticker_symbol}. Check the ticker symbol.")
            return None
        return historical_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    sp500_data = fetch_historical_data(TICKER_SYMBOL, years=10)
    if sp500_data is not None:
        # Print the first few rows of the data
        print(sp500_data.head())
        
        # Plot the closing prices
        sp500_data.plot.line(y='Close', use_index=True, title=f'{TICKER_SYMBOL} Closing Prices Over Last 10 Years')
        plt.xlabel('Date')  # Adding the x-axis label
        plt.ylabel('Close Price')  # Adding the y-axis label
        plt.show()  # Display the plot
