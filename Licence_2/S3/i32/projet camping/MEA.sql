CREATE TABLE "Clients" (
	"id_clients" serial NOT NULL,
	"Nom" char NOT NULL,
	"Prénom" serial NOT NULL,
	"Adresse" serial NOT NULL,
	"Ville" char NOT NULL,
	"Téléphone" serial NOT NULL,
	"Mail" serial NOT NULL,
	CONSTRAINT "Clients_pk" PRIMARY KEY ("id_clients")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Réservation" (
	"id_clients" bigint NOT NULL,
	"Type" char NOT NULL,
	"Date arrivée" DATE NOT NULL,
	"Date départ" DATE NOT NULL,
	"NbrPersonnes" bigint NOT NULL,
	"id_demipension" bigint NOT NULL,
	CONSTRAINT "Réservation_pk" PRIMARY KEY ("Type")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Emplacements" (
	"Numéro" bigint NOT NULL,
	"Type" char NOT NULL,
	"Nbremplacements" serial NOT NULL,
	CONSTRAINT "Emplacements_pk" PRIMARY KEY ("Numéro")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Tarif emplacement" (
	"Numéro" bigint NOT NULL,
	"id_tarif" bigint NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Activité" (
	"id_activité" serial NOT NULL,
	"Activité" character NOT NULL,
	CONSTRAINT "Activité_pk" PRIMARY KEY ("id_activité")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Tarif_activité" (
	"id_activité" bigint NOT NULL,
	"id_tarif" bigint NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Client_activité" (
	"id_clients" bigint NOT NULL,
	"id_activité" bigint NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Tarif" (
	"id_tarif" serial NOT NULL,
	"prix" DECIMAL NOT NULL,
	CONSTRAINT "Tarif_pk" PRIMARY KEY ("id_tarif")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Saison" (
	"id_saison" serial NOT NULL,
	"saison" char NOT NULL,
	"date_debut" DATE NOT NULL,
	"date_fin" DATE NOT NULL,
	CONSTRAINT "Saison_pk" PRIMARY KEY ("id_saison")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Tarif_saison" (
	"id_saison" bigint NOT NULL,
	"id_tarif" bigint NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Demi_pension" (
	"id_demipension" bigint NOT NULL,
	"id_clients" bigint NOT NULL,
	CONSTRAINT "Demi_pension_pk" PRIMARY KEY ("id_demipension")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Tarif_demipension" (
	"id_demipension" bigint NOT NULL,
	"id_tarif" bigint NOT NULL
) WITH (
  OIDS=FALSE
);


ALTER TABLE "Réservation" ADD CONSTRAINT "Réservation_fk0" FOREIGN KEY ("id_clients") REFERENCES "Clients"("id_clients");
ALTER TABLE "Réservation" ADD CONSTRAINT "Réservation_fk1" FOREIGN KEY ("id_demipension") REFERENCES "Demi_pension"("id_demipension");

ALTER TABLE "Emplacements" ADD CONSTRAINT "Emplacements_fk0" FOREIGN KEY ("Type") REFERENCES "Réservation"("Type");

ALTER TABLE "Tarif emplacement" ADD CONSTRAINT "Tarif emplacement_fk0" FOREIGN KEY ("Numéro") REFERENCES "Emplacements"("Numéro");
ALTER TABLE "Tarif emplacement" ADD CONSTRAINT "Tarif emplacement_fk1" FOREIGN KEY ("id_tarif") REFERENCES "Tarif"("id_tarif");


ALTER TABLE "Tarif_activité" ADD CONSTRAINT "Tarif_activité_fk0" FOREIGN KEY ("id_activité") REFERENCES "Activité"("id_activité");
ALTER TABLE "Tarif_activité" ADD CONSTRAINT "Tarif_activité_fk1" FOREIGN KEY ("id_tarif") REFERENCES "Tarif"("id_tarif");

ALTER TABLE "Client_activité" ADD CONSTRAINT "Client_activité_fk0" FOREIGN KEY ("id_clients") REFERENCES "Clients"("id_clients");
ALTER TABLE "Client_activité" ADD CONSTRAINT "Client_activité_fk1" FOREIGN KEY ("id_activité") REFERENCES "Activité"("id_activité");


ALTER TABLE "Tarif_saison" ADD CONSTRAINT "Tarif_saison_fk0" FOREIGN KEY ("id_saison") REFERENCES "Saison"("id_saison");
ALTER TABLE "Tarif_saison" ADD CONSTRAINT "Tarif_saison_fk1" FOREIGN KEY ("id_tarif") REFERENCES "Tarif"("id_tarif");


ALTER TABLE "Demi_pension" ADD CONSTRAINT "Demi_pension_fk0" FOREIGN KEY ("id_clients") REFERENCES "Clients"("id_clients");

ALTER TABLE "Tarif_demipension" ADD CONSTRAINT "Tarif_demipension_fk0" FOREIGN KEY ("id_demipension") REFERENCES "Demi_pension"("id_demipension");
ALTER TABLE "Tarif_demipension" ADD CONSTRAINT "Tarif_demipension_fk1" FOREIGN KEY ("id_tarif") REFERENCES "Tarif"("id_tarif");