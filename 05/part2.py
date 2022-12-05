import re
import aoc_utils


def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        # Sépare la structure initiale des moves subséquents
        return puzzle_input.read().split("\n\n")


def changer_crates_listes(crates) -> list:
    # Transformer les crates en listes
    ls_crates = [[], [], [], [], [], [], [], [], []]
    # Position où il peut y avoir des lettres: rangées où mettre la lettre
    conversion_index_a_ls_crates = {"1": 0,
                                    "5": 1,
                                    "9": 2,
                                    "13": 3,
                                    "17": 4,
                                    "21": 5,
                                    "25": 6,
                                    "29": 7,
                                    "33": 8,
                                    "37": 9}
    # Séparer par rangée, commence par en bas, enlève les chiffres
    crates = list(reversed(crates.split("\n")[:-1]))

    # Placer les crates dans leur liste
    for rangee in crates:
        rangee_crates = re.findall(r"\w", rangee)
        crate_index = 0
        for crate in rangee_crates:
            crate_index = rangee.index(crate, crate_index + 1)  # Éviter les doublons
            ls_crates[conversion_index_a_ls_crates[f"{crate_index}"]].append(crate)

    return ls_crates


def formater_moves(moves: str) -> list:
    # combien, source, destination
    ls_moves = []
    for move in moves.split("\n"):
        ls_moves.append(aoc_utils.extraire_nb_de_str(move))

    return ls_moves


def do_solution_2() -> str:
    crates, moves = fn_lire_data("puzzle")
    ls_crates = changer_crates_listes(crates)
    ls_moves = formater_moves(moves)

    print(ls_crates)

    # On bouge les caisses !
    for combien, source, destination in ls_moves:
        # Ajuster pour l'index qu'il commence à 0
        source -= 1
        destination -= 1
        crate = ls_crates[source][-combien:]  # Copie les crates
        ls_crates[source] = ls_crates[source][:-combien]  # Enlève les crates
        ls_crates[destination] = ls_crates[destination] + crate  # Ajoute les crates

    # Lire les tops crates
    sequence = ""
    for colonne in ls_crates:
        try:
            sequence += colonne[-1]
        except:  # Si y'a pas de crate on ignore la colonne
            pass

    return sequence


if __name__ == "__main__":
    print(do_solution_2())
