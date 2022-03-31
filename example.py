celcius = [0,10,20,30,32.1, 34.2]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]

fahrenheit
[32.0, 50.0, 68.0, 86.0, 89.78, 93.56]

fahrenheit = []
for temp in celcius:
    fahrenheit.append(( (9/5)*temp + 32))

    results = [x if x%2==0 else 'ODD' for x in range (0,11)]

odd
   [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

   mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
    mylist.append(x*y)

    help(mylist) = [x*y for x in[2,4,6] for y in [100,200,300]]

    mylist
    [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

    def name_of_function():

        def say_hello():
    print("hello")
    print('are')
    print('you')

    def say_hello(name):
    print(f'Hello {name}')

    say_hello('Zbyszek')

    def print_result(a,b):
    print(a+b)

    def return_result(a,b):
    return a+b

    def myfunc(a,b):
    print(a+b)
    return a+b
result = myfunc(12,41)
53

def even_check(number):
    result =number % 2 == 0
    return result
    even_check(13)
        false

        def even_check(number):
    return number % 2 == 0

    def chech_even_list(num_list):
    # zwróć true jeżeli któryś z numerów jest parzysty wewnątrz listy
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False\\def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False



 def myfunc(a,b,c=0,d=,0,e=0):
    # zwraca pięć procent z sumy a i b
    return sum((a,b)) * 0.05
    
    myfunc(31,12)



def myfunc(*args):
    return sum(args) * 0.05

    myfunc(12,31,413,31,123,12,1,1,1,1,)
    31,3


    def myfunc(*args):
    print(args)

def myfunc(*args):
    a=list(args)
    for num in a:
        if num%2==0:
            return [num for num in args if num%2==0]
def myfunc(*args):
    for item in args:
        print(item)
myfunc(1,2,3,4,5)

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I didnt fint any fruit here')

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I didnt fint any fruit here')

myfunc(fruit='apple', veggie = 'lettuce', drink = 'lemoniade')
    My fruit of choice is apple

ef myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I wolud like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange', food='eggs',animal='dog')
myfunc(10,20,30,fruit='orange', food='eggs',animal='dog')
(10, 20, 30)
{'fruit': 'orange', 'food': 'eggs', 'animal': 'dog'}
I wolud like 10 eggs




example = [1,2,3,4,5,6,7]
from random import shuffle
result = shuffle(example)
example
[2, 7, 3, 5, 6, 4, 1]


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
result
[6, 2, 3, 7, 4, 5, 1]

mylist = [' ', 'O', ' ']
shuffle_list(mylist)
[' ', ' ', 'O']

def player_guess():
    
    guess=''  # Gracz musi zgadnąć gdzie jest kulka. Zaczynamy od pustych podejrzeń
    
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1, or 2")
        
    return int(guess)

    (dodajemy ten warunek, aby gracz został zmuszony do wybrania właściwej opcji)
player_guess()
Pick a number: 0,1, or 23
Pick a number: 0,1, or 21
1

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("You win")
    else:
        print("You lose")
        print(mylist)


 # 1.Początkowa lista do wyboru
mylist = [ ' ','O',' '] # lista jest 3 składowym ciągiem 
    
 # 2.Uporządkuj listę, abyś mógł z niej korzystać. (1 funkcja)
mixedup_list = shuffle_list(mylist)

 # 3. Opisz wybór gracza (2 funkcja)
guess = player_guess()
    
 # 4.Sprawdź czy wybór jest poprawny (3 funkcja)
check_guess(mixedup_list,guess) # tutaj funkcje zaczynają ze sobą współdziałać. 

def myfunc(*args):
    a=list(args)
    for num in a:
        if num%2==0:
            return [num for num in args if num%2==0]

 def lesset_of_two_evens(a,b):  

    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return(b)
        elif a < b:
            return(a)   
    elif a % 2 != 0 and b % 2 != 0:
        if a > b:
            return(a)
        elif a < b:
            return(b)


def makes_twenty(a,b):
    if a + b == 20:
        return(True)
    elif a + b != 20:
        return(False)

def animal_crackers(string):
    s1, s2 = string.split()
    if s1[0] == s2[0]:
        return(True)
    elif s1[0] != s2[0]:
        return(False)
    #return(s1, s2)

animal_crackers('Kuna Lovegood')


def old_macdonald(name):
    first_letter = name [0] #potrzebujemy pierwszej litery, oznaczamy ją zero
    inbetween = name[1:3] # litery pośrednie pomiędzy tymi co nas interesują
    fourth_letter = name[3] # nasza czwarta litera
    rest = name[4:] # wiadomo o co chodzi
    #a teraz zobaczmy czy to działa
    #return first_letter. + inbetween + fourth_letter + rest #(działa)
    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

    def old_macdonald(name):
    first_half = name[:3] # część Mac
    second_half = name[3:] # część donald
    return first_half.capitalize() + second_half.capitalize()

    def master_yoda(text):
    wordlist = text.split() #to czego potrzebujemy musi być równe podzielonej liście
    reversed = wordlist[::-1] #pamiętasz to z konkatenacji. Tym sposobem odwracamy sobie ciąg.nadamy też jej nową zmienną
    return reversed

def master_yoda(text):
    wordlist = text.split() #to czego potrzebujemy musi być równe podzielonej liście
    reversed = wordlist[::-1] #pamiętasz to z konkatenacji. Tym sposobem odwracamy sobie ciąg.nadamy też jej nową zmienną
    
    return ' '.join(reversed)

return '1234'.join(reversed)

 master_yoda('Jan Stefan Bambaryła')     
'Bambaryła1234Stefan1234Jan'

def almost_there(n):
    
    # return abs(100-n) <= 10 # a więc teraz sprawdzamy czy 100 minus nasze n jest mniejsze bądź równe 10
     return (abs(100-n) <= 10) or (abs(200-n) <=10)


     def has_33(nums):
    
    for i in range(0,len(nums)-1): # aby to wykonać potrzebujemy następującej logiki od 0 do długości parametru minus 1
        if nums[i] == 3 and nums[i+1] ==3: # i teraz warunek, stosunkowo proste. Jeżeli pierwsza i druga liczba są ok
            return True
    return False

    def has_33(nums):
    
    for i in range(0,len(nums)-1): # aby to wykonać potrzebujemy następującej logiki od 0 do długości parametru minus 1
        if nums[i:i+2] ==[3,3]: # Wersja druga z wykorzystaniem krojenia.
            return True
    return False

    def paper_doll(text):
    result='' #sprawa nie będzie skomplikowana, jeżeli zorientujesz się że trzeba zacząć od pustego ciągu
    
    for character in text:
        result += character*3 
        ## lub result += character + charachter + character
    return result
     def paper_doll(text):
    result='' #sprawa nie będzie skomplikowana, jeżeli zorientujesz się że trzeba zacząć od pustego ciągu
    
    paper_doll('Zbyszkowno')
    'ZZZbbbyyyssszzzkkkooowwwnnnooo'

    def blackjack(a,b,c):
    
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif a == 11 or b == 11 or c == 11 <=31 :
    ## elif 11 in [a,b,c] and sum ([a,b,c]) <=31:
        return sum([a,b,c]) - 10
    elif sum([a,b,c]) >= 21:
        return('BUST')


def summer_69(arr):
    
    total = 0 # suma na początku wynosi zero. Musimy to uwzględnić
    add = True # oraz warunek, który musimy spełnić
    
    for num in arr: ## tworzymy więc funkcję w naszej Macierzy
        while add:  # nasza pętla, wykonująca się do momentu, kiedy spełniony zostanie warunek.
            if num!= 6: # jeśli numer nie jest równy 6
                total += num # total plus num
                break # konieczny warunek do zakończenia funkcju
            else:
                add = False # Jeż
        while not add: # jeżeli add nie jest równe do  
            if num != 9: # 
                break
            else:
                add = True
                break
    return total


summer_69([2, 1, 6, 7, 9, 11, ])
14

summer_69([2, 1, 6, 7, 9, 11, 7])
21


def spy_game(nums):
    
    # sposób pierwszy. Zrobimy zewnętrzny kod 007, a następnie przepuścimy przez niego listę, przez każdy kolejny element
    code =[0,0,7, 'x']
    
    for num in nums:
        if num == code[0]: # jeśli mój aktualny numer jest równy
            code.pop(0)
# oznacza to tyle, że za każdym razem sprawdzamy, czy ten numer jest równy do pierwszego numeru w iteracji.
# tak? To następna iteracja kodu wygląda już tak:
# [0,7, 'x'], a potem
#[ 7, 'x'] a potem,
# ['x'] do momentu aż długość ciągu = 1
# a więc nasz długośc naszego kodu musi być równa == 1
            
    return len(code) == 1
    

    def scuare(num):
    return num**2

    my_nums = [1,2,3,4,5]


map(square, my_nums)
<map at 0x18160a8c7c8>

for item in map(square, my_nums):
    print (item)

    list(map(square,my_nums))
    [1, 4, 9, 16, 25]

    def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Zbyszek'

        names = ['Andrzej', 'Jan', 'Zbigniew']

        list(map( splicer,names))
        ['A', 'J', 'Zbyszek']

def check_even(num):
    return num%2 == 0

 mynums = [1,2,3,4,5,6,7,8,9,10]

 filter(check_even,mynums)
<filter at 0x18160b6de88>

list(filter(check_even,mynums))

for n in filter(check_even,mynums):
    print(n)

    def square(num):
    result = num ** 2
    return result

    def square(num):
    return num ** 2

    def square(num): return num ** 2

    lambda num: num ** 2

    square = lambda num: num ** 2


    ##
    list(map(lambda num:num**2,mynums))
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    def check_even(num):
    return num%2 == 0

    list(filter(lambda num:num%2 == 0,mynums))
    [2, 4, 6, 8, 10]

    x = 25
def printer():
    x = 50
    return x

    print(x) ==> 25

    print(printer()) ==> 50

    ## zmienna NAME jest zdefiniowana dwa razy raz, globalnie, a dwa lokalnie
name = 'To jest ciąg globalnym zasięgiem obdarzony' 

def greet(): # nasza główna funkcja, ustala ona nazwę zmiennej na Sammie
    
    name = 'Sammie' # zmienna o charakterze lokalnym działająca wewnątrz tej funkcji
    
    def hello(): # wewnątrz tej funkcji hello drukujemy Hello oraz imię
        print('Hello ' + name)
    hello()    

greet() ==> Hello Sammie


## zmienna NAME jest zdefiniowana dwa razy raz, globalnie, a dwa lokalnie
name = 'To jest ciąg globalnym zasięgiem obdarzony' 

def greet(): # nasza główna funkcja, ustala ona nazwę zmiennej na Sammie
    
   # name = 'Sammie' # zmienna o charakterze lokalnym działająca wewnątrz tej funkcji
    
    def hello(): # wewnątrz tej funkcji hello drukujemy Hello oraz imię
        print('Hello ' + name)
    hello()    

    Hello To jest ciąg globalnym zasięgiem obdarzony

    # Zasięg globalny
name = 'To jest ciąg globalnym zasięgiem obdarzony' 

def greet(): 
    
    name = 'Sammie' # zasięg Wewnętrzny ENCLOSING
    
    def hello(): 
        name = 'Jestem lokalnego zasięgu'#zasięg lokalny
        print('Hello ' + name)
        
    hello()    
    
greet()

Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

    x = 50

def func(x):
    print(f'X is {x}')

func(x)


    x = 50

def func(x):
    print(f'X is {x}')
    # lokalne 
    x = 200 
    print (f'Właśnie lokalnie zmieniłem swoje zdanie. X to {x}')
func(x)
X is 50
 Właśnie lokalnie zmieniłem swoje zdanie. X to 200

 print(x)
 50

print([1,2,3])
print([4,5,6])
print([7,8,9])
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
 

 def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

    example_row = [1,2,3]

display(example_row,example_row,example_row)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

display(row1,row2,row3)

[' ',' ',' ']
[' ','X',' ']
[' ',' ',' ']



row2[1] = 'X'

result = input("Enter a number: ")
Enter a number: 
#ta komórka nie zadziała dopóki nie wprowadzimy powyżej danych
2+2


def user_choice():
    #Najpierw potrzebujemy kilku zmiennych
    
    # Początek
    choice='WRONG'
    
    #Musimy określić jaki jest zakres danych, które będą akceptowalne. Z użyciem funkcji Range. Ważny jest też warunek False
    acceptable_range = range (0-10)
    within_range = False
    
    # Następny krok to sprawdzenie warunków
    #Dwóch 1. To czy to jest faktycznie liczba,
    # oraz czy faktycznie jest w zasięgu funkcji
       
    while choice.isdigit() == False or within_range==False:
    
        choice = input("Please enter a number(0-10): ")
        
     #Kontrola poprawności zapisu
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
    # Kontrola poprawności zasięgu
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("You are out of acceptable range (0-10)")
                within_range = False
    return int(choice)


game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list")
    print(game_list)

display_game(game_list)

Here is the current list: 
[0, 1, 2]

def position_choice():
        #prosta funkcja na temat wyboru pozycji,
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2):")
        
        if choice not in ['0','1','2']:
            print("Sorry, wrong choice")
    return int(choice)

position_choice()

def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list

replacement_choice(game_list,1)

Type a string to place at position: 3
[0, '3', 2]


def gameon_choice():
    
    #Oryginalny wybór powinien być pomiędzy Y lub N
    
    choice = 'wrong'
    
    #gdy wybór nie jest DIGITem, dalej pytaj o wejściową
    
    while choice not in['Y','N']:
        
        #Teraz nie możemy tego skonwertować, Inaczej wyskoczy nam błąd o złych danych wejściowych.
        
        choice = input("Would you like to keep playng? (Y or N)")
        
        if choice not in ['Y', 'N']:
            #Teraz czyścimy aktualne dane wyjściowe zanim 
         
            
            print("Sorry, i didnt understand. Please make sure to choose Y or N")
            
            
    #Opcjonalnie można wyczyścić zbędny kod kiedy już funkcja ruszy
    
    if choice == "Y":
        #Gra działa dalej
        return True
    else:
        #Gra nie działa
        return False

#check
gameon_choice()
Would you like to keep playng? (Y or N)daw
Sorry, i didnt understand. Please make sure to choose Y or N
Would you like to keep playng? (Y or N)daw
Sorry, i didnt understand. Please make sure to choose Y or N
Would you like to keep playng? (Y or N)Y
True

game_on = True
game_list = [0,1,2]

while game_on == True:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list, position)
    
    display_game(game_list)
    
    game_on == gameon_choice()

    class Sample():
    pass

