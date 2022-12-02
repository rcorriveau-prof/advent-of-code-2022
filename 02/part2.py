def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def do_solution_2() -> int:
    ls_rondes = fn_lire_data("puzzle")

    total_points = 0
    for adversaire, _, resultat in ls_rondes:
        # Calculer les points de résultats
        if resultat == "Y":  # Nulle
            total_points += 3
        elif resultat == "Z":  # Victoire
            total_points += 6

        # Calculer les points de symboles
        if resultat == "X" and adversaire == "A" \
                or resultat == "Y" and adversaire == "C" \
                or resultat == "Z" and adversaire == "B":
            total_points += 3  # Ciseau
        elif resultat == "X" and adversaire == "B" \
                or resultat == "Y" and adversaire == "A" \
                or resultat == "Z" and adversaire == "C":
            total_points += 1  # Roche
        elif resultat == "X" and adversaire == "C" \
                or resultat == "Y" and adversaire == "B" \
                or resultat == "Z" and adversaire == "A":
            total_points += 2  # Papier

    return total_points


if __name__ == "__main__":
    print(do_solution_2())

    # X = défaite
    # Y = nulle
    # Z = victoire
