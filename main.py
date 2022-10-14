from random import randint
import art
import game_data 

print(art.logo)

#Select random position
def select_random_position(data):
  position=randint(0, len(data))  
  return position

#Retrieving data
def retrieve_data(data, random_position):
  return (f"{data[random_position]['name']}, {data[random_position]['description']}, {data[random_position]['country']}")
  
#Returning number of followers  
def retrieve_followers (data, random_position):
  followers=data[random_position]['follower_count']
  return followers
  
#Comparison
def compare_followers (compare_a, compare_b):
  if compare_a > compare_b:
    return 'A'
  else:
    return 'B'

#Game start
def play_game():
  #Compare A
  position_random_a=select_random_position(game_data.data)
  compare_a=retrieve_data(game_data.data, position_random_a)
  print (f"Compare A: {compare_a}")
  
  print(art.vs)
  
  #Compare B
  position_random_b=select_random_position(game_data.data)
  compare_b=retrieve_data(game_data.data, position_random_b)
  print (f"Against B: {compare_b}")
  
  followers_a=retrieve_followers(game_data.data, position_random_a)
  followers_b=retrieve_followers(game_data.data, position_random_b)

  has_more_followers=compare_followers(followers_a, followers_b)
  
  score=0
  continue_playing=True
  
  while continue_playing!=False:
    player_choice=input("Who has more followers? Type 'A' or 'B': ")
    if has_more_followers==player_choice:
      score+=1
      print(f"You are right. Current score: {score}")
      compare_a=compare_b
      print (f"Compare A: {compare_a}")
      compare_b=retrieve_data(game_data.data, select_random_position(game_data.data))
      print (f"Against B: {compare_b}")
      continue_playing=True

    else:
      print (f"Sorry, that's wrong. Final score: {score}")
      continue_playing=False
play_game()


