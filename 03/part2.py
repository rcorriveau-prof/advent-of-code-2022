import string


def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def fn_prep_data(p_puzzle_data: any) -> any:
    return any


def do_solution_2() -> int:
    ls_rucksacks = fn_lire_data("puzzle")

    # Séparer par équipe de 3
    ls_equipe_3 = []
    equipe = []
    for i in range(0, len(ls_rucksacks), 3):
        ls_equipe_3.append(ls_rucksacks[i:i + 3])

    # Trouver ce qui est pareil dans chaque sac
    ls_pareils = []
    for lutin1, lutin2, lutin3 in ls_equipe_3:
        ls_pareils.append(list(item for item in lutin1 if item in lutin2 and item in lutin3))

    # Créer une liste de l'alphabet, la valeur va être index + 1
    ls_alpha = string.ascii_lowercase + string.ascii_uppercase

    # Convertir et additionner
    somme = 0
    for pareil in ls_pareils:
        somme += ls_alpha.index(pareil[0]) + 1

    return somme


if __name__ == "__main__":
    print(do_solution_2())