from .csvreadwrite import data_set
from .query import *

import csv
import time
from string import ascii_uppercase

# Helper functions to get our data
# ** GET **



#Function: searchPlayers(data)
#Description: Searches for input user provided within the datasets and output if any exists
def searchData(data):
    print('Searching... :', data)

    data_obj = {}

    ##searchs for features and returns results if exists
    player_name = queryPlayerName(data, data_set)
    city_name = queryCityName(data, data_set)
    nickname = queryTeamName(data, data_set)
    team_id = queryTeamID(data, data_set)

    ##Stores query results to data_obj
    data_obj['Players'] = player_name
    data_obj['City'] = city_name
    data_obj['Teams'] = nickname
    data_obj['Team_ID'] = team_id

    print("Search request finished.")
    return data_obj


def searchCity(data):
    print('Searching... :', data)

    data_obj = {}
    ##searchs for features and returns results if exists
    city_name = queryCityName(data, data_set)

    ##Stores query results to data_obj
    data_obj['City'] = city_name

    print("Search request finished.")
    return data_obj


def searchPlayer(data):
    print('Searching... :', data)
    data_obj = {}

    ##searchs for features and returns results if exists
    player_name = queryPlayerName(data, data_set)

    ##Stores query results to data_obj
    data_obj['Players'] = player_name
    print("Search request finished.")
    return data_obj


def searchTeam(data):
    print('Searching... :', data)
    data_obj = {}

    ##searchs for features and returns results if exists
    nickname = queryTeamName(data, data_set)

    ##Stores query results to data_obj
    data_obj['Teams'] = nickname
    print("Search request finished.")
    return data_obj


def searchTeamID(data):
    print('Searching... :', data)
    data_obj = {}

    ##searchs for features and returns results if exists
    team_id = queryTeamID(data, data_set)

    ##Stores query results to data_obj
    data_obj['Team_ID'] = team_id
    print("Search request finished.")
    return data_obj


#insert
def insertPlayerData(data):
    data_set['players'].append(data)

    # with open('../data/players.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(data)
    #     file.close()


def insertTeamData(data):
    data_set['teams'].append(data)


'''    with open('../data/teams.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()'''


def insertGamesDetailsData(data):
    data_set['games_details'].append(data)


'''    with open('../data/games_details_backup.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()'''


def insertRankingData(data):
    # check if our teams have been sorted by wins
    # if top_teams list length is 0, append data to ranking data object
    if len(data_set['top_teams']) == 0:
        print('Empty')
        print()
        data_set['ranking'].append(data)
    # else if teams sorted, append to sorted list
    elif len(data_set['top_teams']) != 0:
        # new_ranking will hold a dictionary of the necessary info for top teams
        new_ranking = []
        # new ranking will contain only the neccesary infor for our top teams data set (teams sorted by wins and season)
        new_ranking.append({
            'season_id': int(data['season_id']),
            'team': data['team'],
            'g': data['g'],
            'w': int(data['w']),
        })
        print('Sorted')
        print()
        data_set['top_teams'].append(new_ranking)

    # append a 1 to our win_changes so we know changes have been made to our team wins
    # ex: user can enter a new team and wins so we can later sort the teams based on wins and season
    data_set['win_changes'].append(1)


'''    with open('../data/ranking.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()'''


#delete
def deletePlayerData(data):
    # data holds the player the user wants to delete
    # ex: Look for Steph Curry and delete entire row
    lines = list()

    # get data_set to delete player
    temp_data = data_set['players']

    # get row in data_set
    for line in temp_data:

        lines.append(line)
        # check if col == data
        if line['player_name'] == data:
            lines.remove(line)

    data_set['players'] = lines


def deleteTeamData(data):
    lines = list()

    # get data_set to delete player
    temp_data = data_set['teams']

    # get row in data_set
    for line in temp_data:

        lines.append(line)
        # check if col == data
        if line['nickname'] == data:
            lines.remove(line)

    data_set['teams'] = lines



#update
def updatePlayerData(data):
    # data[0] = player name
    # data[1] = new team id
    lines = list()

    # get data_set to delete player
    temp_data = data_set['players']

    # get row in data_set
    for line in temp_data:
        lines.append(line)
        # check if col == data
        if line['player_name'] == data[0]:
            line['team_id'] = data[1]

    data_set['players'] = lines


