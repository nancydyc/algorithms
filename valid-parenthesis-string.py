def checkValidString(str):
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




#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
