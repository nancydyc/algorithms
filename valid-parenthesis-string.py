def checkValidString(s):
    """Given a string containing only three types of characters: '(', ')' and '*',

       Any left parenthesis '(' must have a corresponding right parenthesis ')'.
       Any right parenthesis ')' must have a corresponding left parenthesis '('.
       Left parenthesis '(' must go before the corresponding right parenthesis ')'.
       '*' could be treated as a single right parenthesis ')'
       or a single left parenthesis '('
       or an empty string.
       An empty string is also valid.

       Example:
       >>> checkValidString("()")
       True
       >>> checkValidString("(*)")
       True
       >>> checkValidString("(*))")
       True
       >>> checkValidString("(*))((")
       False
       >>> checkValidString("(((******))")
       True
       >>> checkValidString("((()))()(())(*()()())**(())()()()()((*()*))((*()*)")
       True
       >>> checkValidString("(((()*())))((()(((()(()))()**(*)())))())()()*")
       True
    """

    if s == "" or s == "*":
        return True

    if s[0] == ")":
        return False

    lst = list(s)
    track_lst = []
    star_lst = []

    while lst:
        char = lst.pop(0)
        if char == '(':
            track_lst.append(char)

        if char == '*':
            star_lst.append(char)

        if char == ")":
            if track_lst:
                track_lst.pop()

            elif star_lst:
                star_lst.pop()

            else:
                return False

    while track_lst:
        if star_lst == []:
            return False

        else:
            star_lst.pop()
            track_lst.pop()

    return True








#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
