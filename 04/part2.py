def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def fn_prep_data(p_puzzle_data: any) -> any:
    ls_paires = []
    for paire in p_puzzle_data:
        ls_2_elfes = []
        # On sépare les 2 ranges
        for elfe in paire.split(","):
            ls_elfe = []
            # On sépare le début et la fin
            for nb in elfe.split("-"):
                # On converti en int
                ls_elfe.append(int(nb))
            ls_2_elfes.append(ls_elfe)
        ls_paires.append(ls_2_elfes)

    return ls_paires


def do_solution_2() -> int:
    puzzle_data = fn_lire_data("puzzle")
    ls_paires = fn_prep_data(puzzle_data)

    # Vérifier si un range overlap avec l'autre
    somme = 0
    for elfe1, elfe2 in ls_paires:
        if elfe1[0] in range(elfe2[0], elfe2[1] + 1) \
                or elfe1[1] in range(elfe2[0], elfe2[1] + 1) \
                or elfe2[0] in range(elfe1[0], elfe1[1] + 1) \
                or elfe2[1] in range(elfe1[0], elfe1[1] + 1):
            somme += 1

    return somme


if __name__ == "__main__":
    print(do_solution_2())