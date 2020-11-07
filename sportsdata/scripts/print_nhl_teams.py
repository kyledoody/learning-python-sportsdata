from sportsdata.nhl import get_nhl_team_names


def main():
    for name in get_nhl_team_names():
        print(name)


# Allow the file to be run as a standalone script
# See https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    main()
