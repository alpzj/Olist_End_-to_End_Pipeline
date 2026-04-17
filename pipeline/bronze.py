import dlt
from pyspark.sql.functions import *

# =========================
# CUSTOMERS
# =========================
@dlt.table(
    name="customers_bronze"
)
def customers():
    return spark.read.format("csv") \
        .option("header", True) \
        .option("inferSchema", True) \
        .load("/Volumes/e-commerce_databricks_project/default/e-commerce_datasets/olist_customers_dataset.csv")


# =========================
# ORDERS
# =========================
@dlt.table(
    name="orders_bronze"
)
def orders():
    return spark.read.format("csv") \
        .option("header", True) \
        .option("inferSchema", True) \
        .load("/Volumes/e-commerce_databricks_project/default/e-commerce_datasets/olist_orders_dataset.csv")


# =========================
# ORDER ITEMS
# =========================
@dlt.table(
    name="order_items_bronze"
)
def order_items():
    return spark.read.format("csv") \
        .option("header", True) \
        .option("inferSchema", True) \
        .load("/Volumes/e-commerce_databricks_project/default/e-commerce_datasets/olist_order_items_dataset.csv")


# =========================
# PAYMENTS
# =========================
@dlt.table(
    name="payments_bronze"
)
def payments():
    return spark.read.format("csv") \
        .option("header", True) \
        .option("inferSchema", True) \
        .load("/Volumes/e-commerce_databricks_project/default/e-commerce_datasets/olist_order_payments_dataset.csv")


# =========================
# PRODUCTS
# =========================
@dlt.table(
    name="products_bronze"
)
def products():
    return spark.read.format("csv") \
        .option("header", True) \
        .option("inferSchema", True) \
        .load("/Volumes/e-commerce_databricks_project/default/e-commerce_datasets/olist_products_dataset.csv")