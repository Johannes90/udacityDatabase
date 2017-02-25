#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
# This document contains functions as the basis for a swiss tournament system. The user needs to innitialize the database
# first as described in the Readme.md in this repository.

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname=tournament")
        cursor = db.cursor()
        return db, cursor
    except:
        print("Could not connect to the database")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = "DELETE FROM matches"
    cursor.execute(query)
    db.commit()
    db.close()

    return "Matches deleted"


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    try:
        cursor.execute("TRUNCATE TABLE players CASCADE")
        print("deleted all players")
    except:
        print("could not delete")

    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = "SELECT COUNT(*) FROM players"
    cursor.execute(query)
    count = cursor.fetchone()
    db.close()

    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    db, cursor = connect()
    try:
        query = "INSERT INTO players(name) VALUES (%s)"
        data = (name, )
        cursor.execute(query, data)
    except:
        print("Could not insert player")
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
    try:
        query = "SELECT * FROM playerStandings"
        cursor.execute(query)
        standings = cursor.fetchall()
        db.close()
        return standings
    except:
        print("Could not retrieve player standings")


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    try:
        query = "INSERT INTO matches(winner,loser) VALUES (%s, %s)"
        data = (winner, loser)
        cursor.execute(query, data)
    except:
        print("Could not insert match")

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
    db, cursor = connect()
    query = "SELECT * FROM playerStandings"
    cursor.execute(query)
    standings = cursor.fetchall()
    pairingNum = len(standings)
    pairings = []

    for player in range(0, pairingNum, 2):
        match = (standings[player][0], standings[player][1], standings[player + 1][0], standings[player + 1][1])
        pairings.append(match)
    return pairings