my_sample = Sample()

class Dog():
    
    def _init_(self,breed)

    type(my_dog)
    ->__main__.Dog

    my_dog.breed
    ->'Sheepdog'

    class Dog():
    my_dog = Dog(breed='Lab', name='Zbyszek', spots=False)
    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        
        # oczekuję, że boolean = True/False
        self.spots = spots

class Dog():
    
    species = 'mammal'
    
    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        
        # oczekuję, że boolean = True/False
        self.spots = spots

     my_dog.bark
        <bound method Dog.bark of <__main__.Dog object at 0x000001858539EE48>>

    my_dog.bark()
        Woof!
        class Dog():
    
    species = 'mammal'
    
    
    
    
    def __init__(self,breed,name):
        
        self.breed = breed
        self.name = name
        #tworzymy metodę
    def bark(self):
        print("Woof! My name is {}.format()")

         def __init__(self,breed,name):
        
        self.breed = breed
        self.name = name
        #tworzymy metodę
    def bark(self):
        print("Woof! My name is {}".format(self.name))

        Woof! My name is Andżej
           
    def __init__(self,breed,name):
        
        self.breed = breed
        self.name = name
        #tworzymy metodę
    def bark(self,number):
        print("Woof! My name is {}and the number is{}".format(self.name,number))

