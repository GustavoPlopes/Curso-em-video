use cadastro;
describe gafanhotos;

alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos
add foreign key (cursopreferido)
references cursos(idcurso);

select * from gafanhotos;

update gafanhotos
set cursopreferido = '6' where id = '1';

select gafanhotos.nome, cursos.nome, cursos.ano from gafanhotos join cursos
on cursos.idcurso = gafanhotos.cursopreferido;

update gafanhotos
set cursopreferido = '4'
where id = '12';

select g.nome, c.nome, c.ano from gafanhotos as g
inner join cursos as c
on c.idcurso = g.cursopreferido;

select g.nome, c.nome, c.ano from gafanhotos as g 
left outer join cursos as c
on c.idcurso = g.cursopreferido;

select g.nome, c.nome, c.ano from gafanhotos as g
right outer join cursos as c
on c.idcurso = g.cursopreferido; 