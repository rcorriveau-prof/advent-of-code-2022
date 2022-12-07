def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().split("\n")


def creer_arborescence(ls_commandes: list) -> dict:
    dt_dossiers = {"/": {"1": 0, "2": []}}  # Les dossiers et leur contenu cle 1 = total fichiers, cle 2 = liste dossier
    ls_path = []  # L'arborescence des dossiers
    cwd = "/"  # Le nom du dossier où on travaille
    for commande in ls_commandes:
        if commande.startswith("$"):
            # Gérer les commandes ls
            if "$ ls" in commande:
                continue  # Fait rien

            # Gérer les commandes cd
            _, __, cwd = commande.split(" ")
            if cwd == "..":
                ls_path.pop()
            else:
                ls_path.append(cwd)

        else:
            # Vérifier que le dossier existe, sinon on le crée
            cwd = ls_path[-1]
            if cwd not in dt_dossiers.keys():
                dt_dossiers[ls_path[-1]] = {"1": 0, "2": []}

            partie1, partie2 = commande.split(" ")

            # Gérer les fichiers
            if partie1.isnumeric():  # Additionner l'espace fichier
                dt_dossiers[cwd]["1"] += int(partie1)

            # Gérer les commandes dir
            else:
                dt_dossiers[cwd]["2"].append(partie2)  # Ajouter à la liste de dossier contenus

    return dt_dossiers


def somme_un_dossier(dossier: str, dt_dossiers: dict) -> int:
    return dt_dossiers[dossier]["1"]


def somme_sous_dossier(dossier: str, dt_dossiers: dict) -> int:
    somme_dossier = 0
    for sous_dossier in dt_dossiers[dossier]["2"]:
        somme_dossier += somme_un_dossier(sous_dossier, dt_dossiers)
    return somme_dossier


def do_solution_1() -> int:
    ls_commandes = fn_lire_data("test")
    dt_arbo = creer_arborescence(ls_commandes)

    ls_somme = []
    for dossier in dt_arbo.keys():
        somme_dossier = dt_arbo[dossier]["1"]
        for sous_dossier in dt_arbo[dossier]["2"]:
            somme_dossier += somme_un_dossier(sous_dossier, dt_arbo)
        ls_somme.append(somme_dossier)

    print(dt_arbo)

    return ls_somme


if __name__ == "__main__":
    print(do_solution_1())