def updateTeamData(data):
    print("*********")
    print(data[0])
    print(data[1])
    print("*********")
    lines = list()

    # get data_set to delete player
    temp_data = data_set['games']

    #get row in data_set
    for line in temp_data:
        lines.append(line)
        # check if col == data
        if line['nickname'] == data[0]:
            line['owner'] = data[1]

    data_set['teams'] = lines


def updateTeamWinsData(team_data):
    team = team_data[0]
    season = int(team_data[1])
    wins = int(team_data[2])
    updated_wins = []
    rankings_data = data_set['ranking']

    print('team: ' + team)
    print('season: ' + str(season))


    # print(rankings_data)

    for line in rankings_data:
        if line['team'] == team:
            if line['season_id'] == season:
                line['w'] = wins
        updated_wins.append(line)

    data_set['ranking'] = updated_wins



def updatePlayerPoints(season, player, points):
    top_scorer_data = data_set['top_scorers']
    i = 0

    for top_scorer in top_scorer_data:
        if top_scorer['season_id'] == season and top_scorer['player_name'] == player:
            top_scorer['points_scored'] = points
            break
    data_obj = {}



# analyze
# use ranking_backup.csv to look up data
def analyzeTop5Wins(season):
    data_obj = {}
    season = int(season)
    team_count =0
    # get all the teams in the nba
    all_teams = []
    # get top 5 teams based on wins
    top5_teams = []
    # list containing the sorted teams based on wins in a season
    sorted_teams = data_set['top_teams']
    # get ranking data_set so we can get
    ranking_data = data_set['ranking']
    # changes made to team wins
    team_win_changes = data_set['win_changes']



    # get top_teams data_set
    # this should contain our sorted teams based on wins for the season.
    # If empty then sort, else get top 5 teams based on season
    t0 = time.time()
    # if top_teams_data is empty then our wins data has never been sorted
    if len(sorted_teams) == 0:
        # loop through our dataset to get data of teams who have completed an entire season
        # example: if a team has only played 50 games, the season is not over yet.
        for line in ranking_data:
            # check if season is over
            if line['g'] == '82':
                # if season is over, append to our all_teams data
                # only append necessary data
                all_teams.append({
                    'season_id': int(line['season_id']),
                    'team': line['team'],
                    'g': line['g'],
                    'w': int(line['w']),
                })

        # sort teams by wins
        dataset = sorted(all_teams, key=lambda x: x['w'], reverse=True)
        # next sort team by season
        dataset = sorted(dataset, key=lambda x: x['season_id'], reverse=True)

        # remove any duplicates in our all_teams
        for line in dataset:
            if line not in sorted_teams:
                sorted_teams.append(line)


    # if top_teams_data is not empty then our wins data has been sorted
    elif len(sorted_teams) != 0:
        # check if any changes have been made to our sorted data
        # if yes, add changes to sorted data (continue until all changes accounted for)
        # ex: if three teams added, run while loop until 3 teams have been placed in the
        #     correct location
        while len(team_win_changes) != 0:
            newPlaceFound = False
            i = 0
            # get the last team on list which is the recently added team
            new_team = sorted_teams[-1]
            # remove the brackets encapsulating our dictionary data
            # ex: [{data}] -> {data}
            new_team = new_team[0]

            # remove last team
            sorted_teams.pop()

            while newPlaceFound == False and i < len(sorted_teams):
                # get the team from sorted_teams at index i
                team = sorted_teams[i]
                new_team_season_id = new_team['season_id']
                new_team_wins = new_team['w']
                if team['season_id'] == new_team_season_id:
                    if team['w'] == new_team_wins or team['w'] < new_team_wins:
                        sorted_teams.insert(i, new_team)
                        newPlaceFound = True

                i+=1

            # empty our list since changes were applied
            data_set['win_changes'].pop()


    t1 = time.time()


    # get the top 5 teams based on the season the user asked for
    for i in range(len(sorted_teams)):
        if sorted_teams[i]['season_id'] == season:
            # since the data is sorted by wins and year, we can get the top 5 teams from that year
            if team_count <5:
                top5_teams.append({
                    'team': sorted_teams[i]['team'],
                    'wins': sorted_teams[i]['w']
                })
                team_count += 1


    total = t1 - t0
    print('Total time sorting Top 5 Teams: ' + str(total))
    # save sorted data
    data_set['top_teams'] = sorted_teams

    # return top 5 teams in order to display
    data_obj['teams'] = top5_teams

    return data_obj




