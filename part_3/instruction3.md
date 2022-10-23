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
Dans la deuxième partie il faut reprendre l'output de la partie 1 avec certains changements
a) Le dates des 3 types d'enregistrements sont donnés en chaine de caractères. Il faut
    les convertir en dattes.

b) le montant est donné en chaine de caractères et en centimes. Il faut le transformer
    en décimales. Par exemple pour 000000115 la convertion est 1.15 euros (voir "Nombre de décimales"
    dans les tables du document CFONB). Le montant il faut aussi le créditer comme montant créditeur ou débiteur.( voir b.1)

b.1) Il faut donner le montant créditeur ou débiteur.
Pour identifier si le montant est Créditeur ou Débiteur le protocole ETEBAC donne
l'indice sur le 104-ième caractère de chaque ligne. L'indice donné est une combinaison
entre le système hexadécimal et le codage ASCII. Pour vous faciliter la tache nous
donnons la traduction des symboles. Pour les lettres de A  jusque'à I et le caractère '{'
il s'agit d'un montant créditeur et pour les lettres de J jusque'à R et le carchtère '}'
il s'agit d'un montant débiteur.

-----------------------------------------------------------------------------------------------
Dans la troisième partie il faut traiter les données par bloc.
Pour comprendre mieux il est nécessaire d'ajouter quelque information sur la base de données.

Le document Relevé de compte en txt nous donne les informations suivantes: Le numéro de la banque . Les numéros de
compte (il y a plusieurs) et les types des opérations. Un numéro de compte peut y avoir plusieurs extraits de comptes
(si le document inclus plusieurs jours). Un extrait de compte commence par le code d'enregistrement "04" qui représente
l'ancienne solde et termine par le code d'enregistrement "07" qui représente la fin de l'extrait (nouveau solde). Entre
les deux nous avons les types d'opérations qui sont identifié par le code d'enregistrement "04". Si la ligne du code 
d'enregistrement "04" est suivie par des lignes avec le code "05", tous les lignes "05" ne sont rien d'autre que des
informations suplémentaires du code "04".

Docn nous pouvons avoir, ce type de donnés:

0112240    00974EUR2 30000899222  260322                                                  0000000415454R
0412240000200974EUR2E3000089922202260322  222822REM CHQTLC 909784921182022                0000000000714E                
0512240000200974EUR2E3000089922202260322   22LIB00000380508685700021139681404                            
0712240    00974EUR2 30000899222  290322   22                                             0000000414740M                
0112240    00974EUR2 30003393222  260322   22   ** PAS DE MOUVEMENT11E JOUR **            0000000342123D           
0712240    00974EUR2 30003393222  290322   22   -------------------11---------            0000000342123D      
0112240    00974EUR2 30000899222  260322                                                  0000000414740R
0412240000200974EUR2E3000089922202260322  222822REM CHQTLC 909784921182022                0000000002000E                
0512240000200974EUR2E3000089922202260322   Rembourssement, Banque Abcd type alpha1                      
0512240000200974EUR2E3000089922202260322   Autre description complementaire le meme type
0512240000200974EUR2E3000089922202260322   d'opération mais utilisation des lignes supplémentaires                           
0712240    00974EUR2 30000899222  290322   11                                             0000000412740M 
0112240    00974EUR2 30003393222  260322                                                  0000000342123D
0412240000200974EUR2E3000089922202260322      CB                                          0000000002500E                
0712240    00974EUR2 30003393222  290322                                                  0000000344623D

Si Nous Ajoutons les colonnes pour mieux comprendre les données, nous aurons la forme suivante.

Code    
Enreg-  
istre-  Code       Autres       Nr de            Date       Libéllé de l'opération            Montant Crédit    Nr d'ex-                  
ment    Banque     déails       compte                                                        ou Débit          trait!!!

