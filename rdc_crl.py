'''
  ******************************************************************************
  * @file    rdc_crl.py
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

import time
from gensim.summarization import keywords
import copy
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk import ne_chunk, pos_tag
from nltk.corpus import stopwords

class rdc_crl:
    def __init__(selfname):
        pass
    def run(self):
        liste_site = self.open_tampon('C:\\Users\\alexa\\projects\\Privacy_Sequence\\venv\\tampon_bdd3.txt')
        site_keyword = []
        print('nombre de site:',len(liste_site))

        liste_site_keyword= []
        keys = []
        liste_occurence=[]
        for site in liste_site:
            site_keyword = keywords(site[1],lemmatize=True,deacc=True)
            for word in site_keyword.split('\n'):
                if not(self.banword(word)):
                    keys = keys+[word]
                    liste_occurence = liste_occurence + [site[1].count(word)]
            liste_site_keyword = liste_site_keyword+[[site[0],keys,copy.copy(liste_occurence)]]
            liste_occurence =[]
            keys = []

        print(liste_site_keyword)
        self.save(liste_site_keyword)

    def banword(self,word):
        banlist1=list(stopwords.words('English'))
        banlist2=list(stopwords.words('French'))

        if word in banlist1:
            return True
        if word in banlist2:
            return True
        if word in banlist1:
            return True
        if word in banlist1:
            return True
        if word in banlist1:
            return True
        return False


    def save(self,sites):
        name_folder = 'C:\\Users\\alexa\\projects\\Privacy_Sequence\\venv\\URL'
        word=''
        print('nombre de sites',len(sites))
        for i,site in enumerate(sites):
            word = word + str(site[0]) + '\n'
            for i in range(len(site[1])):
                word = word+str(site[1][i])+';'+str(site[2][i])+'\n'

            word= word+'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'

        doc = open(name_folder+'\\'+'BDD SOUS FORME TXT'+'.txt','w',encoding='utf-8')
        doc.write(word)
        doc.close







    def open_tampon(self,name):
        doc = open(name, 'r', encoding='utf-8')
        txt = doc.read()
        doc.close()
        txt_list = txt.split('\n')

        liste_des_sites = []
        site = ['', '']
        contenue = ''
        longueur = 0
        compteur = 0

        for t in txt_list:
            longueur = len(t)

            if longueur >= 5:
                if t[0:4] == 'http':
                    contenue = ''

                    liste_des_sites = liste_des_sites + [copy.copy(site)]

                    #print('dans la boucle')
                    #for tampom in liste_des_sites:
                    #    print(tampom)

                    print(' .....................  ')

                    site[0] = t
                    site[1] = ''
                else:
                    site[1] = site[1] + str(t)
            compteur += 1

        #print('dans la fonction')
        #for tampom in liste_des_sites:
        #    print(tampom)

        return liste_des_sites

if __name__ == '__main__':
    #text = "Ceci est une phrase quelconque d'un site quelconque contenant des mots ordinaires racontant des faits banales"
    #text = "this is a perfectly normal sentence from a usual site with casual word telling ordinary things  "
    #words = word_tokenize(text, language='english')
    #explicit = nltk.pos_tag(words)

    #print(words)

    #for token in explicit:
    #    print(token)
    banlist1 = list(stopwords.words('English'))
    banlist2 = set(stopwords.words('French'))

    print(banlist1)
    print(banlist2)
    RDC = rdc_crl()
    RDC.run()