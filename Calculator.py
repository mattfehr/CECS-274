import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
import re



class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList) #ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for char in s:
            if char == "(":
                stack.add(0,char)
            if char == ")":
                if not stack:
                    return False
                else:
                    stack.remove(0)
        if stack:
            return False
        else:
            return True
        

    def _build_parse_tree(self, exp: str) -> str:
        if self.matched_expression(exp) == False:
            return ValueError
        tokens = []
        i = 0
        exp = exp.replace(" ", "")
        while i < len(exp):
            current_token = ""
            if exp[i].isalnum() == False:
                current_token = exp[i]
                tokens.append(current_token)
                i += 1
                continue
            while exp[i].isalnum() == True:
                current_token += exp[i]
                i += 1
            tokens.append(current_token)
        t = BinaryTree.BinaryTree()
        t.r = t.Node()
        current = t.r
        for token in tokens:
            node = t.Node()
            if token == "(":
                current = current.insert_left(node)
            elif token =="+" or token == "-" or token =="*" or token =="/":
                current.set_key(token)
                current.set_val(token)
                current = current.insert_right(node)
            elif token.isalnum():
                current.set_val(float(self.dict.find(token)))
                current.set_key(token)
                current = current.parent
            elif token == ")":
                current = current.parent
        return t     

    def _evaluate(self, u):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left != None and u.right != None:
            fn = op[u.k]
            return fn(self._evaluate(u.left), self._evaluate(u.right))
        elif u.left == None and u.right == None:
            if u.v != None:
                return u.v
            raise ValueError(f"Missing value for variable {u.k}")
        elif u.left != None:
            return self._evaluate(u.left)
        else:
            return self._evaluate(u.right)


    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)
    
    def print_expression(self, expr):
        variables = [x for x in re.split('\W+', expr) if x.isalnum()]
        everything_else = re.split('\w+', expr)
        variables.append('')
        expression = ""
        for i in range(len(variables)):
            expression += everything_else[i]
            expression += variables[i]
        for variable in variables:
            if self.dict.find(variable) != None and variable != '':
                expression = expression.replace(variable, str(self.dict.find(variable)))
        print(expression)
        return expression

'''
calc = Calculator()
calc.set_variable("d1", "1.0")
calc.set_variable("alpha1", "2.2")
calc.set_variable("b", "3.9")
calc.set_variable("d2", "6")
print(calc.dict)
calc.print_expression("d1*(alpha1+b)+((f/d2) + r)")
'''
'''
calc = Calculator()

calc.print_expression("(I+R)/(W/L+H)((W/L+H)")
'''


