..  _`tâche bd.sql.schema`:

tâche bd.sql.schema
===================

:résumé: L'objectif de cette tâche est d'implémenter le schéma
    SQL de la base de données en partant du modèle de relations.

:langage: SQL
:artefacts:
    * ``bd/sql/schema/schema.sql``

Introduction
------------

Il s'agit d'implémenter en SQL le schéma de la base de données. Si un
modèle de relations existe alors on cherchera a réaliser une traduction
aussi fidèle et homogène que faire se peut.

..  attention::

    Dans certains cas une base de données appelée "CyberMovies" peut
    être fournie à titre d'exemple. Pour vérifier si c'est le cas ouvrir
    ouvrir le fichier ``bd/sql/schema/schema.sql`` et observer son
    contenu. Si cet exemple n'est pas fourni, dans les tâches
    ci-dessous le schéma et les données devront être créés avant toute
    chose.

    Au contraire si l'exemple CyberMovies est fourni alors les ressources
    associées peuvent servir à comprendre/tester la création d'une
    base de données, à réaliser des premières requêtes, etc. Dans ce cas
    il est alors fortement conseillé d'utiliser tout d'abord
    cette base et de lire/tester toutes les tâches ``bd.sql.*``
    avant de commencer à écrire le nouveau schéma de données.

(A) Schéma
----------

Implémenter le schéma relationnel en SQL revient concrètement
à écrire différentes instructions ``CREATE TABLE``. Ces instructions
doivent être écrites dans le fichier ``schema.sql``.
Se référer à la documentation du SGBD utilisé pour connaître le détail de
la syntaxe SQL, les types de données disponibles, la manière d'écrire
les contraintes, etc.

Voici a titre d'illustration une instruction SQL de
création de table.

..  code-block:: sql

    CREATE TABLE Opinions(
        spectator VARCHAR(100),     -- => Spectators.name
        movie VARCHAR(100),         -- => Movies.title
        stars INTEGER,              -- BETWEEN 0 AND 5

        CONSTRAINT PK
            PRIMARY KEY (spectator, movie),
        CONSTRAINT Dom_stars
            CHECK (stars IN ('0', '1', '2', '3', '4', '5')),
        CONSTRAINT FK_spectator
            FOREIGN KEY (spectator) REFERENCES Spectators(name),
        CONSTRAINT FK_movie
            FOREIGN KEY (movie) REFERENCES Movies(title)
    );

..  note::

    Comme on le voit certaines normes de programmation doivent
    être suivies :

    *   tous les mots clés SQL doivent être en majuscules,

    *   l'indentation de 4 ou 8 espaces comme ci-dessus doit être respectée,

    *   les contraintes doivent être définie de manière standardisée
        comme ci-dessus.

            * ``PK`` signifie Primary Key
            * ``Dom_<attributs>`` pour les contraintes sur un domaine
            * ``FK_<name>`` pour les contraintes d'intégrité référentielle


(B) Automatisation
------------------

Un script de création ``bd/sql/cree-la-bd.sh`` a pour rôle d'automatiser
la création de la base de données à partir du schéma. Le contenu de
ce script est fourni pour le SGBD ``sqlite``. Il pourra dans ce cas être
utilisé tel quel. Si un autre SGBD est utilisé, ce script peut être
réécrit/adapté, l'objectif étant d'avoir une seule et unique commande
pour créer la base de données.

Avec sqlite entrer la commande suivante à partir du répertoire
``bd/sql/``: ::

    cree-la-bd.sh

Ce script crée une base de données vide ``bd/sql/bd.sqlite3`` et charge
le schéma ``bd/sql/schema/schema.sql``. L'exécution du script devrait
ressembler à cela : ::

    Nettoyage de la base de données ... fait.
    Chargement du schéma ... done.
    Base de données vide créée.

..  attention::
    Faire attention aux éventuelles erreurs produites lors de la
    création. Le script ne teste pas les erreurs, elles sont simplement
    affichées.

Se référer éventuellement au contenu du script pour plus d'information ;
pour changer par exemple la localisation de la base de données. Si un autre
SGBD est utilisé le contenu de ce script devra être adapté.

(C) Vérifications
-----------------

Une fois la base de données créée il est possible si on le désire
d'utiliser le SGBD selectionné (ici sqlite3) pour consulter le schéma et
le contenu de la base de données.

..  attention::

    L'exemple ci-dessous suppose que l'exemple CyberMovies est disponible.

::

    $ sqlite3 bd.sqlite3
    SQLite version 3.22.0
    Enter ".help" for usage hints.
    sqlite> .tables
    Cinemas     Frequents   IsOn        Movies      Opinions    Spectators
    sqlite> SELECT * FROM Cinemas ;
    sqlite>

Comme on peut le voir avec la dernière requête le contenu de la base
de données est initialement vide. La :ref:`tâche bd.sql.jdd`
montre comment remplir la base avec un jeux de données (jdd).

(Z) Suivi et status
-------------------

**Suivi**: Des questions ou des hypothèses ? Voir la
:ref:`tâche projet.suivis`.

**Status**: Avant de terminer cette tâche écrire le status. Voir la
:ref:`tâche projet.status`.