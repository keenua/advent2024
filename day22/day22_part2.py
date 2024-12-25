from day22_part1 import read_file, step, STEPS
from typing import Dict, Tuple, List, Optional
from collections import Counter


Combination = Tuple[int, ...]


def get_combs(number: int) -> Dict[Combination, int]:
    combs: Dict[Combination, int] = {}

    current_comb: List[int] = []

    prev_number: Optional[int] = None

    for _ in range(STEPS):
        prev_number = number
        number = step(number)
        diff = (number % 10) - (prev_number % 10)

        current_comb.append(diff)

        if len(current_comb) == 4:
            comb_tuple = tuple(current_comb)

            if comb_tuple not in combs:
                combs[comb_tuple] = number % 10
            current_comb.pop(0)

    return combs


def get_bananas(numbers: List[int]) -> int:
    counter: Counter[Combination] = Counter()

    for number in numbers:
        combs = get_combs(number)
        counter.update(combs)

    return counter.most_common(1)[0][1]


if __name__ == "__main__":
    numbers = read_file("day22/data.txt")
    print(get_bananas(numbers))
