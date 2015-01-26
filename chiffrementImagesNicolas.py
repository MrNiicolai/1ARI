import pygame, sys
from pygame.locals import *
pygame.init()
import numpy

def ouExclusif(bit1, bit2):
    if bit1 == bit2:
        return 0
    else:
        return 1

def conversionBinaire(entier):
    listeReste = []
    listeResteOrdonnée  = []
    difference = 0
    resultatBinaire = ''
    while entier >= 2:
        listeReste.append(entier%2)
        entier = entier//2
    listeReste.append(entier%2)
    if len(listeReste)<8: #Test si listeReste a une longueur inférieur à 8
        difference = 8 - len(listeReste)
        for i in range(difference): #Boucle for rajoutant difference fois de 0 pour que la chaîne de caractères finale...
            listeReste.append(0) #...en comporte bien 8
    for i in range(len(listeReste)-1, -1, -1): #Boucle for permettant d'inverser la listeReste pour qu'elle soit ordonnée...
        listeResteOrdonnée.append(listeReste[i]) #...et ainsi lire le bon résultat
    for i in range(len(listeResteOrdonnée)):
        resultatBinaire += str(listeResteOrdonnée[i])
    return resultatBinaire

def ouExclusifEntiers(entier1, entier2):
    listeResultatOuExclusif = ''
    entier1 = conversionBinaire(entier1)
    entier2 = conversionBinaire(entier2)
    for x, y in zip(entier1, entier2):
        resultatOuExclusif = ouExclusif(x, y)
        listeResultatOuExclusif += str(resultatOuExclusif)
    return int(listeResultatOuExclusif)

def ouExclusifTuples(tuple1, tuple2):
    tupleResultat = []
    for entier1, entier2 in zip(tuple1, tuple2):
        resultat = ouExclusifEntiers(entier1, entier2)
        tupleResultat.append(resultat)
    return tuple(tupleResultat)
        
def creationImage(l, h, nomImage):
    fenetre = pygame.display.set_mode((l, h))
    pygame.display.set_caption('Arithmétique et cryptographie | Mini-Projet 1ARI')
    surface = pygame.surfarray.pixels2d(pygame.Surface((l, h)))  # création d'un tableau de pixels de dimensions l*h
    pixel = (numpy.random.rand(l, h) * 255 * 255 * 255)
    pygame.surfarray.blit_array(fenetre, pixel)  # affichage des pixels sur la fenêtre
    pygame.image.save(fenetre, nomImage)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

'''def chiffrageImage(l, h, nomFichier1, nomFichier2, nomFichier3):'''

print(ouExclusif(1, 1))
print(conversionBinaire(77))
print(conversionBinaire(88))
print(ouExclusifEntiers(77, 88))
print(ouExclusifTuples((200, 77, 125), (104, 77, 194)))
creationImage(500, 500, 'imageChiffree.bmp')
'''chiffrageImage(500, 500, 'nomFichier1', 'nomFichier2', 'nomFichier3')'''