# data contains the player and stat the user wants. We return the player's career stat.
# Ex: On average, how many three pointers does Stephen Curry make?
def analyzePlayerStat(data):
    data_obj = {}

    # player name
    player = data[0]
    # player stat (we only have 3 pointers so far aka 'fg3m')
    stat = data[1]
    # total 3 pointer made by player
    totalThrees = 0.0
    # total games played in career
    games = 0
    # game id will help us find the date for the game in games_backup.csv
    game_id_list = list()
    # made_3pt will tell us how many 3's were made for a specific game
    made_3pt_list = list()
    # avg_3_list
    career_avg = list()
    avg_3 = []
    # data from our data structure
    games_details_data = data_set['games_details']

    for line in games_details_data:
        # find the row with our player
        if line['player_name'] == player:
            # if user wants to see 3 pointer stats
            if stat == "3 point":
                # make sure the stat is not empty, meaning they did not play
                if line['fg3m'] is not "":
                    game_id_list.append((line['game_id']))
                    made_3pt_list.append(line['fg3m'])
                    totalThrees += float(line['fg3m'])
                    games += 1
                    # average 3's per game
                    average_3pts = totalThrees / games
                    career_avg.append("{:.2f}".format(average_3pts))

    for i in range(len(game_id_list)):
        avg_3.append({'game_id': game_id_list[i],
                     'made_3pt': made_3pt_list[i],
                      })

    data_obj['3_pt_avg'] = avg_3
    return data_obj


# use games_backup.csv.csv to lookup home and away team stats
# returns average pts a home and away team scored in a specific
def analyzeTeamStat(data):
    data_obj = {}
    team_pts = []

    teams = ['Home', 'Away']
    points = []

    season = data[0]
    stat = data[1]
    home_pts = float()
    away_pts = float()

    team_data = data_set['games']

    for line in team_data:
        # get season user asked for
        if line['season'] == season:
            # if user wants to see home points vs away pts
            if stat == "points":
                # get home pts
                home_pts += float(line['pts_home'])
                # get away
                away_pts += float(line['pts_away'])

    # compute season average
    home_pts_avg = home_pts / (82 * 15)
    home_pts_avg = "{:.2f}".format(home_pts_avg)
    away_pts_avg = away_pts / (82 * 15)
    away_pts_avg = "{:.2f}".format(away_pts_avg)

    points.append(home_pts_avg)
    points.append(away_pts_avg)

    for i in range(len(teams)):
        team_pts.append({'name': teams[i],
                        'pts': points[i],})

    data_obj['pts'] = team_pts
    return data_obj



# for analyzeTopScorer we will get the top scorer for each player in each team for each season
# It currently takes really long. We do not know if it is because the large amount of checks
# Ex: 10 seasons * 30 teams * each team about 15-20 players * 82 games in season
def analyzeTopScorer(team_id, season,sorted_game_details):
    data_obj = {}
    top_scorers = []
    games_details_data = data_set['games_details']
    sorted_top_scorers = data_set['top_scorers']

    t0 = time.time()
    if len(sorted_top_scorers) == 0:
        # for loop will get a team from our games_details
        for team in sorted_game_details:
            for i in range(len(team['player_names'])):
                # sort our players based on team and season
                sorted_top_scorers.append({'season_id': team['season'],
                                           'team_id': team['team_id'],
                                           'player_id': team['team_roster'][i],
                                           'player_name': team['player_names'][i],
                                           'points_scored': team['points_scored'][i],
                                           'game_id': team['game_id'],
                                           })

        # For loop will get row in games_details data. A row will hold how many
        # points a player scored for a specific game
        for games_details in games_details_data:
            i = 0
            playerFound = False
            while playerFound == False and i < len(sorted_top_scorers):
                player = sorted_top_scorers[i]
                if games_details['player_name'] == player['player_name']:

                    if games_details['game_id'] in player['game_id']:
                        playerFound = True
                        # print('found game')
                        if games_details['pts'] != "":
                            print('Season: ' + player['season_id'])
                            print('Player Name: ' + player['player_name'])
                            print('Current Points: ' + str(player['points_scored']))
                            player['points_scored'] += float(games_details['pts'])
                            print('Updated Points: ' + str(player['points_scored']))
                i += 1

    for player in sorted_top_scorers:
        if player['team_id'] == team_id:
            if player['season_id'] == season:
                top_scorers.append({'player': player['player_name'],
                                    'points': player['points_scored'],
                                    })

    t1 = time.time()

    total = t1 - t0

    print('Total time sorting Top Scorers: ' + str(total))

    data_obj['top_scorer'] = top_scorers
    data_set['top_scorers'] = sorted_top_scorers

    return data_obj



