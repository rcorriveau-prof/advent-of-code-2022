def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def fn_prep_data(p_puzzle_data: any) -> any:
    cal_par_lutin = [cal for cal in p_puzzle_data.split("\n\n")]  # encore en str

    # les chiffres en int
    total_par_lutin_int = []
    for no_lutin, collation_lutin in enumerate(cal_par_lutin):
        total_par_lutin_int.append(sum([int(col) for col in collation_lutin.split("\n")]))

    return total_par_lutin_int


def do_solution_2() -> int:
    puzzle_data = fn_lire_data("puzzle")
    col_par_lutin = fn_prep_data(puzzle_data)

    # Total des 3 plus grands
    total_3 = sum(sorted(col_par_lutin, reverse=True)[:3])

    return total_3


if __name__ == "__main__":
    print(do_solution_2())