class Circle():
    
    #Atrybut obiektu klasy
    
    pi = 3.14
    
    def __init__(self,radius=1): #domyślna wartość dla RADIUS to 1
        
        self.radius = radius
        self.area = radius*radius*self.pi
        #PIr2 - na pole koła mamy wzór
        
        #Metoda
    def get_circumference(self): #obwód koła 
        #odrobina matematyki
        return self.radius * self.pi * 2
    #2PIr -> obwód koła

    my_circle = Circle()

    my_circle.pi
    -> 3.14

    my_circle.radius
    -> 1

    my_circle.get_circumference()
    -> 6.28

 my_circle = Circle(30)

    my_circle.radius
    -> 30

    my_circle.get_circumference()
    -> 188.4

    my_circle.area #bez nawiasów
    -> 2826.0


class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")

class Dog(Animal):

myanimal = Animal()
-> Animal Created

myanimal.eat()
I am eating

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

mydog = Dog()
Animal Created
Dog Created

mydog.eat()
I am eating

myanimal.who_am_i()

class Dog():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says woof"

class Cat():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says meow"


niko = Dog("niko")
felix = Cat("Felix")

print(niko.speak())
->niko says woof

print(felix.speak())
->Felix says meow

for pet_class in [niko,felix]:
    print(type(pet_class))
    print(pet_class.speak())

