import os
import argparse

# PIL module is used to extract
# pixels of image and modify it
from PIL import Image

# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .bmp or .png file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."

def validate_file(file_name):
    '''
    validate file name and path.
    '''
    if not valid_path(file_name):
        print(INVALID_PATH_MSG%(file_name))
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG%(file_name))
        quit()
    return
     
def valid_filetype(file_name):
    # validate file type
    return file_name.endswith('.bmp') or file_name.endswith('.png') 
 
def valid_path(path):
    # validate file path
    return os.path.exists(path)


# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
 
        # list of binary codes
        # of given data
        newd = []
 
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd
 
# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
 
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
 
    for i in range(lendata):
 
        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]
 
        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1
 
        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
 
def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modPix(newimg.getdata(), data):
 
        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
 
# Encode data into image
def encode(args):
    image_name = args.encode[0]

    validate_file(image_name)

#    image = Image.open(image_name, 'r')

    data = args.encode[1]
    if (len(data) == 0):
        raise ValueError('Data is empty')
 
    new_image_name = args.encode[2]
    
    # validate the image file
    if not valid_filetype(new_image_name):
        print(INVALID_FILETYPE_MSG%(new_image_name))
        exit()
 
 #   newimg = image.copy()
 #   encode_enc(newimg, data)
 
 #   newimg.save(new_image_name, str(new_image_name.split(".")[1].upper()))
    encode(image_name, data, new_image_name)

def encode(image_name, data, new_image_name):
    image = Image.open(image_name, 'r')
    newimg = image.copy()
    encode_enc(newimg, data)
    newimg.save(new_image_name, str(new_image_name.split(".")[1].upper()))

# Decode the data in the image
def decode(args):
    image_name = args.decode[0]
    # validate the image file
    if not valid_filetype(image_name):
        print(INVALID_FILETYPE_MSG%(image_name))
        exit()

    # validate path
    if not valid_path(image_name):
        print("Error: No such directory found.")
        exit()
    return decode(image_name)


def decode(image_name):
    image = Image.open(image_name, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        # string of binary data
        binstr = ''
 
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data


# Main Function
def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "A steganography encoder/decoder application!")
 
    # defining arguments for parser object
    parser.add_argument("-e", "--encode", type = str, nargs = 3,
                        metavar = ("image", "data", "new_image"),
                        help = "Encode data inside the image and save the result in new_image.")
     
    parser.add_argument("-d", "--decode", type = str, nargs = 1,
                        metavar = "image", default = None,
                        help = "Retrieve the message encoded inside the image")
 
    # parse the arguments from standard input
    args = parser.parse_args()
     
    # calling functions depending on type of argument
    if args.encode != None:
        encode(args)
    elif args.decode != None:
        print("Decoded message:  " + decode(args))
    else:
        print("Use -h to see the options!")

 
# Driver Code
if __name__ == '__main__' :
 
    # Calling main function
    main()