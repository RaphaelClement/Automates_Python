def creer_afd():
    print("=== Création de l'AFD ===")
    Q, alphabet = input("États (séparés par des espaces) : ").split(), input("Alphabet (séparé par des espaces) : ").split()
    initial_etat = input("État initial : "); final_etats = [e for e in input("États finaux (séparés par des espaces) : ").split() if e in Q]
    print("=== Définissez les transitions ===")
    transitions = {e: {s: (d if (d := input(f"({e}, {s}) --> ")) in Q else None) for s in alphabet} for e in Q}
    return Q, alphabet, transitions, initial_etat, final_etats

def simuler_afd(afd, mot):
    Q, alphabet, transitions, etat, finals = afd
    for s in mot:
        if s not in alphabet or (etat := transitions[etat].get(s)) is None:
            return print(f"Symbole non reconnu ou transition manquante : {s}"), False
    return etat in finals

def tester_afd():
    afd = creer_afd()
    print("=== AFD créé avec succès ===")
    while (mot := input("Mot à tester (ou 'quit' pour quitter) : ").strip()) != 'quit':
        print(f"Le mot '{mot}' est {'accepté' if simuler_afd(afd, mot) else 'non accepté'} par l'AFD.")

if __name__ == "__main__":
    tester_afd()