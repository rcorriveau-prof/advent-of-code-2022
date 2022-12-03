import string

def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def fn_prep_data(p_puzzle_data: any) -> any:
    return any


def do_solution_1() -> int:
    ls_rucksacks = fn_lire_data("puzzle")

    # Séparer au milieu
    ls_compartiment_par_sac = [[sac[:int(len(sac) / 2)], sac[int(len(sac) / 2):]] for sac in ls_rucksacks]

    # Trouver ce qui est pareil dans chaque sac
    ls_pareils = []
    for compartiment_1, compartiment_2 in ls_compartiment_par_sac:
        ls_pareils.append(list(item for item in compartiment_1 if item in compartiment_2))

    # Créer une liste de l'alphabet, la valeur va être index + 1
    ls_alpha = string.ascii_lowercase + string.ascii_uppercase

    # Convertir et additionner
    somme = 0
    for pareil in ls_pareils:
        somme += ls_alpha.index(pareil[0]) + 1

    return somme


if __name__ == "__main__":
    print(do_solution_1())