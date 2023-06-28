#first exercise: my interpretation of classes, a parent class Person and two subclasses : Adult and Child
class Person:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __str__(self):
        return '<Person named {}>'.format(self.name)
    
    def eat(self,food):
        print("{} likes to eat {} ".format(self.name, food))

class Child(Person):
    def __init__(self, name, age, hobby):        
        super().__init__(name, age, hobby)
        if self.age >= 18:
            raise ValueError('This is not a child!')

    def school(self, number_class):
        if number_class < 1 and number_class > 8:
            raise ValueError('Does not {} visit a school?'.format(self.name))
        else:
            print("{} is in {}th class".format(self.name, number_class))

    def go_to_bed(self):
        return '{} goes in bed at 9 PM'.format(self.name)
    
class Adult(Person):
    def __init__(self, name, age, hobby):        
        super().__init__(name, age, hobby)
        if self.age < 18:
             raise ValueError('This is not an Adult')
      
    def work(self, profession):
        print('{} works as {}'.format(self.name, profession))
    
    def go_to_bed(self):
        return '{} goes in bed at 11 PM'.format(self.name)

    
marian = Adult('Marian', 41, 'playing chess')
mihaela = Child('Mihaela', 17, 'playing Heroes')

marian.work("software engineer")
mihaela.school(7)

persons = [marian, mihaela]
for person in persons:
    person.eat('pasta and ice cream')
    print(person.go_to_bed())



# the Sample Topic from homework lecture 12:

class Board_Game():
    """Board Game
    has properties:
    - name - mandatory
    - play time
    - number of players min
    - number of players max
    - from age
    - year first published
    - number of times played
    has methods:
    - __str__ - print the name
    - __init__ - accepts arguments for each property and sets them
    - play(num_people, expected_fun_duration, min_age)"""
    def __init__(self, 
                 name : str, 
                 play_time:int = 60, 
                 min_players:int = 0, 
                 max_players:int = 10, 
                 age_limit:int = 0, 
                 year_published:int = 1900, 
                 count_games:int = 0):
        self.name = name
        self.play_time = play_time
        self.min_players = min_players
        self.max_players = max_players
        self.age_limit = age_limit
        self.year_published = year_published
        self.count_games = count_games

    def __str__(self):
        return '<The game you are playing is {}>'.format(self.name)
    
    def play(self, num_people : int, expected_fun_duration : int, min_age : int):
        if num_people <= self.min_players:
            print('To few players!')
            return False
        if num_people >= self.max_players:
            print('Too many players!')
            return False
        if expected_fun_duration > self.play_time:
            print('Too long game!')
            return False
        if min_age < self.age_limit:
            print('The player is too young!')
            return False
        self.count_games += 1
        print(f'Well, you played one more game. Good job! You already have {self.count_games}  games')
        return True


'''Wargame
- has a new property: violence_level (low/medium/high)
- implements its own play() method printing a more in depth story about how the game
would be played based on the violence_level if the original conditions of the play()
method of the parent class are met - it returns True.
'''

class Wargame(Board_Game):
    def __init__(self, 
                 name, 
                 violence_level,
                 play_time:int = 60, 
                 min_players:int = 0, 
                 max_players:int = 10, 
                 age_limit:int = 12,    #I am changing the default value of age_limit
                 year_published:int = 1900, 
                 count_games:int = 0,
                ):
        if age_limit < 12 :
            raise ValueError('You are too young to play War game! ')
        
        if not violence_level in ['low', 'medium', 'high']:
            raise ValueError('You have to choose between "low", "medium" or "high" violence level')
        
        self.violence_level = violence_level
        super().__init__(name, play_time, min_players, max_players, age_limit, year_published, count_games)

    def play(self, num_people : int, expected_fun_duration : int, min_age : int):
        if self.violence_level == 'high' and min_age < 18:
            print('You can not play a high violence game because you are under 18 years old!')
            return False
        return super().play(num_people, expected_fun_duration, min_age)
        
'''Eurogame has new properties:
- figures_material with following allowed options: cardboard, wood, plastic, metal,
None
- has a new method campfire_allowed() checking and printing if you can safely play
the board game next to a campfire based on the material of the play figures'''

class Eurogame(Board_Game):
    def __init__(self, 
                 name, 
                 figures_material = None,
                 play_time:int = 60, 
                 min_players:int = 0, 
                 max_players:int = 10, 
                 age_limit:int = 0,    
                 year_published:int = 1900, 
                 count_games:int = 0,
                ):
        if not figures_material in  ['cardboard', 'wood', 'plastic', 'metal', None]:
            print ('You have to choose between \'cardboard\', \'wood\', \'plastic\' and \'metal\'')
        self.figures_material = figures_material
        super().__init__(name, play_time, min_players, max_players, age_limit, year_published, count_games)

    def campfire_allowed(self):
        if self.figures_material in ['metal', None]:
            print ('You can play around the fire:)')
            return True
        print('hmm, your game maybe will not survive around the fire')
        return False
    

memoir_44 = Wargame('Memoir 44', 'high', 120, 2 ,6, 17, 2014, 0)
print(memoir_44)
print (memoir_44.play(4, 90, 15) )
print(memoir_44.count_games)
print (memoir_44.play(4, 90, 19) )
print (memoir_44.play(3, 100, 35) )

ticket_to_ride = Eurogame('Ticket to Ride', 'plastic', 130, 2,9, year_published= 2000, count_games= 0)

print(ticket_to_ride)
print (ticket_to_ride.play(4, 90, 15) )
print(ticket_to_ride.count_games)
print(ticket_to_ride.campfire_allowed())
print (ticket_to_ride.play(4, 90, 19) )
print (ticket_to_ride.play(1, 100, 35) )
            