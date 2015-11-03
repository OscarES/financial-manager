from __future__ import division # needed for 1/2 = 0.5
import math

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

def grossMargin(grossProfit, sales):
    return grossProfit/sales

#print grossMargin(14871, 46417)

def operatingMargin(operatingIncome, sales):
    return operatingIncome/sales

#print operatingMargin(11187, 46417)

# Earnings Before Intrest and Taxes (EBIT)
def EBIT_Margin(EBIT, sales):
    return EBIT/sales

def netProfitMargin(netIncome, sales):
    return netIncome/sales

#print netProfitMargin(7003, 46417)

def currentRatio(currentAssets, currentLiabilities):
    return currentAssets/currentLiabilities

#print currentRatio(17003, 27075)

def quickRatio(cash, accountsReceivable, currentLiabilities):
    return (cash + accountsReceivable)/currentLiabilities

#print quickRatio(6252, 9259, 27075)
#print quickRatio(7138, 10744, 24025)

def cashRatio(cash, currentLiabilities):
    return cash/currentLiabilities

#print cashRatio(6252, 27075)
#print cashRatio(7138, 24025)

# rounds up days
# from a year ago to now
def accountsReceivableDays(accountsReceivable, averageDailySales):
    return math.ceil(accountsReceivable/averageDailySales)

#print accountsReceivableDays(10744, 46417/365)

# from a year ago to now
def accountsPayableDays(accountsPayable, averageDailyCostOfSales):
    return math.ceil(accountsPayable/averageDailyCostOfSales)

# from a year ago to now
def inventoryDays(inventory, averageDailyCostOfSales):
    return math.ceil(inventory/averageDailyCostOfSales)

## Turnover ratios

def inventoryTurnover(annualCostOfSales, inventory):
    return annualCostOfSales/inventory

#print inventoryTurnover(31546, 486)

def accountsReceivableTurnover(annualSales, accountsReceivable):
    return annualSales/accountsReceivable

def accountsPayableTurnover(annualCostOfSales, accountsPayable):
    return annualCostOfSales/accountsPayable

## intrest coverage ratios

def EBIT_ToIntrestRatio(EBIT, intrest):
    return EBIT/intrest

#print EBIT_ToIntrestRatio(9927, 429)
#print EBIT_ToIntrestRatio(11481, 1932)

# Earnings Before Intrest, Taxes, Depreciation, and Amortization (EBITDA)
def EBITDA(EBIT, depreciationAndAmortization):
    return EBIT + depreciationAndAmortization

def EBITBA_ToIntrestRatio(EBITDA, intrest):
    return EBITDA/intrest

#print EBITBA_ToIntrestRatio(EBITDA(9927, 6150), 429)
#print EBITBA_ToIntrestRatio(EBITDA(11481, 4050), 1932)

## leverage (gearing)

def totalDebt(shortTermFinancialDebt, longTermBorrowing):
    return shortTermFinancialDebt + longTermBorrowing

def debtEquityRatio(totalDebt, totalEquity):
    return totalDebt/totalEquity

#print debtEquityRatio(totalDebt(8789, 37349), 78202)

def debtToCapitalRatio(totalDebt, totalEquity):
    return totalDebt/(totalEquity + totalDebt)

def netDebt(totalDebt, excessCashAndShortTermInvestments):
    return totalDebt - excessCashAndShortTermInvestments

def debtToEnterpriseValueRatio(netDebt, marketValueOfEquity):
    return netDebt/(marketValueOfEquity + netDebt)

#print debtToEnterpriseValueRatio(39000, 87142)

## enterpriseValue = marketValueOfEquity + netDebt
#def debtToEnterpriseValueRatio(netDebt, enterpriseValue):
#    return netDebt/enterpriseValue
#
#print debtToEnterpriseValueRatio(39000, 126142)

def equityMultiplier(totalAssets, bookValueOfEquity):
    return totalAssets/bookValueOfEquity

def marketValueEquityMultiplier(enterpriseValue, marketValueOfEquity):
    return enterpriseValue/marketValueOfEquity

## valuation raitios

## price-earnings ratio (P/E)

def marketToBookRatio(marketValueOfEquity, bookValueOfEquity):
    return marketValueOfEquity/bookValueOfEquity

#def priceEarningsRatio(marketCapitalization, netIncome):
#    return marketCapitalization/netIncome
#
#print priceEarningsRatio(87142, 7003)

# price-earnings ratio (P/E)
def priceEarningsRatio(sharePrice, earningsPerShare):
    return sharePrice/earningsPerShare

#print priceEarningsRatio(1.72, 0.1374)

def enterpriseValueRatios(enterpriseValue, EBIT):
    return enterpriseValue/EBIT

#def enterpriseValueRatios(enterpriseValue, EBITDA):
#    return enterpriseValue/EBITDA

#def enterpriseValueRatios(enterpriseValue, sales):
#    return enterpriseValue/sales


## investment returns

def assetTurnover(sales, totalAssets):
    return sales/totalAssets

# return on equity (ROE)
def returnOnEquity(netIncome, bookValueOfEquity):
    return netIncome/bookValueOfEquity

#print returnOnEquity(7003, 78202)

# return on assets (ROA)
def returnOnAssets(netIncome, intrestExpense, bookValueOfAssets):
    return (netIncome + intrestExpense)/bookValueOfAssets

#print returnOnAssets(7870, 429, 151220)
#print returnOnAssets(7003, 1932, 139576)

# return on invested capital (ROIC)
# after-tax EBIT = net income = pretax income * (1 - tax rate)
# estimate (1 - tax rate) = net income / pretax income
# don't forget to deduct the cash in the denominator
def returnOnInvestedCapital(EBIT, taxRate, bookValueOfEquity, netDebt):
    return EBIT*(1-taxRate)/(bookValueOfEquity + netDebt)

## the DuPont identity

# (net profit margin)*(asset turnover)*(equity multiplier)
def duPontROE(netIncome, sales, totalAssets, bookValueOfEquity):
    return (netIncome/sales)*(sales/totalAssets)*(totalAssets/bookValueOfEquity)

# s. 59