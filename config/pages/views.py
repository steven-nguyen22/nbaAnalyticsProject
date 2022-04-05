from django.shortcuts import render
from django.http import HttpResponse

from .src import csvreadwrite
from .src import utils


from csv import writer

##enter functions below


def homePageView(request):
    context = csvreadwrite.loadCSV()
    return render(request, 'index.html', context)


def search_all(request):
    print('Search request received.')
    if request.method == 'GET':
        data = request.GET.get('search_all')
        context = utils.searchData(data)
        return render(request, 'search.html', context)


def search_city(request):
    print('Search request received.')
    if request.method == 'GET':
        data = request.GET.get('search_city')
        context = utils.searchCity(data)
        # print("*************")
        # print("Context: ")
        # print(context)
        # print(type(context))
        # print("*************")
        return render(request, 'searchCity.html', context)


def search_player(request):
    print('Search request received.')
    if request.method == 'GET':
        data = request.GET.get('search_player')
        context = utils.searchPlayer(data)
        return render(request, 'searchPlayer.html', context)


def search_team(request):
    print('Search request received.')
    if request.method == 'GET':
        data = request.GET.get('search_team')
        context = utils.searchTeam(data)
        return render(request, 'searchTeam.html', context)


def search_team_id(request):
    print('Search request received.')
    if request.method == 'GET':
        data = request.GET.get('search_team_id')
        context = utils.searchTeamID(data)
        return render(request, 'searchGameDetails.html', context)


def insert(request):
    print('Insert request received.')
    if request.method == 'GET':
        # data = request.GET.get('search_team_id')
        # context = utils.searchTeamID(data)
        return render(request, 'insert_options.html')


def insert_player(request):
    print('Insert Player request received.')
    # if request.method == 'GET':
    #     data = request.GET.get('player_name')
    #     utils.insertPlayerData(data)
    print("Success!!!")
    return render(request, 'insert_options_players.html')


def insert_new_player(request):
    print('Insert New Player request received.')

    player = request.GET.get('insert_player_name')
    team_id = request.GET.get('insert_team_id')
    player_id = request.GET.get('insert_player_id')
    season = request.GET.get('insert_season')

    #input = [player, team_id, player_id, season]
    input = {
        'player_name': player,
        'team_id': team_id,
        'player_id': player_id,
        'season': season,
    }

    utils.insertPlayerData(input)

    #return render(request, 'insert_options.html')
    return render(request, 'index.html')


def insert_team(request):
    return render(request, 'insert_options_team.html')


def insert_new_team(request):

    # user inputs for our new team
    league_id = request.GET.get('insert-league-id')
    team_id = request.GET.get('insert-team-id')
    min_year = request.GET.get('insert-min-year')
    max_year = request.GET.get('insert-max-year')
    abb = request.GET.get('insert-abv')
    nickname = request.GET.get('insert-nickname')
    year_found = request.GET.get('insert-year-founded')
    city = request.GET.get('insert-city')
    arena = request.GET.get('insert-arena')
    capacity = request.GET.get('insert-arena-capacity')
    owner = request.GET.get('insert-owner')
    general_manager = request.GET.get('insert-general-manager')
    head_coach = request.GET.get('insert-head-coach')
    d_league = request.GET.get('insert-d-league')

    input = {
        'league_id': league_id,
        'team_id': team_id,
        'min_year': min_year,
        'max_year': max_year,
        'abbreviation': abb,
        'nickname': nickname,
        'yearfounded': year_found,
        'city': city,
        'arena': arena,
        'arenacapacity': capacity,
        'owner': owner,
        'generalmanager': general_manager,
        'headcoach': head_coach,
        'dleagueaffiliation': d_league,
    }
    utils.insertTeamData(input)

    return render(request, 'index.html')


def insert_games_details(request):
    return render(request, 'insert_options_game.html')


