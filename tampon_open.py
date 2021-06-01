import copy


def open_tampon(name):
    doc = open(name,'r',encoding='utf-8')
    txt = doc.read()
    doc.close()
    txt_list = txt.split('\n')

    liste_des_sites = []
    site = ['','']
    contenue = ''
    longueur = 0
    compteur = 0

    for t in txt_list:
        longueur = len(t)

        if longueur>=5:
            if t[0:4] == 'http':
                contenue = ''

                liste_des_sites = liste_des_sites+[copy.copy(site)]

                print('dans la boucle')
                for tampom in liste_des_sites:
                    print(tampom)

                print(' .....................  ')



                site[0] = t
                site[1] = ''
            else:
                site[1] =site[1]+str(t)
        compteur+=1

    print('dans la fonction')
    for tampom in liste_des_sites:
        print(tampom)

    return liste_des_sites

if __name__ =='__main__':
    liste_tampon = open_tampon('C:\\Users\\alexa\\projects\\Privacy_Sequence\\venv\\tampon_bdd3.txt')
    for tampon in liste_tampon:
        print(tampon)
    #print(liste_tampon)
