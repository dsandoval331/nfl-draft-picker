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

    def __init__(self, name, score=0, place="tbd", file=None):
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
    all_instances = []

    def __init__(self, id, first_name, last_name, college, classification, position, position_rank, height, weight):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.college = college
        self.classification = classification
        self.position = position
        self.position_rank = position_rank
        self.height = height
        self.weight = weight
        Draftee.all_instances.append(self)

    def __repr__(self):
        """
        Defines the 'computer string' representation of the object.
        This is useful for debugging and printing the list of objects.
        """
        return f"Draftee(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', college='{self.college}', classification='{self.classification}', position='{self.position}', position_rank={self.position_rank}, height={self.height}, weight={self.weight})"

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
      my_players_list = []
      print(f"\nSetting up {player_count} players for the league...")
      for i in range(1, int(player_count) + 1):
          print(f"\nEnter the name of player {i}:")
          player_name = input()
          new_player = Player(player_name, 0, "N/A")
          # my_players_list.append(new_player)
          print(f"Player {i} named {player_name} has been added to the league.")
          print(f"Testing: {Player.all_instances}")
      return my_players_list
      
def setup_draft(draft_type, player):
      if draft_type.lower() == "offline":
          players_draftee_list = []
          print("\nSetting up an offline draft...")
          print(f"Setting up draft for player: {player.name}...")
          print(f"What is name of {player.name}'s file with results:")
          player.file = input()
          players_draftee_list = import_draftees(player.file)
          return players_draftee_list
      else:
          print("\nOnline draft setup is currently under development. Please check back later.")

def import_draftees(file):
        print(f"\nImporting draftees from file: {file}")
        draftees_list = []
        try:
            with open(file, 'r') as f:
                for line in f:
                    print (f":{line}")
                    data = line.split(',')
                    print(f"Len(data) is: {len(data)}")
                    print(f"Data: {data}")
                    if len(data) == 9:  # Ensure there are enough fields
                        draftee = Draftee(
                            id=int(data[0]),
                            first_name=data[1],
                            last_name=data[2],
                            college=data[3],
                            classification=data[4],
                            position=data[5],
                            position_rank=int(data[6]),
                            height=(data[7]),
                            weight=int(data[8])
                        )
                        draftees_list.append(draftee)
        except FileNotFoundError:
            print(f"Error: File '{file}' not found. Please ensure the file is in the correct location.")
        print("Draftees imported successfully!\n")
        return draftees_list    
       

def intro():
        print("\nWelcome to the NFL Draft Fantasy Pick'em game!")
        print("In this game, you'll make fantasy picks for the NFL Draft.") 
        print("Good luck!\n")

def calculate_scores(plyr_draftee_list, master_draftee_list, scoring_system, rnds):
        points = 1
        streak = 0
        print("\nCalculating scores... (functionality to be implemented)\n")
        print(f"Player's draftee list: {plyr_draftee_list}")
        print(f"The league's scoring system is: {scoring_system}")
        # Score calculation logic will be based on the league's scoring system and the performance of each draftee in the player's list
        score = 0
        #for draftee in plyr_draftee_list:
            #score += draftee.position_rank  # Example scoring logic
        #print(f"Player's calculated score: {score}")

        for obj1, obj2 in zip(plyr_draftee_list, master_draftee_list):
            if obj1.id == obj2.id:
                print(f"Objects with IDs {obj1.id} and {obj2.id} are equal.")
                if scoring_system == "standard with bonuses":
                    streak += 1
                    score = score + points + (streak - 1) # Example scoring logic for a correct match
                else:
                    score += points  # Example scoring logic for a correct match without bonuses
                print(f"Score updated to: {score}")
            else:
                print(f"Objects with IDs {obj1.id} and {obj2.id} are not equal.")
                streak = 0  # Reset streak on a mismatch
            points += 1
        return score


def display_results():
        print("\nHere are the final scores:\n")
        sorted_results = sorted(Player.all_instances, key=lambda player: player.score, reverse=True)
        i = 1
        for player in sorted_results:
            print(f"{player.name}: {player.score} points - Place: {i}")
            i += 1

def outro():
        print("\nThanks for playing the NFL Draft Fantasy Pick'em game!\n")

def main():
        intro()
        league = setup_league_settings()
        players_list = setup_players(league.players)
        #setup_draft(league.draft_type)
        file = 'output_data.txt'
        draftees_list = import_draftees(file)

        for draftee in draftees_list:
             print(f"Draftee ID: {draftee.id}, Name: {draftee.first_name} {draftee.last_name}, College: {draftee.college}, Classification: {draftee.classification}, Position: {draftee.position}, Position Rank: {draftee.position_rank}, Height: {draftee.height} inches, Weight: {draftee.weight} lbs")
             print("hmmm")
        print(f"Testing: {players_list}")
        for player in Player.all_instances:
             plyr_draftee_list = []
             plyr_draftee_list = setup_draft(league.draft_type, player)
             player.score = calculate_scores(plyr_draftee_list, draftees_list, league.scoring_system, league.rounds)
             
        display_results()
        outro()
        print("testing")
        #print(Draftee.all_instances)
        print("end testing")

main()