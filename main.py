class Greetings():
    def __init__(self , name , lname) -> None:
        self.name = name
        self.lname = lname
        if self.revisit_check() == True:
            self.revisit()
        else:
            self.visit()

    def revisit_check(self):
        return False
    
    def visit(self):
        print('Nice to meet you! Welcome to my first git oriented programming!')

    def revisit(self):
        print("Welcome back {}! You've been here {} Tiems!".format(self.name , self.visits_Num()))

    def visits_Num(self):
        return 1
    
name = input('Whats your name ?')
lname = input('Whats your last name ?')
name_greet = Greetings(name , lname)