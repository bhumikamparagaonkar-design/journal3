

def process_scores():
    print("Enter scores separated by spaces:")
    scores = list(map(int, input().split()))

    total = sum(scores)
    average = total / len(scores)

    print("\n---- Results (Main/Master Branch) ----")
    print("Sum of scores:", total)
    print("Average of scores:", average)


if __name__ == "__main__":
    process_scores()
