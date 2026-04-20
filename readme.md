# E-Commerce Data Engineering Pipeline using Delta Live Tables (DLT)

## Overview
This project implements an end-to-end data engineering pipeline using Databricks Delta Live Tables (DLT) following the Medallion Architecture (Bronze, Silver, Gold).

The pipeline ingests raw e-commerce datasets, performs data cleaning and transformations, and generates analytics-ready datasets. A dashboard is built on top of the Gold layer to provide business insights.

---

## Architecture

Raw Data (CSV)
    ↓
Bronze Layer (Raw Ingestion)
    ↓
Silver Layer (Data Cleaning & Integration)
    ↓
Gold Layer (Aggregations & Analytics)
    ↓
Dashboard / BI

---

## Technology Stack

- Databricks  
- Delta Live Tables (DLT)  
- PySpark  
- Delta Lake  
- SQL  
- Databricks SQL Dashboard  

---

## Data Sources

The project uses multiple datasets representing an e-commerce platform:

- Customers  
- Orders  
- Order Items  
- Payments  
- Products  

---

## Bronze Layer — Raw Data

### Description
- Ingests raw CSV files into Delta tables  
- No transformations applied  
- Maintains source data integrity  

### Tables
- customers_bronze  
- orders_bronze  
- order_items_bronze  
- payments_bronze  
- products_bronze  

---

## Silver Layer — Data Cleaning & Transformation

### Description
- Cleans and standardizes data  
- Removes duplicates  
- Handles missing values  
- Performs joins across datasets  

### Key Transformations
- Casting timestamps  
- Filtering invalid payments  
- Filling missing product data  
- Joining all tables into a unified dataset  

### Output Table
- ecommerce_silver  

### Derived Columns
- order_year  
- order_month  
- total_price  

---

## Gold Layer — Business Analytics

### Description
- Aggregated datasets for reporting and insights  

### Tables

#### Customer Insights
- top_customers  
- repeat_customers  
- customer_segments  

#### Revenue Analysis
- monthly_revenue  
- top_cities  

#### Product Analysis
- top_products  
- category_performance  
- top_product_per_category  

#### Operations
- delivery_performance  

#### Payment Analysis
- payment_analysis  

---

## Dashboard

The dashboard is built using Databricks SQL and provides interactive visualizations for business insights.

### Key Features
- Total revenue, orders, and customers overview  
- Monthly revenue trends  
- Revenue distribution by city  
- Order status analysis  
- Payment method analysis  
- Top product categories  
- Delivery performance insights  

---

## Execution Steps

1. Upload datasets to Databricks Volume  
2. Create a Delta Live Tables pipeline  
3. Add Bronze, Silver, and Gold scripts  
4. Run the pipeline  
5. Query Gold tables or connect to dashboard  

---

## Key Outcomes

- End-to-end data pipeline implementation  
- Clean and integrated analytical dataset  
- Customer segmentation based on spending  
- Revenue and product performance insights  
- Delivery and payment analysis  

---

## Future Enhancements

- Real-time data processing using streaming  
- Integration with BI tools (Power BI, Tableau)  
- Data validation and quality checks  
- CI/CD pipeline for automation  

---
