{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Projet maison n° 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# imports\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. US baby names\n",
    "\n",
    "On va s'intéresser au dataset **National data** de la SSA : https://www.ssa.gov/oact/babynames/limits.html\n",
    "\n",
    "1. Télécharger le dataset des prénoms US : https://www.ssa.gov/oact/babynames/names.zip\n",
    "\n",
    "2. Implémenter une fonction Python qui produit un unique DataFrame avec tous les fichiers en utilisant pandas  (par ex. fonction \\\"concat\\\" ou méthode \\\"append\\\"), pas de bash :)\n",
    "\n",
    "Ordre et noms des colonnes : 'year', 'name', 'gender', 'births'\n",
    "\n",
    "Le DataFrame doit être trié selon l'année croissante puis selon l'ordre défini par les différents fichiers (voir la documentation ci-dessus)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1) implémentation avec glob + append\n",
    "import glob\n",
    "\n",
    "def df_names_us():\n",
    "    df = pd.DataFrame()\n",
    "    files = glob.glob('names/*.txt')\n",
    "    files.sort()\n",
    "    for filename in files:\n",
    "        csv = pd.read_csv(filename,\n",
    "                          names=['name', 'gender', 'births'])\n",
    "        csv['year'] = int(filename[-8:-4]) # yobAAAA.txt\n",
    "        df = df.append(csv, ignore_index=True)\n",
    "    df = df[['year', 'name', 'gender', 'births']]\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%time\n",
    "df_us = df_names_us()\n",
    "df_us.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# head\n",
    "df_us.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2) implémentation avec range + concat\n",
    "def df_names_us():\n",
    "    dfs = []\n",
    "    for year in range(1880, 2020):\n",
    "        csv = pd.read_csv(f'names/yob{year}.txt',\n",
    "                          names=['name', 'gender', 'births'])\n",
    "        csv['year'] = year\n",
    "        dfs.append(csv)\n",
    "    df = pd.concat(dfs, ignore_index=True)\n",
    "    df = df[['year', 'name', 'gender', 'births']]\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%time\n",
    "df_us = df_names_us()\n",
    "df_us.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# head\n",
    "df_us.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**slice vs regex**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# slice 140 x 96.1ns = ~14ms\n",
    "%timeit 'yob2020.txt'[-8: -4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# regex 140 x 1.37µs = ~192ms (x14)\n",
    "import re\n",
    "%timeit re.search('(\\d+)', 'yob2020.txt').group(0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Prénoms français"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "On va s'intéresser au dataset **Fichiers France hors Mayotte** de l'INSEE :  https://www.insee.fr/fr/statistiques/2540004/\n",
    "\n",
    "L'idée est de charger les données et ensuite de les conformer au DataFrame des prénoms US. Ainsi, toute manipulation sur le DataFrame des prénoms US pourra être directement réutilisée avec le DataFrame des prénoms français.\n",
    " \n",
    "1. Télécharger le dataset des prénoms français : https://www.insee.fr/fr/statistiques/fichier/2540004/nat2019_csv.zip\n",
    "\n",
    "\n",
    "Lire la documentation, ça peut être utile...\n",
    " \n",
    "2. Implémenter une fonction Python qui produit un DataFrame avec les prénoms français en prenant le DataFrame des prénoms US comme modèle :\n",
    " \n",
    " - Même ordre et mêmes noms des colonnes : year, name, gender, births\n",
    " - Mêmes dtypes pour les colonnes\n",
    " - Mêmes valeurs pour la colonne 'gender'\n",
    " - Seuls les prénoms de 2 caractères et plus sont conservés\n",
    " - La casse des prénoms doit être identique : initiales en majuscule, autres lettres en minuscule\n",
    " - Les lignes avec des données inutilisables doivent être supprimées\n",
    " - Les données sont triées à l'identique : années (↑), puis gender (↑), puis births (↓) et enfin name (↑)\n",
    " - L'index du DataFrame doit aller de 0 à N-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def df_names_fr():\n",
    "    # genres\n",
    "    d = {'1': 'M', '2': 'F'}\n",
    "    # read_csv\n",
    "    df = pd.read_csv('nat2019.csv',\n",
    "                      sep=';',\n",
    "                      header=0,\n",
    "                      names=['gender', 'name', 'year', 'births'],\n",
    "                      converters={\n",
    "                          'gender': d.get,\n",
    "                          'name': str.title\n",
    "                      })\n",
    "    # clean\n",
    "    df = df.loc[(df['name'].str.len() > 1)\n",
    "                & (df['year'] != 'XXXX')\n",
    "                & ~df['name'].str.startswith('_')]\n",
    "    # types\n",
    "    df['year'] = df['year'].astype(int)\n",
    "    # ordre colonnes\n",
    "    df = df[['year', 'name', 'gender', 'births']]\n",
    "    # tri\n",
    "    df = df.sort_values(['year', 'gender', 'births', 'name'],\n",
    "                   ascending=[True, True, False, True])\n",
    "    df = df.reset_index(drop=True)\n",
    "    \n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%time\n",
    "df_fr = df_names_fr()\n",
    "df_fr.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# head\n",
    "df_fr.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# prénom NA\n",
    "df_fr.loc[df_fr['name']=='Na']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# impact du converters / name\n",
    "d = {'1': 'M', '2': 'F'}\n",
    "\n",
    "df = pd.read_csv('nat2019.csv',\n",
    "                  sep=';',\n",
    "                  header=0,\n",
    "                  names=['gender', 'name', 'year', 'births'],\n",
    "                  converters={\n",
    "                      'gender': d.get,\n",
    "                      #'name': str.title\n",
    "                  })\n",
    "\n",
    "df['name'].isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# capitalize\n",
    "'JEAN-MARIE'.capitalize()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# title\n",
    "'JEAN-MARIE'.title()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# comment faire title avec capitalize :)\n",
    "'-'.join(map(str.capitalize, 'JEAN-MARIE'.split('-')))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Taux de change\n",
    "\n",
    "On va s'intéresser au dataset des cours des devises de la Banque de France :  http://webstat.banque-france.fr/fr/browseBox.do?node=5385566\n",
    "\n",
    "L'idée est de charger les données, de les nettoyer et de pouvoir accéder aux cours de certaines devises à partir de leur code ISO3.\n",
    " \n",
    "1. Télécharger le dataset des taux de change : http://webstat.banque-france.fr/fr/downloadFile.do?id=5385698&exportType=csv\n",
    "\n",
    "\n",
    "2. Implémenter une fonction qui produit un DataFrame avec les taux de change par date pour une liste de codes ISO3 de devises passée en argument. L'index du DataFrame doit correspondre aux dates (voir la fonction pd.to_datetime() avec le format '%d/%m/%Y'). Les colonnes du DataFrame doivent correspondre aux devises."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def df_taux_change(devises):\n",
    "    df = pd.read_csv(\"Webstat_Export.csv\",\n",
    "                     sep=\";\",\n",
    "                     na_values='-',\n",
    "                     decimal=',',\n",
    "                     skiprows=[0, 1, 3, 4, 5],  # le skiprows permet à l'option \"decimal\" de fonctionner\n",
    "                     converters={0: lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='ignore')})\n",
    "\n",
    "    # extraction des codes monnaies\n",
    "    cols = pd.Series(df.columns.tolist()).str.extract('\\(([A-Z]{3})\\)', expand=True)\n",
    "    cols.iloc[0] = 'Date'\n",
    "    df.columns = cols[0]\n",
    "\n",
    "    # selection des devises\n",
    "    df = df[['Date'] + devises]\n",
    "\n",
    "    # drop na\n",
    "    df = df.dropna()\n",
    "\n",
    "    # set index\n",
    "    df = df.set_index('Date')\n",
    "    \n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%time\n",
    "df_tx = df_taux_change(['CHF', 'GBP', 'USD'])\n",
    "df_tx.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# head\n",
    "df_tx"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Tests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import unittest\n",
    "\n",
    "class Lesson4Tests(unittest.TestCase):\n",
    "    def test_df_names_us(self):\n",
    "        df = df_names_us()\n",
    "        # colonnes\n",
    "        self.assertEqual(list(df.columns), ['year', 'name', 'gender', 'births'])\n",
    "        # lignes\n",
    "        self.assertEqual(len(df), 1989401)\n",
    "        # index\n",
    "        self.assertTrue(isinstance(df.index, pd.core.indexes.range.RangeIndex))\n",
    "        # test NaN\n",
    "        self.assertTrue(df.loc[df.isnull().any(axis=1)].empty)\n",
    "        \n",
    "    def test_df_names_fr(self):\n",
    "        df = df_names_fr()\n",
    "        # colonnes\n",
    "        self.assertEqual(list(df.columns), ['year', 'name', 'gender', 'births'])\n",
    "        # lignes\n",
    "        self.assertEqual(len(df), 615912)\n",
    "        # index\n",
    "        self.assertTrue(isinstance(df.index, pd.core.indexes.range.RangeIndex))\n",
    "        # test names\n",
    "        self.assertTrue(df.loc[df['name'].str.contains('^[A-Z]+(?:-[A-Z]+)?$')].empty)\n",
    "        # test gender\n",
    "        self.assertEqual(len(df), len(df.loc[df['gender']=='F']) + len(df.loc[df['gender']=='M']))\n",
    "        # test NaN\n",
    "        self.assertTrue(df.loc[df.isnull().any(axis=1)].empty)\n",
    "\n",
    "    def test_df_taux_change(self):\n",
    "        df = df_taux_change(['CHF', 'GBP', 'USD'])\n",
    "        # colonnes\n",
    "        self.assertEqual(list(df.columns), ['CHF', 'GBP', 'USD'])\n",
    "        # index\n",
    "        self.assertTrue(isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex))\n",
    "        # types taux\n",
    "        self.assertTrue((df.dtypes == 'float').all())\n",
    "        # test NaN\n",
    "        self.assertTrue(df.loc[df.isnull().any(axis=1)].empty)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# run tests\n",
    "def run_tests():\n",
    "    test_suite = unittest.makeSuite(Lesson4Tests)\n",
    "    runner = unittest.TextTestRunner(verbosity=2)\n",
    "    runner.run(test_suite)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# run tests\n",
    "\n",
    "run_tests()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Un peu de Data Science...\n",
    "\n",
    "**Question n° 1**\n",
    "\n",
    "Pourquoi le value_counts() du \"gender\" donne-t-il un tel écart entre F et M ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# value_counts du gender\n",
    "\n",
    "df_us['gender'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pct_change\n",
    "\n",
    "df_us['gender'].value_counts().pct_change()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Question n° 2**\n",
    "\n",
    "Pourquoi le value_counts() du \"name\" donne-t-il ce résultat ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# value_counts du gender\n",
    "\n",
    "df_us['name'].value_counts().head(16)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Question n° 3**\n",
    "\n",
    "Pourquoi le value_counts() du \"year\" donne-t-il ce résultat ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# value_counts du gender\n",
    "\n",
    "df_us['year'].value_counts().head(16)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercice n° 1**\n",
    "\n",
    "Donnez le prénom qui a été le plus donné lors d'une année."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercice n° 2**\n",
    "\n",
    "Donnez la liste des prénoms qui contiennent dans l'ordre a, e, i, o et u (US) ou bien a, e, i et o (FR)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Méthodes de reshaping (1)\n",
    "\n",
    "#### pivot_table\n",
    "\n",
    "La méthode pivot_table() prend en argument :\n",
    "- values : valeurs qui doivent être agrégées selon les modalités de la colonne passée en \"index\" et de la colonne passée en \"columns\"\n",
    "- index : colonne(s) dont les valeurs vont servir d'index à la table pivot\n",
    "- columns : colonne(s) dont les valeurs vont servir de colonnes à la table pivot\n",
    "- aggfunc : fonction d'aggrégation des values, par défaut 'mean', 'median', 'min', 'max', 'count', 'sum', 'nunique', et n'importe quelle lambda ou liste de fonctions.\n",
    "\n",
    "On obtient NaN s'il n'y a pas d'occurence croisée.\n",
    "\n",
    "Excel = tableau croisé dynamique."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# exemple\n",
    "df = pd.DataFrame([{'A': 1,'B': 1, 'C': 1},\n",
    "                   {'A': 1,'B': 1, 'C': 2},\n",
    "                   {'A': 1,'B': 2, 'C': -1},\n",
    "                   {'A': 2,'B': 1, 'C': 4},\n",
    "                   {'A': 2,'B': 1, 'C': 5},\n",
    "                  ])\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# exemple\n",
    "df.pivot_table(values='C',\n",
    "              index='A',\n",
    "              columns='B',\n",
    "              aggfunc='mean')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercice n° 3**\n",
    "\n",
    "Calculez une table pivot avec le nombre total de naissances par année et par genre."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercice n° 4**\n",
    "\n",
    "Calculez une table pivot avec la diversité des prénoms (nombre de prénoms distincts) par année et par genre."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### crosstab\n",
    "\n",
    "crosstab() est une fonction de reshaping qui prend 2 colonnes d'un DataFrame en argument et produit le décompte croisé des occurrence.\n",
    "\n",
    "On obtient 0 s'il n'y a pas d'occurence croisée."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# exemple\n",
    "pd.crosstab(df['A'], df['B'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# initial\n",
    "df_us['initial'] = df_us['name'].str[0].str.upper()\n",
    "# terminal\n",
    "df_us['terminal'] = df_us['name'].str[-1].str.upper()\n",
    "\n",
    "df_us.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# crosstab\n",
    "pd.crosstab(df_us['initial'], df_us['terminal'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pivot_table\n",
    "df_us.pivot_table(values='name',\n",
    "                  index='initial',\n",
    "                  columns='terminal',\n",
    "                  aggfunc='nunique')#.fillna(0).astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Z x Z\n",
    "df_us.loc[(df_us['initial'] == 'Z') & (df_us['terminal'] == 'Z')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Z x Z\n",
    "df_us.loc[df_us['name'].str.startswith('Z') & df_us['name'].str.endswith('z')]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
