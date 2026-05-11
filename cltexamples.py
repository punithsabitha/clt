import random
import statistics

print("Central Limit Theorem Examples")

example1 = []
for i in range(100):
    data = [random.randint(1, 6) for j in range(30)]
    example1.append(statistics.mean(data))

print("Dice Mean:", round(statistics.mean(example1), 2))

example2 = []
for i in range(100):
    data = [random.randint(50, 100) for j in range(20)]
    example2.append(statistics.mean(data))

print("Marks Mean:", round(statistics.mean(example2), 2))

example3 = []
for i in range(100):
    data = [random.randint(1, 100) for j in range(25)]
    example3.append(statistics.mean(data))

print("Random Numbers Mean:", round(statistics.mean(example3), 2))

example4 = [random.randint(10, 20) for i in range(50)]
print("Height Mean:", round(statistics.mean(example4), 2))

example5 = [random.randint(100, 500) for i in range(50)]
print("Salary Mean:", round(statistics.mean(example5), 2))

print("Central Limit Theorem shows averages become normal.")