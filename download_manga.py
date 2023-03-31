import requests
import shutil
import os

#This script by AlbertoN97 on GitHub. If you like my work please leave the credit comment and reference to me if you share it online
#This stores the system path where you will put the folder and the folder you want to create. In Windows you have to change backslashes \ in the path for slashes / as in Unix systems
working_path='/some/path/'
main_folder='myfavouritemanga'

#Attemps to create the main folder for the chapters.
try:
    os.mkdir(working_path+'/'+main_folder)
    print(f"Main folder {main_folder} created in {working_path}")
except:
    print(f"Error: couldn'\ t make {main_folder} folder")

chap=1
#Declares the manga you want to download, until the name of the manga like the example
manga_page="https://domain.domain/manga/NameOfManga/"
img="{}-{}.png"

#Makes the loop for each chapter using a range from the first to the last. Note: final value of the range must be the last chapter + 1
for chap in range(1,1005):
    pag=1
    chap2='{:0>4}'.format(chap)
    pag2='{:0>3}'.format(pag)
    path=(working_path+'/'+main_folder+'/'+chap2)

#Attemps to create the folder of the chapter with format nnnn(i.e. 0037)
    try:
        os.mkdir(path)
    except:
        print("Couldn\' create folder "+path)

#Change current directory to the chapter directory
    try:
        os.chdir(path)
        print(f"Changed current path to {path}")
    except:
        print(f"WARNING: Couldn\'t create {path}"   )
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

#Removes the last image that make out of the loop (that image doesn't work, its a currupted one that is downloaded)
    try:
        os.remove(path+"/"+(img.format(chap2,pag2)))
        print(f"Chapter {chap2} successfully downloaded")
    except:
        print(f"ERROR: Could\'nt remove the image {path}+"/f"+(img.format({chap2},{pag2}))")
