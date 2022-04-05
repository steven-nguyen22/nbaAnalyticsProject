

##csv data stored into list
data_set = {}


#Function name: loadCSV()
#Description: On homepage load, csv data is automatically stored into list
def loadCSV():

    # will hold the data from their designated csv
    players = []
    games_details = []
    ranking = []
    teams = []
    games = []
    top5_teams = []

    print("Loading csv data...")

    # Stores teams_backup.csv to teams list
    with open('backup/games_backup.csv', "r") as file:
        for line in file:
            line = line.strip("\n")
            columns = line.split(",")
            games.append({
                'game_date_est': columns[0],
                'game_id': columns[1],
                'game_status_text': columns[2],
                'home_team_id': columns[3],
                'visitor_team_id': columns[4],
                'season': columns[5],
                'team_id_home': columns[6],
                'pts_home': columns[7],
                'fg_pct_home': columns[8],
                'ft_pct_home': columns[9],
                'fg3_pct_home': columns[10],
                'ast_home': columns[11],
                'reb_home': columns[12],
                'away_id_home': columns[13],
                'pts_away': columns[14],
                'fg_pct_away': columns[15],
                'ft_pct_away': columns[16],
                'fg3_pct_away': columns[17],
                'ast_away': columns[18],
                'reb_away': columns[19],
            })
        file.close()

    # Stores games_details_backup.csv to games_details list
    with open('backup/games_details_backup.csv', "r") as file:
        for line in file:
            line = line.strip("\n")
            columns = line.split(",")
            games_details.append({
                ##create object here
                'game_id': columns[0],
                'team_id': columns[1],
                'team_abbreviation': columns[2],
                'team_city': columns[3],
                'player_id': columns[4],
                'player_name': columns[5],
                'start_position': columns[6],
                'comment': columns[7],
                'min': columns[8],
                'fgm': columns[9],
                'fga': columns[10],
                'fg_pct': columns[11],
                'fg3m': columns[12],
                'fg3a': columns[13],
                'fg3_pct': columns[14],
                'ftm': columns[15],
                'fta': columns[16],
                'ft_pct': columns[17],
                'oreb': columns[18],
                'dreb': columns[19],
                'reb': columns[20],
                'ast': columns[21],
                'stl': columns[22],
                'blk': columns[23],
                'to': columns[24],
                'pf': columns[25],
                'pts': columns[26],
                'pf': columns[25],
                'pts': columns[26],
                'plus_minus': columns[27],
            })
        file.close()

    #Stores players_backup.csv to players list
    with open('backup/players_backup.csv', "r") as file:
        for line in file:
            line = line.strip("\n")
            columns = line.split(",")
            players.append({
                'player_name': columns[0],
                'team_id': columns[1],
                'player_id': columns[2],
                'season': columns[3]
            })
        file.close()


    #Stores ranking_backup.csv to ranking list
    with open('backup/ranking_backup.csv', "r") as file:
        for line in file:
            line = line.strip("\n")
            columns = line.split(",")
            ranking.append({
                'team_id': columns[0],
                'league_id': columns[1],
                'season_id': columns[2],
                'standings_date': columns[3],
                'conference': columns[4],
                'team': columns[5],
                'g': columns[6],
                'w': columns[7],
                'l': columns[8],
                'w_pct': columns[9],
                'home_record': columns[10],
                'road_record': columns[11],
                'returntoplay': columns[12]
            })
        file.close()


    #Stores teams_backup.csv to teams list
    with open('backup/teams_backup.csv', "r") as file:
        for line in file:
            line = line.strip("\n")
            columns = line.split(",")
            teams.append({
                'league_id' : columns[0],
                'team_id' :  columns[1],
                'min_year' :  columns[2],
                'max_year' :  columns[3],
                'abbreviation' :  columns[4],
                'nickname' :  columns[5],
                'yearfounded' :  columns[6],
                'city' :  columns[7],
                'arena' :  columns[8],
                'arenacapacity' :  columns[9],
                'owner' :  columns[10],
                'generalmanager' :  columns[11],
                'headcoach' :  columns[12],
                'dleagueaffiliation' :  columns[13]
            })
        file.close()




    # #Stores ranking_backup.csv to ranking list
    # with open('../data/ranking.csv', "r") as file:
    #     for line in file:
    #         line = line.strip("\n")
    #         columns = line.split(",")
    #         top5_teams.append({
    #             'season_id': columns[2],
    #             'team': columns[5],
    #             'g': columns[6],
    #             'w': columns[7],
    #             'l': columns[8],
    #         })
    #     file.close()


    createDataObj(players, games_details, ranking, teams, games)
    return data_set



#Function: createDataObj(players, games, ranking, teams)
#Description: Creates an Object consisting of all data sets
def createDataObj(players, games_details, ranking, teams, games):
    data_set['players'] = players
    data_set['games_details'] = games_details
    data_set['ranking'] = ranking
    data_set['teams'] = teams
    data_set['games'] = games
    data_set['top_teams'] = []
    data_set['top_scorers'] = []
    data_set['win_changes'] = []
    # data_set['top5_teams'] = top5_teams



