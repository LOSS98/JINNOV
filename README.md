# Liste des fonctionnalités de la base de donnée

## Comptes administrateurs
Les comptes administrateurs servent à avoir un accès à la partie administrateur du site, et de notamment créer, modifier ou supprimer des articles.
<br>
Informations stockées concernant un compte administrateur :
- Un identifiant unique (nombre entier)
- Son nom complet
- Son adresse e-mail
- Son mot de passe chiffré
- Le sel du chiffrage de  son mot de passe 

## Articles
Informations stockées concernant un article :
- Un identifiant unique (nombre entier)
- L'identifiant unique de son créateur (nombre entier)
- L'heure de publication
- Le titre de l'article
- Le corps de l'article
- Les quelconques fichiers (images) attachés, sous forme d'une liste d'url

La syntaxe du corps de l'article peut éventuellement être du markdown, du html ou alors un langage simplifié qui devra être traduit côté backend.

## Études
Informations stockées concernant une étude qui va être publiée sur le site :
- Un identifiant unique (nombre entier)
- Une date (correspondant à la fin d'étude ?)
- Le nom du client
- Un lien (site web) du client
- Corps de la description de l'étude (similaire au corps d'un article)

## Membres de la junior
Stocker les membres actifs de la junior permet d'avoir une liste facilement modifiable de ces derniers, par exemple dans le panel administrateur du site.

Informations stockées concernant un membre de la junior :
- Son nom complet
- Son email @jinnov-insa.fr
- Son numéro de téléphone	
- Le nom de son pôle
- Le nom de son poste
- Le lien de sa photo de profil


## Traçage des utilisateurs du site
Le fonctionnement est assez basique, lorsqu'il accède au site web, l'utilisateur reçoit un cookie aléatoire qu'il va garder tout le long de sa session. Le cookie va disparaître quand l'utilisateur fermera l'onglet.

Informations stockées concernant un chemin de navigation d'un utilisateur anonyme :
- Date de début
- Date de fin
- Chemin emprunté sous la forme d'une liste de nom de page séparés par des virgules (ex: home>etudes_passees>formulaire_etude)