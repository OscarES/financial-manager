from __future__ import division # needed for 1/2 = 0.5

# EPS
def earningsPerShare(netIncome, sharesOutstanding):
    return netIncome/sharesOutstanding

print earningsPerShare(6967,50664)

def retainedEarnings(netIncome, dividends):
    return netIncome - dividends

#print retainedEarnings(7003,6947)
