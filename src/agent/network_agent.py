from typing import Iterable


def to_n(L: int, i: int, j: int) -> int:
    """ This function returns the number of associated to agent(i,j)

    Args:
        L (int): lenght of agent population N where N = L * L (N : total number of agent)
        i (int): line 
        j (int): column

    Returns:
        int: number associated to agent(i,j)
    """
    return i + j * L


def east(L: int, n: int) -> int:
    """ This function returns the east neighboor's number of agent number n

    Args:
        L (int): lenght of agent population N where N = L * L (N : total number of agent)
        n: agent number

    Returns:
        int: east neighboor's number
    """
    
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    m = i + (j + 1) * L
    return m - L * L if m >= L * L else m


def south(L: int, n: int) -> int:
    """ This function returns the south neighboor's number of agent number n

    Args:
        L (int): lenght of agent population N where N = L * L (N : total number of agent)
        n: agent number

    Returns:
        int: south neighboor's number
    """
    
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return j * L if i + 1 == L else (i + 1) + j * L


def west(L: int, n: int) -> int:
    """ This function returns the west neighboor's number of agent number n

    Args:
        L (int): lenght of agent population N where N = L * L (N : total number of agent)
        n: agent number

    Returns:
        int: west neighboor's number
    """
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return i + (L - 1) * L if j == 0 else i + (j - 1) * L


def north(L: int, n: int) -> int:
    """ This function returns the north neighboor's number of agent number n

    Args:
        L (int): lenght of agent population N where N = L * L (N : total number of agent)
        n: agent number

    Returns:
        int: north neighboor's number
    """
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return L - 1 + j * L if i == 0 else i - 1 + j * L