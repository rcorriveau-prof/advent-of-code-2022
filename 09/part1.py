def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [(move[:1], int(move[2:])) for move in puzzle_input.read().split("\n")]


def do_solution_1() -> int:
    ls_moves = fn_lire_data("puzzle")

    # Pour chaque move, bouger H puis T
    coord_H = [0, 0]
    coord_T = [0, 0]
    ls_cases_T = []
    for direction, repetitions in ls_moves:
        for _ in range(repetitions):
            print(f"H : {coord_H}")
            print(f"T : {coord_T}")
            ls_cases_T.append(tuple(coord_T))
            # Bouger H
            if direction == "R":
                coord_H[0] += 1
            elif direction == "L":
                coord_H[0] -= 1
            elif direction == "D":
                coord_H[1] += 1
            elif direction == "U":
                coord_H[1] -= 1

            xH, yH = coord_H
            xT, yT = coord_T
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
                    coord_T[0] -= 1
                else:  # Déplacement vers la droite
                    coord_T[0] += 1
                continue

            # Bouger T, axe y
            if xT == xH:
                if yT > yH:  # Déplacement vers le bas
                    coord_T[1] -= 1
                else:  # Déplacement vers le haut
                    coord_T[1] += 1
                continue

            # Bouger T, diagonale
            if xT > xH:  # Déplacement vers la gauche
                coord_T[0] -= 1
            else:  # Déplacement vers la droite
                coord_T[0] += 1
            if yT > yH:  # Déplacement vers le bas
                coord_T[1] -= 1
            else:  # Déplacement vers le haut
                coord_T[1] += 1

    # Retourne le nombre de cases uniques visitées par T
    return len(set(ls_cases_T))


if __name__ == "__main__":
    print(do_solution_1())