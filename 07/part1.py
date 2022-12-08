import os


def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().split("\n")


def creer_arborescence_pour_vrai(ls_commandes: list):
    for commande in ls_commandes[2:]:
        if commande.startswith("$"):
            # Gérer les commandes ls
            if "$ ls" in commande:
                continue  # Fait rien

            else:  # Gérer les commandes cd
                _, __, cwd = commande.split(" ")
                if cwd == "..":  # On remonte dans le parent
                    os.chdir(os.pardir)
                else:  # On descend dans l'enfant
                    os.chdir(cwd)

        else:
            partie1, partie2 = commande.split(" ")

            # Gérer les fichiers, partie1 -> taille du fichier
            if partie1.isnumeric():  # Additionner l'espace fichier
                os.system(f"echo {partie1} > {partie1}")

            # Gérer les commandes dir, partie 2 -> nom du dossier
            else:
                os.mkdir(partie2)  # Créer le dossier


def do_solution_1() -> int:
    ls_commandes = fn_lire_data("puzzle")

    os.chdir(r"C:\Users\Remy\drive_ecole\AdventOfCode\2022\07\root")

    creer_arborescence_pour_vrai(ls_commandes)

    ls_sommes = []
    # Trouve tous les dossiers et sous-dossiers à partir de root.
    # os.walk retourne : (dirpath, dirnames, filenames)
    ls_tous_dossiers = [x[0] for x in os.walk(r"C:\Users\Remy\drive_ecole\AdventOfCode\2022\07\root")]

    for dossier in ls_tous_dossiers:
        ls_fichiers = [x[2] for x in os.walk(dossier)]
        print(ls_fichiers)
        somme = 0
        for fichiers in ls_fichiers:
            if fichiers:
                somme += sum([int(fichier) for fichier in fichiers])
        ls_sommes.append(somme)

    somme = sum(int(espace) for espace in ls_sommes if espace <= 100_000)

    return somme


if __name__ == "__main__":
    print(do_solution_1())
