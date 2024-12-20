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