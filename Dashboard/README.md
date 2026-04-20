# E-Commerce Data Pipeline and Analytics Dashboard

## Overview
This project presents a complete end-to-end data engineering and analytics solution built using Databricks Delta Live Tables (DLT) and the Medallion Architecture (Bronze, Silver, Gold).

The pipeline processes raw e-commerce data into clean, structured datasets and delivers business insights through an interactive analytics dashboard.

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
Dashboard & Analytics

---

## Technology Stack

- Databricks  
- Delta Live Tables (DLT)  
- PySpark  
- Delta Lake  
- SQL  
- Databricks Dashboard  

---

## Data Sources

The pipeline uses multiple datasets:

- Customers  
- Orders  
- Order Items  
- Payments  
- Products  

---

## Bronze Layer — Raw Data Ingestion

### Objective
Ingest raw CSV data into Delta tables without transformations.

### Tables
- customers_bronze  
- orders_bronze  
- order_items_bronze  
- payments_bronze  
- products_bronze  

---

## Silver Layer — Data Cleaning and Transformation

### Objective
Clean, validate, and integrate data from multiple sources.

### Key Transformations
- Duplicate removal  
- Null handling  
- Data type casting  
- Filtering invalid records  
- Joining datasets  

### Final Table
- ecommerce_silver  

### Derived Columns
- order_year  
- order_month  
- total_price  

---

## Gold Layer — Business Insights

### Objective
Generate analytics-ready datasets for reporting.

### Key Tables

#### Customer Analytics
- top_customers  
- repeat_customers  
- customer_segments  

#### Revenue Analysis
- monthly_revenue  
- top_cities  

#### Product Insights
- top_products  
- category_performance  
- top_product_per_category  

#### Operations
- delivery_performance  

#### Payment Analysis
- payment_analysis  

---

## Dashboard

### Overview Dashboard

![Dashboard Page 1](./assets/dashboard_page1.png)

### Detailed Analytics Dashboard

![Dashboard Page 2](./assets/dashboard_page2.png)

---

## Dashboard Insights

- Total revenue, orders, and customer overview  
- Monthly revenue trends over time  
- Revenue distribution across cities  
- Payment method analysis  
- Order status distribution  
- Delivery performance insights  
- Top product categories and sales distribution  
- State-wise category performance  

---

## Project Structure

project/
│
├── bronze_layer.py  
├── silver_layer.py  
├── gold_layer.py  
├── datasets/  
├── assets/  
│   ├── dashboard_page1.png  
│   └── dashboard_page2.png  
└── README.md  

---

## Execution Steps

1. Upload datasets to Databricks  
2. Create a Delta Live Tables pipeline  
3. Add Bronze, Silver, and Gold scripts  
4. Run the pipeline  
5. Build dashboard using Gold tables  

---

## Outcomes

- End-to-end automated data pipeline  
- Clean and unified analytical dataset  
- Interactive dashboard for business insights  
- Customer segmentation and revenue analysis  
- Product and operational performance insights  

---

## Future Enhancements

- Real-time streaming pipeline  
- Integration with external BI tools  
- Advanced data quality checks  
- CI/CD pipeline integration  
