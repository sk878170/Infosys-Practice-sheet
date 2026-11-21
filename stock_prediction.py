# Given an array prices[] of non-negative integers, representing the prices of the stocks on different days, return the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

# Note: Stock must be bought before being sold.

prices = [7, 10, 1, 3, 6, 9, 2]
mini=prices[0]
profit=0
for i in range(1,len(prices)):
  mini=min(mini,prices[i])
  profit=max(profit,prices[i]-mini)
  print(mini,profit)

print(profit)
  
  
  
