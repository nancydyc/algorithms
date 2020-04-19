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
       >>> checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
       False
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
        if char != ')':
            track_lst.append(char)

        else:
            if track_lst == []:
                return False

            else:
                if '(' in track_lst:
                    rev_lst = track_lst[::-1]

                    rev_lst.remove('(')

                    track_lst = rev_lst[::-1]

                else:
                    track_lst.pop()

    while track_lst:
        if '(' not in track_lst:

            return True

        last = track_lst.pop()

        if last == '(' and star_lst == []:
            return False

        if last == '*':
            star_lst.append(last)

        else:
            star_lst.pop()

    return True








#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
