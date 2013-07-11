Dive Into Python 3
==================

Projet de traduction fr
-----------------------

TODO: expliquer le projet, comment participer, qui contacter, à quelle on mange, pourquoi les escargots n'ont pas de dents...

GIT : petit guide à l'usage du débutant
---------------------------------------

Git est un système de gestion de versions décentralisé [DVCS](https://en.wikipedia.org/wiki/Distributed_revision_control). Voilà pour les gros mots. 

Passons maintenant à quelque chose de compréhensible pour l'humain courant. Ce guide doit vous mettre le pied à l'étrier du projet de traduction de Dive Into Python 3.

### Git : kesako ?

Git permet de gérer des versions de fichiers. Grâce à Git, on sait qui a fait quoi et à quel moment. Le savoir c'est bien, mais en faire quelque chose c'est mieux. Grâce à cette faculté de versionning, il est ainsi possible de voyager dans le temps : essayer de nouvelles choses, revenir en arrière... Moultes possibilités à découvrir.

### Je n'y connais rien. Que fais je ?

Eh bien vous apprenez. Pas de panique : inutile d'avoir fait Polytechnique. La courbe d'apprentissage des commandes de base est très rapide. Vous allez apprendre comment fonctionne Git avec des explications pour être humain et comment utiliser les commandes de base de Git : clone, pull, push, log, commit, branch, status...

#### Installation

Pour utiliser Git, il vous faut tout d'abord [l'installer sur votre poste](http://git-scm.com/book/fr/D%C3%A9marrage-rapide-Installation-de-Git). L'installation est très simple et surtout, Git est disponible sur de nombreux systèmes, même si vous n'utilisez pas un système libre (tant pis pour vous). 

Cette installation ne concerne que le moteur. Vous n'aurez besoin de rien d'autre mais vous pouvez aussi faire le choix d'y ajouter une interface graphique. Le présent guide vous donnera les bases de l'utilisation en ligne de commande (donc sans interface graphique).

#### Principes de fonctionnement

Les principes sont assez simples :
  * Créer un nouveau dépôt ou copier un dépôt existant. En langage Git, copier s'appelle cloner.
    
    Dans les deux cas, cela revient au même : vous disposez localement d'un dépôt sur lequel vous allez pouvoir travailler.
    
  * Travailler sur votre dépôt.
  
    Une fois satisfait de votre modification ou de votre ajout, vous pouvez versionner vos modifications. En langage Git, on parle de commit. Ce commit crée une nouvelle version du fichier. S'il s'agit d'un nouveau fichier, ce sera la première version.

  * Versionner vos modifications → Créer un commit. 

    Vos commits sont dans votre dépôt local. Vous avez alors la possibilité de les publier vers le dépôt initial ou même vers un autre dépôt. En langage Git, on parle de push. Si vous ne disposez pas des droit de publication sur dépôt distant, vous pouvez aussi proposer vos modifications au responsable du dépôt. En langage Git on parle de pull request.

  * Publier vos modifications.
    
En résumé, vous créez un dépôt local, vous travaillez, vous committez et vous publiez. Facile, non ?

#### Du rêve à la réalité

Concrètement, voici ce que ça donne pour ce projet. Commençons pas cloner joyeusement le projet. Dans votre dossier personnel, placez vous à l'endroit où vous souhaitez créer votre dépôt local puis exécutez la commande de clonage

```bash
$ git clone https://github.com/framasoft/plongez-dans-python3.git
```

Vous devriez obtenir le résultat suivant. Vous remarquerez que cette opération crée automatiquement un dossier dans lequel figurera votre dépôt :
    
```bash
Cloning into 'plongez-dans-python3'...
remote: Counting objects: 5482, done.
remote: Compressing objects: 100% (3893/3893), done.
remote: Total 5482 (delta 1587), reused 5471 (delta 1579)
Receiving objects: 100% (5482/5482), 25.51 MiB | 1.92 MiB/s, done.
Resolving deltas: 100% (1587/1587), done.
```

Faites une modification. Vous pouvez obtenir à tout moment le statut de votre dépôt :

```bash
$ git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	README.md
nothing added to commit but untracked files present (use "git add" to track)
```

Ici un fichier README.md a été ajouté mais n'a pas encore été committé. Git le voit et vous informe qu'il existe mais ne le suit. Vous pouvez obtenir d'autres types de réponses de statut pour les fichiers déjà suivis et ayant fait l'objet d'une modification

```bash
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   README.md
#
```
    
Ajoutons maintenant le fichier au suivi de version et committons. L'opération se déroule donc en deux fois : add puis commit. Un commit est toujours accompagné d'un message expliquant ce que vous avez fait.

```bash
$ git add README.md 
$ git commit -m "Ajout du README.md" 
[master 2c53431] Ajout du README.md
 1 file changed, 80 insertions(+)
 create mode 100644 README.md
```

Il ne reste plus qu'à publier la modification sur le dépôt distant :

```bash
$ git push origin master
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 2.14 KiB, done.
Total 3 (delta 1), reused 0 (delta 0)
To https://github.com/framasoft/plongez-dans-python3.git
   67ef8e6..2c53431  master -> master
```

#### C'est bien joli, mais je ne suis pas tout seul

Effectivement, d'autres que vous travaillent sur cette traduction. Il faut donc que vous puissiez récupérer leurs modifications. Encore une fois, c'est un jeu d'enfant. Placez vous simplement dans votre dépôt et magie :

```bash
$ git pull origin master
From https://github.com/framasoft/plongez-dans-python3
 * branch            master     -> FETCH_HEAD
Already up-to-date.
```

Ici ce n'est pas très parlant : le dépôt local était déjà à jour. Mais c'est bien là que vous verrez apparaître toutes les modifications de vos petits camarades. Attention, si vous avez des modifications en cours, Git refusera de faire l'opération de pull. Il suffit de mettre de côté vos modifications, de récupérer la dernière version du dépôt distant puis d'y appliquer vos modifications en cours. En langage git, ça donne ça :

```bash
$ git stash
Saved working directory and index state WIP on master: 7583460 README : coloration syntaxique pour les blocs de code
HEAD is now at 7583460 README : coloration syntaxique pour les blocs de code
```

puis :

```bash
$ git pull origin master
```

et enfin :

```bash
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   README.md
#
no changes added to commit (use "git add" and/or "git commit -a")
```

#### Origin master : c'est quoi cette bouteille de lait ?

Lors des opérations de récupératio (pull) et publication (push), vous avez utilisé des choses inconnues : origin master. Tout d'abord, c'est dangereux d'exécuter une commande sans savoir ce qu'elle fait :) . Bon, ici aucun chaton n'a été tué, l'honneur est sauf. Mais alors qu'est ce que c'est que ce 'origin master' ?

