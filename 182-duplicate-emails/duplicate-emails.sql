# Write your MySQL query statement below
select email from (select email, count(*) as c from Person group by email) as count_email where c>1