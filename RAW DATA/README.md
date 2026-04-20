# E-Commerce Raw Datasets (Bronze Layer)

## Overview
This repository contains the raw source datasets used for building the E-Commerce Data Pipeline. These datasets represent the **Bronze layer** in the Medallion Architecture and are ingested without any transformations.

The data is sourced from the Brazilian Olist E-Commerce dataset and is used for downstream processing in Silver and Gold layers.

---

## Dataset Description

The raw data consists of multiple related tables representing different aspects of an e-commerce platform:

### 1. Customers Dataset
**File:** `olist_customers_dataset.csv`

Contains customer-related information.

**Key Columns:**
- `customer_id` – Unique customer identifier  
- `customer_unique_id` – Unique identifier per customer  
- `customer_city` – Customer city  
- `customer_state` – Customer state  

---

### 2. Orders Dataset
**File:** `olist_orders_dataset.csv`

Contains order-level information.

**Key Columns:**
- `order_id` – Unique order identifier  
- `customer_id` – Customer reference  
- `order_status` – Status of the order  
- `order_purchase_timestamp` – Purchase date  
- `order_approved_at` – Approval timestamp  
- `order_delivered_customer_date` – Delivery date  
- `order_estimated_delivery_date` – Estimated delivery date  

---

### 3. Order Items Dataset
**File:** `olist_order_items_dataset.csv`

Contains details of items within each order.

**Key Columns:**
- `order_id` – Order reference  
- `order_item_id` – Item sequence number  
- `product_id` – Product reference  
- `seller_id` – Seller identifier  
- `price` – Item price  
- `freight_value` – Shipping cost  

---

### 4. Payments Dataset
**File:** `olist_order_payments_dataset.csv`

Contains payment transaction details.

**Key Columns:**
- `order_id` – Order reference  
- `payment_type` – Payment method  
- `payment_installments` – Number of installments  
- `payment_value` – Payment amount  

---

### 5. Products Dataset
**File:** `olist_products_dataset.csv`

Contains product-level information.

**Key Columns:**
- `product_id` – Unique product identifier  
- `product_category_name` – Product category  
- `product_name_length` – Length of product name  
- `product_description_length` – Description length  
- `product_photos_qty` – Number of product images  

---

## Data Characteristics

- Structured CSV format  
- Contains missing and inconsistent values  
- Requires cleaning and transformation in the Silver layer  
- Multiple tables connected via foreign keys (e.g., `customer_id`, `order_id`, `product_id`)  

---

## Usage

These datasets are used for:

- Data ingestion into Bronze layer  
- Data cleaning and transformation in Silver layer  
- Analytical processing in Gold layer  

---

## Notes

- No preprocessing is applied at this stage  
- Data is ingested as-is to maintain source integrity  
- All transformations are handled in downstream layers  
