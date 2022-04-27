-- Création des tables primaires
DROP TABLE IF EXISTS institution;
DROP TABLE IF EXISTS publication;
DROP TABLE IF EXISTS concept;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS source;

-- Création des relations entre les tables
DROP TABLE IF EXISTS authorInstitution;
DROP TABLE IF EXISTS authorPublication;
DROP TABLE IF EXISTS authorPublicationConcept;

-- Lien entre la source et les différentes éléménts
DROP TABLE IF EXISTS sourcePublication;
DROP TABLE IF EXISTS sourceAuthor;

CREATE TABLE IF NOT EXISTS institution (
    id_institution int(11) NOT NULL AUTO_INCREMENT,
    idAlex_institution varchar(100),
    display_name varchar(100),
    country_code varchar(100),
    type_institution varchar(100),
    idRor_insitution varchar(100),
    PRIMARY KEY (id_institution)
);

CREATE TABLE IF NOT EXISTS publication (
    id_publication int(11) NOT NULL AUTO_INCREMENT,
    idDoi_publication varchar(500),
    title varchar(500),
    display_name varchar(500),
    type_publication varchar(100),
    publication_year varchar(100),
    publication_date varchar(100),
    updated_date varchar(100),
    created_date varchar(100),
    PRIMARY KEY (id_publication)
);

CREATE TABLE IF NOT EXISTS source(
    id_source int(11) NOT NULL AUTO_INCREMENT,
    display_name varchar(600) NOT NULL,
    website_url varchar(600) NOT NULL,
    PRIMARY KEY (id_source)
);

INSERT INTO source (id_source,display_name,website_url) VALUES
(1, "OpenAlex", "https://openalex.org/"),
(2, "GoogleScholar", "https://scholar.google.com/");

CREATE TABLE IF NOT EXISTS sourcePublication(
    id_sourcePublication int(11) NOT NULL AUTO_INCREMENT,
    id_publication int(11) NOT NULL,
    id_source int(11) NOT NULL,
    specificId varchar(600),
    PRIMARY KEY (id_sourcePublication),
    FOREIGN KEY (id_publication) REFERENCES publication(id_publication),
    FOREIGN KEY (id_source) REFERENCES source(id_source)
);

CREATE TABLE IF NOT EXISTS concept(
    id_concept int(11) NOT NULL AUTO_INCREMENT,
    idAlex_concept varchar(100),
    wikidata varchar(100),
    display_name varchar(500),
    PRIMARY KEY (id_concept)
);

CREATE TABLE IF NOT EXISTS author (
    id_author int(11) NOT NULL AUTO_INCREMENT,
    orcid_id varchar(2000),
    display_name varchar(2000),
    display_name_alternatives varchar(2000),
    -- works_count varchar(500),
    -- cited_by_count varchar(500),
    PRIMARY KEY (id_author)
);

CREATE TABLE IF NOT EXISTS sourceAuthor(
    id_sourceAuthor int(11) NOT NULL AUTO_INCREMENT,
    id_author int(11) NOT NULL,
    id_source int(11) NOT NULL,
    specificId varchar(600),
    PRIMARY KEY (id_sourceAuthor),
    FOREIGN KEY (id_author) REFERENCES author(id_author),
    FOREIGN KEY (id_source) REFERENCES source(id_source)
);


CREATE TABLE IF NOT EXISTS authorInstitution (
    id_authorInstitution int(11) NOT NULL AUTO_INCREMENT,
    id_author int(11) NOT NULL,
    id_institution int(11) NOT NULL,
    PRIMARY KEY (id_authorInstitution),
    FOREIGN KEY (id_author) REFERENCES author(id_author),
    FOREIGN KEY (id_institution) REFERENCES institution(id_institution)
);

CREATE TABLE IF NOT EXISTS authorPublication (
    id_authorPublication int(11) NOT NULL AUTO_INCREMENT,
    id_author int(11) NOT NULL,
    id_publication int(11) NOT NULL,
    author_position varchar(100) NOT NULL,
    PRIMARY KEY (id_authorPublication),
    FOREIGN KEY (id_author) REFERENCES author(id_author),
    FOREIGN KEY (id_publication) REFERENCES publication(id_publication)
);


CREATE TABLE IF NOT EXISTS authorPublicationConcept (
    id_authorPublicationConcept int(11) NOT NULL AUTO_INCREMENT,
    id_author varchar(11),
    id_publication varchar(11),
    id_concept varchar(11) NOT NULL,
    level_concept varchar(11),
    score_concept varchar(11),
    PRIMARY KEY (id_authorPublicationConcept),
    FOREIGN KEY (id_author) REFERENCES author(id_author),
    FOREIGN KEY (id_publication) REFERENCES publication(id_publication),
    FOREIGN KEY (id_concept) REFERENCES concept(id_concept)
);

