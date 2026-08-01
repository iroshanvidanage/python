import subprocess
import argparse

from debugging_cards import Deck

class GameOver(Exception):
    ''' An exception raised when the player is out of money.
    '''

class Player:
    def __init__(self) -> None:
        self.money = 1_000
        self.cards = []

def prompt_for_bet(money: int) -> int:
    try:
        return abs(int(input(f"How much of your ${money} would you like to wager? ")))
    except ValueError:
        print('Your bet must be an integer. Example: 42')
        # remove the return keyword and try first with a string value.
        return prompt_for_bet(money)
    except:
        raise

def score(cards) -> int:
    ''' Calculate the score for the set of cards.

        Create some cards to use for testing the score.
        >>> _k = Card('♠', 'K')
        >>> _a = Card('♠', 'A')
        >>> _2 = Card('♠', '2')
        >>> _3 = Card('♠', '3')
        >>> _5 = Card('♠', '5')

        >>> assert score([_k, _a]) == 21
        >>> assert score([_k, _a, _a]) == 12
        >>> assert score([_2, _3, _5]) == 10

        ♥, ♠, ♦, ♣
    '''
    # Create a point value lookup using a dictionary.
    # Aces can be used as either a 1 or an 11.
    # This lookup sets the default as 11.
    scores = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    # Calculate the score assuming the ace is 11.
    score = sum([scores[card.rank] for card in cards]) or 0

    # Adjust the score if needed to allow aces to be used as 1.
    for card in cards:
        # If the score is greater than 21 and at least one of the
        # cards is an ace then we can turn the ace into a
        # 1 by subtracting 10 from the score
        if score > 21 and card.rank == 'A':
            score -= 10
    return score

def format_winner(winner: str) -> str:
    ''' Format the message displayed to the winner and return the str. '''
    winner = f'{winner.title() } wins!'
    winner = f'{winner:@^80}' # center text
    return winner

def format_cards(player: Player, dealer: Player) -> str:
    ''' Displays the cards for the player and dealer. '''
    cards = f'{"dealer":-^80}\n'
    cards += f'{" ".join([str(card) for card in dealer.cards])}\n'
    cards = f'{"player":-^80}\n'
    cards += f'{" ".join([str(card) for card in player.cards])}\n'
    cards += f'{"total: {}".format(score(player.cards)): ^80}'
    return cards

def clear_screen() -> None:
    ''' Clear the terminal screen using either cls on Windows otherwise clear.

        The double pipe operator || on Linux and Windows is used to
        attempt the first command and fallback to the second.

        So cls||clear attempts cls and is a non-zero status code is returned clear is attempted.
    '''
    # os.system('cls||clear') # deprecated
    subprocess.run('cls||clear', shell=True, check=False)

