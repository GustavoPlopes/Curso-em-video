select * from cursos;

select * from cursos
where nome like 'p%';

select * from cursos
where nome like '%a';

select * from cursos
where nome like '%a%';

select * from cursos
where nome not like '%a%';

select * from cursos
where nome like 'ph%p';

select * from cursos
where nome like 'ph%p%';

select * from cursos
where nome like 'ph%p_';

select *from gafanhotos
where nome like '%silva%';

select *from gafanhotos
where nome like '%_silva%';

select distinct carga from cursos
order by carga;

select distinct ano from cursos
order by ano;

select count(*) from cursos;

select count(*) from cursos
where carga > 40;

select max(carga) from cursos;

select max(totaulas) from cursos
where ano = '2016';

select min(totaulas) from cursos;

select nome, min(totaulas) from cursos;

select sum(totaulas) from cursos;

select sum(totaulas) from cursos
where ano = '2016';

select avg(totaulas) from cursos;

select avg(totaulas) from cursos
where ano = '2016';