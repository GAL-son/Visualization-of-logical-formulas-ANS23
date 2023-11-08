class Variable:
    def __init__(self,name_,clause_):
        self.name=name_
        self.clausulesUsing=[clause_]
    def appendClause(self,clause_):
       self.clausulesUsing.append(clause_)
    def __str__(self):
        str_="variable "+str(self.name)+" is part of clausules:"
        for i in self.clausulesUsing:
            str_+=i+" "
        return str_
