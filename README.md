# Implication de mineurs dans des affaires judiciaires aux Etats-Unis

## Description du contexte 

    Le sujet du projet est l'implication des mineurs dans des affaires judiciaires. 
Les données concernent uniquement les Etats-Unis pour la raison suivante:
les Etats-Unis disposent d'une législation différente de celle de la France 
et nous avons ainsi accès à plus de catégories de données comme l'ethnie des 
mineurs par exemple.

## Les données

    Les données sont disponibles sur 
https://www.icpsr.umich.edu/icpsrweb/NACJD/studies/37056/summary

Il y a 1,437,138 de lignes de données et 89 colonnes. 
Une description des données est données dans un codebook disponible dans le 
dossier: data/ICPSR_37056/DS0001 sous le nom: "37056-0001-Codebook"

## Pre processing des données

    Les données ont été récupérées sous format ".tsv". 
Le fichier est disponible dans le dossier data/ICPSR_37056/DS0001
sous le nom "37056-0001-Data.tsv"
Le script Python "modif_data" permet de retourner les données modifiées
pour ne garder que les données nécessaires et sous forme d'un fichier ".csv"
nommé "new_data.csv"


## Le script

    Afin de lancer le script, il faut lancer app.py
    
## Problèmes rencontrés
    
    Nous avons essayé de faire un histogramme par rapport à l'age des mineurs 
impliqués mais il y a eu un problème de conversion de type.