from functions import *
import base64



ENCRYPT=1
DECRYPT=0


with open('image_text.txt','r') as f:
    key_element=f.read().splitlines()

print('Enter Elements of Public Key One by One to Reconstruct Image')
public=[int(input('\n'))for no in range (2)] 
decrypt_msg=(decrypt(public, key_element))

out=str(decrypt_msg)


imgdata = base64.b64decode(out) 
with open('output.png', 'wb') as f:
        f.write(imgdata)


img2 = Image.open('output.png')
hidden_text = decode_image(img2)

print('\nMessage Extracted from Image. Enter your Key to Decrypt Message\n')

key=str(input())

d=des()
r2 = d.decrypt(key,hidden_text)

print('Message Inside Image is:\n',r2)

input('Press Any Key to Exit')
