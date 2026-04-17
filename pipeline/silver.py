import dlt
from pyspark.sql.functions import *

# =========================
# CUSTOMERS CLEAN
# =========================
@dlt.table(name="customers_silver")
def customers_clean():
    df = dlt.read("customers_bronze")
    return df.dropDuplicates()


# =========================
# ORDERS CLEAN
# =========================
@dlt.table(name="orders_silver")
def orders_clean():
    df = dlt.read("orders_bronze")

    return df.withColumn("order_approved_at", col("order_approved_at").cast("timestamp")) \
             .fillna({"order_approved_at": "1970-01-01 00:00:00"}) \
             .dropDuplicates()


# # =========================
# # PAYMENTS CLEAN
# # =========================
@dlt.table(name="payments_silver")
def payments_clean():
    df = dlt.read("payments_bronze")
    return df.filter(col("payment_value") > 0).dropDuplicates()


# # =========================
# # PRODUCTS CLEAN
# # =========================
@dlt.table(name="products_silver")
def products_clean():
    df = dlt.read("products_bronze")

    return df.fillna({
        "product_category_name": "unknown",
        "product_name_lenght": 0,
        "product_description_lenght": 0,
        "product_photos_qty": 0
    }).dropDuplicates()


# # =========================
# # ORDER ITEMS CLEAN
# # =========================
@dlt.table(name="order_items_silver")
def order_items_clean():
    df = dlt.read("order_items_bronze")
    return df.dropDuplicates()


# # =========================
# # FINAL SILVER JOIN
# # =========================
@dlt.table(name="ecommerce_silver")
def ecommerce_silver():

    orders = dlt.read("orders_silver")
    customers = dlt.read("customers_silver")
    items = dlt.read("order_items_silver")
    products = dlt.read("products_silver")
    payments = dlt.read("payments_silver")

    df = orders.alias("o") \
        .join(customers.alias("c"), "customer_id", "left") \
        .join(items.alias("oi"), "order_id", "left") \
        .join(products.alias("p"), "product_id", "left") \
        .join(payments.alias("pay"), "order_id", "left")

    return df.withColumn("order_year", year("order_purchase_timestamp")) \
             .withColumn("order_month", month("order_purchase_timestamp")) \
             .withColumn("total_price", col("price") + col("freight_value"))
