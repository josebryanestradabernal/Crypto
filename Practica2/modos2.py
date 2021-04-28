#Import image processing standard library
from PIL import Image,ImageTk
#Import the pycrypto library, reference the aes encryption module, need to be installed through the pip command under cmd (installation is more troublesome)
from Crypto.Cipher import AES
import random
import string

#Randomly generate 16 strings composed of lowercase letters
"""def key_generator(size = 16, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))"""



#filename = "Imagen1.bmp"
#filename_encrypted_ecb = "Imagen1_eECB"
#filename_encrypted_cbc= "bImagen1_eCBC"
#format = "BMP"
#Using a function to randomly generate a string of lowercase letters
#key = 'This is a key123'


# AES encrypted plaintext space is an integer multiple of 16, which cannot be divided evenly, so it needs to be filled
#In the corresponding ascii, "\x00" means 0x00, the specific value is NULL, b means that it is expressed in bytes
def pad(data):
    return data + b"\x00" * (16 - len(data) % 16)


# Map the image data to RGB
def trans_format_RGB(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, green, blue))
    return pixels


def encrypt_image_ecb(filename, key):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    #Convert image data into pixel value bytes
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    #for i in range(original):
        #print(data[i])
    #Map the pixel value of the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_ecb_encrypt(key.encode("utf8"), pad(value_vector))[:imlength])
    #for i in range(original):
        #print(new[i])

    #Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4] +'_eECB.'+ "BMP", "BMP")


def decrypt_image_ecb(filename, key):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    #Convert image data into pixel value bytes
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    #for i in range(original):
        #print(data[i])
    #Map the pixel value of the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_ecb_decrypt(key.encode("utf8"), pad(value_vector))[:imlength])
    #for i in range(original):
        #print(new[i])

    #Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4] +'_dECB.'+ "BMP", "BMP")

def encrypt_image_cbc(filename, key, IV):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    value_vector = im.convert("RGB").tobytes()

    # Convert image data to pixel value bytes
    imlength = len(value_vector)

    # Perform pixel value mapping on the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_cbc_encrypt(IV, key.encode("utf8"), pad(value_vector))[:imlength])

    # Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4] +'_eCBC.'+ "BMP", "BMP")


def decrypt_image_cbc(filename, key, IV):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    value_vector = im.convert("RGB").tobytes()

    # Convert image data to pixel value bytes
    imlength = len(value_vector)

    # Perform pixel value mapping on the filled and encrypted data
    value_encrypt = trans_format_RGB(aes_cbc_decrypt(IV, key.encode("utf8"), pad(value_vector))[:imlength])

    # Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename[0:-4] +'_dCBC.'+ "BMP", "BMP")

# CBC encryption
def aes_cbc_encrypt(IV, key, data, mode=AES.MODE_CBC):
    #IV is a random value
    #IV = 'This is an IV456'
    aes = AES.new(key, mode, IV.encode("utf8"))
    new_data = aes.encrypt(data)
    return new_data

# CBC decryption
def aes_cbc_decrypt(IV, key, data, mode=AES.MODE_CBC):
    #IV is a random value
    #IV = 'This is an IV456'
    aes = AES.new(key, mode, IV.encode("utf8"))
    new_data = aes.decrypt(data)
    return new_data


# ECB encryption
def aes_ecb_encrypt(key, data, mode=AES.MODE_ECB):
    #The default mode is ECB encryption
    aes = AES.new(key, mode)
    new_data = aes.encrypt(data)
    return new_data

# ECB decryption
def aes_ecb_decrypt(key, data, mode=AES.MODE_ECB):
    #The default mode is ECB encryption
    aes = AES.new(key, mode)
    new_data = aes.decrypt(data)
    return new_data

#Execute the encryption function on the image, and generate the encrypted image in the relevant directory
#encrypt_image_cbc("Imagen1.bmp", 'This is a key123', 'This is an IV456')
#encrypt_image_ecb("Imagen1.bmp", 'This is a key123')
#decrypt_image_cbc("Imagen1_eCBC.BMP", 'This is a key123', 'This is an IV456')
#decrypt_image_ecb("Imagen1_eECB.BMP", 'This is a key123')