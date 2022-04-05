from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    # homepage paths
    path('', views.homePageView, name='index'),
    path('search_all', views.search_all, name='search_all'),
    path('search_city', views.search_city, name='search_city'),
    path('search_player', views.search_player, name='search_player'),
    path('search_team', views.search_team, name='search_team'),
    path('search_team_id', views.search_team_id, name='search_team_id'),

    #insert paths
    path('insert', views.insert, name='insert'),
    path('insert_player', views.insert_player, name='insert_player'),
    path('insert_new_player', views.insert_new_player, name='insert_new_player'),
    path('insert_team', views.insert_team, name='insert_team'),
    path('insert_new_team', views.insert_new_team, name='insert_new_team'),
    path('insert_games_details', views.insert_games_details, name='insert_games_details'),
    path('insert_new_games_details', views.insert_new_games_details, name='insert_new_games_details'),
    path('insert_ranking', views.insert_ranking, name='insert_ranking'),
    path('insert_new_ranking', views.insert_new_ranking, name='insert_new_ranking'),

    # delete paths
    path('delete', views.delete, name='delete'),
    path('delete_player', views.delete_player, name='delete_player'),
    path('delete_player_info', views.delete_player_info, name='delete_player_info'),
    path('delete_team', views.delete_team, name='delete_team'),
    path('delete_team_info', views.delete_team_info, name='delete_team_info'),

    # update paths
    path('update', views.update, name='update'),
    path('update_player', views.update_player, name='update_player'),
    path('update_options_players', views.update_options_players, name='update_options_players'),
    path('update_team', views.update_team, name='update_team'),
    path('update_options_team', views.update_options_team, name='update_options_team'),
    path('update_player_pts', views.update_player_pts, name='update_player_pts'),
    path('update_options_player_pts', views.update_options_player_pts, name='update_options_player_pts'),
    path('update_team_wins', views.update_team_wins, name='update_team_wins'),
    path('update_options_team_wins', views.update_options_team_wins, name='update_options_team_wins'),

    #backup
    path('backup', views.backup, name='backup'),
    path('backupFunction', views.backupFunction, name='backupFunction'),

    # analyze paths
    path('analytics', views.analytics, name='analytics'),
    path('top5_win_pct', views.top5_win, name='top5_win_pct'),
    path('top_5_win_lookup', views.top_5_win_lookup, name='top_5_win_lookup'),
    path('player_stat', views.player_stat, name='player_stat'),
    path('player_stat_lookup', views.player_stat_lookup, name='player_stat_lookup'),
    path('home_team_stat', views.home_team_stat, name='home_team_stat'),
    path('home_team_stat_lookup', views.home_team_stat_lookup, name='home_team_stat_lookup'),

    path('top_season_scorer', views.top_season_scorer, name='top_season_scorer'),
    path('top_season_scorer_lookup', views.top_season_scorer_lookup, name='top_season_scorer_lookup'),

    path('compare_two_players', views.compare_two_players, name='compare_two_players'),
    path('compare_two_players_lookup', views.compare_two_players_lookup, name='compare_two_players_lookup'),


    path('index.', views.home_team_stat_lookup, name='home_team_stat_lookup'),

    # css test
    path('cssPages', views.cssPages, name='cssPages'),

    # search paths
    path('searchPage', views.searchPage, name='searchPage'),
    path('searchCityPage', views.searchCityPage, name='searchCityPage'),
    path('searchPlayerPage', views.searchPlayerPage, name='searchPlayerPage'),
    path('searchTeamPage', views.searchTeamPage, name='searchTeamPage'),
    path('searchGameDetails', views.searchGameDetails, name='searchGameDetails'),

    path('home', views.home, name='home'),

    # backup / import
    path('backup', views.backup, name='backup'),
    path('importPage', views.importPage, name='importPage'),

]
