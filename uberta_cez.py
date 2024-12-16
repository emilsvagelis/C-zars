def cezars(text, shift, mode="encrypt"):

    if mode=='decrypt':

        shift=shift

    result=''

    for char in text:

        if char.isalpha():

            start=ord('A') if char.isupper else ord('a')

            new_letter=chr((ord(char)-start+shift)%26+start)

            result+=new_letter

        else:

            result+=char

    return result

#example

org_text="Hello!My name is emils and im not a big orange apple.My job is tpo be a ggood soldier on the battlefield and to obey command from the penguin and the polar bear."

solis=3

# šifrēsim
shifreet=cezars(org_text,solis,mode="encrypt")
print("\u0160ifrēts teksts: ",shifreet)

# atšifrēsim
at_shifreet=cezars(org_text,solis,mode="decrypt")
print("\u0160ifrēts teksts: ",at_shifreet)