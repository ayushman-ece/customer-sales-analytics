import pandas as pd
import matplotlib.pyplot as plt

def load_sales_data(file_path):
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    df["revenue"] = df["quantity"] * df["price"]

    return df


def calculate_sales_metrics(df):
    total_revenue = df["revenue"].sum()

    total_orders = df["order_id"].nunique()

    total_quantity = df["quantity"].sum()

    average_order_value = total_revenue / total_orders

    print("\n========== SALES OVERVIEW ==========")

    print(f"Total Revenue: ₹{total_revenue:,.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Units Sold: {total_quantity}")
    print(f"Average Order Value: ₹{average_order_value:,.2f}")

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_quantity": total_quantity,
        "average_order_value": average_order_value
    }
    
def analyze_products_and_customers(df):

    # Product analysis
    product_analysis = df.groupby("product").agg(
        units_sold=("quantity", "sum"),
        total_revenue=("revenue", "sum")
    ).sort_values(by="total_revenue", ascending=False)

    print("\n========== PRODUCT PERFORMANCE ==========")
    print(product_analysis)

    # Customer analysis
    customer_analysis = df.groupby("customer").agg(
        total_orders=("order_id", "nunique"),
        total_spent=("revenue", "sum")
    ).sort_values(by="total_spent", ascending=False)

    print("\n========== TOP CUSTOMERS ==========")
    print(customer_analysis)

    return product_analysis, customer_analysis


def analyze_monthly_revenue(df):

    df["month"] = df["date"].dt.to_period("M")

    monthly_revenue = df.groupby("month").agg(
        total_revenue=("revenue", "sum"),
        total_orders=("order_id", "nunique")
    ).sort_index()

    print("\n========== MONTHLY REVENUE ==========")
    print(monthly_revenue)

    return monthly_revenue

def plot_monthly_revenue(monthly_revenue):

    months = monthly_revenue.index.astype(str)
    revenue = monthly_revenue["total_revenue"]

    plt.figure(figsize=(9, 5))

    plt.bar(months, revenue)

    plt.title("Monthly Revenue Analysis")
    plt.xlabel("Month")
    plt.ylabel("Revenue (₹)")

    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()

    plt.savefig("monthly_revenue.png")
    plt.show()
    
def export_reports(df, product_analysis, customer_analysis, monthly_revenue):

    df.to_csv("sales_report.csv", index=False)
    product_analysis.to_csv("product_report.csv")
    customer_analysis.to_csv("customer_report.csv")
    monthly_revenue.to_csv("monthly_report.csv")

    print("\n========== REPORTS EXPORTED ==========")
    print("1. sales_report.csv")
    print("2. product_report.csv")
    print("3. customer_report.csv")
    print("4. monthly_report.csv")
    

def load_sales_data(file_path):

    required_columns = [
        "order_id", "customer", "product",
        "category", "quantity", "price", "date"
    ]

    df = pd.read_csv(file_path)

    # Check required columns
    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    # Check missing values
    if df[required_columns].isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    # Convert data types
    df["date"] = pd.to_datetime(df["date"], errors="raise")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="raise")
    df["price"] = pd.to_numeric(df["price"], errors="raise")

    # Validate numeric values
    if (df["quantity"] <= 0).any() or (df["price"] < 0).any():
        raise ValueError("Quantity must be positive and price cannot be negative.")

    # Calculate revenue
    df["revenue"] = df["quantity"] * df["price"]

    return df

    
    