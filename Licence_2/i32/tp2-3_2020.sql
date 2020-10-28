1)
select nom, age
from participant;

2)
select avg(age)
from participant;

3)
select count(sexe)as M,count(sexe) as F
from participant
where sexe='M';

4)
select count(distinct danse) as danse
from cours;

6)
select danse, id_participant
from inscription
natural join cours;

6)
select danse
from inscription
right join cours on inscription.id_cours=cours.id_cours
where inscription.id_participant is null;

7)
select nom
from intervenant,atelier
where intervenant.id_intervenant=atelier.id_intervenant and id_cours
not in (select id_cours from inscription);

8)
select distinct nom
from participant natural join inscription natural join cours
where danse in ('salsa','rock');

9)
select danse, count(id_intervenant)
from atelier natural join cours
group by danse;

10)
select id_cours, nomselect id_participant,nom,max(age) as age
from participant;
from intervenant natural join atelier;

11)
select id_participant,nom,age
from participant
order by age desc
limit 1;

12)
select danse,count(id_cours)
from inscription natural join cours
group by cours.danse
order by count desc
limit 1;

13)
select id_cours
from atelier
group by id_cours
having count(id_cours)=1
order by id_cours;

14)
select id_cours
from atelier
group by id_cours
having count(id_cours)>=all(select count(*) from atelier group by id_cours);

15)
select id_cours,count(id_participant)
from inscription
group by id_cours;

16)
select count(id_cours)
from atelier where id_intervenant=2;

17)
select id_participant,nom
from participant natural join inscription natural join cours
where danse='salsa';
