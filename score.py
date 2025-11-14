

def process_scores():
    print("Enter scores separated by spaces:")
    scores = list(map(int, input().split()))

    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("\n---- Results (Local Branch) ----")
    print("Sum of scores:", total)
    print("Average of scores:", average)
    print("Maximum score:", maximum)
    print("Minimum score:", minimum)


if __name__ == "__main__":
    process_scores()
