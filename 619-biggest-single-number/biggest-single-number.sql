# Write your MySQL query statement below
SELECT
    MAX(num) As num

FROM
(

    SELECT
        NUM
    
    FROM MyNumbers

    GROUP BY num

    HAVING COUNT(*)=1

)As SingleNumbers;