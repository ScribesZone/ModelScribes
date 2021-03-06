..  _`tâche concepts.classes.diag`:

tâche concepts.classes.diag
===========================

:résumé: L'objectif de cette tâche est de créer un ou plusieurs diagrammes
    de classes.
:langage:  :ref:`ClassScript1`
:artefacts:
    * ``concepts/classes/diagrammes/classes.cld.clt``
    * ``concepts/classes/diagrammes/classes.cld.png``
    * ``concepts/classes/diagrammes/<NOM>.cld.clt``
    * ``concepts/classes/diagrammes/<NOM>.cld.png``


(A) Diagramme global
--------------------

Il s'agit tout d'abord de créer un "diagramme global" de classes.
Un tel diagramme doit présenter toutes les classes du modèle ;
par opposition avec les "vues" qui ne présentent que certaines
classes sélectionnées.

..  note::

    Si une ébauche de diagramme a été fournie le diagramme dessiné
    devra en respecter la disposition.

Pour créer un diagramme de classes utiliser la commande suivante : ::

    use concepts/classes/classes.cl1

Se référer ensuite à la documentation de `USE OCL sur ScribesTools`_.

Respecter impérativement les consignes suivantes :

*   (1) Sauvegarder le diagramme dans le fichier
    ``concepts/classes/diagrammes/classes.cld.clt`` (remplacer le
    fichier existant). Utiliser pour cela la commande ``Save Layout``
    comme indiqué dans la documentation.
    NOTE: Le fichier ``.clt`` ("CLass Layout") contient le diagramme,
    c'est à dire le "graphique", la disposition des classes et des
    associations dans l'espace. Par opposition le fichier ``.cl1``
    contient le modèle de classes, sans aucun rendu graphique.

*   (2) Faire ensuite une copie d'écran du diagramme et remplacer le
    fichier ``concepts/classes/diagrammes/classes.cld.png`` fourni.
    Respecter **impérativement** les noms de fichiers, entre autre
    l'extension ``.png``.

..  attention::
    **les diagrammes doivent impérativement montrer les**
    **cardinalités** ; afficher si possible les noms de rôles ou
    d'associations si le diagramme reste visible. Utiliser le
    menu contextuel (click droit) pour avoir accès à ces options.

(B) Vues
--------

Il peut vous être demandé de réaliser plusieurs diagrammes de vues.
Contrairement au diagramme global qui montre toutes les classes
(et est parfois peu lisible), une "vue" ne montre que certaines classes
sélectionnées, en montrant par exemple le détail de ces classes.

Les classes à masquer peuvent être définies avec le menu contextuel de
l'outil (click droit)

Tout comme pour le diagramme global, les fichiers à produire sont
``concepts/classes/diagrammes/<NOM>.cld.clt|png``
où ``<NOM>`` fait référence au nom de la vue, ``.clt`` fait référence
au diagramme et ``.png`` à la capture d'écran correspondante.



..  _`use ocl`:
    http://scribetools.readthedocs.io/en/latest/useocl/index.html

..  _`USE OCL sur ScribesTools`:
    http://scribetools.readthedocs.io/en/latest/useocl/index.html#creating-diagrams