def insert_new_games_details(request):
    game_id = request.GET.get('insert_game_id')
    team_id = request.GET.get('insert_team_id')
    team_abbreviation = request.GET.get('insert_team_abv')
    team_city = request.GET.get('insert_team_city')
    player_id = request.GET.get('insert_player_id')
    player_name = request.GET.get('insert_player_name')
    start_position = request.GET.get('insert_start_position')
    comment = request.GET.get('insert_comment')
    min = request.GET.get('insert_min')
    fgm = request.GET.get('insert_fgm')
    fga = request.GET.get('insert_fga')
    fg_pct = request.GET.get('insert_fg_pct')
    fg3m = request.GET.get('insert_fg3m')
    fg3a = request.GET.get('insert_fg3a')
    fg3_pct = request.GET.get('insert_fg3_pct')
    ftm = request.GET.get('insert_ftm')
    fta = request.GET.get('insert_fta')
    ft_pct = request.GET.get('insert_ft_pct')
    oreb = request.GET.get('insert_oreb')
    dreb = request.GET.get('insert_dreb')
    reb = request.GET.get('insert_reb')
    ast = request.GET.get('insert_ast')
    stl = request.GET.get('insert_stl')
    blk = request.GET.get('insert_blk')
    to = request.GET.get('insert_to')
    pf = request.GET.get('insert_pf')
    pts = request.GET.get('insert_pts')
    plus_minus = request.GET.get('insert_plus_minus')

    input = {
        'game_id': game_id,
        'team_id': team_id,
        'team_abbreviation': team_abbreviation,
        'team_city': team_city,
        'player_id': player_id,
        'player_name': player_name,
        'start_position': start_position,
        'comment': comment,
        'min': min,
        'fgm': fgm,
        'fga': fga,
        'fg_pct': fg_pct,
        'fg3m': fg3m,
        'fg3a': fg3a,
        'fg3_pct': fg3_pct,
        'ftm': ftm,
        'fta': fta,
        'ft_pct': ft_pct,
        'oreb': oreb,
        'dreb': dreb,
        'reb': reb,
        'ast': ast,
        'stl': stl,
        'blk': blk,
        'to': to,
        'pf': pf,
        'pts': pts,
        'plus_minus': plus_minus,
    }
    utils.insertGamesDetailsData(input)

    return render(request, 'index.html')


def insert_ranking(request):
    return render(request, 'insert_options_ranking.html')


def insert_new_ranking(request):
    team_id = request.GET.get('insert-team-id')
    league_id = '00'
    season_id = '2' + request.GET.get('insert-season-id')
    standingsdate = request.GET.get('insert-standingsdate')
    conference = request.GET.get('insert-conference')
    team = request.GET.get('insert-team')
    g = request.GET.get('insert-g')
    w = request.GET.get('insert-w')
    l = request.GET.get('insert-l')
    w_pct = str(float(g) / float(w))
    home_record = request.GET.get('insert-home_record')
    road_record = request.GET.get('insert-road_record')
    returntoplay = '0'

    input = {
        'team_id': team_id,
        'league_id': league_id,
        'season_id': season_id,
        'standings_date': standingsdate,
        'conference': conference,
        'team': team,
        'g': g,
        'w': w,
        'l': l,
        'w_pct': w_pct,
        'home_record': home_record,
        'road_record': road_record,
        'returntoplay': returntoplay,
    }

    utils.insertRankingData(input)
    return render(request, 'index.html')


#  *** Delete functions ***
# render delete_options page when the delete button is clicked in the homepage
def delete(request):
    # load the delete options page if user clicks delete
    return render(request, 'delete_options.html')
# render delete_options_players page when the delete player button is clicked in the delete_options
def delete_player(request):
    return render(request, 'delete_options_players.html')
# user entered a player name to delete, we have to delete it from our database with util.deletePlayerData()
def delete_player_info(request):
    print('Delete Player request received.')
    # get the player user wants to delete
    player = request.GET.get('delete_player')
    # pass player name to utils so we can delete
    utils.deletePlayerData(player)
    return render(request, 'index.html')

def delete_team(request):
    return render(request, 'delete_options_team.html')

