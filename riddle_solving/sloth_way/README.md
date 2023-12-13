# Sloth_way 🦥:

## Problem Statement
A sloth is trying to climb a slippery pole. During the day, it climbs 6 meters, but at night, it slips down 5 meters. The pole has a height of 30 meters, and the sloth starts its journey from the ground (0 meters). How many days will it take for the sloth to reach the top of the pole?

## Solution
We can use a Python function to calculate the number of days required for the sloth to climb the pole. The provided function `sloth_way` takes three parameters: `up` (meters climbed during the day), `down` (meters slipped at night), and `high` (height of the pole). It returns the number of days required, considering the sloth's climbing and slipping pattern.

Example:
```python
from math import ceil

def sloth_way(up, down, high):
    days = ceil((high - up) / (up - down)) + 1
    return days

print(sloth_way(6, 5, 30))
```

This will output the number of days the sloth needs to climb the pole.  
The ceil function is used to ensure that fractional days are rounded up to the nearest whole day, 
as the sloth cannot climb a fraction of a day.
