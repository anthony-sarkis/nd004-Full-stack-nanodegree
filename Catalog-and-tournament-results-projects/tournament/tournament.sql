

-- this file is part of the tournmant psql project
-- it creates the basic data structures and 3 views central to tournament.py


-- built in drop function to allow easy testing

drop database tournament;
create database tournament;
\c tournament;


create table players (
	player_id	serial		primary key,
	name		text
);

-- 

create table matches (
	match_id	serial		primary key,
	winner		integer 	references players (player_id),
	loser		integer 	references players (player_id)
);

-- create a view of winners by joining players and matches
-- match on player_id = winner (which is also a player id)
-- use left join as a player may not yet have a win or match for that matter

create view winners as
	select players.player_id, players.name, count(matches.winner) as wins
	from players left join matches on players.player_id = matches.winner
	group by players.player_id, players.name order by players.player_id;

-- same concept as winners for losers
-- ! important, make sure in from statement comparing player ID to loser in loser view

create view losers as
	select players.player_id, players.name, count(matches.loser) as losses
	from players left join matches on players.player_id = matches.loser
	group by players.player_id, players.name order by players.player_id;


-- combine winners and losers view into a unified view
-- (winner.wins + losers.losses) = total count
-- perform join on user ID
-- in order to fulfill requirement that first entry on the list is player in first place

create view standings as
	select winners.player_id, winners.name, winners.wins, (winners.wins + losers.losses) as matches
	from winners left join losers on winners.player_id = losers.player_id
	order by winners.wins DESC;