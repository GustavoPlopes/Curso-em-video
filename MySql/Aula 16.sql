create table gafanhoto_assiste_curso (
id int not null auto_increment,
data date,
idgafanhoto int,
idcurso int,
primary key(id),
foreign key (idgafanhoto) references gafanhotos(id),
foreign key (idcurso) references cursos(idcurso)
) default charset = utf8;

insert into gafanhoto_assiste_curso values
(default, '2014-03-01', '1', '2');

insert into gafanhoto_assiste_curso values
(default, '2015-02-14', '3', '6'),
(default, '2014-01-01', '22', '12'),
(default, '2016-05-12', '1', '1');

select g.id, g.nome, ag.idgafanhoto, ag.idcurso, c.nome from gafanhotos as g
join gafanhoto_assiste_curso as ag
on g.id = ag.idgafanhoto
join cursos as c
on c.idcurso = ag.idcurso
order by g.nome;

select * from gafanhoto_assiste_curso;