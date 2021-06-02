from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode

hash = "SHA-1"
privada = ""
publica = ""

def newkeys(keysize,name):
    random_generator = Random.new().read
    key = RSA.generate(keysize, random_generator)
    private, public = key, key.publickey()
    with open ("llavesPublicas/"+name+'_public.pem',"wb") as f:
        f.write(public.export_key())
    with open ("llavePrivada/"+name+'_private.pem',"wb") as f: 
        f.write(private.export_key())
    return public, private

def generarllaves ():
    newkeys(1024,"bryan")
    newkeys(1024,"jose")
    newkeys(1024,"oscar")

def encrypt(message, pub_key):
    #RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
    #RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)

def sign(message, priv_key ):
    
    signer = PKCS1_v1_5.new(priv_key)
    digest = SHA.new()
    digest.update(message)
    return signer.sign(digest)

def verify(message, signature, pub_key):
    signer = PKCS1_v1_5.new(pub_key)
    digest = SHA.new()
    digest.update(message)
    return signer.verify(digest, signature)



def leerLlavePub(path): 
    global publica
    publica = RSA.importKey(open(path,"rb").read())

def leerLlavePriv(path): 
    global privada
    privada = RSA.importKey(open(path,"rb").read())


def rellenar_combokeys():
    import os
    pub = os.listdir("llavesPublicas")
    priv = os.listdir("llavePrivada")
    unknown_support.w.cmbKeys['values'] = pub + priv 
