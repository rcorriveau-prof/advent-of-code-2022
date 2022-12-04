from typing import List
import re


def extraire_nb_de_str(chaine: str) -> List[int]:
    """
    Extrait et convertis en int tous les nombres d'une chaîne. Ils doivent être séparé entre eux.

    :param chaine: Cahîne de texte contenant un ou plusieurs nombres.
    :return: Liste contenant les nombres trouvés.
    """
    return list(map(int, re.findall(r'\d+', chaine)))


def sous_diviser_iter(iterateur: any, taille_mcx: int) -> List[list]:
    """
    Sous-divise un itérateur en une liste avec des sous-listes de la grandeure désirée.

    :param iterateur: La séquence initiale à sous-diviser.
    :param taille_mcx: La longueur des morceaux.
    :return: Liste avec sous-liste de la longueur demandée.
    """
    ls_avec_sous_listes = []
    for i in range(0, len(iterateur), taille_mcx):
        ls_avec_sous_listes.append(iterateur[i:i + taille_mcx])

    return ls_avec_sous_listes