def analyzeComparePlayers(data):
    data_obj = {}

    # player1 name
    player1 = data[0]
    # player2 name
    player2 = data[1]
    # player stat (we only have 3 pointers so far aka 'fg3m')
    stat = data[2]

    # hold the fg_pct for each player
    player1_fg_pct = 0.0
    player2_fg_pct = 0.0

    games1 = 0
    games2 = 0

    compare_players = []
    players = [player1, player2]
    fg_pct = []

    avg_player2_fg = float()

    # data for game details
    games_details_data = data_set['games_details']

    for line in games_details_data:
        # find the row with our player1
        if line['player_name'] == player1:
            print("****** Player 1 found ******")
            # if user wants to see 3 pointer stats
            if stat == "fg pct":
                # make sure the stat is not empty, meaning they did not play
                if line['fg_pct'] != "":
                    player1_fg_pct += float(line['fg_pct'])
                    games1 += 1
        if line['player_name'] == player2:
            print("$$$$$ Player 2 found $$$$$")
            # if user wants to see 3 pointer stats
            if stat == "fg pct":
                # make sure the stat is not empty, meaning they did not play
                if line['fg_pct'] != "":
                    print("$$$$$ Player 2 Stat found $$$$$")
                    player2_fg_pct += float(line['fg_pct'])
                    games2 += 1

    print("games1:  " + str(games1))
    print("player1: " + str(player1_fg_pct))
    # return 1
    #
    avg_player1_fg = player1_fg_pct / games1
    avg_player2_fg = player2_fg_pct / games2

    fg_pct.append(avg_player1_fg * 100.0)
    fg_pct.append(avg_player2_fg * 100.0)


    for i in range(2):
        compare_players.append({'player': players[i],
                      'fg_pct': fg_pct[i],
                      })

    data_obj['compare_players'] = compare_players
    return data_obj





# ---- HELPER FUNCTIONS TO RETRIEVE DATA ----
def getTeamID(team):
    team_data = data_set['teams']
    team_id = ""
    for line in team_data:
        if line['nickname'] == team:
            team_id = line['team_id']
    return team_id

def getTeamRoster(team_id, season):
    # get data from players.csv
    player_data = data_set['players']
    # list of players on team
    player_roster = list()

    for line in player_data:
        if line['season'] == season:
            if line['team_id'] == team_id:
                player_roster.append(line['player_id'])

    return player_roster

def getGamesPlayed(season, team_id):
    # get data from players.csv
    games_data = data_set['games']
    # list of games played in 'season'
    games_played = list()

    for game in games_data:
        if game['season'] == season:
            if game['home_team_id'] == team_id:
                games_played.append(game['game_id'])
            elif game['visitor_team_id'] == team_id:
                games_played.append(game['game_id'])
    return games_played


def getAllTeamNames():
    # team_names will hold all the team names in the NBA
    team_names = []
    # teams contains our teams data
    teams = data_set['teams']

    # check if line contains a new team name
    for line in teams:
        team_name = line['nickname']
        # if new team name found, append to team_names
        if team_name not in team_names:
            team_names.append(team_name)
    team_names.remove('NICKNAME')
    # return the list of our team names
    return team_names


