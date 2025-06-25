-- 0. create a database
CREATE DATABASE credit_card_db;

-- 1. TABLE CREATION
-- 1.1 create credit_card_details table
CREATE TABLE credit_card_details (
	Client_Num INT,
    Card_Category VARCHAR(20),
    Annual_Fees INT,
    Activation_30_Days INT,
    Customer_Acq_Cost INT,
    Week_Start_Date DATE,
    Week_Num VARCHAR(20),
    Qtr VARCHAR(10),
    current_year INT,
    Credit_Limit DECIMAL(10,2),
    Total_Revolving_Bal INT,
    Total_Trans_Amt INT,
    Total_Trans_Ct INT,
    Avg_Utilization_Ratio DECIMAL(10,3),
    Use_Chip VARCHAR(10),
    Exp_Type VARCHAR(50),
    Interest_Earned DECIMAL(10,3),
    Delinquent_Acc VARCHAR(5)
);

-- 1.2 create customer_details
CREATE TABLE customer_details (
    Client_Num INT,
    Customer_Age INT,
    Gender VARCHAR(5),
    Dependent_Count INT,
    Education_Level VARCHAR(50),
    Marital_Status VARCHAR(20),
    State_cd VARCHAR(50),
    Zipcode VARCHAR(20),
    Car_Owner VARCHAR(5),
    House_Owner VARCHAR(5),
    Personal_Loan VARCHAR(5),
    Contact VARCHAR(50),
    Customer_Job VARCHAR(50),
    Income INT,
    Cust_Satisfaction_Score INT
);

-- 2. COPY CSV DATA INTO SQL
-- 2.1 copy credit_card_details table
-- By default, PostgreSQL expects dates in the format YYYY-MM-DD, but your file uses DD-MM-YYYY
-- You can change the DateStyle so PostgreSQL parses the date format in your CSV file.
SET datestyle = 'DMY';

COPY credit_card_details
FROM 'C:\Credit_Card_Financial_Dashboard\credit_card.csv'
DELIMITER ','
CSV HEADER

-- 2.2 copy customer details table
COPY customer_details
FROM 'C:\Credit_Card_Financial_Dashboard\customer.csv'
DELIMITER ','
CSV HEADER


