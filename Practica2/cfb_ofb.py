from Crypto.Cipher import AES
from Crypto import Random
from PIL import Image
import string

#llave aleatoria
key = Random.new().read(AES.block_size)
#vector aleatorio
IV = Random.new().read(AES.block_size)

def pad(data):
    return data + b"\x00" * (16 - len(data) % 16)

def trans_format_RGB(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, green, blue))
    return pixels

def encrypt_image_cfb(filename, key,IV):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    #Convert image data into pixel value bytes
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    #Map the pixel value of the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_cfb_encrypt(IV,key.encode("utf8"), pad(value_vector))[:imlength])

    #Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4]+"_eCFB" + "." + "BMP", "BMP")

# ECB encryption
def aes_cfb_encrypt(IV,key, data, mode=AES.MODE_CFB):
    #The default mode is ECB encryption
    aes = AES.new(key, mode, IV.encode("utf8"))
    new_data = aes.encrypt(data)
    return new_data

def decrypt_image_cfb(filename, key, IV):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    value_vector = im.convert("RGB").tobytes()

    # Convert image data to pixel value bytes
    imlength = len(value_vector)

    # Perform pixel value mapping on the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_cfb_decrypt(IV, key.encode("utf8"), pad(value_vector))[:imlength])

    # Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4] + "_dCFB." + "BMP", "BMP")

# CBC decryption
def aes_cfb_decrypt(IV, key, data, mode=AES.MODE_CFB):
    #IV is a random value
    #IV = 'This is an IV456'
    aes = AES.new(key, mode, IV.encode("utf8"))
    new_data = aes.decrypt(data)
    return new_data

def encrypt_image_ofb(filename, key, IV):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    value_vector = im.convert("RGB").tobytes()

    # Convert image data to pixel value bytes
    imlength = len(value_vector)

    # Perform pixel value mapping on the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_ofb_encrypt(IV, key.encode("utf8"), pad(value_vector))[:imlength])

    # Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4] +'_eOFB'+ "." + "BMP", "BMP")

def aes_ofb_encrypt(IV, key, data, mode=AES.MODE_OFB):
    #IV is a random value
    #IV = 'This is an IV456'
    aes = AES.new(key, mode, IV.encode("utf8"))
    new_data = aes.encrypt(data)
    return new_data

def decrypt_image_ofb(filename, key, IV):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    value_vector = im.convert("RGB").tobytes()

    # Convert image data to pixel value bytes
    imlength = len(value_vector)

    # Perform pixel value mapping on the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_ofb_decrypt(IV, key.encode("utf8"), pad(value_vector))[:imlength])

    # Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4] +'_dOFB.'+ "BMP", "BMP")

def aes_ofb_decrypt(IV, key, data, mode=AES.MODE_OFB):
    #IV is a random value
    #IV = 'This is an IV456'
    aes = AES.new(key, mode, IV.encode("utf8"))
    new_data = aes.decrypt(data)
    return new_data

#ejemplos CFB
#encrypt_image_cfb("Imagen1.bmp",'This is a key123')
#decrypt_image_cfb("Imagen1_eCFB.BMP",'This is a key123',IV)

#ejemplo OFB
#encrypt_image_ofb('Imagen1.bmp','This is a key123',IV)
#decrypt_image_ofb('Imagen1_eOFB.BMP','This is a key123',IV)