# function turns player id into a name
def getPlayerNames(team_roster):
    player_names = []
    check_duplicate_names = []
    player_data = data_set['players']

    for player in team_roster:
        for line in player_data:
            if player == line['player_id']:
                if player not in player_names:
                    player_names.append(line['player_name'])
                # print('line:' + line['player_id'])
                # print('player: ' + player)
                # print()

    for player in player_names:
        if player not in check_duplicate_names:
            check_duplicate_names.append(player)

    player_names = check_duplicate_names

    return player_names


# Retrieve the team abbreviation (ex: NY Knicks -> NYK)
# input: team_id
# output: team_abbreviation
def getTeamAbbreviation(team_id):
    teams_data = data_set['teams']
    for line in teams_data:
        if line['team_id'] == team_id:
            team_abbreviations = line['abbreviation']
    return team_abbreviations


def sortGamesDetailsByTeam(all_teams_abbreviations):
    print('sortedGames')
    games_details_data = data_set['games_details']
    sorted_by_team = []

    for team in all_teams_abbreviations:
        for line in games_details_data:
            if line['team_abbreviation'] == team:
                sorted_by_team.append(line)

    data_set['games_details'] = sorted_by_team

def checkIfDataSortedByPoints():
    if len(data_set['top_scorers']) == 0:
        return False
    return True


# update data_set['win_changes] so we know changes have been made.
# We want to know if changes
def changesInWins():
    win_changes = data_set['win_changes']
    win_changes.append(1)

#backup
def backupData(data):
    if data == 'players':
        with open('../backup/' + data + '_backup.csv', 'w', newline='') as back_file:
            writer = csv.writer(back_file)
            for item in data_set['players']:
                writer.writerow(
                    [item['player_name'], item['team_id'], item['player_id'], item['season']])
            back_file.close()
    if data == 'teams':
        with open('../backup/' + data + '_backup.csv', 'w', newline='') as back_file:
            writer = csv.writer(back_file)
            for item in data_set['teams']:
                writer.writerow([item['league_id'], item['team_id'], item['min_year'], item['max_year'], item['abbreviation'], item['nickname'], item['yearfounded'],
                                item['city'], item['arena'], item['arenacapacity'], item['owner'], item['generalmanager'], item['headcoach'], item['dleagueaffiliation']])
            back_file.close()
    if data == 'ranking':
        with open('../backup/' + data + '_backup.csv', 'w', newline='') as back_file:
            writer = csv.writer(back_file)
            for item in data_set['ranking']:
                writer.writerow([item['team_id'], item['league_id'], item['season_id'], item['standings_date'], item['conference'], item['team'],
                                item['g'], item['w'], item['l'], item['w_pct'], item['home_record'], item['road_record'], item['returntoplay']])
            back_file.close()

    if data == 'games-details':
        with open('../backup/' + data + '_backup.csv', 'w', newline='') as back_file:
            writer = csv.writer(back_file)
            for item in data_set['games_details']:
                writer.writerow([item['game_id'], item['team_id'], item['team_abbreviation'], item['team_city'], item['player_id'], item['player_name'],
                                item['start_position'], item['comment'], item['min'], item['fgm'], item['fga'], item['fg_pct'], item['fg3m'],
                                item['fg3a'], item['fg3_pct'], item['ftm'], item['fta'], item['ft_pct'], item['oreb'], item['dreb'],
                                item['reb'], item['ast'], item['stl'], item['blk'], item['to'], item['pf'], item['pts'], item['plus_minus']])
            back_file.close()


'''with open('../backup/' + data + '_backup.csv', 'w') as back_file, open('../data/players.csv', 'r') as file:
            for line in file:
                back_file.write(line)
        back_file.close()
        file.close()
    if(data == 'ranking'):
        with open('../backup/' + data + '_backup.csv', 'w') as back_file, open('../data/ranking.csv', 'r') as file:
            for line in file:
                back_file.write(line)
        back_file.close()
        file.close()
    if(data == 'games-details'):
        with open('../backup/' + data + '_backup.csv', 'w') as back_file, open('../data/games_details_backup.csv', 'r') as file:
            for line in file:
                back_file.write(line)
        back_file.close()
        file.close()
    if(data == 'teams'):
        with open('../backup/' + data + '_backup.csv', 'w') as back_file, open('../data/teams.csv', 'r') as file:
            for line in file:
                back_file.write(line)
        back_file.close()
        file.close()


'''
