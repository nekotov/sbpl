"""
This module is sub functions for project.
"""


iota_global = 0


def iota(reset: object = False) -> int:
    """:rtype: object
    iota implementation. on call returning +1. to reset just run with argument Ture
    """

    global iota_global
    if reset:
        iota_global = 0
    loc = iota_global
    iota_global += 1
    return loc
