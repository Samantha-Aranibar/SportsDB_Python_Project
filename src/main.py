from sportsdb.project import SportsDBClient

def print_team(team: dict):
    print("\n--- Team Info ---")
    print("Team Name:    ", team.get("strTeam", "N/A"))
    print("Country:    ", team.get("strCountry","N/A"))
    print("League:    ",team.get("strLeague","N/A"))
    print("Stadium:    ",team.get("strStadium","N/A"))

def main():
    client = SportsDBClient()

    team_name = input("Enter a soccer team name:  ").strip()

    if not team_name:
        print("No team name entered!")
        return
    data = client.search_team(team_name)
    teams = data.get("teams")

    if not teams:
        print("No teams found.")
        return
    
    print_team(teams[0])

if __name__ == "__main__":
    main()

