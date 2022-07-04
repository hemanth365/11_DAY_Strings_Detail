# -------------------capitalize()---------------
# a="hello python world"
# print(a.capitalize())

# b="this Is Business"
# print(b.capitalize())

# c="python plays a KEY role"
# print(c.capitalize())

# d="123 python"
# print(d.capitalize())     # No change as it has numeric value at starting of the statement

# -------------casefold()--------------------

# a="Python Is a Interpreted Language"
# print(a.casefold())


# b="PYTHON IS A KEY LANGUAGE"
# print(b.casefold())

# c="456758 PYTHON"
# print(c.casefold())

# --------------------------lower()-----------------

# a="Hello World"
# print(a.lower())

# b="HELLO PYTHON"
# print(b.lower())

# c="HELLO WORLD 125469872"
# print(c.lower())

# ------------------islower()--------------------------
 
# a="hello world"
# print(a.islower())


# b="Hello World"
# print(b.islower())


# c="hello World"
# print(c.islower())

# d="123 hello python"
# print(d.islower())


# ------------------------upper()--------------

# a="today is monday"
# print(a.upper())

# b="Tomorrow is Tuesday"
# print(b.upper())

# c="python"
# print(c.upper())


# ----------------------isupper()------------------

# a="Hello world"
# print(a.isupper())

# b="HeLLO WORLD"
# print(b.isupper())

# c="HELLO WORLD"
# print(c.isupper())

# ------------------count()---------------

# a='''johnny johnny yes papa'''
# print(a.count('h'))
# print(a.count('n'))
# print(a.count('p'))
# print(a.count('johnny'))


# b="dacjkhfvuayfhuyehndkjncnjvhhfvnjjnwjc"
# print(b.count('h'))
# print(b.count('c'))
# print(b.count('f'))
# print(b.count('hh'))
# print(b.count('y'))


# ---------------endswith()-----------------


# a="www.google.com"
# print(a.endswith('m'))
# print(a.endswith('om'))
# print(a.endswith('com'))
# print(a.endswith('google'))


# b="youtube.com/INDIA"
# print(b.endswith('a'))       # CASE SENSITIVE
# print(b.endswith('INDIA'))      
# print(b.endswith('com'))       
# print(b.endswith('youtube'))       
# print(b.endswith('A'))     

# ------------------find()-------------------

# a='Hello World'
# print(a.find('l'))
# print(a.find('o'))
# print(a.find('r'))
# print(a.find('world'))
# print(a.find('ll'))

# b='HI_PYTHON_123'
# print(b.find('_'))
# print(b.find('123'))
# print(b.find('1'))
# print(b.find('PYTHON'))    # It is starting from the index value (3)
# print(b.find('H'))


# -----------------------index()---------------

# a='Hello World'
# print(a.index('W'))
# print(a.index('World'))
# print(a.index('Hello'))
# print(a.index('H'))
# print(a.index('l'))

# b='hi_python'
# print(b.index('i'))
# print(b.index('_'))
# print(b.index('python'))
# print(b.index('n'))

# ------------------title()-----------------------

# a="hey this is python"
# print(a.title())

# b='Hey there is an ambush'
# print(b.title())

# c='123-abc'
# print(c.title())


# ----------------------zfill()-----------------

# a='hello'
# print(a.zfill(10))
# print(a.zfill(20))


# b='hello world'
# print(b.zfill(15))             # Space is counted 
# print(b.zfill(5))               
# print(b.zfill(8))


# ---------------------join()--------------------

# a=""
# print(a.join("Iam a learner"))

# b="-"
# print(b.join('Iam a learner'))

# c='_'
# print(c.join('Iam','a','learner'))      # TYPE ERROR IT TAKES ONLY ONE ARGUMENT

# d='_'
# print(d.join('bubblegum'))


# -----------------------startswith()--------------

# a="www.google.com"
# print(a.startswith('w'))
# print(a.startswith('www'))
# print(a.startswith('W'))               # Case Sensitive
# print(a.startswith('com'))

# b="Youtube.com"
# print(b.startswith('y'))  
# print(b.startswith('youtube'))  
# print(b.startswith('com'))  
# print(b.startswith('YOUTUBE'))  
# print(b.startswith('Yo'))  
# print(b.startswith('Youtube.com'))  


# ----------------------replace()---------------------

# a='apple banana'
# print(a.replace('banana','kiwi'))

# b="Hello World!"
# print(b.replace('Hello','Hi'))

# c='apple banana orange mango'
# print(c.replace('orange','pineapple'))


# -----------------strip()------------------------

# a='  hello world!  '
# print(a.strip())

# b="!!! THIS IS PYTHON !!!"
# print(b.strip('!'))
# print(b.strip(' '))
# print(b.strip('! '))

# ---------------------split()-----------------------

# a="This is my World!!"
# print(a.split())
# print(a.split(maxsplit=1))
# print(a.split(maxsplit=2))


# b="THIS WORLD BELONGS TO ME"
# print(b.split())
# print(b.split(maxsplit=1))
# print(b.split(maxsplit=2))
# print(b.split(maxsplit=3))


# ------------------------swapcase()--------------------

# a="Hello pyThon"
# print(a.swapcase())

# b="HELLO WORLD !!!"
# print(b.swapcase())

# c="hello world !!!"
# print(c.swapcase())

# d="hElLo PyThOn"
# print(d.swapcase())

# --------------------isidentifier()--------------

print('hemanth'.isidentifier())
print('@123_'.isidentifier())
print('fight_23'.isidentifier())
print('2254865'.isidentifier())
print('_22458hng'.isidentifier())
print('goole.com'.isidentifier())
print('hero_21'.isidentifier())
print('_23456'.isidentifier())
print('.hiinnt'.isidentifier())
print('5874.66'.isidentifier())
print('Hemanth@123'.isidentifier())
print('_signal_problem_@'.isidentifier())


















































































































