'''
Import the randint callable from the built-in random module.
Implement the constructors for the Sparkle and Shine classes.

These must call the __init__ method of the base class.
Sparkle power is worth 2points and has an avatar of *
Shine power is worth 3points and has an avatar of #
The SuperSlothBot requires a class attribute named randint_gen_callable which must be bound to the radiant callable.

Implement the activate method of the SuperSlothBot class.

If the number argument is less than 0 or greater than 50 raise a valueError with the following message: 'number must be between 1-50'

Conditionally assign self.last_power to a Power object.

if the number argument is between 0-25 create a Sparkle object and assign it to the self.last_power.
if the number argument is between 26-50 create a Shine object and assign it to the self.last_power.

Once the last_power instance attribute is bound to the correct Power object:
Call the last power's activate method and provide the randint_gen_callable class attribute as the argument.
Return results from the call to the last_power.activate.
SuperSlothBot must run the following code when converted to a str via str(sloth).

try:
    return f'{self.name} conjours: {self.last_power.avatar} for a total of: {self.last_power.points} points.'
except:
    return 'no power is currently activated'

NOTE: 

'''


from random import randint

class Power:

    def __init__(self, points, avatar):
        self.points = points
        self.avatar = avatar
    
    def activate(self, amplifier_callable: callable = randint):
        amplifier = amplifier_callable(1, 10)

        self.avatar = ' '.join([self.avatar] * amplifier)
        self.points *= amplifier

        return self.avatar, self.points


class Sparkle(Power):
    ''' Sparkle power is worth 2points and has an avatar of * '''
    def __init__(self, points=2, avatar='*'):
        super().__init__(points, avatar)


class Shine(Power):
    ''' Shine power is worth 3points and has an avatar of # '''
    def __init__(self, points=3, avatar='#'):
        super().__init__(points, avatar)


class SuperSlothBot:

    def __init__(self, name: str):
        '''
            Args:
                name    | The name of the bot.
        '''

        self.last_power = None
        self.name = name
    
    @property
    def randint_gen_callable(self):
        ...

    def activate(self, number: int):
        '''
            Args:
                number  | A randomly generated number between 0 and 50.
            
            Goal:
                Conditionally assign self.last_power to a Power object.
                    if the number argument is between 0-25 create a Sparkle object and assign it to the self.last_power.
                    if the number argument is between 26-50 create a Shine object and assign it to the self.last_power.

                Once the last_power instance attribute is bound to the correct Power object:
                    Call the last power's activate method and provide the randint_gen_callable class attribute as the argument.
                    Return results from the call to the last_power.activate. 

            Raises:
                ValueError('number must be between 1-50')   | raised if number < 0 or number > 50
        
            >>> SuperSlothBot.randint_gen_callable = lambda *_: 5
            >>> for number in [20, 40]:
            ...     SuperSlothBot('bot 01').activate(number)
            ('* * * * *', 10)
            ('# # # # #', 15)

            >>> sloth = SuperSlothBot('bot 01')
            >>> sloth.activate(10)
            ('* * * * *', 10)

            >>> str(sloth)
            'bot 01 conjours: * * * * * for a total of: 10 points.'

            >>> SpuerSlothBot('bot 01').activate(-1)
            Traceback (most recent call last):
                ...
            ValueError: number must be between 1-50

            >>> SpuerSlothBot('bot 01').activate(101)
            Traceback (most recent call last):
                ...
            ValueError: number must be between 1-50
        '''

        try:
            if 0 <= number < 25:...
        except ValueError:
            ...


def play(rounds:int =5):
    '''
        Make bots 1 and 2 fight.

        >>> from unittest.mock import MagicMock
        >>> randint_mock = magicMock(side_effect=[40, 10, 20, 5, 20, 6, 30, 3])
        >>> SuperSlothBot.randint_gen_callable = randint_mock
        >>> play(2)

        ROUND 1, FIGHT!

        **************************************************************************************
        bot 1 conjours: * * * * * * * * * * for a total of: 30 points.
        bot 2 conjours: # # # # # for a total of: 10 points.
        **************************************************************************************
        ROUND 1, FIGHT!

        **************************************************************************************
        bot 1 conjours: * * * * * * for a total of: 12 points.
        bot 2 conjours: # # # for a total of: 9 points.
        **************************************************************************************
        ___________________________1st Place: Bot 1 with 42 Points!___________________________
        ___________________________2nd Place: Bot 2 with 19 Points!___________________________
    '''
    bots = {
        1: SuperSlothBot('bot 1'),
        2: SuperSlothBot('bot 2')
    }

    scores = {
        1: 0,
        2: 0
    }

    for round in range(rounds):
        print(f'ROUND {round + 1}, FIGHT!', end=f'\n\n{"*" * 80}\n')

        for n, bot in bots.items():
            bot.activate(SuperSlothBot.randint_gen_callable(0, 50))
            scores[n] += bot.last_power.points

        print(*[str(bot) for bot in bots.values()], sep='\n')
        print('*' * 80)
    
    # Sort by score descending.
    winners = sorted(scores.items(), key=lambda _tuple: _tuple[1], reverse=True)
    one, two = winners

    # For the sake of this application ties are not handled. If there's a tie, one of these bots is going to get mad!
    print(f'''{
        ''.join(('1st', f' place: {bots[one[0]].name} with {scores[one[0]]} points!'.title())):_^80
        }
    ''')
    print(f'''{
        ''.join(('2st', f' place: {bots[two[0]].name} with {scores[two[0]]} points!'.title())):_^80
        }
    ''')