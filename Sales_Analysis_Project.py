import csv

def load_data(file_name):
    orders = []
    try:
        with open(file_name,'r',newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['Quantity']=int(row['Quantity'])
                    row['Unit_Price']=int(row['Unit_Price'])
                    if row['Quantity']<=0:
                        raise ValueError('Quantity must be greater than zero')
                    if row['Unit_Price']<=0:
                        raise ValueError('Unit_Price must be greater than zero')
                    row['sales_amount']=(row['Quantity']*row['Unit_Price'])
                    orders.append(row)
                except ValueError as e:
                    print('Invalid records:',row['Order_ID'],e)
    except FileNotFoundError:
        print('sales file not found.please check your path')

    return orders


def Total_revenue(Orders):
    total = 0
    for order in Orders:
        total+= order['sales_amount']
    return total
# print(Total_revenue(Data))
def Total_Orders(Orders):
    total = 0
    for order in Orders:
        total+= 1
    return total
# print(Total_Orders(Data))
def total_units(orders):
    total = 0
    for order in orders:
        total+=(order['Quantity'])
    return total
# print(total_units(Data))    
def average_sales(orders):
   if len(orders)==0:
       return 0
   return Total_revenue(orders)/Total_Orders(orders)
# print(average_sales(Data))
def highest_order(orders):
    highest = orders[0]
    for order in orders:
        if order['sales_amount']>highest['sales_amount']:
            highest = order 
    return highest
# print(highest_order(Data))
 
def lowest_order(orders):
    lowest = orders[0]
    for order in orders:
        if order['sales_amount']<lowest['sales_amount']:
            lowest = order 
    return lowest
# print(lowest_order(Data))
def unique_category(orders):
    unique = set()
    for order in orders:
        unique.add(order['Category'])
    return unique
# print(unique_category(Data))
def unique_cities(orders):
    unique = set()
    for order in orders:
        unique.add(order['City'])
    return unique
# print(unique_cities(Data))
def payment_summary(orders):
    payment_count = {}
    for order in orders:
        payment = order['Payment_Mode']
        if payment not in payment_count:
            payment_count[payment]=0
        payment_count[payment]+=1  
    return payment_count
# print(payment_summary(Data))
#        
'''Day 2'''
def category_summary(orders):
    category_sales = {}
    for order in orders:
        category = order['Category']
        amount = order['sales_amount']
        if category not in category_sales:
            category_sales[category]=0
        category_sales[category]+=amount
    return category_sales
# print(category_summary(Data)) 
def city_summary(orders):
    city_sales = {}
    for order in orders:
        cities = order['City']
        amount = order['sales_amount'] 
        if cities not in city_sales:
            city_sales[cities]=0
        city_sales[cities]+=amount
    return city_sales
# print(city_summary(Data))  
def product_revenue(orders):
    product_sales ={}
    for order in orders:
        product = order['Product']
        amount = order['sales_amount']
        if product not in product_sales:
            product_sales[product]=0
        product_sales[product]+=amount
    return product_sales
# print(product_revenue(Data))       
def top_product(orders):
    highest = orders[0]
    for order in orders:
        if order['Unit_Price']>highest['Unit_Price']:
            highest = order
    return highest['Product']
# print(top_product(Data))   
def customer_summary(orders):
    customer_sales = {}
    for order in orders:
        customer = order['Customer']
        amount = order['sales_amount'] 
        if customer not in customer_sales:
            customer_sales[customer]=0
        customer_sales[customer]+=amount
    return customer_sales
# print(customer_summary(Data))  
def customer_search(orders):
    name = input('Enter customer name: ')
    found = False
    for order in orders:
        if order['Customer'].lower()==name.lower():
            print(order['Order_ID'],order['Product'],order['sales_amount'])
            found = True
    if not found:
        print('coustomer not found')
# customer_search(Data)   
def city_search(orders):
    city = input('Enter the city: ')
    found = False
    ord = 0
    units = 0
    revenue = 0
    for order in orders:
        if order['City'].lower()==city.lower():
           ord+=1
           units+=order['Quantity']
           revenue+=order['sales_amount']
           found = True
    return f'orders={ord}\nunits = {units}\nrevenue={revenue}'
# print(city_search(Data))
def generate_report(orders):
    with open('sales_report.txt','w') as file:
        file.write('===== SALES REPORT =====\n\n')
        file.write(f'Total Orders = {Total_Orders(orders)}\n')
        file.write(f'Total Units = {total_units(orders)}\n')
        file.write(f'Total Revenue = Rs.{Total_revenue(orders)}\n')
        file.write(f'Average Order Value = Rs.{average_sales(orders)}\n\n')

        file.write('CATEGORY WISE REVENUE\n\n')
        for category, amount in category_summary(orders).items():
            file.write(f'{category} = Rs.{amount}\n')
        file.write('\nCITY WISE REVENUE\n\n')
        for city, amount in city_summary(orders).items():
            file.write(f'{city} = Rs.{amount}\n')
        file.write('\nPAYMENT MODE SUM\n\n')
        for payment, count in payment_summary(orders).items():
            file.write(f'{payment} = {count}\n')
    print('sales report generate succesfully')

def main():
    data = load_data(r'sales data- Python.csv')
    while True:
        print('\n========== SALES ANALYSIS SYSTEM ==========')
        print('1 Total Revenue')
        print('2 Total Units')
        print('3 Average Order Value')
        print('4 Highest Order')
        print('5 Lowest Order')
        print('6 Category Wise Revenue')
        print('7 City Wise Revenue')
        print('8 Customer Search')
        print('9 Payment Summary')
        print('10 Generate Report')
        print('11 Exit')

        choice = int(input('Enter your choicee: '))
        try:
            if choice==1:
                print('Total Revenue: ',Total_revenue(data))
            elif choice==2:
                print('Total Units: ',total_units(data))
            elif choice==3:
                print('Averagr Order Value: ',average_sales(data))
            elif choice==4:
                print('Highest Order: ',highest_order(data))
            elif choice==5:
                print('Lowest Order: ',lowest_order(data))
            elif choice==6:
                print('Category Wise Revenue: ',category_summary(data))
            elif choice==7:
                print('City Wise Revenue: ',city_summary(data))
            elif choice==8:
                customer_search(data)
            elif choice==9:
                print('payment Summary: ',payment_summary(data))
            elif choice==10:
                generate_report(data)
            elif choice==11:
                print('Program Completed')
                break
            else :
                raise ValueError('Invalid Input')
        except ValueError as e:
            print('Error: ',e)
    

main()
  