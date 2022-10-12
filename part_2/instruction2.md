#CONSTRUIR UN RELEVE DE COMPTE PARTIR D'UN FICHIER SELON LA NORME CFONB.

Un client a besoin de votre aide. Sa banque envoie son relevé de compte en document text transmis par ETEBAC. 
Avec ce protocole, les données sont envoyées sous une chaine de caractères sans virgule ou point virgule pour distinguer les colonnes. C'est là que nous avons besoin de votre aide.
Il faut faire de sort de créer les colonnes selon les 4 premières tables du document "CFONB - Structure des fichiers ETEBAC3.pdf". ***01 Entête : Ancien Solde***, ***04 Ecriture Détail***, ***05 Libellé complémentaire*** et ***07 Nouveau Solde***. 
Ses tables vous donnent les indices de positionnement des variables que  vous êtes sensé à  créer sur la nouvelle base de données avec des colonnes distinguées.

* Dans la partie 1, ignorez l'enregistrement suplémentaire 05 *
certaines lignes de ce document ressemblent aux 3 lignes suivantes:

0112300453    222102EUR256    LIB123000451299   0000000004567
07232222122345222202EUR333123  45 21987654322   0000000100000
01111111111   221111EUR224     NOminal 123412   0000000001000

# Atention !!! #
Il pourrait que le fichier se lit comme une grande chaine de caractères, en donnant l'impression que le document est juste une ligne avec une centaine des milliers de caracterès.
En réalité les lignes existent et si on ouvre le document avec notepad++ on verra à la fin de chaque ligne il y a le symbole LF (voir ASCII). On pourra utiliser cet indice pour lire correctement le document.

----------------------------------------------------------------------------
Dans la deuxième partie il faut reprendre l'autput de la partie 1 avec certains changements
a) Le dattes des 3 types d'engistrements sont donnée en chaine de caracteres. Il faut 
    les convertir en dattes.

b) le montant est donné en chaine de characteres et en centimes. Il faut le transformer
    en décimales. Par example pour 000000115 il faut le convertir en 1.15 euros

c) Il faut donner le montant créditeur ou débiteur.
Pour identifier si le montant est Créditeur ou Débiteur le protocole ETEBAC donne
l'indice sur le 104-ième charactere de chaque ligne. L'indice donnée est une combinaison
entre le système hexadécimal et le codage ASCII. Pour vous faciliter la tache nous
donnons la traduction des symboles. Pour les lettres de A  jusque à I et le charactere '{'
il s'agit d'un montant créditaire et pour les lettres de J jusque à R et le charchtere '}'
il s'agit d'un montant débit. 
