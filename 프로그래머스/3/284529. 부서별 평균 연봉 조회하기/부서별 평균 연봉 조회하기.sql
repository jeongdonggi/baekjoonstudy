-- 코드를 작성해주세요
select d.dept_id, d.dept_name_en, round(sum(e.sal) / count(e.dept_id),0) as avg_sal
from hr_department d inner join hr_employees e using(dept_id)
group by d.dept_id
order by avg_sal desc