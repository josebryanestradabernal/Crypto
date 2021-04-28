###Vigenere Equipo 13 
###Encrypt and Decrypt 
alphabeto = []
for i in range (65, 91):
    alphabeto.append(chr(i))
class Vigenere (object):
    def __init__ (self,key="", m="" , c=""): 
        self.key= key
        self.m = m 
        self.c = c

    def Encrypt(self):
        self.c=""
        k=len(self.key)
        for i in range(len(self.m)):
            self.c+= chr((((ord(self.m[i])-65)+
            (ord(self.key[i%k])-65))%26)+65)
        print("Encrypt : ",self.c)
        return self.c

    def Decrypt(self):
        #key invertida
        unkey =""
        for i in self.key: 
            unkey+= chr (((26-(ord(i)-65))%26)+65)
        self.m=""
        k=len(unkey)
        for i in range(len(self.c)):
            self.m+= chr((((ord(self.c[i])-65)+
            (ord(unkey[i%k])-65))%26)+65)
        print("Decrypt: ",self.m)
        return self.m


if __name__ == "__main__": 
    vig = Vigenere("TROYA","HABILIDOSO")
    c=vig.Encrypt()
    vig.Decrypt()