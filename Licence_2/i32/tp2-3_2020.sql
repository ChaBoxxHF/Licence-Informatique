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

18)
select id_participant,nom
from participant natural join inscription natural join cours
group by id_participant
having count(DISTINCT danse) = 2;


19)
select id_cours,danse
from intervenant natural join atelier natural join cours
where nom='amandine';

20)
select id_cours,danse,count(id_participant) as nb_de_participants
from intervenant natural join atelier natural join cours natural join inscription
where nom='amandine'
group by id_cours,danse;

21)
select id_cours,danse
from cours natural join inscription natural join participant
where nom='henri' or nom='melanie'
group by id_cours
having count(id_cours)=2;

22)
SELECT participant.id_participant, participant.nom
FROM participant, intervenant, inscription, atelier
WHERE participant.id_participant = inscription.id_participant
and inscription.id_cours = atelier.id_cours
and intervenant.id_intervenant = atelier.id_intervenant
and intervenant.nom = 'denis';

23)
select count(*) as nombre_participant
from participant,intervenant, inscription, atelier
where participant.id_participant=inscription.id_participant and inscription.id_cours = atelier.id_cours and intervenant.id_intervenant = atelier.id_intervenant
and intervenant.nom in ('amandine', 'denis');

24)
select id_cours, danse
from cours c
group by id_cours
having(
  select count(p.sexe)
  from inscription i, participant p
  where c.id_cours = i.id_cours
  and i.id_participant = p.id_participant
  and p.sexe = 'M'
) > ALL (
  select count(p.sexe)
  from inscription i, participant p
  where c.id_cours = i.id_cours
  and i.id_participant = p.id_participant
  and p.sexe = 'F'
);
