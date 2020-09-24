# Session 2
**Plan de la session**

- Exercices
- Correction des exercices
- Correction devoir maison
- Présentation de CRISP-DM
- Introduction à pandas
- Series et DataFrame

**Projet maison n° 1**

- Ajoutez une colonne 'CP Ville' avec le Code postal + un espace + et le nom de la Ville.
- Ecrivez une fonction qui détermine la commune la plus proche d'un point à partir de sa latitude et sa longitude.
- Ajoutez une fonction de conversion pour pouvoir utiliser la première fonction avec un GPS (degrés, minutes, secondes).

**Projet maison n° 2**

La colonne "geo_shape" comporte des chaines de catactères au format  JSON. Elles représentent les formes géométriques des communes qui sont  soit des polygones soit composées de plusieurs polygones.

- Utiliser la librairie Python json pour parser la colonne "geo_shape".
- Donner le décompte des valeurs accédées avec la clé "type".
- Donner le décompte des longueurs des listes accédées avec la clé "coordinates".
- Quelle commune est la plus complexe géométriquement ?
- Quelle commune est la seconde la plus complexe géométriquement ?
- Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ?
- Pour ces villes vérifier que le premier polygone contient bien le  second (enclave). NB : installer la librairie shapely, utiliser la  classe Polygon de shapely.geometry. Sur Windows shapely peut nécessiter  d'installer la dll "geos_c.dll" dans le répertoire "Library/bin" de  votre environnement Python.

**Utilisation d'environnements virtuels** :

Pour isoler les librairies utilisées dans un projet, se créer un environnement Python par projet, par exemple :

<code>conda create --name myenv</code>

Ensuite activer l'environnement à utiliser dans un terminal au niveau de votre notebook :

<code>conda activate myenv</code> (linux) ou <code>activate myenv</code> (Windows)

Puis lancer jupyter :

<code>jupyter notebook</code>

Votre notebook sera dans l'envrionnement sélectionné.

Voir la doc complète sur le sujet : https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html 

**Utilisation de git**

- Se créer un compte sur github et le mettre dans l'organisation du Master
- Rappatrier le cours une première fois avec : <code>git clone https://github.com/fran6w/MDI721</code>
- Puis le mettre à jour à chaque fois avec : <code>git fetch</code>
- Copier ce repository local dans un répertoire de travail pour suivre le cours ou faire les projets.
- Copier ensuite vos travaux dans le repository local de <u>votre compte github</u> et les exporter avec la séquence  :
  - <code>git add .</code>
  - <code>git commit -m "message"</code>
  - <code>git push origine</code>