Votre dépôt local est autonome. Vous pouvez n'utiliser que lui et ne jamais rien publier. Mais si vous souhaitez contribuer à un autre dépôt, il y a un moment où votre votre dépôt local doit connaitre un plusieurs dépôts externes vers lesquels il pourra publier ou desquels il pourra récupérer des mise à jour. En langage Git, cela s'appelle un remote. Un remote est un dépôt distant qui est associé au votre. 

Par ailleurs, votre dépôt local peut être associé à plusieurs remotes. Il faut donc un moyen de différencier ces remotes. Ils sont donc nommés. 

Enfin, un remote contient au moins une branche, il faut donc pouvoir identifier la branche distante avec laquelle vous souhaitez communiquer. Comment ça vous ne savez pas ce qu'est une branche ? Un peu de patience, ça vient.

Pour en revenir à ce qui nous intéresse, origin est donc un dépôt distant et master une branche dans ce dépôt. La magie, c'est que vous n'avez rien fait pour créer ou nommer ce remote. En fait, Git l'a fait tout seul comme un grand lorsque vous avez cloné le dépôt. Vous pouvez voir les dépôts auxquels vous être abonnés avec une simple commande :

```bash
$ git remote -v
origin	git@github.com:framasoft/plongez-dans-python3.git (fetch)
origin	git@github.com:framasoft/plongez-dans-python3.git (push)
no changes added to commit (use "git add" and/or "git commit -a")
```

