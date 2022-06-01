import json
import xlsxwriter
import random

passing_params = ["playerId", "teamName", "playedPositions", "positionText", "rating", "totalPassesPerGame", "accurateCrossesPerGame", "accurateCrossesPerGame", "accurateLongPassPerGame", "accurateThroughBallPerGame", "passSuccess"]
summary_params = ["name"]
offensive_params = ["goal", "assistTotal", "shotsPerGame", "keyPassPerGame", "dribbleWonPerGame", "foulGivenPerGame", "offsideGivenPerGame", "dispossessedPerGame", "turnoverPerGame"]
defensive_params = ["apps", "subOn", "minsPlayed", "tacklePerGame", "interceptionPerGame", "foulsPerGame", "offsideWonPerGame", "clearancePerGame", "wasDribbledPerGame", "outfielderBlockPerGame", "goalOwn"]
detailed_params = ["shotSixYardBox", "shotPenaltyArea", "shotOboxTotal", "shotsTotal"]

player_listId = []
players = 0
row = 0
column = 0

workbook = xlsxwriter.Workbook('database.xlsx')
worksheet = workbook.add_worksheet()

# ------------------PASSING------------------
passing_file = open('passing.json', encoding="utf8")
passing_database = json.load(passing_file)
list_passing = passing_database['playerTableStats']

for passing_parameter in passing_params:
    worksheet.write(row, column, passing_parameter)
    row += 1
    for player_passing_parameter in list_passing:
        if passing_parameter == "playerId":
            players += 1
            player_listId.append(player_passing_parameter[passing_parameter])
        worksheet.write(row, column, player_passing_parameter[passing_parameter])
        row += 1
    column += 1
    row = 0

passing_file.close()

# ------------------SUMMARY------------------
summary_file = open('summary.json', encoding="utf8")
summary_database = json.load(summary_file)
list_summary = summary_database['playerTableStats']

for summary_parameter in summary_params:
    worksheet.write(row, column, summary_parameter)
    row += 1
    for player_summary_parameter in list_summary:
        if player_summary_parameter["playerId"] in player_listId:
            worksheet.write(row, column, player_summary_parameter[summary_parameter])
            row += 1
    column += 1
    row = 0

summary_file.close()

# ------------------OFFENSIVE------------------
offensive_file = open('offensive.json', encoding="utf8")
offensive_database = json.load(offensive_file)
list_offensive = offensive_database['playerTableStats']

for offensive_parameter in offensive_params:
    worksheet.write(row, column, offensive_parameter)
    row += 1
    for player_offensive_parameter in list_offensive:
        if player_offensive_parameter["playerId"] in player_listId:
            worksheet.write(row, column, player_offensive_parameter[offensive_parameter])
            row += 1
    column += 1
    row = 0

offensive_file.close()

# ------------------DEFENSIVE------------------
defensive_file = open('defensive.json', encoding="utf8")
defensive_database = json.load(defensive_file)
list_defensive = defensive_database['playerTableStats']

for defensive_parameter in defensive_params:
    worksheet.write(row, column, defensive_parameter)
    row += 1
    for player_defensive_parameter in list_defensive:
        if player_defensive_parameter["playerId"] in player_listId:
            worksheet.write(row, column, player_defensive_parameter[defensive_parameter])
            row += 1
    column += 1
    row = 0

defensive_file.close()

# ------------------DETAILED------------------
detailed_file = open('detailed.json', encoding="utf8")
detailed_database = json.load(detailed_file)
list_detailed = detailed_database['playerTableStats']

for detailed_parameter in detailed_params:
    worksheet.write(row, column, detailed_parameter)
    row += 1
    for player_detailed_parameter in list_detailed:
        if player_detailed_parameter["playerId"] in player_listId:
            worksheet.write(row, column, player_detailed_parameter[detailed_parameter])
            row += 1
    column += 1
    row = 0

detailed_file.close()

# ------------------VALUE------------------
worksheet.write(row, column, "value")
row += 1
for player in range(players):
    worksheet.write(row, column, round(random.uniform(0.1, 99.9), 2))
    row += 1
workbook.close()