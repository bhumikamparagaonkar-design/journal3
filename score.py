import sys

if len(sys.argv) < 2:
    print("Usage: python score.py 10 20 30 40")
    sys.exit(1)

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
