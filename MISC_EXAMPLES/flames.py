name1 = input('Name of first person: ').casefold()
name2 = input('Name of second person: ').casefold()

def flames(name1, name2):
    n1 = sum(letter not in name2 for letter in name1)
    n2 = sum(letter not in name1 for letter in name2)
    results = 'friend love affection marriage enemy'.split()
    index = (n1 + n2) % len(results) - 1
    return results[index]

print('Relationship is', flames(name1, name2))