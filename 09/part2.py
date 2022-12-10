def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [(move[:1], int(move[2:])) for move in puzzle_input.read().split("\n")]


def do_solution_2() -> int:
    ls_moves = fn_lire_data("puzzle")

    # Pour chaque move, bouger H puis T
    corde_10_knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    ls_pos_knot_9 = []
    for direction, repetitions in ls_moves:
        for _ in range(repetitions):
            ls_pos_knot_9.append(tuple(corde_10_knots[9]))
            # Bouger H
            if direction == "R":
                corde_10_knots[0][0] += 1
            elif direction == "L":
                corde_10_knots[0][0] -= 1
            elif direction == "D":
                corde_10_knots[0][1] += 1
            elif direction == "U":
                corde_10_knots[0][1] -= 1

            for knot in range(1, 10):
                xH, yH = corde_10_knots[knot - 1][0], corde_10_knots[knot - 1][1]
                xT, yT = corde_10_knots[knot][0], corde_10_knots[knot][1]
                # Créer des listes avec les coordonnées +- 1
                coordonnees_acceptables_x = []
                coordonnees_acceptables_y = []
                for i in range(-1, 2):
                    coordonnees_acceptables_x.append(xH + i)
                    coordonnees_acceptables_y.append(yH + i)
                # Bouge PAS T : même case, adjacent côté ou diagonale
                print(f"coordonnees_acceptables_x : {coordonnees_acceptables_x}")
                print(f"coordonnees_acceptables_y : {coordonnees_acceptables_y}")
                if xT in coordonnees_acceptables_x and yT in coordonnees_acceptables_y:
                    continue

                # Bouger T, axe x
                if yT == yH:
                    if xT > xH:  # Déplacement vers la gauche
                        corde_10_knots[knot][0] -= 1
                    else:  # Déplacement vers la droite
                        corde_10_knots[knot][0] += 1
                    continue

                # Bouger T, axe y
                if xT == xH:
                    if yT > yH:  # Déplacement vers le bas
                        corde_10_knots[knot][1] -= 1
                    else:  # Déplacement vers le haut
                        corde_10_knots[knot][1] += 1
                    continue

                # Bouger T, diagonale
                if xT > xH:  # Déplacement vers la gauche
                    corde_10_knots[knot][0] -= 1
                else:  # Déplacement vers la droite
                    corde_10_knots[knot][0] += 1
                if yT > yH:  # Déplacement vers le bas
                    corde_10_knots[knot][1] -= 1
                else:  # Déplacement vers le haut
                    corde_10_knots[knot][1] += 1

    # Retourne le nombre de cases uniques visitées par T
    return len(set(ls_pos_knot_9))


if __name__ == "__main__":
    print(do_solution_2())