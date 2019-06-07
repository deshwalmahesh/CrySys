import base64
from functions import*

ENCRYPT=1
DECRYPT=0

text= input("Enter Message to Send\n")   
key = input("Enter Key of Minimum 8 characters to Encrypt Message\n") 

d = des()
r = d.encrypt(key,text)


original_image_file = "image.png"

img = Image.open(original_image_file)


encoded_image_file = "enc_" + original_image_file


secret_msg =r

img_encoded = encode_image(img, secret_msg)
img_encoded.save(encoded_image_file)




##############################################################################################################################################

p = int(input("Enter a Prime Number: "))
q = int(input("Enter a Different Prime Number: "))
public, private = generate_keypair(p, q)
print ("\nYour Public Key is: ", public , "\nYour Private Key is: ", private)

with open("enc_image.PNG", "rb") as image:
     img_list=(base64.b64encode(image.read()))
     
encrypted_msg = encrypt(private, img_list)

test=(''.join(map(lambda x: str(x), encrypted_msg)))


with open ('image_text.txt','w') as f:
    for no in encrypted_msg:
        f.write('%i\n'%no)

input('\nPress Any Key to Exit')

