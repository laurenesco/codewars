# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l: list[int | str]) -> str:
    return [_ for _ in l if isinstance(_, int)]
