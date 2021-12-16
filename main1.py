""" This Research paper implementation describe the efficient way to transmit the information.
    This project has three components
    1. Encryption Decryption of text using Asymmetric key Cryptography Algorithm ( RSA )
    2. Compression Decompression Encrypted text using Huffman coding
    3. Hide and retrieve Compress data into image using LSB Steganography

    """

import text_main as tm
import Stego as st
from PIL import Image
import numpy as np

#  Encode the image and text. In other word this function perform Encryption of text, Compression of Encrypted text and Hide compress data into image

def Encoder(image_path):
    # Cryptography Encryption and Compression
    Tree, message=tm.Encoder_text()
#      Steganography
    new_image=st.Encode_text(image_path,message)
    new_image=Image.fromarray(new_image)
    new_image.save("new_image.png")
    return Tree

 # Decode the image and text. In other word this function perform Retrive compress data, Decompression of Encrypted text and Decryption of text

def Decoder(Tree):
    im=Image.open("new_image.png")
    image=np.array(im)
    message=st.Decode_text(image)
    msg=tm.Decoder_text(Tree,message)
    with open("Process_text.txt",'w') as f:
        f.write(msg)

if __name__=="__main__":
    Tree=Encoder("download1.jpg")
    Decoder(Tree)
    print("Execution Successful")
