CREATE TABLE client_loan_summary (
    client_id VARCHAR(255),
    month_id INT,
    number_of_loans INT,
    total_loan_amount DECIMAL(18,2)
) AS SELECT client_id,
    month_id,
    number_of_loans,
    total_loan_amount,
    FROM CSVREAD('C:\Users\sicha\GIT\Pyspark_demo\data\client_loan_summary.csv')
