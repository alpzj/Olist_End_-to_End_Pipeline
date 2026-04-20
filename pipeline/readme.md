# E-Commerce Data Pipeline using Delta Live Tables (DLT)

## Overview
This project implements a production-grade data engineering pipeline using Databricks Delta Live Tables (DLT) and the Medallion Architecture (Bronze, Silver, Gold).

The pipeline ingests raw e-commerce data, performs data cleaning and transformations, and produces analytics-ready datasets for business insights and reporting.

---

## Architecture

Raw Data (CSV)
    ↓
Bronze Layer (Ingestion)
    ↓
Silver Layer (Cleaning & Transformation)
    ↓
Gold Layer (Aggregations & Insights)
    ↓
Analytics / BI

---

## Technology Stack

- Databricks  
- Delta Live Tables (DLT)  
- PySpark  
- Delta Lake  
- SQL  

---

## Data Sources

The pipeline processes the following datasets:

- Customers  
- Orders  
- Order Items  
- Payments  
- Products  

---

## Bronze Layer — Raw Data Ingestion

### Objective
Ingest raw data from source files into Delta tables without applying transformations.

### Key Features
- Schema inference enabled  
- Raw, unprocessed data  
- Acts as the source of truth  

### Tables
- customers_bronze  
- orders_bronze  
- order_items_bronze  
- payments_bronze  
- products_bronze  

---

## Silver Layer — Data Cleaning and Transformation

### Objective
Transform raw data into clean, structured, and reliable datasets.

### Key Transformations
- Removal of duplicate records  
- Handling of missing values  
- Data type casting  
- Filtering invalid records (e.g., payment_value > 0)  
- Joining multiple datasets  

### Final Table
- ecommerce_silver  

### Derived Columns
- order_year  
- order_month  
- total_price  

---

## Gold Layer — Business Insights

### Objective
Create aggregated datasets optimized for analytics and reporting.

### Customer Analytics
- top_customers  
- repeat_customers  
- customer_segments  

### Revenue Analysis
- monthly_revenue  
- top_cities  

### Product Insights
- top_products  
- category_performance  
- top_product_per_category  

### Operations
- delivery_performance  

### Payment Analysis
- payment_analysis  

---

## Pipeline Features

- End-to-end pipeline using Delta Live Tables  
- Scalable Medallion Architecture design  
- Data quality improvements in Silver layer  
- Analytical aggregations in Gold layer  
- Use of window functions for advanced analysis  

---

## Execution Steps

1. Upload datasets to Databricks  
2. Create a Delta Live Tables pipeline  
3. Add Bronze, Silver, and Gold scripts  
4. Run the pipeline  
5. Query Gold tables for analysis  

---

## Outcomes

- Clean and integrated analytical dataset  
- Customer segmentation based on spending  
- Monthly revenue trend analysis  
- Product and category performance insights  
- Delivery and payment analysis  

---

## Future Enhancements

- Real-time data processing using streaming  
- Integration with BI tools (Power BI, Tableau)  
- Data quality validation checks  
- CI/CD pipeline integration  
