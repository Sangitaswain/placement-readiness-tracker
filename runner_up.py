"""Print the second-highest distinct score using standard input/output."""


def runner_up_score(scores):
    """Remove duplicates, sort ascending, and return the second-last value."""
    distinct_scores = sorted(set(scores))
    return distinct_scores[-2]


def main():
    # Valid assignment input has at least two distinct scores, all in 0-100.
    n = int(input("Enter number of scores: "))
    scores = list(map(int, input("Enter scores separated by spaces: ").split()))

    if len(scores) != n:
        raise ValueError("The number of scores must match n.")

    # No interactive prompts: the output contains only the required answer.
    print(runner_up_score(scores))


if __name__ == "__main__":
    main()

