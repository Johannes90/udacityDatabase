-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- initialize Database, use psql and then \i tournament.sql in the terminal to initialize.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- Creating Tables

CREATE TABLE IF NOT EXISTS players (
  	id SERIAL PRIMARY KEY,
  	name VARCHAR(40)
);

ALTER SEQUENCE players_id_seq RESTART;

CREATE TABLE IF NOT EXISTS matches (
	id SERIAL PRIMARY KEY,
  	winner integer REFERENCES players (id),
  	loser integer REFERENCES players (id)
);

ALTER SEQUENCE matches_id_seq RESTART;


-- Creating Views

CREATE VIEW playerStandings AS
SELECT 	id, 
		name, 
		(SELECT count(*) FROM matches WHERE players.id = matches.winner) AS wins, 
		(SELECT count(*) FROM matches WHERE players.id = matches.loser OR players.id = matches.winner) AS matches
FROM players
ORDER BY wins DESC;


