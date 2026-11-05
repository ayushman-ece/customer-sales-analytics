
import pandas as pd

from analyzer import (
    load_sales_data,
    calculate_sales_metrics,
    analyze_products_and_customers,
    analyze_monthly_revenue,
    plot_monthly_revenue,
    export_reports
)


def main():

    print("\n====================================")
    print(" CUSTOMER SALES ANALYTICS SYSTEM")
    print("====================================")

    # Step 1: Load and validate dataset
    try:
        df = load_sales_data("sample_sales.csv")

    except FileNotFoundError:
        print("Error: sample_sales.csv was not found.")
        return

    except (ValueError, pd.errors.ParserError) as error:
        print(f"Dataset Error: {error}")
        return

    # Step 2: Calculate overall sales metrics
    calculate_sales_metrics(df)

    # Step 3: Analyze products and customers
    product_data, customer_data = analyze_products_and_customers(df)

    # Step 4: Analyze monthly revenue
    monthly_data = analyze_monthly_revenue(df)

    # Step 5: Generate monthly revenue chart
    plot_monthly_revenue(monthly_data)

    # Step 6: Export analytical reports
    export_reports(
        df,
        product_data,
        customer_data,
        monthly_data
    )

    print("\n====================================")
    print(" ANALYSIS COMPLETED SUCCESSFULLY")
    print("====================================")


if __name__ == "__main__":
    main()
