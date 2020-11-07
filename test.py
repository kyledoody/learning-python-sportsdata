from sportsdata.nhl import get_nhl_teams, get_nhl_team_names, print_names_as_grid
import json

# name = "Kyle"
# data = f"You're the man {name} but, it's too bad you're so stupid"
# name = "Chris"
# data_1 = f"I'm going to count to four, if you don't stop being an asshole I'll start calling you {name}"
# data_2 = f"fuck you {name}"
#
# print(data)
# print(data_1)
#
# def function():
#     print(1, 2, 3, 4)
#
# function()
# print(data_2)
#
# print(get_nhl_teams())
# data = get_nhl_teams()
# text = json.dumps(data, indent=2)
# print(text)
# print(data["copyright"])
# print(data["teams"][0]["teamName"])
# for team in data["teams"]:
#     print(team["teamName"])

# print(get_nhl_team_names())

# # Matrix
# teamnames = get_nhl_team_names()
# #
# # for i, name in enumerate(teamnames):
# #     print(name, end=", ")
# #     if i % 4 == 0:
# #         print()
#
# maxname = ""
# for name in teamnames:
#     if len(name) > len(maxname):
#         maxname = name
# print(maxname)
# width = len(maxname) + 2
# print(width)
#
# for i, name in enumerate(teamnames):
#     if i < len(teamnames) - 1:
#         name = name + ","
#     name = name.ljust(width)
#     print(name, end="")
#     if i % 4 == 3:
#         print()

print_names_as_grid()
