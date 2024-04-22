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