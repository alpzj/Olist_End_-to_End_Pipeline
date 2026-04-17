import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# =========================
# BASE SILVER TABLE
# =========================
def silver_df():
    return dlt.read("ecommerce_silver")

# =========================
# TOP CUSTOMERS
# =========================
@dlt.table(name="top_customers")
def top_customers():
    df = silver_df()
    return df.groupBy("customer_id") \
        .agg(sum("payment_value").alias("total_spent")) \
        .orderBy(col("total_spent").desc())

# =========================
# MONTHLY REVENUE
# =========================
@dlt.table(name="monthly_revenue")
def monthly_revenue():
    df = silver_df()
    return df.groupBy("order_year", "order_month") \
        .agg(sum("payment_value").alias("revenue"))

# =========================
# TOP PRODUCTS
# =========================
@dlt.table(name="top_products")
def top_products():
    df = silver_df()
    return df.groupBy("product_id", "product_category_name") \
        .agg(count("order_item_id").alias("total_orders")) \
        .orderBy(col("total_orders").desc())

# =========================
# REPEAT CUSTOMERS
# =========================
@dlt.table(name="repeat_customers")
def repeat_customers():
    df = silver_df()
    return df.groupBy("customer_id") \
        .agg(count("order_id").alias("order_count")) \
        .filter(col("order_count") > 1)

# =========================
# CUSTOMER SEGMENTATION
# =========================
@dlt.table(name="customer_segments")
def customer_segments():
    df = silver_df()
    return df.groupBy("customer_id") \
        .agg(sum("payment_value").alias("total_spent")) \
        .withColumn("segment",
            when(col("total_spent") > 5000, "High Value")
            .when(col("total_spent") > 2000, "Medium Value")
            .otherwise("Low Value")
        )

# =========================
# DELIVERY PERFORMANCE
# =========================
@dlt.table(name="delivery_performance")
def delivery_performance():
    df = silver_df()
    return df.withColumn(
        "delivery_delay",
        datediff("order_delivered_customer_date",
                 "order_estimated_delivery_date")
    )

# =========================
# TOP CITIES BY REVENUE
# =========================
@dlt.table(name="top_cities")
def top_cities():
    df = silver_df()
    return df.groupBy("customer_city") \
        .agg(sum("payment_value").alias("total_revenue")) \
        .orderBy(col("total_revenue").desc())

# =========================
# PAYMENT ANALYSIS
# =========================
@dlt.table(name="payment_analysis")
def payment_analysis():
    df = silver_df()
    return df.groupBy("payment_type") \
        .agg(sum("payment_value").alias("total_amount"))

# =========================
# CATEGORY PERFORMANCE
# =========================
@dlt.table(name="category_performance")
def category_performance():
    df = silver_df()
    return df.groupBy("product_category_name") \
        .agg(
            sum("payment_value").alias("revenue"),
            count("order_item_id").alias("orders")
        ) \
        .orderBy(col("revenue").desc())

# =========================
# TOP PRODUCT PER CATEGORY (WINDOW FUNCTION)
# =========================
@dlt.table(name="top_product_per_category")
def top_product_per_category():
    df = silver_df()

    window_spec = Window.partitionBy("product_category_name") \
        .orderBy(col("price").desc())

    return df.withColumn("rank", row_number().over(window_spec)) \
        .filter(col("rank") == 1)