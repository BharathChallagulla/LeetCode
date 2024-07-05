# [SQL 50 from leetcode](https://leetcode.com/studyplan/top-sql-50/)

## Select

## 1757. Recyclable and Low Fat Products
```sql
SELECT product_id 
FROM Products 
WHERE low_fats='Y' and recyclable='Y';
```

## 584. Find Customer Referee
```sql
SELECT name 
FROM Customer 
WHERE referee_id!=2 or referee_id IS NULL;
```

## 595. Big Countries
```sql
SELECT name, population, area 
FROM World 
WHERE area>=3000000 OR population>=25000000;
```

## 1148. Article Views I
```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id=viewer_id
ORDER BY id;
```

## 1683. Invalid Tweets
```sql
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content)>15;
```

## 1378. Replace Employee ID With The Unique Identifier
```sql
SELECT EU.unique_id AS unique_id, E.name AS name
FROM EmployeeUNI EU RIGHT JOIN Employees E
ON E.id = EU.id;
```

## 1068. Product Sales Analysis I
```sql
SELECT P.product_name, S.year, S.price
FROM Product P JOIN Sales S 
ON P.product_id = S.product_id;
```

## 1581. Customer Who Visited but Did Not Make Any Transactions
```sql
SELECT v.customer_id,
       COUNT(v.customer_id) AS count_no_trans
FROM   visits v
       LEFT JOIN transactions t
              ON v.visit_id = t.visit_id
WHERE  t.transaction_id IS NULL
GROUP  BY v.customer_id; 
```

## 1661. Average Time of Process per Machine
```sql
SELECT A1.machine_id as machine_id, ROUND(AVG(A2.timestamp - A1.timestamp), 3) as processing_time
FROM Activity A1
JOIN Activity A2 ON A1.machine_id = A2.machine_id
  AND A1.process_id = A2.process_id
  AND A1.activity_type = 'start'
  AND A2.activity_type = 'end'
GROUP BY machine_id;
```

## 1731. The Number of Employees Which Report to Each Employee
```sql
SELECT e2.employee_id        AS employee_id,
       e2.name               AS name,
       Count(*)              AS reports_count,
       Round(Avg(e1.age), 0) AS average_age
FROM   employees e1
       JOIN employees e2
         ON e1.reports_to = e2.employee_id
GROUP  BY e2.employee_id
ORDER  BY employee_id; 
```

## 602. Friend Requests II: Who Has the Most Friends
```sql
WITH combining_ids AS
(
       SELECT requester_id AS id
       FROM   requestaccepted
       UNION ALL
       SELECT accepter_id AS id
       FROM   requestaccepted )
SELECT   id,
         Count(*) AS num
FROM     combining_ids
GROUP BY id
ORDER BY num DESC limit 1;
```