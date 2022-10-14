
# Challenge One
years_of_service_time = int(input('Enter Your Years of Service Time: '))
salary = int(input('Enter your salary: '))

if years_of_service_time >= 5:
    print('your salary is', salary, 'and', 'you got bonus', 'now your net bonus amount is', (salary / 100) * 5 + salary)
else:
    print('your years of service time is not enough. Try next year')

# Challenge Two

product_purchase_quantity = int(input('Enter the number of product you buy: '))
per_product_cost = int(input('Enter average per product cost: '))
customer_total_cost = product_purchase_quantity * per_product_cost
discount = (customer_total_cost / 100 ) * 10
if customer_total_cost >1000:
    print('you got discount', discount, 'TK.', ' Now your total cost is', customer_total_cost - discount, 'TK.' )
else:
    print('If you want discount Please next time buy more product')

















