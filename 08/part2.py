import math

def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().split("\n")


def fn_prep_data(p_puzzle_data: any) -> any:
    """
    Converti l'entrée en liste de liste de int.
    """
    return [list(map(int, rangee)) for rangee in p_puzzle_data]


def calculer_score_scenique(position: tuple, foret: list) -> int:
    """
    Vérifier si l'arbre est visible dans 4 directions : N, S, E, O
    Un arbre est visible si aucun autre arbre d'une même grandeur ou plus
    n'est devant lui.

    :param foret: Le tableau qui représente la forêt.
    :param position: Coordonnées (x, y) dans la forêt.
    :return: Visible: True, Caché: False
    """
    dimension_foret = len(foret)
    x, y = position
    hauteur_arbre = foret[x][y]
    ls_score_par_direction = []

    # Éliminer le périmètre d'une foret CARRÉE
    if 0 in position or dimension_foret - 1 in position:
        return 0

    # Vérifier Nord
    somme_direction = 0
    for i in range(x - 1, -1, -1):
        somme_direction += 1
        if not foret[i][y] < hauteur_arbre:
            break
    ls_score_par_direction.append(somme_direction)

    # Vérifier Sud
    somme_direction = 0
    for i in range(x + 1, dimension_foret):
        somme_direction += 1
        if not foret[i][y] < hauteur_arbre:
            break
    ls_score_par_direction.append(somme_direction)

    # Vérifier Est
    somme_direction = 0
    for i in range(y + 1, dimension_foret):
        somme_direction += 1
        if not foret[x][i] < hauteur_arbre:
            break
    ls_score_par_direction.append(somme_direction)

    # Vérifier Ouest
    somme_direction = 0
    for i in range(y - 1, -1, -1):
        somme_direction += 1
        if not foret[x][i] < hauteur_arbre:
            break
    ls_score_par_direction.append(somme_direction)

    # Multiplier toutes les directions pour calculer le score scénique
    return math.prod(ls_score_par_direction)


def do_solution_2() -> int:
    puzzle_data = fn_lire_data("puzzle")
    ls_foret = fn_prep_data(puzzle_data)

    # Tous les arbres de la forêt
    ls_scenic_score = []
    for rangee in range(0, len(ls_foret)):  # x
        for colonne in range(0, len(ls_foret[rangee])):  # y
            arbre = (rangee, colonne)
            ls_scenic_score.append(calculer_score_scenique(arbre, ls_foret))
            print(arbre)
            print(ls_foret[rangee][colonne])
            print(ls_scenic_score[-1])

    print(ls_scenic_score.index(max(ls_scenic_score)))
    return max(ls_scenic_score)


if __name__ == "__main__":
    print(do_solution_2())