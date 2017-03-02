#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection.

    11/9/2016 Per udacity suggestion, refactored connect method to deal with
    both cursor and db. And to setup better exception handling with try/except

    """

    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error connecting.")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()

    cursor.execute("""
        delete from matches
        ;""")

    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()

    cursor.execute("""
        delete from players
        ;""")

    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()

    cursor.execute("""
        select count(players)
        from players
        ;""")
    results = cursor.fetchone()

    db.close()
    return results[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).

      Passing variable so as to avoid SQL injection.
    """
    db, cursor = connect()

    query = "insert into players (name) values (%s);"
    params = (name, )
    cursor.execute(query, params)

    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    db, cursor = connect()

    cursor.execute("select * from standings;")
    results = cursor.fetchall()

    db.close()
    return results

    """
    alternate statement, can be useful for testing views functions

        select player_id, name,
        count(matches.winner = player_id), count(matches)
        from players left join matches
           on players.player_id = matches.winner or
            players.player_id = matches.loser
        group by players.player_id

    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()

    cursor.execute("insert into matches (winner, loser) values (%s, %s);", (winner, loser,))

    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # create a blank arrary to store results

    results = []

    # run the player standings function to get a list of win records
    standings = playerStandings()

    """
    aggregates two slices of standings lists into one iterator

    Here is an example I created to better unerstand:
    Consider a given list a=[1,2,3,4]
    Then for a,b in zip(a[0::2], a[0::2])
        a = 1, b = 2, then a = 3, b = 4, etc.

    the 0:: slice is the starting point, and then skips by 2 (the ::2 part)
    the 1:: slice is the second point, also skipping by 2.

    feel free to try in a python window:
    1) a=[1,2,3,4]
    2) a[0::2]
    3) a[1::2]

    or uncomment print below line for visual while running
        the tournament_test.py file.

    print standings[0::2], standings[1::2]
    """

    for a, b in zip(standings[0::2], standings[1::2]):
        # append results,
        # taking the player_id ([0] indexed) and
        # the name (at the [1] index)
        # the index is per the standings view in tournament.sql
        results.append([a[0], a[1], b[0], b[1]])
    return results