def delete_team_info(request):
    print('Delete Team request received.')
    # get the team user wants to delete
    team = request.GET.get('delete_team')
    # pass team name to utils so we can delete
    utils.deleteTeamData(team)
    return render(request, 'index.html')


#  *** Update functions ***
def update(request):
    return render(request, 'update_options.html')

def update_player(request):
    return render(request, 'update_options_players.html')

def update_options_players(request):
    print('Update player request received.')
    # get the player user wants to delete
    player = request.GET.get('update_player')
    team_id = request.GET.get('update_team_id')
    items = [player,team_id]
    # pass player name to utils so we can delete
    utils.updatePlayerData(items)
    return render(request, 'index.html')

def update_team(request):
    return render(request, 'update_options_team.html')

def update_options_team(request):
    print('Update team request received.')
    # get the team owner user wants to update
    team = request.GET.get('update_team')
    owner = request.GET.get('update_owner')
    items = [team,owner]
    # pass player name to utils so we can delete
    utils.updateTeamData(items)
    return render(request, 'index.html')


def update_player_pts(request):
    return render(request, 'update_options_player_pts.html')

def update_options_player_pts(request):
    print('Update options player points received')
    season = request.GET.get('season')
    player = request.GET.get('player_name')
    points = request.GET.get('points_scored')
    points = float(points)

    utils.updatePlayerPoints(season, player, points)
    return render(request, 'index.html')


def update_team_wins(request):
    return render(request, 'update_options_team_wins.html')

# update_options_team_wins will update the amount of wins a team has for a specific season
def update_options_team_wins(request):
    print('Update team wins request received.')
    # get what the user entered for team and season in the
    # update_options_team.html.
    team = request.GET.get('team')
    season = request.GET.get('season')
    # add '2' to the front to season so it matches .csv data
    # ex: 2009 is represented as 22019 in our data
    season = '2'+season
    # get the new number amount of wins to replace old
    # ex: switching a team's total wins from 70 to 80 wins
    wins = request.GET.get('wins')
    team_data = [team,season, wins]


    utils.updateTeamWinsData(team_data)

    utils.changesInWins()


    return render(request, 'analytics_options_top5.html')




# *** Analytics functions***
def analytics(request):
    return render(request, 'analytics_options.html')


def top5_win(request):
    return render(request, 'analytics_options_top5.html')


def top_5_win_lookup(request):
    print('Analyze top 5 win % request received.')
    season = request.GET.get('season')
    # print("here we are ************")
    season = '2' + season
    context = utils.analyzeTop5Wins(season)
    print(context)
    return render(request, 'display_top5_stat.html', context)


def player_stat(request):
    return render(request, 'analytics_options_players.html')


def player_stat_lookup(request):
    print('Analyze Player Stat request received.')
    # get the player and stat user wants to lookup
    player = request.GET.get('player')
    stat = request.GET.get('stat')
    items = [player,stat]
    # pass player name to utils so we can delete
    context = utils.analyzePlayerStat(items)

    print("**********")
    test = context['3_pt_avg']
    test = test[0]

    print(test['game_id'])
    print("**********")
    return render(request, 'display_player_stat.html', context)


def home_team_stat(request):
    return render(request, 'analytics_options_team.html')

def home_team_stat_lookup(request):
    print('Analyze Team Stat request received.')
    # get the team user wants to lookup
    season = request.GET.get('season')
    stat = request.GET.get('stat')
    season_stat = [season, stat]
    # pass player name to utils so we can delete
    context = utils.analyzeTeamStat(season_stat)

    print("**********")
    print(context)
    print("**********")
    return render(request, 'display_team_stat.html', context )

#
def top_season_scorer(request):
    return render(request, 'analytics_top_season_scorer.html')



