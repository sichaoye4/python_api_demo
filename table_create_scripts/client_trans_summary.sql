CREATE TABLE client_trans_summary (
    client_id VARCHAR(255),
    month_id INT,
    operation VARCHAR(50),
    number_of_trans INT,
    total_trans_amount DECIMAL(18,2)
) AS SELECT client_id,
    month_id,
    operation,
    number_of_trans,
    total_trans_amount,
    FROM CSVREAD('C:\Users\sicha\GIT\Pyspark_demo\data\client_trans_summary.csv')
