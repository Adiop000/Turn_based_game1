from django.shortcuts import render
import random

def game_view(request):
    # Initialize default values for the game state
    user_health = 100
    opponent_health = 100
    round_number = 1
    log = []  # Log for actions
    result = ""

    # If this is a POST request, retrieve the game state from the form
    if request.method == "POST":
        user_health = int(request.POST.get('user_health'))
        opponent_health = int(request.POST.get('opponent_health'))
        round_number = int(request.POST.get('round_number'))
        log = eval(request.POST.get('log'))  # Convert log back to a Python list

        # Get the user's move
        user_move = int(request.POST.get('user_move'))

        # Define available moves
        available_moves = {
            1: {"name": "Fireball", "type": "damage", "damage_range": (18, 25)},
            2: {"name": "Conflagrate", "type": "damage", "damage_range": (5, 50)},
            3: {"name": "Psychic Strike", "type": "damage", "damage_range": (10, 20)},
        }

        # User's turn
        move = available_moves[user_move]
        if move["type"] == "damage":
            damage = random.randint(*move["damage_range"])
            opponent_health -= damage
            log.append(f"You used {move['name']} and dealt {damage} damage to the opponent.")

        # Opponent's turn (AI logic)
        if opponent_health > 0:  # Only allow the opponent to attack if they are still alive
            opponent_move = random.choice(list(available_moves.keys()))
            move = available_moves[opponent_move]
            if move["type"] == "damage":
                damage = random.randint(*move["damage_range"])
                user_health -= damage
                log.append(f"The opponent used {move['name']} and dealt {damage} damage to you.")

        # Increment the round number
        round_number += 1

    # Check for game over
    game_over = False
    if user_health <= 0:
        game_over = True
        result = "You have been defeated!"
    elif opponent_health <= 0:
        game_over = True
        result = "You won!"

    # Pass all necessary information to the template
    return render(request, 'TBG/game.html', {
        'user_health': user_health,
        'opponent_health': opponent_health,
        'log': log,
        'game_over': game_over,
        'result': result,
        'round_number': round_number,
    })
