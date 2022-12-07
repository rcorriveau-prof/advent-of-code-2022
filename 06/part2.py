def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def do_solution_2() -> int:
    datastream = fn_lire_data("puzzle")

    for i in range(len(datastream)):
        # Vérifier si ce sont 4 caractères uniques
        if len(set(datastream[i: i + 14])) == 14:
            reponse = i + 14
            break


    return reponse


if __name__ == "__main__":
    print(do_solution_2())

    # Test réponse : 7-5-6-10-11