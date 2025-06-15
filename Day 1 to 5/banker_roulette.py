import random

friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emmanuel']

friend = random.randint(0, 4)

print(friends[friend])

# Answer #2
print(random.choice(friends))