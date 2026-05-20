import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Show first rows
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Shape
print("\nROWS AND COLUMNS")
print(df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create Total Sales column
df['Total_Sales'] = df['Quantity'] * df['Price']

# Metrics
total_revenue = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()

best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Results
print("\nANALYSIS RESULTS")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Average Sales: ₹{average_sales}")
print(f"Best Product: {best_product}")