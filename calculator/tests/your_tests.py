#!/usr/bin/env python3
from calculator_adapter import run

### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "8" for an input of "3 + 5"
assert run("3 + 5").output == "8"

# Checks that the program outputs "6" for an input of "10 - 4"
assert run("10 - 4").output == "6"

print("All tests passed!")
