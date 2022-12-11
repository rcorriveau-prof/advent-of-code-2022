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


def do_solution_1() -> int:
    ls_commandes = fn_lire_data("puzzle")
    ls_commandes = fn_prep_data(ls_commandes)

    no_cycle = 0
    force_signal = 0
    register = 1
    cycle_surveille = [20, 60, 100, 140, 180, 220]
    for commande in ls_commandes:
        no_cycle += 1

        # Cycle surveillé ? 20-60-100-140-180-220
        if no_cycle in cycle_surveille:
            force_signal += no_cycle * register

        if commande == "noop":  # no operation
            continue
        else:
            register += int(commande.split(" ")[1])




    return force_signal


if __name__ == "__main__":
    print(do_solution_1())

    # Test réponse : 13140