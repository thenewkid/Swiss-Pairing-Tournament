-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table matches (
       id serial not null,
       winnerid	 int not null,
       loserid int not null
);

create table players (
       id serial not null,
       name text not null
);


