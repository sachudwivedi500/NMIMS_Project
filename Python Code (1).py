import numpy as np
from PIL import Image

# defining a  new Function "nucleus" to get the desired output

def nucleus(f):
    img = Image.open(f) 
    image1 = np.array(img)
    ni=image1.reshape(307200,3)
    h=np.array([0.2432356,-0.7945695,0.5563234])
    req=np.inner(h, ni)
    r1=np.column_stack((req,req,req))
    Bw=np.where(r1<41.875,0,255)
    final=Bw.reshape(480,640,3)
    im = Image.fromarray((final).astype(np.uint8))
    return im

f= "BloodImage_00000.jpg"
i=nucleus(f)
i
i.save("Converted_BloodImage_00000.jpg")




#Explaining the defined function "nucleus" in detail 

#importing required image
filename = "BloodImage_00000.jpg"
img = Image.open(filename)
img

#converting image in array which is 3D
image1 = np.array(img)
image1

#converting 3D array into 2D array
ni=image1.reshape(307200,3)
ni

#defined a new function to retrive RGB values of a particular pixel

def rgb1(a,b,f):
    i=np.array(f)
    r=i[a,b,0]
    g=i[a,b,1]
    b=i[a,b,2]
    x=[r,g,b]
    y=np.array(x)
    return y

#Using the above function we found the RGB  values for colours(purple,brown,white)
f=image1
 
ip=rgb1(220,450,f)
ip
#purple=array([187, 163, 215]

ib=rgb1(0,0,f)
ib
#brown=rarray([176, 154, 143]

iw=rgb1(479,420,f)
iw
#white=array([207, 209, 208]



#Using the R software, found the orthonormalized vectors given below 
#sequence of vectors 
#u1= rgb(brown) ,u2= rgb(white),u3= rgb(purple)

#where h is orthonormalized vector of u3(purple)

h=np.array([0.2432356,-0.7945695,0.5563234])
h

#taking inner product with the 2D array of the image matrix
req=np.inner(h, ni)
req

#the "req" matrix is matrix with one column
#so we converted the it into a matrix with 3 columns
r1=np.column_stack((req,req,req))

#converted the "r1" matrix to (0,255)matrix
#as desired range for image reproduction from an array is (0,255)
#Threshold value for the inner product is 41.875
Bw=np.where(r1<41.875,0,255)
Bw

#converting back the 2D matrix to 3D matrix
final=Bw.reshape(480,640,3)
final

#Converting the final 3D array to the desired imaged(grayscale)
#with required data type by Python(uint.8)
im = Image.fromarray((final).astype(np.uint8))
im

#saving the processed image in device
im.save("Converted_BloodImage_00000.jpg")



