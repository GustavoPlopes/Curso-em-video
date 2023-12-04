select * from gafanhotos
where sexo = 'F'
order by nome;

select * from gafanhotos
where nascimento > '2000-01-01' and nascimento < '2015-12-31'
order by nascimento;

select nome from gafanhotos
where sexo = 'M' and profissao = 'Programador';

select * from gafanhotos
where sexo = 'F' and nacionalidade = 'Brasil' and nome like 'j%';

select nome, nacionalidade from gafanhotos
where sexo = 'M' and nome like '%silva%' and nacionalidade != 'Brasil' and peso < '100';

select max(altura) from gafanhotos
where sexo = 'M' and nacionalidade = 'Brasil';

select avg(peso) from gafanhotos;

select min(peso) from gafanhotos
where sexo = 'F' and nacionalidade != 'Brasil' and nascimento > '1990-01-01' 
and nascimento < '2000-12-31';

select count(*) from gafanhotos
where sexo = 'F' and altura > '1.90';

