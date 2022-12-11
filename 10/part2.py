from pprint import pprint


def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().split("\n")


# Co-pilot a écrit cette fonction là tout seul.
def fn_prep_data(p_puzzle_data: any) -> any:
    """Prepend "noop" for each addx instruction."""
    ls_prep_data = []
    for ligne in p_puzzle_data:
        if ligne.startswith("addx"):
            ls_prep_data.append("noop")
        ls_prep_data.append(ligne)
    return ls_prep_data


def do_solution_2():
    ls_commandes = fn_lire_data("puzzle")
    ls_commandes = fn_prep_data(ls_commandes)

    no_cycle = 0
    register = 1
    cycle_surveille = [40, 80, 120, 160, 200, 240]
    ecran_crt = [[], [], [], [], [], []]
    rangee_ecran = 0
    for commande in ls_commandes:
        no_cycle += 1
        pixel_drawn = no_cycle - 1

        # Dessiner le pixel.
        if pixel_drawn in (register - 1, register, register + 1):
            ecran_crt[rangee_ecran].append("#")
        else:
            ecran_crt[rangee_ecran].append(".")

        # Modifier le register
        if commande == "noop":
            pass  # Register ne change pas.
        else:
            register += int(commande.split(" ")[1])

        # Cycle surveillé ? 40, 80, 120, 160, 200, 240
        if no_cycle in cycle_surveille:
            rangee_ecran += 1
            no_cycle = 0

    # Affichage de l'écran.
    for ligne in ecran_crt:
        for pixel in ligne:
            print(pixel, end="")
        print()


if __name__ == "__main__":
    do_solution_2()

    # Puzzle réponse : PLGFKAZG