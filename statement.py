import clause
import variables


class Statement:

    def __init__(self, DIMACS):
        self.clauses = []
        self.variables = []
        self.counter = 1
        self.clause_supplementary = []
        self.variables_already_existing = []
        self.DIMACS = DIMACS
        self.zeroNumFlag = 0
        self.Connections=[]
        self.lastVariable=0




        numericalDimacs=[int(s) for s in DIMACS.split() if s.isdigit() or  s[0] =='-' ]

        for i in numericalDimacs:
            if abs(i)>self.lastVariable:
                self.lastVariable=abs(i)
                #print(self.lastVariable)

        for i in range(1,self.lastVariable+1):
            self.variables.append(variables.Variable("C" + str(i)))

        for number in numericalDimacs:
            #print(number)
            if number == 0:
                # print(["sent"]+self.clause_supplementary)
                self.clauses.append(clause.Clause(self.clause_supplementary, ("C" + str(self.counter))))
                self.clause_supplementary = []
                self.counter += 1
                #print("znaleziono 0")
            else:
                self.clause_supplementary.append(number)
                modlal = abs(number)
                #print("accesing index:" + str(modlal))
                self.variables[modlal-1].appendClause("C" + str(self.counter))
    def int(self):
        print("kszz")
        for i in self.clauses:
            #print(i)
            for n in self.clauses:
                if i.name!=n.name:
                    print(n.variables)
                   # print("aaa")
                    intesrection=list(set(i.variables).intersection(n.variables))
                    print(str(i.name)+"connects with "+str(n.name)+"by variables: "+ str(intesrection))

        print("kszz")





