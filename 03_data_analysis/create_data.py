import pandas as pd
import numpy as np
from datetime import datetime

# 固定随机种子，保证每次生成的数据一致
np.random.seed(42)

# 参数设置：生成1000行数据
num_rows = 1000
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# 1. 生成日期列（从2023年中随机选择）
date_range = pd.date_range(start_date, end_date)
dates = np.random.choice(date_range, num_rows)

# 2. 定义产品类别及其具体产品
categories_products = {
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Tablet', 'Smartwatch'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Shoes'],
    'Home': ['Cookware', 'Bedding', 'Furniture', 'Decor', 'Tools'],
    'Food': ['Snacks', 'Beverages', 'Dairy', 'Bakery', 'Fruits']
}

# 为每一行随机选择类别，再根据类别随机选择产品
product_category = np.random.choice(list(categories_products.keys()), num_rows)
product_name = [np.random.choice(categories_products[cat]) for cat in product_category]

# 3. 生成数量（1~5）
quantity = np.random.randint(1, 6, num_rows)

# 4. 生成单价（10~500元），保留两位小数
price = np.random.uniform(10, 500, num_rows).round(2)

# 5. 计算总金额
total_amount = (quantity * price).round(2)

# 6. 客户ID（1~200）
customer_id = np.random.randint(1, 201, num_rows)

# 7. 地区
region = np.random.choice(['North', 'South', 'East', 'West'], num_rows)

# 组装DataFrame
df = pd.DataFrame({
    'transaction_id': range(1, num_rows + 1),
    'date': dates,
    'product_category': product_category,
    'product_name': product_name,
    'quantity': quantity,
    'price': price,
    'total_amount': total_amount,
    'customer_id': customer_id,
    'region': region
})

# 保存为CSV文件（不包含行索引）
df.to_csv('data.csv', index=False)
print("已生成 data.csv，包含1000行销售记录。")