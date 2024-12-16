def cezars(text, shift, mode="encrypt"): # kādi parametri mums nepieciešami
    pass

"""
:parametrs text: teksts -->šifrējam vai atšifrējam
:parametrs shift: pozitīvs skaitlis - kā veidojas nobīde M 1 L
:parametrs mode: 'encrypt'-šifrējam (kodējam), 'decrypt'- atšifrējam
:return: kodēts vai dekodēts teksts

"""
    if mode=='decrypt':
        shift=-shift
    rezultats=''
    
    for char in text:
        if char.isalpha():
            # parbaudit, vai burts ir leils vai mazs
            start=ord('A') if char.isupper() else ord('a')
            # aprēķina jauno burtu
            jauns_burts=((ord(char)-start+shift)%26+start)
            rezultats+=jauns_burts
        else:
            #Ja nav burts, ja[ievieno simbolu nemainot!
            rezultats+=char
    return rezultats






# piemērs
org_text="Sveika, pasaule!"
solis=3


