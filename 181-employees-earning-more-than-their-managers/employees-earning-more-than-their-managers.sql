# Write your MySQL query statement below
select name as Employee from Employee as e where e.managerId is not NULL and e.salary>(select salary from Employee e2 where e2.id=e.managerId)