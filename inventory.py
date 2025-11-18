initial_stock = 125
sold_today = 37
price_per_unit = 2.50
remaing_stocks_after_today_sales= initial_stock -sold_today
revenue_today= sold_today*price_per_unit
percentage_stock_sold= (sold_today/initial_stock)*100

print("remaing stocks after today sales:", remaing_stocks_after_today_sales)
print("revenue today:",revenue_today)
print("pertcentage_stock_sold",percentage_stock_sold)
 
print(type(price_per_unit))
print(type(sold_today))
print(type(revenue_today))
print(type(initial_stock))
print(type(remaing_stocks_after_today_sales))

"""F STRINGS"""
#This was done using the "f strings {}" allows anything inside to be replaced by the value it contanains 
# ex. if i say  print print(f"what number is this {age}")
# and i have a value age = 28 then the output is gonna be 
# what number is this 28

print(f"intial stock:{type(initial_stock)}")
print(f"sold today:{type(sold_today)}")
print(f"remaining stock:{type(remaing_stocks_after_today_sales)}")
print(f"revenue today:{type(revenue_today)}")
print(f"percentage stock sold:{type(percentage_stock_sold)}")

"""F STRINGS FOR FORMAT"""
## here we are using the f string to format in this case an int value to a floating one with one or more decimals
## the number of decimals is given by:.1 

print(f"revenue today: {revenue_today:.2f}")
print(f"percentage stock sold: {percentage_stock_sold:.1f}%")