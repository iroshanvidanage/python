# list comprehensions
list_example = []
for num in range(5):
    list_example.append(num)

# same can be styled as follows
list_example2 = [num for num in range(5)] 

persons = ['iroshan', 'shihan', 'hanni', 'dani', 'minji']
persons = [person.title() for person in persons]
print(persons)

suit = ['h', 'd', 's', 't']
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
cards = [f'{r}{s}' for s in suit for r in rank]
print(cards)

# dict comprehensions
player_scores = {
    'player1' : 2_000,
    'player2' : 4_000,
    'player3' : 1_000,
    'player4' : 7_000
}

player_scores1 = {player: score + 10_000 for player, score in player_scores.items()}
print(player_scores1)

player_scores2 = {player.title(): score * 2 for player, score in player_scores.items() if score > 3_000}
print(player_scores2)

"""
Here the condition has en else part, but the dictionary key is the same and the conditon is there to filter the value (score)
Therefore the else statement is configured for the value only
"""
print({player.title(): score * 2 if score > 3_000 else score * 3 for player, score in player_scores.items()})

# set comprehensions
people_to_know = ['iroshan', 'shihan', 'hanni', 'dani', 'minji', 'Hanni']

# this will remove duplicates and sort the list
print({person.title() for person in people_to_know})