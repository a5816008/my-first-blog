.mode column
.width 30 20 10
.headers ON

SELECT publisher,  AVG(price) AS "AVG(price)", SUM(price) AS "SUM(price)"
from book
GROUP BY publisher;
