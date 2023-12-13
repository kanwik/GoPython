from math import ceil

def sloth_way(up, down, high):
    days = ceil((high - up) / (up - down)) + 1
    return days

print(sloth_way(6, 5, 30))
