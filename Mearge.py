#Libraries Start
from PIL import Image
#Libraries End

#Global Varaibles Start
Images_Addrs=[]
Images_Img=[]
Width=0
Heigth=0
#Global Varaibles End

#Get Resive Images Address Start
def Get_Images_Addrs():
    addr=input("Enter New Image Address : ")
    while addr != "" :
        Images_Addrs.append(addr)
        addr=input("Enter New Image Address : ")
#Get Resive Images Address End

#Get Mirage Start
def Miarge_Images_Addrs_Array():
    
    #Get Read Image From Address Start
    for i in Images_Addrs:
        Images_Img.append(Image.open(i))
    #Get Read Image From Address End    

    Width=int(input("Enter New Image Width : "))
    Heigth=int(input("Enter New Image Heigth : "))

    Mrg_Image=Image.new('RGB',(Width,Heigth))

    for Imgs in Images_Img :
        Mrg_Image.paste(Imgs)

    Mrg_Image.save(input("Enter Save Address : "))

#Get Mirage End

#Main Function Start
def main():
    Get_Images_Addrs()
    Miarge_Images_Addrs_Array()
#Main Function End

#Main Runner Start
if __name__=="__main__":
    main()
#Main Runner End