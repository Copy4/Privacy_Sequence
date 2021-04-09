'''
  ******************************************************************************
  * @file    bdd_mc.py
  * @author  Régis Pellegrin
  * @version V1.0.0
  * @date    02 April 2021
  * @brief   Privacy Software
  ******************************************************************************
  *
  * REMARK: this program was validated on Python release below:
  *           - Python 3.7.7
  *
  *
  ******************************************************************************
'''

class bdd_mc:

    def __init__(self):
        import sqlite3 as lite

    def run(self, bdd, site):

        cur,con = self.connexion(bdd)
        self.ajout_site(site, cur)
        con.commit()

    def connexion(self, bdd):

        con = lite.connect(str(bdd))

        if con :

            print("connection ok !")

            con.row_factory = lite.Row
            cur = con.cursor()

            return (cur,con)

        else :
            print("connexion echouee")

    def ajout_site(self, site, cur):

        fichier = open(str(site),"r")
        text = fichier.read()

        text = text.split('\n')
        url = text[0]
        header = text[1]
        site = (url, header)
        url = (url,)

        cur.execute('SELECT id_site FROM site WHERE url = (?)', (url))
        try :
            #vérification que le site ne soit pas déjà dans la bdd
            id_site = cur.fetchone()['id_site']
        except :
            #ajout du site
            cur.execute('INSERT INTO site(url, header) VALUES (?,?)',(site))
            cur.execute('SELECT id_site FROM site WHERE url = (?)', (url))
            id_site = cur.fetchone()['id_site']

            for i in range (len(text)) :
            #ajout des nouveaux mots clés et des occurences des mots clés
                if i > 1 :
                    mot = ""
                    condition = True
                    info_mot_cle = text[i].split(';')

                    occurence = int(info_mot_cle[1])
                    mot = (info_mot_cle[0],)

                    cur.execute('SELECT id_mot_cle FROM mot_cle WHERE mot_cle = ?', mot)
                    try :
                        #vérification que le mot clé n'est pas présent dans la bdd
                        id_mot_cle = cur.fetchone()['id_mot_cle']
                    except :
                        #ajout des nouveaux mots cles dans la bdd
                        cur.execute('INSERT INTO mot_cle(mot_cle) VALUES (?)', mot)
                        cur.execute('SELECT id_mot_cle FROM mot_cle WHERE mot_cle = ?', mot)
                        id_mot_cle = cur.fetchone()['id_mot_cle']

                    infos = (id_mot_cle,id_site,occurence)

                    #ajout des occurences des mots clés
                    cur.execute('INSERT INTO occurence(id_mot_cle,id_site,occurence) VALUES (?,?,?)', infos)



if __name__ ==  '__main__' :

    bdd = bdd_mc()
    bdd.run(r'C:\Users\Régis\Documents\0 - KIN\Projet Garcin\bdd_mot_cle.bd',r'C:\Users\Régis\Desktop\test.txt')
