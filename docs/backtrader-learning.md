Definitions
===========
Lines
-----
-   Succession of points that when joined together form a line
    -   Any one of these types can be in a line:
        -   Combination of Open, High, Low, Close, Volume, and OpenInterest
-   Data Feeds, Indicators and Strategies have lines

### "Line" part - Open
-   Market opens at 9:30AM EST
-   Market closes at 4:00PM
-   Price of option/security at 9:30AM

### "Line" part - High
-   Highest price a stock hit throughout the trading day

### "Line" part - Low
-   Lowest price a stock hit throughout the trading day

### "Line" part - Close
-   Price of option/security at 4:00PM

### "Line" part - Volume
-   Total amount of shares that were bought or sold throughout the day

### "Line" part - OpenInterest
-   Amount of people that actually have contracts open
-   Number of people invested into a company?

-   If we also consider "DateTime"

Index 0 Approach
----------------
-   0 = current position
-   -1 = last position

-   If array is:
        0  1  2  3  4  5
    -   accessing index "-1" refers to "5" above

Strategy
--------
-   What the algorithm is focused on? [confirm this]
    -   e.g. buying stock in Japan, shorting a security

Simple Moving average
---------------------
-   Average of the last X points, changing based on current position in time

Data Feed
---------
-   Current asset (i.e. individual stock) you're looking at - all of the data streaming in for it

-   Note: for Questrade:
    -   If you get the $80/$90 package, you get it on a minute-by-minute basis
    -   If you don't, it's every 15min (basically just retrospective)

DataSeries
----------
-   The underlying class in Data Feeds
-   Have aliases to access the well known OHLC (Open High Low Close) daily values

Cerebro
-------
-   Central class in Backtrader for:
    -   Gathering all inputs (Data Feeds), actors (Stratgegies), spectators (Observers),
        critics (Analyzers) and documenters (Writers) ensuring the show still goes on at any moment.
    -   Execute the backtesting/or live data feeding/trading
    -   Returning the results
    -   Giving access to the plotting facilities
-   (It's a God object)

Broker
------
- Basically your "bank account" in backtrader
- Stores

## Order types
-   ?

Slippage models
---------------
-   Slippage is the difference between estimated transaction costs and the amount
    actually paid. Brokers may not always be effective enough at executing orders.
    Market-impacted, liquidity, and frictional costs may also contribute.

Commission schemes
------------------
-   Structure of any costs we have to incur for interacting with the platform
    -   e.g. cost per each trade, cost per day of trading, etc.

Candle
------
-   Candle settles once / minute
-   You see the tug-of-war in real-time

Bid and ask
-----------
### Bid
-   Price where you'll buy (when a stock drops to it)

### Ask
-   Price where you'll sell (when a stock rises to it)

Margin order
------------
-   Purchase based on funds you don't have
    -   Purchasing stock based on the bank's money
-   Just fucking don't (for now)

Leverage
--------
-   The amount you can borrow
    -   Number of times you've borrowed against a portfolio determines the amount
        you're able to borrow


----------------------------------------------------------------------------------------------------
Backtrader terms
================
Exit concept
------------
-   When to sell



----------------------------------------------------------------------------------------------------
Indicators
----------
-   Examples:
    -   Moving average convergence divergence (MACD)
        -   Most common
        -   Long-term moving average
        -   Short-term moving average
        -   If a short-term moving average converges on a long-term moving average
        -   Detects "momentum" / "hype"
            -   (Example: Pump and dump will set this off)
            -   Picks up bubbles retrospectively
        -   Big thing here is when the lines cross, it's a good idea
        -   Note that it's not that reliable, you could be looking at just noise
            that's resulted in a cluster (i.e. a false pattern)

    -   Moving average

    -   Volume (for a particular stock)

    -   Standard deviation (volatility / risk)

-   If you want to track something about a stock over time

Motions
-------
-   Just what the market is doing
-


Resampling and Replaying
------------------------
# Resampling
-   ?

# Replaying
-   ?

Optimization scenario
---------------------
- (see Optimization section for more info)


----------------------------------------------------------------------------------------------------
Algorithm notes
===============
Factors for selection stocks
----------------------------
-    DO NOT TOUCH PENNY STOCKS
    -   The transaction cost is too high


----------------------------------------------------------------------------------------------------
####
CURRENT POSITION :: Just finished this section: "The broker says: Show me the money!"
https://www.backtrader.com/docu/quickstart/quickstart/#the-broker-says-show-me-the-money
####

