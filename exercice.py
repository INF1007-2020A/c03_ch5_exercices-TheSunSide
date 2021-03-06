#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    
    return abs(number)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    liste = List[str]
    for i in prefixes :
       liste.append(prefixes[i] + suffixes)
    return liste


def prime_integer_summation() -> int:
    number = 0
    liste = List[int]
    
    for i in range(100) :
       
    return i


def factorial(number: int) -> int:
     cpt = 1
     stocker = 1
     while cpt <= number:
         stocker *=cpt
     return stocker


def use_continue() -> None:
    for i in range(10):
        if(i != 5):
          print(i)
        else:
          print(i)

    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute( -8)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
