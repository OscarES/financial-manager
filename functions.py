from __future__ import division # needed for 1/2 = 0.5

# The balance sheet equation
def balanceSheetEquation(liabilities, shareholdersEquity):
    return liabilities + shareholdersEquity

#print balanceSheetEquation(61374, 78202)

# market value of equity, also called market capitalization. Is function, there also exists a variable with this name
def marketValueOfEquity(sharesOutstanding, marketPricePerShare):
    return sharesOutstanding*marketPricePerShare

#print marketValueOfEquity(50664, 1.72)

# market-to-book ratio, also called price-to-book [P/B] ratio
def marketToBookRatio(marketValueOfEquity, bookValueOfEquity):
    return marketValueOfEquity/bookValueOfEquity

#marketValueOfEquity = 87142
#print marketToBookRatio(marketValueOfEquity,78202)

# total enterprise value (TEV)
def enterpriseValue(marketValueOfEquity, debt, cash):
    return marketValueOfEquity + debt - cash

#print enterpriseValue(87142, 46138, 7138)

# EPS
def earningsPerShare(netIncome, sharesOutstanding):
    return netIncome/sharesOutstanding

#print earningsPerShare(6967,50664)

def retainedEarnings(netIncome, dividends):
    return netIncome - dividends

#print retainedEarnings(7003,6947)

def changeInShareholdersEquity(retainedEarnings, netSalesOfShares):
    return retainedEarnings + netSalesOfShares

#print changeInShareholdersEquity()

def changeInShareholdersEquity(netIncome, dividends, salesOfShares, repurchasesOfShares):  
    return netIncome - dividends + salesOfShares - repurchasesOfShares

#print changeInShareholdersEquity(7003, 6947, )
# s. 34