<class '__main__.Dog'>
niko says woof
<class '__main__.Cat'>
Felix says meow


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
->niko says woof
pet_speak(felix)
->niko says woof


class Animal():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotInplementedError("Subclass must implement this abstract method")

    myanimal.speak()

    class Dog(Animal):
    
    def speak(self):
        return self.name + " Says woof!"

    class Cat(Animal):
    
    def speak(self):
        return self.name + " Says meow!"

fido = Dog("fidon")
->fidon Says woof!

ISIS = Cat("Isis")
->Isis Says meow!

class Book:
    
    def __init__ (self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages


b = Book('Python rzondzi', 'Bob', 2137)

print(b) or str(b)
-><__main__.Book object at 0x000001858519BC48>

class Book:
    
    def __init__ (self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages


    
    def __str__(self):
        return f"{self.title} by {self.author} by {self.pages}"

        print(b) or str(b)

'Python rzondzi by Bob by 2137'

class Book:
    
    [...]
    
    def __str__(self):
        return f"{self.title} by {self.author} by {self.pages}"
    
    def __len__(self):
        return self.pages

len(b)
->2137


del b

b
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-161-89e6c98d9288> in <module>
----> 1 b

NameError: name 'b' is not defined


class Book:
    
    def __init__ (self,title,author,pages):
     [..]
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("Objekt książka został usunięty")


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return ((x2-x1)**2 + (y2 - y1)**2)**0.5
    
    def slope(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return (y2-y1) / (x2-x1)



coor1 = (3,2)
coor2 = (8,10)

myline = Line(coor1,coor2)

myline.distance()
->9.433981132056603

myline.slope()
->1.6

class Account:
    
    def __init__ (self,owner,balance = 0):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner is: {self.owner}\nThe current balance is: {self.balance}$'


    def deposit(self,depo):
       
        self.balance += depo
        
        print("Deposit accepted")
        
        
        
    def withdraw (self,wdraw):
           
        if self.balance >= wdraw:
            self.balance -=wdraw
            print("Whithdrawal accepted")

        
        elif self.balance < wdraw:
            
            print("Funds Unavalible!")
        