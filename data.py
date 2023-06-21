"""
gallow figures split on white lines to iterate through,
copied from https://github.com/madeinouweland/python-hangman/blob/main/data.py
"""

gallows = r"""
+---
|
|
|
^

+---,
|
|
|
^

+---,
|   o
|
|
^

+---,
|   o
|   |
|
^

+---,
|   o
|  /|
|
^

+---,
|   o
|  /|\
|
^

+---,
|   o
|  /|\
|  /
^

+---,
|   o
|  /|\
|  / \
^
""".strip().split("\n\n")
