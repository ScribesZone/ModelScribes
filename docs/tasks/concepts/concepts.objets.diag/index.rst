.. _`tâche concepts.objets.diag`:

tâche concepts.objets.diag
==========================

:résumé: L'objectif de cette tâche est de créer des diagrammes
    d'objets.

:langage:  :ref:`ObjectScript1`
:artefacts:
    * ``concepts/objets/o<N>/diagrammes/o<N>.obd.olt``
    * ``concepts/objets/o<N>/diagrammes/o<N>.obd.png``

(A) Diagrammes
--------------

Pour produire un diagramme d'objets procéder de manière analogue à la
production de diagrammes de classes.

Lancer l'outil USE avec la
commande suivante (remplacer ``<N>`` par le numéro du modèle d'objets) : ::

    use concepts/classes/classes.cl1 concepts/objets/o<N>/o<N>.ob1

Utiliser le menu ``View > Create View > Object Diagram``.

De manière analogue à la création de diagramme de classes il s'agit de
produire deux fichiers :

*   le diagramme lui même, ``concepts/objets/o<N>/diagrammes/o<N>.obd.olt``
    (".olt" est un acronyme pour OBject Layout).

*   le diagramme sous forme de copie d'écran
    (``concepts/objets/o<N>/diagrammes/o<N>.obd.png``).

NOTE1: La disposition des objets doit autant que possible refléter
la disposition du diagramme de classes.

NOTE2: La création des diagrammes d'objets et de classes est similaire
dans le principe. Se référer à la :ref:`tâche concepts.classes.diag` si
nécessaire).

(B) ObjetsIsoles
----------------

Observer la présence ou non d'objets isolés dans le diagramme, des objets
ou groupe d'objets connectés à aucun autre. Vérifier s'il s'agit d'un
problème dans le modèle d'objets textuel lui même ou un problème dans
la traduction qui en a été faite.
