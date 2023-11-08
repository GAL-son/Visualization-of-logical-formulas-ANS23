class Clause:

    def __init__(self, variables, name):
        self.variables = []
        self.name= 'C'
        for varialbe in variables:
            self.variables.append(varialbe)
            self.name = name
    def __str__(self):
        str_=self.name+" Variables:"
        for i in self.variables:

            str_+=str(i)+" "
        return str_;



# test = Clause(['-1', '-2', '3','4'],'c1')
# print(test)