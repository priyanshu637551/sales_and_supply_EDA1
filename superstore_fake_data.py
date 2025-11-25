#Eda project

import numpy as np
import pandas as pd
from faker import Faker
import random as rd

fk = Faker()  # fk means Fake
#ct means  categories
ct = { 
    "Furniture": ['Chair','Table','Sofa','Bed','Cupboard','Dining table'],
    'Office Supplies': ['Pen','Notebook','Stapler','File Folder','Calculator','Stamp'],
    'Electronics': ['Laptop','Mouse','Keyboard','Headphones','Kettle','Charger','Monitor'],
    'Grocery': ['Maggi','Chips','Cold drinks','Juice packs','Chocolate','Protein']
}

regions = ['North','East','South','West']
payment_modes = ['UPI','Cash','Credit card','Pay check']
delivery_status = ['Delivered','Pending','Returned','Cancelled']
customer_segment_list = ['Consumer','Corporate','Home office']

records = []

for i in range(1000):
    order_id = f'ORD{1000+i}'
    order_date = fk.date_between(start_date='-2y', end_date='today')
    ship_date = order_date + pd.Timedelta(days=rd.randint(1,7))

    customer_name = fk.name()
    customer_id = f'CUST{rd.randint(100,999)}'
    customer_segment = rd.choice(customer_segment_list)

    category = rd.choice(list(ct.keys()))
    product_name = rd.choice(ct[category])
    product_id = f'PROD{rd.randint(1000,9999)}'

    region = rd.choice(regions)
    state = fk.state()
    city = fk.city()

    quantity = rd.randint(1,10)
    unit_price = rd.randint(100,5000)
    discount = rd.choice([0,5,10,15,20])

    sales_amount = quantity * unit_price * (1 - discount/100)
    cost_price = sales_amount * rd.uniform(0.6,0.9)
    profit = sales_amount - cost_price

    stock_left = rd.randint(0,50)

    if stock_left < 10:
        auto_reorder = 'Yes'
        reorder_quantity = rd.randint(20,50)
    else:
        auto_reorder = 'No'
        reorder_quantity = 0

    supplier_name = fk.company()
    supplier_email = fk.company_email()
    payment_mode = rd.choice(payment_modes)
    delivery = rd.choice(delivery_status)

    records.append({
        'Order ID': order_id,
        'Order Date': order_date,
        'Ship Date': ship_date,
        'Customer ID': customer_id,
        'Customer Name': customer_name,
        'Customer Segment': customer_segment,
        'Product ID': product_id,
        'Product Name': product_name,
        'Category': category,
        'Region': region,
        'State': state,
        'City': city,
        'Quantity': quantity,
        'Unit Price': unit_price,
        'Discount %': discount,
        'Sales Amount': round(sales_amount, 2),
        'Cost Price': round(cost_price, 2),
        'Profit': round(profit, 2),
        'Payment Mode': payment_mode,
        'Delivery Status': delivery,
        'Supplier Name': supplier_name,
        'Supplier Email': supplier_email,
        'Stock Left': stock_left,
        'Auto Reorder': auto_reorder,
        'Reorder Quantity': reorder_quantity
    })

df = pd.DataFrame(records)
 #  careting csv file
df.to_csv("Superstore_management_system.csv", index=False)
print("CSV generated successfully")