01      12240      00974EUR2    30000899222     260322                                        0000000415454R        1
04      12240  000200974EUR2E   30000899222     260322  222822REM CHQTLC 909784921182022      0000000000714E        1        
05      12240      00974EUR2E   30000899222     260322   22LIB00000380508685700021139681404                         1  
07      12240       0974EUR2    30000899222     290322   22                                   0000000414740M        1        
01      12240      00974EUR2    30003393222     260322   22   ** PAS DE MOUVEMENT11E JOUR **  0000000342123D        1   
07      12240      00974EUR2    30003393222     290322   22   -------------------11---------  0000000342123D        1
01      12240      00974EUR2    30000899222     260322                                        0000000414740R        1
04      12240    0200974EUR2E   30000899222     260322  222822REM CHQTLC 909784921182022      0000000002000E        1        
05      12240    0200974EUR2E   30000899222     260322   Rembourssement, Banque Abcd                                1
05      12240    0200974EUR2E   30000899222     260322   Autre description complementaire                           1
05      12240    0200974EUR2E   30000899222     260322   sur le meme opération utilisation                          
05      12240    0200974EUR2E   30000899222     260322   des lignes supplémentaires                                 1
07      12240      00974EUR2    30000899222     290322   11                                   0000000412740M        1
01      12240      00974EUR2    30003393222     260322                                        0000000342123D        2
04      12240      00974EUR2E   30000899222     260322   CB                                   0000000002500E        2        
071     2240       00974EUR2    30003393222     290322                                        0000000344623D        2


Il faut noter la colonne Nr d'extrait. Cela On doit l'ajouter pour identifier chaque extrait de compte pour chaque N°
de compte. par exemple:

Nr de       Date        Opération           Nr d'éxtrait      Code Enregist-
compte                                      de compte          rement

11111       260322      AncienneSolde           1               "01"
11111       270322       CB                     1               "04"
11111       270322      Nouveau Solde           1               "07"
11111       270322      AncienneSolde           2               "01"
11111       280322      Chèque                  2               "04"
11111       280322      Nouvea Solde            2               "07"
11111       280322      AncienneSolde           3               "01"
11111       290322      CB                      3               "04"
11111       290322      Nouvea Solde            3               "07"
22222       260322      AncienneSolde           1               "01"
22222       270322       CB                     1               "04"
22222       270322      Nouveau Solde           1               "07"
22222       270322      AncienneSolde           2               "01"
22222       280322      Chèque                  2               "04"
22222       280322      Nouvea Solde            2               "07"
32321       260322      AncienneSolde           1               "01"
32321       270322      Transfer                1               "04"
32321       270322      Nouveau Solde           1               "07"
32321       270322      AncienneSolde           2               "01"
32321       280322      CB                      2               "04"
32321       280322      Nouvea Solde            2               "07"

Donc si on résume. Un numéro de compte peut avoir plusieurs extraits de comptes. Un extrait de compte commence avec le
code d'enregistrement "01" et finis avec le code "07". Alors pour distinguer les extraits de compte du même Nr de 
compte nous devrons lui ajouter un numéro pour chaque extrait de compte. Donc pour réaliser cela, il faut traiter les
données par bloc.

Une fois que nous avons ajouté les numéros d'extraits de compte. on peut ajouter les libellés supplémentaires de 
l'enregistrement "05" à l'opération avec le code d'enregistrement"04". En faite si la ligne avec le code "04" est suivie
par un ou plusieurs lignes qui commencent avec le code "05" tous les libellés de ses lignes sont liées au libellé de
la dernière ligne avec le code "04"

par exemple:

pour la partie:
01      12240        00974EUR   30000899222     260322             0000000414740R
04      12240    0200974EUR2E   30000899222     260322  Lib 1      0000000002000E                
05      12240    0200974EUR2E   30000899222     260322  lib sup.a        
05      12240    0200974EUR2E   30000899222     260322  lib sup.b
04      12240    0200974EUR2E   30000899222     260322  Lib 2      0000000001000E                
05      12240    0200974EUR2E   30000899222     260322  lib sup.c 
07      12240      00974EUR2    30000899222     290322   11        0000000413740M        

Nous devrons avoir:

01      12240    00974EUR2      30000899222   260322                             0000000414740R
04      12240    0200974EUR2E   30000899222   260322  Lib 1 lib sup.a lib sup.b  0000000002000E
04      12240    0200974EUR2E   30000899222   260322  Lib 2 lib sup.c            0000000001000E                
07      12240      00974EUR2    30000899222   290322   11                        0000000412740M 

## Voir le document output dans 'data' pour avoir une idée sur le resultat. A notter que la clé 'libelle indice': peut faire de la solution pour associer les libelles d'enregistements "05" au "04". Il est pas obligé d'utiliser la meme méthode.
