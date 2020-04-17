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
    """

    #



#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
