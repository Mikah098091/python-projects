#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_divisible_by_3(x):
    """Check if 3 can divide x without a remainder."""
    if x % 3 == 0:
        return True
    return False

# Input from the user
try:
    x = int(input("Enter a number: "))
    if is_divisible_by_3(x):
        print(f"Yes, 3 can divide {x}.")
    else:
        print(f"No, 3 cannot divide {x}.")
except ValueError:
    print("Please enter a valid integer.")

