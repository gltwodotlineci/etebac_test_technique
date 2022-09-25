#CONSTRUIR UN RELEVE DE COMPTE PARTIR D'UN FICHIER SELON LA NORME CFONB.#

Un client a besoin de votre aide. Sa banque envoie son relevé de compte en document text transmis par ETEBAC. 
Avec ce protocole, les données sont envoyées sous une chaine de caractères sans virgule ou point virgule pour distinguer les colonnes. C'est là que nous avons besoin de votre aide.
Il faut faire de sort de créer les colonnes selon les 4 premières tables du document "CFONB - Structure des fichiers ETEBAC3.pdf". ***01 Entête : Ancien Solde***, ***04 Ecriture Détail***, ***05 Libellé complémentaire*** et ***07 Nouveau Solde***. 
Ses tables vous donnent les indices de positionnement des variables que  vous êtes sensé à  créer sur la nouvelle base de données avec des colonnes distinguées.

certaines lignes de ce document ressemblent aux 3 lignes suivantes:

0112300453    222102EUR256    LIB123000451299   0000000004567
07232222122345222202EUR333123  45 21987654322   0000000100000
01111111111   221111EUR224     NOminal 123412   0000000001000

# Atention !!! #
Il pourrait que le fichier se lit comme une grande chaine de caractères, en donnant l'impression que le document est juste une ligne avec une centaine des milliers de caracterès.
En réalité les lignes existent et si on ouvre le document avec notepad++ on verra à la fin de chaque ligne il y a le symbole LF (voir ASCII). On pourra utiliser cet indice pour lire correctement le document.
