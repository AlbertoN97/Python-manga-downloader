import requests
import shutil
import os

#This stores the system path where you will put the folder and the folder you want to create. Must be an absolute path (i.e. C:\\X\\Y\\Z for Windows (with double slashes) and /X/Y/Z for Linux,Mac)
working_path='C:\\Users\\Alberto\\Documents'
main_folder='one_piece_color'

#Attemps to create the main folder for the chapters. Swap the commented line if you are on Linux
try:
    os.mkdir(working_path+main_folder)
    #os.mkdir(working_path+'/'+main_folder)
    print("Folder {main_folder} created in {working_path}")
except:
    print(f"Error: couldn'\ t make {main_folder} folder")

chap=1
#Declares the manga you want to download, until the name of the manga like the example
manga_page="https://scans-hot.leanbox.us/manga/One-Piece-Digital-Colored-Comics/"
img="{}-{}.png"

#Makes the loop for each chapter using a range from the first to the last. Note: final value of the range must be the last chapter + 1 .Swap the commented line if you are on Linux
for chap in range(1,1005):
    pag=1
    chap2='{:0>4}'.format(chap)
    pag2='{:0>3}'.format(pag)
    path=(working_path+main_folder+'//'+chap2)
#    path=(working_path+'/'+main_folder+'/'+chap2)

#Attemps to create the folder of the chapter with format nnnn(i.e. 0037)
    try:
        os.mkdir(path)
    except:
        print("Couldn\' create folder "+path)

#Change current directory to the chapter directory
    os.chdir(path)
    url = (manga_page+img).format(chap2,pag2)
    print(f"Downloading chapter {chap2}")
    file_name = f"{chap2}-{pag2}.png"
    res = requests.get(url, stream = True)

#Will make a loop for each page to download it until doesn't find any which will make it go to next chapter
    while res.status_code == 200 :
        pag2='{:0>3}'.format(pag)
        url = (manga_page+img).format(chap2,pag2)
        file_name = f"{chap2}-{pag2}.png"
        res = requests.get(url, stream = True)

#If the image is open (which means that it exists) it will download it in the current directory()
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
        pag+=1

#Removes the last image that make out of the loop (that image doesn't work, its a currupted one that is downloaded).Swap the commented lines if you are on Linux
    os.remove(path+"\\"+(img.format(chap2,pag2)))
#    os.remove(path+'/'+(img.format(chap2,pag2)))