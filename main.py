class League:
    def __init__(self, name, draft_type, players, rounds, scoring_system):
        self.name = name
        self.players = players
        self.draft_type = draft_type
        self.rounds = rounds
        self.scoring_system = scoring_system

    def display_settings(self):
        print("\nLeague Settings:\n")
        print(f"League Name: {self.name}")
        print(f"Number of Players: {self.players}")
        print(f"Draft Type: {self.draft_type}")
        print(f"Number of Rounds: {self.rounds}")
        print(f"Scoring System: {self.scoring_system}")

class Player:
    all_instances = []

    def __init__(self, name, score=0, place="tbd"):
        self.name = name
        ## Generate random number for development
        random_score = __import__('random').randint(0, 100)
        self.score = random_score
        self.place = place
        Player.all_instances.append(self)

    def __repr__(self):
        """
        Defines the 'computer string' representation of the object.
        This is useful for debugging and printing the list of objects.
        """
        return f"Player(name='{self.name}', score={self.score}, place='{self.place}')"

class Draftee:
    def __init__(self, id, name, college, classification, position, position_rank, height, weight):
        self.id = id
        self.name = name.
        self.college = college
        self.classification = classification
        self.position = position
        self.position_rank = position_rank
        self.height = height
        self.weight = weight

        def __repr__(self):
        """
        Defines the 'computer string' representation of the object.
        This is useful for debugging and printing the list of objects.
        """
        return f"Draftee(id={self.id}, name='{self.name}', college='{self.college}', classification='{self.classification}', position='{self.position}', position_rank={self.position_rank}, height={self.height}, weight={self.weight})"

def setup_league_settings():
        print("What would you like to name your league?")
        league_name = input()
        print("What type of league would you like to create? (online/offline)")
        league_draft_type = input()
        print("How many players will participate in your league?")
        league_players = input()
        print("How many rounds will the draft have?")
        league_rounds = input()
        print("What is the scoring system for your league? (standard/standard with bonuses)")
        league_scoring_system = input()
        my_league = League(league_name, league_draft_type, league_players, league_rounds, league_scoring_system)
        my_league.display_settings()
        return my_league

def setup_players(player_count):
      # my_players_list = []
      print(f"\nSetting up {player_count} players for the league...")
      for i in range(1, int(player_count) + 1):
          print(f"\nEnter the name of player {i}:")
          player_name = input()
          new_player = Player(player_name, 0, "N/A")
          # my_players_list.append(new_player)
          print(f"Player {i} named {player_name} has been added to the league.")
          print(f"Testing: {Player.all_instances}")
      #return my_players_list
      
def setup_draft(draft_type):
      if draft_type.lower() == "offline":
          print("\nSetting up an offline draft...")
      else:
          print("\nOnline draft setup is currently under development. Please check back later.")

def import_draftees():
        print("\nImporting draftees... (functionality to be implemented)\n")

def intro():
        print("\nWelcome to the NFL Draft Fantasy Pick'em game!")
        print("In this game, you'll make fantasy picks for the NFL Draft.") 
        print("Good luck!\n")

def calculate_scores():
        print("\nCalculating scores... (functionality to be implemented)\n")


def display_results():
        print("\nHere are the final scores:\n")
        #sorted_results=sorted(Player.all_instances, key=lambda x: x.score, reverse=True)
        i = 1
        for player in Player.all_instances:
            print(f"{player.name}: {player.score} points - Place: {i}")
            i += 1

def outro():
        print("\nThanks for playing the NFL Draft Fantasy Pick'em game!\n")

def main():
        intro()
        league = setup_league_settings()
        #players_list = setup_players(league.players)
        setup_draft(league.draft_type)
        import_draftees()
        calculate_scores()
        display_results()
        outro()
        print("testing")
        print(Player.all_instances)
        print("end testing")

main()