def play_round(
        player: Player,
        dealer: Player,
        deck: Deck,
        action_callable: callable = input,
        bet_callable: callable = prompt_for_bet
    ):
    ''' Play a single round of blackjack.

        Args:
            player          | The player
            dealer          | The dealer
            deck            | The deck of cards to use
            action_callable | Callable to use to prompt a user for an action.
                            |> The callable must accept 1 positional str argument representing the prompt to display to a player.
                            |> The callable must return a str representing the desired action.
                            |> ------------------
                            |> | action | symbol |
                            |> ------------------
                            |> |   hit  |   h    |
                            |> |   stay |   s    |
                            |> ------------------
            bet_callable    | Callable used to prompt a user for their bet.
                            |> The callable must accept 1 positional int argument representing a player's available money.
                            |> The callable must return a positive int representing the bet.
        
        ------------------ Warning ---------------------
        This function mutates the provided arguments
        and will leave them in a non-deterministic state.
        ------------------------------------------------

        Calling this function when a player is out of money should raise a Gameover exception.
        >>> player = Player()
        >>> player.money = 0
        >>> play_round(player, Player(), Deck())
        Traceback (most resent call last):
        ...
        GameOver: Game over! You're bankrupt!

        Calling this function when a player has sufficient funds and a winning hand.
        >>> test_bet_callable = lambda n: 100
        >>> test_act_callable = lambda s: 's'
        >>> player = Player()
        >>> dealer = Player()
        >>> deck = Deck()
        >>> deck.cards = [Card('♠', 'K'), Card('♠', 'A'), Card('♥', 'K'), Card('♥', 'Q')]
        >>> play_round(player, dealer, deck, test_act_callable, test_bet_callable)
        -------------------------------------dealer---------------------------------------
        Q♥ ??
        -------------------------------------player---------------------------------------
        A♠ K♠
                                            total: 21
        -------------------------------------dealer---------------------------------------
        Q♥ K♥
        -------------------------------------player---------------------------------------
        A♠ K♠
                                            total: 21
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Player wins!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        >>> assert player.money == 1200
        
        Calling this function when a player has sufficient funds and a losing hand.
        >>> deck.cards = [Card('♠', '2'), Card('♠', 'A'), Card('♥', 'K'), Card('♥', 'Q')]
        >>> play_round(player, dealer, deck, test_act_callable, test_bet_callable)
        -------------------------------------dealer---------------------------------------
        Q♥ ??
        -------------------------------------player---------------------------------------
        A♠ 2♠
                                            total: 13
        -------------------------------------dealer---------------------------------------
        Q♥ K♥
        -------------------------------------player---------------------------------------
        A♠ 2♠
                                            total: 13
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Dealer wins!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        >>> assert player.money == 1100

        Ensure that we're not losing cards that aren't being put back in the deck after a round.
        >>> assert len(deck.cards) == 4
    '''
    # Step 1
    # Ensure the player has enough money to play. If not, game over!
    if player.money == 0:
        raise GameOver("Game over! You're bankrupt!")

    # Begin the round by resetting the clearing the player and dealer's cards.
    dealer.cards = []
    player.cards = []

    # Step 2
    # The round opens by prompting the player for a bet.
    # Until we have a bet we can't do anything else.
    # Ensure that the player has enough money to place the bet.
    while (rounds_wager := bet_callable(player.money)) > player.money:
        print(f'Please change your bet. You bet ${rounds_wager}. You only have ${player.money}.')

    # Step 3
    # Deal two cards for the dealer. One needs to be face up.
    dealer.cards = [deck.deal(), deck.deal(faceup=False)]

    # Deal two cards for the player.
    player.cards = [deck.deal() for _ in range(2)]
    clear_screen()
    print(format_cards(player, dealer))

    # Step 4
    # the player needs to determine their next action.
    # Will they hit or stay?
    # s for stay, h for hit, anything else is ignored.
    while (action := action_callable('pick your action: (h)it or (s)tay > ')) != 's':
        if action == 'h':
            # Take another card for the player
            player.cards.append(deck.deal())
            # Everytime a player's cards change we need to render the cards.
            clear_screen()
            print(format_cards(player, dealer))

    # Step 5
    # The dealer in a real game would determine for themself if they want to hit or stay.
    # We're going to create some basic rules to simulate a real person as the dealer.
    # While the score of the dealer's hand is less than 17 keep taking cards.
    while score(dealer.cards) < 17:
        dealer.cards.append(deck.deal())

    # Step 6
    # Determine who won by comparing scores.
    # If the player scored 21 then they win.
    # If the dealer scored more than 21 then player wins.
    # If the player scores higher than the dealer and they didn't go over 21 then the player wins.
    dealers_score = score(dealer.cards)
    players_score = score(player.cards)

    # Who won.....
    if (players_score == 21 or dealers_score > 21 or (players_score >= dealers_score and players_score <=21)):
        player.money += rounds_wager * 2
        winner = 'player'
    else:
        player.money -= rounds_wager
        winner = 'dealer'

    # Step 7
    # Display all the cards, including the dealer's previously hidden cards.
    # First need to make them faceup.
    for card in dealer.cards:
        card.faceup = True

    clear_screen()
    print(format_cards(player, dealer))

    # Inform the winner
    print(format_winner(winner))

    # Step 8
    # Return cards to the deck to prevent card-loss.
    # This is not how real blackjack works, but it is a good way to ensure that the deck doesn't run out of cards.
    deck.cards += dealer.cards
    deck.cards += player.cards

def play() -> None:
    ''' Continuously play until the player stops the code. '''
    player = Player()
    dealer = Player()
    deck = Deck()

    # Loop forever unless the code is interrupted by CTRL+C
    while True:
        deck.shuffle()
        play_round(player, dealer, deck)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game of blackjack.')
    parser.add_argument('--test', action='store_true', help='Run the doctests and exit.')

    if parser.parse_args().test:
        import doctest
        doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=True)
    else:
        try:
            play()
        except GameOver as e:
            print(e)
