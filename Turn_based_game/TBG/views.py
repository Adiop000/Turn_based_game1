from django.shortcuts import render, redirect
import random
import time

# Game variables
AVAILABLE_MOVES = {
    1: {"name": "Fireball", "type": "damage", "damage_range": (18, 25)},
    2: {"name": "Conflagrate", "type": "damage", "damage_range": (10, 35)},
    3: {"name": "Renew", "type": "heal", "heal_amount": (18, 25)},
}


def index(request):
    """Landing page for the game."""
    return render(request, 'TBG/game.html')


def play_game(request):
    """Main game logic."""
    if request.method == 'POST':
        # Retrieve health values and user move from POST data
        user_health = int(request.POST['user_health'])
        computer_health = int(request.POST['computer_health'])
        user_move = int(request.POST['user_move'])

        # Process user move
        move = AVAILABLE_MOVES[user_move]
        if move["type"] == "damage":
            damage = random.randint(*move["damage_range"])
            computer_health -= damage
            result_message = f"You used {move['name']}! It dealt {damage} damage."
        elif move["type"] == "heal":
            heal = random.randint(*move["heal_amount"])
            user_health += heal
            result_message = f"You used {move['name']}! You healed {heal} health."

        # Check if computer is defeated
        if computer_health <= 0:
            return redirect('game_result')

        # Computer's turn
        computer_move = random.choice(list(AVAILABLE_MOVES.keys()))
        move = AVAILABLE_MOVES[computer_move]
        if move["type"] == "damage":
            damage = random.randint(*move["damage_range"])
            user_health -= damage
            computer_message = f"The computer used {move['name']}! It dealt {damage} damage."
        elif move["type"] == "heal":
            heal = random.randint(*move["heal_amount"])
            computer_health += heal
            computer_message = f"The computer used {move['name']}! It healed {heal} health."

        # Render the updated game state
        return render(request, 'TBG/game.html', {
            'user_health': user_health,
            'computer_health': computer_health,
            'result_message': result_message,
            'computer_message': computer_message,
        })

    # Initial health values
    return render(request, 'TBG/game.html', {
        'user_health': 100,
        'computer_health': 100,
    })


def result(request):
    """Game result page."""
    return render(request, 'TBG/result.html')
