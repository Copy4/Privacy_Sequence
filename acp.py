'''
  ******************************************************************************
  * @file    acp.py
  * @author  Alexandre Garcin
  * @version V1.0.0
  * @date    16 March 2021
  * @brief   Privacy Software
  ******************************************************************************
  *
  * REMARK: this program was validated on Python release below:
  *           - Python 3.7.7
  *
  *
  ******************************************************************************
'''

from bdd_mc import *
import numpy as np

class acp:
    def __init__(self):
        import bdd_mc
        import numpy as np

    def run(self, bdd, L):

        M = self.recuperation(bdd, L)
        M_cor = slef.correlation(M)
        V = vecteurs_propres(M_cor)
        nouv_coord = nouvelles_coordonnes(,V)

    def recuperation(self,bdd,L):

        bdd_mc = bdd.mc()
        cur,con = bdd_mc.connexion(bdd)

        url = tuple(L)
        question = '?,'*(len(url)-1)+'?'

        cur.execute('SELECT s.url , mc.mot_cle , o.occurence FROM mot_cle mc JOIN occurence o ON mc.id_mot_cle = o.id_mot_cle JOIN site s ON s.id_site = o.id_site WHERE s.url IN('+question+')', (url))
        donnees = cur.fetchall()
        url_brut=[donnees[i][0] for i in range (len(donnees))]
        mot_cle_brut = [donnees[i][1] for i in range (len(donnees))]
        occurence = [donnees[i][2] for i in range (len(donnees))]

        url = [url_brut[0]]
        mot_cle = [mot_cle_brut[0]]

        for i in range (1, len(url_brut)) :
            #creation des listes d'url et de mots cles sans repetition
            if url_brut[i] != url_brut[i-1] :
                url.append(url_brut[i])
            presence = False
            for mot in mot_cle :
                if mot_cle_brut[i] == mot:
                    presence = True
                    pass
            if not presence :
                mot_cle.append(mot_cle_brut[i])

        M = [[0 for i in mot_cle] for i in url]
        for i in range(len(occurence)):
            #creation de la matrice des individus
            for j in range(len(url)) :
                if url_brut[i] == url[j]:
                    rang_url=j
                    pass
            for j in range(len(mot_cle)):
                if mot_cle_brut[i] == mot_cle[j]:
                    rang_mot_cle = j
                    pass
            M[rang_url][rang_mot_cle] = occurence[i]
        return (M)

    def correlation(self, L):

        M_cor = np.array([0. for i in range (l**2)]).reshape(l,l)
        Ln = np.array(L)
        for i in range (len(M_cor)):
            for j in range (len(M_cor)):
                if i == j:
                    M_cor[i,j] = 1
                elif i > j:
                    M_cor[j,i] = M_cor[i,j]
                else:
                    X = Ln[:,i]
                    Y = Ln[:,j]
                    r = np.corrcoef(X,Y)[0,1]
                    print(type(r))
                    M_cor[j,i] = r
        return(M_cor)

    def vecteurs_propres(self, L):
        vecteurs_propres = np.linalg.eig(L)[1]
        return (vecteurs_propres)

    def nouvelles_coordonnees(M,V):
        nouveau_vecteur = np.linalg.inv(M).dot(V)
        return(nouveau_vecteur)


if __name__ ==  '__main__' :
    acp = acp()
    acp.run(r'C:\Users\Régis\Documents\0 - KIN\Projet Garcin\bdd_mot_cle.bd',[1,2,3,4])