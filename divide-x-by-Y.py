#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_divisible_by_y(x):
    """Check if 3 can divide x without a remainder."""
    if x % y == 0:
        return True
    return False

# Input from the user
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a divider: "))
    if is_divisible_by_y(x):
        print(f"Yes, {y} can divide {x}.")
    else:
        print(f"No, {y} cannot divide {x}.")
except ValueError:
    print("Please enter a valid integer.")
