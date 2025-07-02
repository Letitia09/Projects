# 📊 Blinkit Sales Performance & Inventory Analysis Dashboard

## 🔍 Project Objective

To analyze **Blinkit’s sales performance, customer satisfaction, and inventory distribution** using interactive Power BI dashboards, enabling data-driven decisions and business optimization across outlets, item types, and customer ratings.

---

## 📝 Business Requirement

Conduct a comprehensive analysis of:

* Total revenue generation (Sales)
* Item-wise and category-wise performance
* Impact of outlet type, location, size, and establishment year
* Customer satisfaction through ratings
* Inventory visibility and distribution

### Key KPIs:

* **Total Sales**
* **Average Sales**
* **Number of Items**
* **Average Rating**

---

## 🗂️ Dataset Description

| Column Name                 | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| `Item Fat Content`          | Indicates whether the item is Low Fat or Regular                |
| `Item Identifier`           | Unique identifier for each item                                 |
| `Item Type`                 | Category of the item (e.g., Fruits, Snacks, Frozen Foods)       |
| `Outlet Establishment Year` | Year in which the outlet was established                        |
| `Outlet Identifier`         | Unique ID for each store outlet                                 |
| `Outlet Location Type`      | Location classification of the outlet (Tier 1, Tier 2, Tier 3)  |
| `Outlet Size`               | Size category of the outlet (Small, Medium, High)               |
| `Outlet Type`               | Store type (e.g., Supermarket Type1/2/3, Grocery Store)         |
| `Item Visibility`           | Numerical representation of how visible an item is to customers |
| `Item Weight`               | Weight of the item in kilograms                                 |
| `Sales`                     | Total sales revenue from the item                               |
| `Rating`                    | Customer rating (1 to 5)                                        |

---

## ⚙️ Workflow / Process Steps

1. **Requirement Gathering**
2. **Data Walkthrough**
3. **Data Connection**
4. **Data Cleaning / Quality Check**
5. **Data Modeling**
6. **Data Processing**
7. **DAX Calculations**
8. **Dashboard Lay outing**
9. **Charts Development and Formatting**
10. **Dashboard / Report Development**
11. **Insights Generation**

---

## 📊 Visualization Components

| Chart Title                              | Type            | Insight Provided                                                   |
| ---------------------------------------- | --------------- | ------------------------------------------------------------------ |
| Total Sales by Fat Content               | Donut Chart     | Impact of Low Fat vs Regular items                                 |
| Total Sales by Item Type                 | Bar Chart       | Item category sales performance                                    |
| Fat Content by Outlet                    | Stacked Column  | Segment-wise comparison of Fat content across outlet tiers         |
| Total Sales by Outlet Establishment Year | Line Chart      | Sales performance trend over time                                  |
| Sales by Outlet Size                     | Donut/Pie Chart | Contribution of outlet sizes (Small, Medium, High)                 |
| Sales by Outlet Location Type            | Funnel Chart    | Sales breakdown by Tier 1, 2, 3 locations                          |
| Metrics by Outlet Type                   | Matrix Table    | View of sales, ratings, items sold, and visibility per outlet type |

---

## 💻 Technologies Used

* **Power BI** – Dashboard creation, modeling, DAX
* **DAX (Data Analysis Expressions)** – KPI and calculated measure development
* **Excel** – Initial data review and preprocessing
* **Vertabelo (optional)** – Schema modeling and design

---

## 📈 Key Findings

### 🥛 Fat Content Insights

* Regular fat items generate \~82% more total sales than low-fat items.
* Low-fat items are more diverse (6,000 items) compared to regular (3,000).
* Both fat categories have nearly identical average sales (\~\$141–\$142).
* Customer satisfaction is consistent across both fat types (Avg Rating: 4.0).

### 🍎 Item Type Performance

* Top-selling categories: Fruits & Vegetables and Snacks (\$0.18M each).
* Household items have the highest average sale value (\$149).
* Seafood and Baking Goods underperform in both total sales and average sales.
* All item types maintain strong customer satisfaction (Avg Rating: 4.0).

### 🏪 Outlet Size Insights

* Medium-sized outlets have the highest total sales (\$507.90K).
* Small and high-sized outlets tie for the highest average sales (\$142).
* Medium outlets stock the most items (4,000+), followed by small and high.
* Ratings remain stable across all outlet sizes.

### 📍 Outlet Location Insights

* Tier 3 locations lead in total sales (\$472.13K), followed by Tier 2 and Tier 1.
* Tier 1 lags behind in both sales and item count.
* Geographic focus on Tier 3 outlets may yield better revenue results.

### 🏗️ Outlet Establishment Year Trends

* Sales peaked in 2018 (\~\$205K), followed by a decline.
* Post-2020, sales have stabilized around \~\$131K.
* Outlets established before 2016 tend to generate more consistent revenue.

### 🧾 Outlet Type Breakdown

* Supermarket Type1 leads all others with \$787.55K in total sales and 5,577 items.
* Grocery Stores have the highest item visibility score (0.10).
* All outlet types report identical customer ratings (4.0).
* Supermarket Type2 has the highest average sale per item (\$142).

---

## ✅ Business Recommendations

* **Expand low-fat product offerings** due to higher sales and diversity.
* **Focus on Tier 3 and medium-sized outlets** for better performance.
* **Boost inventory and visibility** for underperforming items like seafood.
* **Analyze 2018 sales spike** for repeatable success patterns.
* **Improve item visibility** in lower-performing outlet types using strategies from Grocery Stores.

---
