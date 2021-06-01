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
import sqlite3 as lite

class bdd_mc:

    def __init__(self):
        import sqlite3 as lite

    def run(self, bdd, page):

        cur,con = self.connexion(bdd)
        self.ajout_PAGE(page, cur)
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

    def ajout_PAGE(self, page, cur):

        fichier = open(str(page),"r",encoding='utf-8')
        texte = fichier.read()


        TXT = texte.split('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        for text in TXT:

            text = text.split('\n')
            url = text[1]

            if len(text)>3:

                url = (url,)

                cur.execute('SELECT id_page FROM page WHERE url = (?)', (url))
                try :
                    #vérification que le page ne soit pas déjà dans la bdd
                    id_page = cur.fetchone()['id_page']
                except :
                    #ajout du page si non présent
                    cur.execute('INSERT INTO page(url) VALUES (?)',(url))
                    cur.execute('SELECT id_page FROM page WHERE url = (?)', (url))
                    id_page = cur.fetchone()['id_page']

                    for i in range (len(text)) :
                    #ajout des nouveaux mots clés et des occurences des mots clés
                        if i > 1 :
                            info_mot_cle = text[i].split(';')
                            if len(info_mot_cle)>1:
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

                                infos = (id_mot_cle,id_page,occurence)

                                #ajout des occurences des mots clés
                                cur.execute('INSERT INTO occurence(id_mot_cle,id_page,occurence) VALUES (?,?,?)', infos)
                            else:
                                print('what ?  ',info_mot_cle)


if __name__ ==  '__main__' :

    bdd = bdd_mc()
    bdd.run(r'C:\Users\alexa\projects\Privacy_Sequence\venv\bdd_mot_cle.bd',r'C:\Users\alexa\projects\Privacy_Sequence\venv\URL\BDD SOUS FORME TXT.txt')
