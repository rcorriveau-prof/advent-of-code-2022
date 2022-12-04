def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().split("\n")


def fn_prep_data(p_puzzle_data: any) -> any:
    return any


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")
    ls_lignes = fn_prep_data(puzzle_data)
    return int


if __name__ == "__main__":
    print(do_solution_1())