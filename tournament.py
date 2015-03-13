#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

#declare our global connection object and cursor
gc = connect()
cursor = gc.cursor()

def deleteMatches():
    """Remove all the match records from the database."""
    cursor.execute("""delete from matches""")

def deletePlayers():
    """Remove all the player records from the database."""
    cursor.execute("""delete from players""")

def countPlayers():
    """Returns the number of players currently registered."""
    cursor.execute("""select count(name) from players""")
    return cursor.fetchone()[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    if "'" in name:
        ap_index = name.index("'")
        name = name[0:ap_index] + "''" + name[ap_index+1:]
 
    cursor.execute("""insert into players (name) values ('%s')""" % name)
    gc.commit()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    
    cursor.execute("select * from players")
    player_data = cursor.fetchall()
    wins_sorted = []

    for tup_index in range(len(player_data)):
        #the %s is about 400 ns faster than %d for integer substitution
        cursor.execute("select count(winnerid) from matches where winnerid = %s" % player_data[tup_index][0])
        numMatchesWon = cursor.fetchone()[0]

        cursor.execute("select count(loserid) from matches where loserid = %s" % player_data[tup_index][0])
        numMatchesLost = cursor.fetchone()[0]

        numMatchesPlayed = numMatchesWon + numMatchesLost

        wins_sorted.append(int(numMatchesWon))
        player_data[tup_index] += int(numMatchesWon),
        player_data[tup_index] += int(numMatchesPlayed),
    
    wins_sorted.sort(reverse=True)
    player_data_sorted_bywins = []
    
    #this is how im sorting the data from the database by wins, I'm hoping that this was supposed to be done with python code and not sql
    for w in wins_sorted:
        for tup_ind in range(len(player_data)):
            if player_data[tup_ind][2] == w:
                player_data_sorted_bywins.append(player_data[tup_ind])
                del player_data[tup_ind]
                break
                
    return player_data_sorted_bywins

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
        
    cursor.execute("insert into matches (winnerid, loserid) values (%s, %s)" % (winner, loser))
    gc.commit()
 
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

    # Ok This is where things get interesting, how in the world should i solve this problem
    # A question to the udacity reviewer. Shouldn't standings be passed in to this function since weve already called it in tournament_test.testPairings

    #anyways

    nextRoundPlayers = []
    standings = playerStandings()
    
    # since our players are ordered by wins, first place first and we have an even number of players,
    # this seems like a no-brainer to just have every 2 tuples starting from the beginning to be the next match
    # however this needs to to be implemented algorithmically
    
    #loop through our players and when we get to an even index, we get the previous two players and assign their ids and names to the next tuple 
    #in nextRoundPlayers
    
    i = 0
    while i < len(standings):
        if i % 2 == 0:
            id1 = standings[i-1][0]
            name1 = standings[i-1][1]

            id2 = standings[i-2][0]
            name2 = standings[i-2][1]

            nextRoundPlayers.append((id1, name1, id2, name2))

        i += 1
        
    return nextRoundPlayers
