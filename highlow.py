import random 
import art
import game_data

print(art.logo)
print(" \n")
def data():
  game = random.choice(game_data.data)
  return game

def versus_title():
    #print(choice_one)
    print(choice_one["name"])
    print("has")
    print(choice_one["follower_count"])
    print("followers")
    
    print(art.vs)
    print(" \n")
    
    print(choice_two["name"])
    print("has")
    print(choice_two["follower_count"])
    print("----")
    print("followers \n")


#assigns random game data for options a & b from def data()
option_a = data()
option_b = data()
#print(option_a)
#print(option_b)

choice_one = option_a
choice_two = option_b

#versus_title()
end_game = False

score = 0

while not end_game:
    versus_title()
    #Have user guess higher or lower for choice two
    user_choice = input(f"Does have {choice_two['name']} 'Higher' or 'Lower' followers? ").lower()
    followers_one = int(choice_one["follower_count"])
    followers_two = int(choice_two["follower_count"])
    #Validate user input to check which has more followers
    if user_choice == "higher":
        if followers_two > followers_one:
            score += 1
            print(f"You Win. Your score is {score} \n")
            choice_one = choice_two
            choice_two = data()
        elif followers_two < followers_one:
            print("You Lose. Game Over your score was {score}")
            end_game = True
    elif user_choice == "lower":
        if followers_two < followers_one:
            score += 1
            print(f"You Win. Your score is {score} \n")
            choice_one = choice_two
            choice_two = data()
        elif followers_two > followers_one:
            print(f"You Lose. Game Over your score was {score}")
            end_game = True
            
            
    
    #print(option_b)
    #end_game = True
