CREATE TABLE NbPlacesParType(typeemplvarchar(25) primarykey,nbemplinteger;) 

INSERT  INTO  NbPlacesParType
SELECT  typeempl, count(*) as nbempl
FROM emplacement
GROUP BY typeempl;

CREATE TRIGGER ajout_empl
AFTER INSERT
ON Emplacement
FOR EACH ROW
EXECUTE PROCEDURE ajout_empl();

CREATE OR REPLACE FUNCTION ajout_empl()
RETURNS trigger AS
$$
    DECLARE
        BEGIN
            UPDATE NbPlacesParType SET nbempl=nbempl+1
            WHERE typeempl= new.typeempl;
            RETURN new;
            END;
$$
    LANGUAGE 'plpgsql';

CREATE TRIGGER supp_empl
AFTER DELETE  
ON Emplacement
FOR EACH ROW
EXECUTE PROCEDURE supp_empl();

CREATE OR REPLACE FUNCTION supp_empl()
RETURNS trigger AS
$$
    DECLARE
        BEGIN
            UPDATE NbPlacesParType SET nbempl=nbempl-1
            WHERE typeempl= old.typeempl;
            return old;
            END;
$$
    LANGUAGE 'plpgsql';