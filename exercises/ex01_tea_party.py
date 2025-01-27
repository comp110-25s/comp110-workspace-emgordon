"""This exercise will help plan a tea party."""

__author__: str = "730567557"


def main_planner(guests: int) -> None:
    """Calls each of the following functions and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Compute the number of tea bags needed based on the number of guests."""
    return 2 * people


def treats(people: int) -> int:
    """Compute the number of treats needed based on the number of teas guests are expecting to drink."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computer the cost of the tea bags and the treats combined."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
