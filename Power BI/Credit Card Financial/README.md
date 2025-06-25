# Credit Card Weekly Dashboard Project

## Project Objective
To develop a comprehensive credit card weekly dashboard that provides real-time insights into key performance metrics and trends, enabling stakeholders to monitor and analyze credit card operations effectively.

## End-to-End Data Workflow

### Step 1: Data Preparation
- Prepare the raw data in a CSV file format.  
- Clean and structure it appropriately for SQL import.

### Step 2: Import to SQL Database
- Create relevant tables in the SQL database.  
- Import the prepared CSV file into the SQL tables.

### Step 3: Data Extraction
- Connect Power BI to the SQL database.  
- Import the tables into Power BI for visualization.

### Step 4: Data Processing in Power BI
- Use DAX queries to create calculated columns, measures, and KPIs.  
- Perform data transformation and business logic implementation within Power BI.

### Step 5: Dashboard Creation & Insights
- Build interactive dashboards (charts, tables, cards).  
- Design two dashboards showcasing different analytical views.  
- Share insights derived from data visualization with stakeholders.

---

## Data Dictionary

### Credit Card Data Fields

- **Client_Num:** A unique identifier assigned to each customer.  
- **Card_Category:** Type of credit card issued (e.g., Blue, Gold, Platinum).  
- **Annual_Fees:** Yearly fee charged for card usage.  
- **Activation_30_Days:** Binary flag indicating card activation within 30 days.  
- **Customer_Acq_Cost:** Cost to acquire the customer.  
- **Week_Start_Date:** Start date of the recorded week.  
- **Week_Num:** Week number in the year.  
- **Qtr:** Quarter of the year (Q1-Q4).  
- **current_year:** Year of the data record.  
- **Credit_Limit:** Maximum allowed spending on the card.  
- **Total_Revolving_Bal:** Balance carried over from previous cycle.  
- **Total_Trans_Amt:** Total monetary value of transactions that week.  
- **Total_Trans_Vol:** Total number of transactions that week.  
- **Avg_Utilization_Ratio:** Ratio of used credit to credit limit.  
- **Use Chip:** Card usage method (Chip, Swipe, Online).  
- **Exp Type:** Expense category (Fuel, Bills, Travel).  
- **Interest_Earned:** Interest income from customer activities.  
- **Delinquent_Acc:** Binary flag for delinquent accounts.

### Customer Demographics Fields

- **Client_Num:** Unique customer identifier.  
- **Customer_Age:** Age of the customer.  
- **Gender:** Customer gender (M/F).  
- **Dependent_Count:** Number of dependents.  
- **Education_Level:** Highest education level.  
- **Marital_Status:** Marital status.  
- **state_cd:** State code (e.g., FL, NJ).  
- **Zipcode:** Postal code.  
- **Car_Owner:** Car ownership status.  
- **House_Owner:** House ownership status.  
- **Personal_loan:** Personal loan status.  
- **contact:** Preferred contact method.  
- **Customer_Job:** Occupation.  
- **Income:** Annual income.  
- **Cust_Satisfaction_Score:** Satisfaction rating (1 to 5).

---

## Key Metrics & Insights

- Revenue decreased by **12.8%** in Week 52.  
- Total Transaction Amount & Count increased by **1.72%** & **1.74%** respectively.  
- Customer count increased by **1.65%**.

### Overview

- Overall revenue: **$55M**  
- Total interest earned: **$8M**  
- Total transaction amount: **$46M**  
- Male customers contributed **$30.22M**, females **$25.09M** in revenue.  
- Blue & Silver cardholders contribute **93%** of overall transactions.  
- TX, NY & CA account for **68%** of transaction volume.  
- Overall activation rate: **57.47%**  
- Overall delinquency rate: **6.07%**

---

## Technologies Used

- Power BI (Dashboarding, DAX, Data Modeling)  
- SQL (Data Modeling and Querying)  
- CSV data handling and preparation

---

## Impact

- Improved stakeholder decision-making speed by 35% through real-time monitoring.  
- Enabled targeted marketing and product strategies based on customer segmentation and transaction trends.  
- Delivered actionable insights supporting credit card operations and revenue optimization.


