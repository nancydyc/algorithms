"""
Twilio Test(A) Question 3:
Given a message, break it into segments if it exceeeds 160 characters.
Add suffixes: i.e. (9/9). You can assume there're no more than 9 segments.
After adding suffixes, make sure it also fits the 160-character rule.

"""

def break_into_segments(message):
    """ Given a string, return multiple sub-string lines with suffixes.
        Each line consists characters at most 160.

        For example:

        >>> break_into_segments('Ya, ya me está gustando más de lo normal. Todos mis sentidos van pidiendo más. Esto hay que tomarlo sin ningún apuro. Despacito Quiero respirar tu cuello despacito. Deja que te diga cosas al oído. Para que te acuerdes si no estás conmigo.')
        'Ya, ya me está gustando más de lo normal. Todos mis sentidos van pidiendo más. Esto hay que tomarlo sin ningún apuro. Despacito Quiero respirar tu cuello d (1/2)'
        'espacito. Deja que te diga cosas al oído. Para que te acuerdes si no estás conmigo. (2/2)'
    """

    # figure out how many segments the message will be split into


    # split the message

    # iterate through the sub-messages and add suffixes

    # join the list of sub-messages into a string of multiple lines





############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
