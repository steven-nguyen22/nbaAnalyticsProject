
##Search Player by name
def queryPlayerName(data, data_set):
    results = []

    players = data_set.get("players")
    
    for row in players:
        if data == row["player_name"]:
            results.append(row)
    return results



##Search by City name
def queryCityName(data, data_set):
    results = []

    ranking = data_set.get("ranking")
    
    for row in ranking:
        if data == row["team"]:
            results.append(row)
    return results


##Search by Team name
def queryTeamName(data, data_set):
    results = []

    teams = data_set.get("teams")

    for row in teams:
        if data == row["nickname"]:
            results.append(row)
    return results



##Work in progress: Search something in games_details_backup.csv ##
def queryTeamID(data, data_set):
    results = []

    teams_id = data_set.get("games_details")

    for row in teams_id:
        if data == row["team_id"]:
            results.append(row)
    return results