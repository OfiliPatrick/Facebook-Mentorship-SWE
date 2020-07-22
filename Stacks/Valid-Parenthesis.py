def isValid(s):
    if s == '':
        return True
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)

        elif stack and char == bracket_map[stack[-1]]:
            stack.pop()
              
        else:
            return False
                
    return len(stack) == 0