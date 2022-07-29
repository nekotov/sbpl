"""
This module is sub functions for project.
"""


_iota_global = 0


def iota(reset: object = False) -> int:
    """:rtype: object
    iota implementation. on call returning +1. to reset just run with argument Ture
    """

    global _iota_global
    if reset:
        _iota_global = 0
    loc = _iota_global
    _iota_global += 1
    return loc
