import clause
import variables


class Statement:

    def __init__(self, DIMACS):
        self.clauses = []
        self.variables = []
        self.counter = 1
        self.supplementary = ''
        self.clause_supplementary = []
        self.variables_already_existing = []
        self.DIMACS = DIMACS
        self.zeroNumFlag = 0

        for sign in DIMACS:
            # print(sign)
            if sign == '0':
                if self.zeroNumFlag == 0:
                    # print(["sent"]+self.clause_supplementary)
                    self.clauses.append(clause.Clause(self.clause_supplementary, ("C" + str(self.counter))))

                    self.clause_supplementary = []
                    self.counter += 1
                if self.zeroNumFlag ==1:
                    self.supplementary += sign
                    self.zeroNumFlag = 1

            # print("znaleziono 0")
            else:
                if sign in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
                    self.supplementary += sign
                    self.zeroNumFlag = 1
                    # print("znaleziono cyfre lub -")
                else:
                    if sign == ' ':
                        self.zeroNumFlag = 0
                        if self.supplementary != '':
                            self.clause_supplementary.append(self.supplementary)
                            modlal = abs(int(self.supplementary))
                            if modlal not in self.variables_already_existing:
                                self.variables_already_existing += [modlal]
                                self.variables.append(variables.Variable(modlal, ("C" + str(self.counter))))
                            else:
                                for i in self.variables:
                                    if i.name == modlal:
                                        i.appendClause(("C" + str(self.counter)))
                        # print(self.clause_supplementary + [" status"])
                        # print(self.supplementary + " added")
                        self.supplementary = ''


test = Statement("-1 -2 3 4 0 -1 -2 3 4 0 3 4 -5 -6 0 1 7 8 -9 0 1 2 3 -4 0 10 -10 0")
print("whole statement: " + test.DIMACS)

for i in test.clauses:
    print(i)

print(test.variables_already_existing)
for i in test.variables:
    print(i)
