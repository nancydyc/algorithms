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

    # check the string from the beginning
    # record the num of "(" until next char is not "("
    # if the next char is ")" or "*"
    # count their number until next char is not ")" or "*"
    # if left_par_num - right_par_num = 0,
    # repeat the process until the string ends, return True
    # if num is not 0, check if num < 0 or num > 0
    # if num > 0
    # - if num - star_num != 0, return false
    # - else, keep tracking until the string ends, return True
    # if num < 0
    # - if num + star_num != 0, return false
    # - else, continue tracking till string ends, return True

    if s == "" or s == "*":
        return True

    if s[0] == ")":
        return False

    lst = list(s)

    while lst:
        left_par_num = 0
        right_par_num = 0
        star_num = 0

        while lst and lst[0] != ")":
            if lst[0] == "*":
                star_num += 1
                lst.pop(0)

            else:
                left_par_num += 1
                lst.pop(0)

        while lst and lst[0] != "(":
            if lst[0] == "*":
                star_num += 1
                lst.pop(0)

            else:
                right_par_num += 1
                lst.pop(0)

        if left_par_num - right_par_num > 0:
            if left_par_num - right_par_num - star_num > 0:
                return False

        if left_par_num - right_par_num < 0:
            if left_par_num + star_num - right_par_num < 0:
                return False

    return True








#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
