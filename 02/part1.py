def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def do_solution_1() -> int:
    ls_rondes = fn_lire_data("puzzle")

    total_points = 0
    for adversaire, _, moi in ls_rondes:
        # Calculer les points de résultats
        if adversaire == "A" and moi == "X" \
                or adversaire == "B" and moi == "Y" \
                or adversaire == "C" and moi == "Z":  # Nulles
            total_points += 3
        elif adversaire == "A" and moi == "Y" \
                or adversaire == "B" and moi == "Z" \
                or adversaire == "C" and moi == "X":  # Victoire
            total_points += 6

        # Calculer les points de symboles
        if moi == "X":
            total_points += 1
        elif moi == "Y":
            total_points += 2
        elif moi == "Z":
            total_points += 3

    return total_points


if __name__ == "__main__":
    print(do_solution_1())

    # X = 1  roche
    # Y = 2  papier
    # Z = 3  ciseau
