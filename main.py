class Greetings():
    def __init__(self , name , lname) -> None:
        self.name = name
        self.lname = lname
        if self.revisit_check() == True:
            self.revisit()
        else:
            self.visit()

    def revisit_check(self):
        name_check = self.name + ' ' + self.lname
        with open('names.txt', 'r') as file:
            for line in file:
                if name_check in line:
                    self.num = int(line[-2])
                    return True
        return False
    
    def visit(self):
        print('Nice to meet you! Welcome to my first git oriented programming!')
        line = self.name + ' ' + self.lname + ' 1\n' 
        with open('names.txt', 'a') as file:
            file.write(line)

    def revisit(self):
        self.num += 1
        print("Welcome back {}! You've been here {} Tiems!".format(self.name , self.visits_Num()))

        with open('names.txt', 'r') as file:
            lines = file.readlines()

        for i in range(len(lines)):
            if self.name + ' ' + self.lname in lines[i]:
                lines[i] = self.name + ' ' + self.lname + ' ' + str(self.num) + '\n'

        with open('names.txt', 'w') as file:
            file.writelines(lines)


    def visits_Num(self):
        return self.num
    
name = input('Whats your name ?')
lname = input('Whats your last name ?')
name_greet = Greetings(name , lname)