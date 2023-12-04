select distinct totaulas from cursos
order by totaulas;

select totaulas, count(*) from cursos
group by totaulas
order by totaulas;

select * from cursos 
where totaulas = 30;

select carga, count(*) from cursos
where totaulas = 30
group by carga;

select ano, count(*) from cursos
group by ano
having count(ano) >= 5
order by count(*) desc;