from stack import Stack

def is_match(paren1,paren2):
    if paren1 == "(" and paren2 == ")":
        return True
    elif paren1 == "{" and paren2 == "}":
        return True
    elif paren1 == "[" and paren2 == "]":
        return True
    else:
        return False

def is_parenthesis_balanced(paren_string):
    s = Stack()
    isBalanced = True
    index = 0
    
    while index < len(paren_string) and isBalanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                isBalanced = False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    isBalanced = False
        index += 1
    
    if s.is_empty() and isBalanced:
        return True
    else:
        return False
    

print(is_parenthesis_balanced("()"))
print(is_parenthesis_balanced("(((({}))))"))
print(is_parenthesis_balanced("[][]]]"))
print(is_parenthesis_balanced("[][]"))

