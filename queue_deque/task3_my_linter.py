def check_bracket_symmetry(expression):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}

    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"


print(check_bracket_symmetry("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(check_bracket_symmetry("( 23 ( 2 - 3);"))
print(check_bracket_symmetry("( 11 }"))