Il y a beaucoup de choses que l'on peut faire avec les remotes. Il y a cependant de grandes chances que cette simple commande vous soit suffisante dans le cadre de ce projet.

#### Jardinons un peu : les branches

Pour en terminer avec ce petit voyage au pays de Git, soyons un peu bucoliques. Lorsque vous créez ou clonez un dépôt, Git crée une branche par défaut appelée master. Une branche est une sorte de copie du dépôt (en fait Git ne copie pas vraiment les données, mais nous n'irons pas aussi loin). Vous pouvez alors travailler sur cette copie sans impacter les autres branches : toute ce qui est committé dans cette nouvelle branche n'apparaîtra pas dans les autres. Si au final vous êtes satisfaits de votre travail, il ne vous reste plus qu'à commiter vos modifications dans cette branche puis à les rapatrier dans la branche master. En langage Git, on parle de merge. Mais vous pouvez aussi ne pas être content de ce que vous avez fait et ne pas vouloir conserver ces modifications. Il suffit de les committer puis de supprimer la nouvelle branche. 

Pour connaitre la liste des branches de votre dépôt local : 

```bash
$ git branch
* master
```

Pour créer une nouvelle branche :

```bash
$ git branch maNouvelleBranche
$ git branch
  maNouvelleBranche
* master
```

L'astérisque vous indique le dépôt sur lequel vous travaillez. Changeons de branche pour travailler sur maNouvelleBranche :

```bash
$ git checkout maNouvelleBranche 
M	README.md
Switched to branch 'maNouvelleBranche'
gilles@Arctica:~/Developpement/Python/DiveIntoPython3$ git branch 
* maNouvelleBranche
  master
```

L'astérisque vous montre que vous êtes désormais sur la branche maNouvelleBranche.

#### Faites le petit chef : lister les commits

Dans votre activité professionnelle, vous avez sûrement un (petit) chef qui vient vous voir 20 fois par jour en vous disant "Alors, t'en es où ?". Oui, c'est énervant. 

Mais Git est un gars calme et posé qui répondra toujours à vos sollicitations. Alors n'hésitez pas à faire le chef :

```bash
$ git log
commit 35c2a4c061a953e0ced1f69b0ecaabc1dbb224cd
Author: Sinma <eichi237@mailoo.org>
Date:   Sat Jul 6 23:08:02 2013 +0200

    Correction d’espace insécable (mode typo nazi)

commit 0262e7670d638e98db2e0aee34592612522da980
Author: Sinma <eichi237@mailoo.org>
Date:   Sat Jul 6 22:37:39 2013 +0200

    Réorganisation de «Principes de fonctionnement» et simplification de la présentation des commandes
    
    Dans la partie «Principes de fonctionnement», j’ai placé le texte explicatif avant la description pour les deux derniers points de la liste.
    
    J’ai aussi supprimé ce qu’il y avait avant le $ pour les lignes de commandes, ça risque moins de provoquer la confusion (moi-même je n’ai pas comp

commit f38a3530decc51c6ec72163f9595387409e506af
[...]
```
Vous pouvez naviguer dans l'historique des commits avec les flèches haut et bas de votre clavier. Quittez avec q.

Vous avez désormais les armes pour démarrer. Il y a énormément d'autres choses que vous pouvez faire avec Git mais ce n'est pas l'objet de ce tutoriel. Pour savoir comment faire telle ou telle chose, vous pouvez consulter le [Git Book](http://git-scm.com/book/fr/) ou solliciter la [liste de discussion](http://www.framalistes.org/sympa/info/plongez-dans-python-3). 
