# kā izveidot drošu paroli
import string
import secrets

def veido_paroli(lenght=12): # parametri
    #Definē rakstzīmju kopa
    alfabeets=string.ascii_letters+string.digits+string.punctuation
    #veidojam drošu paroli
    parole=''.join(secrets.choice(alfabeets) for i in range(lenght))    
    return parole


#izsaukt funkciju un paradit paroli

parole=veido_paroli(20) # jautajums - kas ir 20?
print(f"Droša parole ir: {parole}")