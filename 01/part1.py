def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def fn_prep_data(p_puzzle_data: any) -> any:
    cal_par_lutin = [cal for cal in p_puzzle_data.split("\n\n")]  # encore en str

    # les chiffres en int
    col_par_lutin_int = []
    for no_lutin, collation_lutin in enumerate(cal_par_lutin):
        col_par_lutin_int.append([int(col) for col in collation_lutin.split("\n")])

    return col_par_lutin_int


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")
    col_par_lutin = fn_prep_data(puzzle_data)

    # Qui en a le plus
    plus_de_cal = 0
    for cals in col_par_lutin:
        if sum(cals) > plus_de_cal:
            plus_de_cal = sum(cals)

    return plus_de_cal


if __name__ == "__main__":
    print(do_solution_1())