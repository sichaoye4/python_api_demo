CREATE TABLE loan_details (
    loan_id VARCHAR(255) PRIMARY KEY,
    client_id VARCHAR(255),
    account_id VARCHAR(255),
    date DATE,
    amount DECIMAL(10,2),
    duration INT,
    payments DECIMAL(10,2),
    due_date DATE,
    status VARCHAR(20),
    month_id INT) 
    AS SELECT loan_id, 
    client_id, 
    account_id, 
    date, 
    amount, 
    duration,
    payments,
    due_date,
    status,
    month_id
    FROM CSVREAD('C:\Users\sicha\GIT\Pyspark_demo\data\client_loan_details.csv')

