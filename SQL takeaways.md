## SQL takeaways 

#### 177. Nth Highest Salary
1. LIMIT 1 OFFSET N-1   
We skip the first n-1 rows and start with the nth row.  
With order by, we can have the nth highest value
2. IFNULL(xxx,null)
This expression can return a default value if the value is Null  

#### 178. Rank Scores
Solutions:
  
* Always Count  (I use this one)
This one counts, for each score, the number of distinct greater or equal scores.

	SELECT
  Score,
  (SELECT count(distinct Score) FROM Scores WHERE Score >= s.Score) Rank
FROM Scores s
ORDER BY Score desc

* Always Count, Pre-uniqued: 795 ms  
Same as the previous one, but faster because I have a subquery that "uniquifies" the scores first. Not entirely sure why it's faster, I'm guessing MySQL makes tmp a temporary table and uses it for every outer Score.

	SELECT
  Score,
  (SELECT count(*) FROM (SELECT distinct Score s FROM Scores) tmp WHERE s >= Score) Rank
FROM Scores
ORDER BY Score desc

* Filter/count Scores^2: 1414 ms

	Inspired by the attempt in wangkan2001's answer. Finally Id is good for something :-)

	SELECT s.Score, count(distinct t.score) Rank
FROM Scores s JOIN Scores t ON s.Score <= t.score
GROUP BY s.Id
ORDER BY s.Score desc

#### 180. Consecutive Numbers 
Solution:

* query more than one table at once  

SELECT *
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num  

#### 182. Duplicate Emails
* Use Group by and having to deduplicate
select * from *** group by ** having count(*) > 1