def top_season_scorer_lookup(request):
    print('Analyze Top Scorer request received.')
    # get the team user wants to lookup
    user_season = request.GET.get('season')
    user_team = request.GET.get('team')

    sorted_games_details = []

    top_scorers_sorted = utils.checkIfDataSortedByPoints()

    if top_scorers_sorted == False:
        all_teams = utils.getAllTeamNames()
        all_seasons = [*range(2009, 2020, 1)]
        all_team_abbreviations = []


        # Get all of the team_id so we can organize our games_details by team.
        # I want to see if this will cut our runtime
        for team in all_teams:
            team_id = utils.getTeamID(team)
            team_abbreviation = utils.getTeamAbbreviation(team_id)
            all_team_abbreviations.append(team_abbreviation)

        # sort games_details by team
        utils.sortGamesDetailsByTeam(all_team_abbreviations)

        # CONTINUE HERE
        for team in all_teams:
            # print(team)
            # use team to get team_id from teams.csv
            team_id = utils.getTeamID(team)
            # print(team_id)
            for season in all_seasons:
                season = str(season)
                # get players on the team by using team_id and season
                team_roster = utils.getTeamRoster(team_id, season)
                # get games played using season and team_id
                games_played = utils.getGamesPlayed(season, team_id)
                # get player names based on team_roster
                player_names = utils.getPlayerNames(team_roster)
                points_scored = [0] * len(team_roster)
                sorted_games_details.append({'season': season,
                                             'team_id': team_id,
                                             'team_roster': team_roster,
                                             'game_id': games_played,
                                             'player_names': player_names,
                                             'points_scored': points_scored,
                })

    # use team to get team_id from teams.csv
    team_id = utils.getTeamID(user_team)
    # get top scores for the season
    top_scorer = utils.analyzeTopScorer(team_id, user_season,sorted_games_details)

    print("**********")
    print(top_scorer)
    print("**********")
    print()

    return render(request, 'display_top_scorer.html', top_scorer)


# Compare two players
def compare_two_players(request):
    return render(request, 'analytics_compare_players.html')

def compare_two_players_lookup(request):
    print('Analyze Compare Two Players request received.')
    # get the player and stat user wants to lookup
    player1 = request.GET.get('player1')
    player2 = request.GET.get('player2')
    stat = request.GET.get('stat')

    items = [player1, player2, stat]
    # pass player name to utils so we can delete
    context = utils.analyzeComparePlayers(items)

    print("**********")
    print(context)
    print("**********")

    return render(request, 'display_compare_players.html', context)



# display data from analyze
def display_player_stat(request):
    print("")

def display_team_stat(request):
    print("")



#  *** Backup functions ***
# backups data for each csv
def backup(request):
    print('Backup request received.')
    if request.method == 'GET':
        if(request.GET.get('backup-players') == 'players'):
            utils.backupData('players')
        if(request.GET.get('backup-ranking') == 'ranking'):
            utils.backupData('ranking')
        if(request.GET.get('backup-games-details') == 'games-details'):
            utils.backupData('games-details')
        if(request.GET.get('backup-teams') == 'teams'):
            utils.backupData('teams')

    return render(request, 'index.html')

# css test
def cssPages(request):
    return render(request, 'config/pages/static/css/style.css')

# search test
def searchPage(request):
    return render(request, 'search.html')

def searchCityPage(request):
    return render(request, 'searchCity.html')

def searchPlayerPage(request):
    return render(request, 'searchPlayer.html')

def searchTeamPage(request):
    return render(request, 'searchTeam.html')

def searchGameDetails(request):
    return render(request, 'searchGameDetails.html')


# home page test
def home(request):
    return render(request, 'index.html')

# #backup / import
def backup(request):
    return render(request, 'backupPage.html')

#  *** Backup functions ***
# backups data for each csv
def backupFunction(request):
    print('Backup request received.')
    if request.method == 'GET':
        if(request.GET.get('backup-players') == 'players'):
            utils.backupData('players')
        if(request.GET.get('backup-ranking') == 'ranking'):
            utils.backupData('ranking')
        if(request.GET.get('backup-games-details') == 'games-details'):
            utils.backupData('games-details')
        if(request.GET.get('backup-teams') == 'teams'):
            utils.backupData('teams')

    return render(request, 'index.html')


def importPage(request):
    return render(request, 'importPage.html')