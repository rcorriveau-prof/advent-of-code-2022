def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().split("\n")


def fn_prep_data(p_puzzle_data: any) -> any:
    """
    Converti l'entrée en liste de liste de int.
    """
    return [list(map(int, rangee)) for rangee in p_puzzle_data]


def verifier_arbre_visible(position: tuple, foret: list) -> bool:
    """
    Vérifier si l'arbre est visible dans 4 directions : N, S, E, O
    Un arbre est visible si aucun autre arbre d'une même grandeur ou plus
    n'est devant lui.

    :param position: Coordonnées (x, y) dans la forêt.
    :return: Visible: True, Caché: False
    """
    dimension_foret = len(foret)
    x, y = position
    hauteur_arbre = foret[x][y]

    # Vérifier le périmètre d'une foret CARRÉE
    if 0 in position or dimension_foret - 1 in position:
        return True

    # Vérifier Nord
    if not [i for i in range(0, x) if foret[i][y] >= hauteur_arbre]:
        return True

    # Vérifier Sud
    if not [i for i in range(x + 1, dimension_foret) if foret[i][y] >= hauteur_arbre]:
        return True

    # Vérifier Est
    if not [i for i in range(y + 1, dimension_foret) if foret[x][i] >= hauteur_arbre]:
        return True

    # Vérifier Ouest
    if not [i for i in range(0, y) if foret[x][i] >= hauteur_arbre]:
        return True


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")
    np_foret = fn_prep_data(puzzle_data)

    # Tous les arbres de la forêt
    nb_arbres_visibles = 0
    for rangee in range(0, len(np_foret)):  # x
        for colonne in range(0, len(np_foret[rangee])):  # y
            arbre = (rangee, colonne)
            if verifier_arbre_visible(arbre, np_foret):
                nb_arbres_visibles += 1

    return nb_arbres_visibles


if __name__ == "__main__":
    print(do_solution_1())