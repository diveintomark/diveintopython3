Dive Into Python 3
==================

Projet de traduction fr
-----------------------

GIT : petit guide à l'usage du débutant
---------------------------------------

Git est un système de gestion de versions décentralisé [DVCS](https://en.wikipedia.org/wiki/Distributed_revision_control). Voilà pour les gros mots. Passons maintenant à quelque chose de compréhensible pour l'humain courant.

### Git : kesako ?

Git permet de gérer des versions de fichiers. Grâce à Git, on sait qui a fait quoi et à quel moment. Le savoir c'est bien, mais en faire quelque chose c'est mieux. Grâce à cette faculté de versionning, il est ainsi possible de voyager dans le temps : essayer de nouvelles choses, revenir en arrière... Moultes possibilités à découvrir.

### Je n'y connais rien. Que fais je ?

Eh bien vous apprenez. Pas de panique : inutile d'avoir fait Polytechnique. La courbe d'apprentissage des commandes de base est très rapide.

#### Installation

Pour utiliser Git, il vous faut tout d'abord [l'installer sur votre poste](http://git-scm.com/book/fr/D%C3%A9marrage-rapide-Installation-de-Git). L'installation est très simple et surtout, Git est disponible sur de nombreux systèmes, même si vous n'utilisez pas un système libre (tant pis pour vous). 

Cette installation ne concerne que le moteur. Vous n'aurez besoin de rien d'autre mais vous pouvez aussi faire le choix d'y ajouter une interface graphique. Le présent guide vous donnera les bases de l'utilisation en ligne de commande (donc sans interface graphique).

#### Principes de fonctionnement

Les principes sont assez simples :
  * Créer un nouveau dépôt ou copier un dépôt existant. En langage Git, copier s'appelle cloner.
    
    Dans les deux cas, cela revient au même : vous disposez localement d'un dépôt sur lequel vous allez pouvoir travailler.
    
  * Travailler sur votre dépôt.
  * Versionner vos modifications -> Créer un commit. 
  
    Une fois satisfait de votre modification ou de votre ajout, vous pouvez versionner vos modifications. En langage Git, on parle de commit. Ce commit crée une nouvelle version du fichier. S'il s'agit d'un nouveau fichier, ce sera la première version.

  * Publier vos modifications.
  
    Vos commits sont dans votre dépôt local. Vous avez alors la possibilité de les publier vers le dépôt initial ou même vers un autre dépôt. En langage Git, on parle de push. Si vous ne disposez pas des droit de publication sur dépôt distant, vous pouvez aussi proposer vos modifications au responsable du dépôt. En langage Git on parle de pull request.
    
En résumé, vous créez un dépôt local, vous travaillez, vous committez et vous publiez. Facile, non ?

#### Du rêve à la réalité

Concrètement, voici ce que ça donne pour ce projet :

  * Clonons joyeusement le projet : dans votre dossier personnel, placez vous à l'endroit où vous souhaitez créer votre dépôt local puis exécutez la commande de clonage

```
git clone https://github.com/framasoft/plongez-dans-python3.git
```

    Vous devriez obtenir le résultat suivant. Vous remarquerez que cette opération crée automatiquement un dossier dans lequel figurera votre dépôt :
    
```
Cloning into 'plongez-dans-python3'...
remote: Counting objects: 5482, done.
remote: Compressing objects: 100% (3893/3893), done.
remote: Total 5482 (delta 1587), reused 5471 (delta 1579)
Receiving objects: 100% (5482/5482), 25.51 MiB | 1.92 MiB/s, done.
Resolving deltas: 100% (1587/1587), done.
```

  * Faites une modification. Vous pouvez obtenir à tout moment le statut de votre dépôt :

```
Blake:plongez-dans-python3 gcoulais$ git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	README.md
nothing added to commit but untracked files present (use "git add" to track)
Blake:plongez-dans-python3 gcoulais$ 
```

    Ici un fichier README.md a été ajouté mais n'a pas encore été committé. Git le voit et vous informe qu'il existe mais ne le suit.
  

