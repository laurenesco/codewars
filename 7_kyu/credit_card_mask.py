# https://www.codewars.com/kata/5412509bd436bd33920011bc

def maskify(cc):
    """
    Returns a masked version of the string with only
    the last 4 characters exposed.
    """

    return ''.join('#' for _ in cc[:-4]) + cc[-4:]
