import os
import shutil

count=0


bird_img_dir = "..\\datasets\\birds\\images"
bird_label_dir = "..\\datasets\\birds\\labels\\train"
bird_folder_dir = "..\\yolov5\\400Birds_Gerry\\train"
data_dir = "\\data"


def handleImages():
    folder_count=0
    count=0

    for directory in os.listdir(bird_folder_dir):
        dir_src = os.path.join(bird_folder_dir, directory)
        arr = os.listdir(dir_src)
        for i in arr:
            src_img = os.path.join(dir_src, i)
            shutil.copy(src_img, bird_img_dir)
            
            
            oldname = os.path.join(bird_img_dir, i)
            temp = str(count) + "b.jpg"
            newname = os.path.join(bird_img_dir, temp)
            os.rename(oldname, newname)

            createLabel(count, folder_count)

            count=count+1
        folder_count+=1

def createLabel(count, folder_count):
    temp = str(count) + "b.txt"
    newlabel = os.path.join(bird_label_dir, temp)
    f = open(newlabel,"w")
    f.write(str(folder_count) + " 0.500000 0.500000 1.000000 1.000000")
    f.close

def handleNames():

    arr=os.listdir(bird_folder_dir)
    newfile = os.path.join(os.getcwd(), "birdnames.txt")
    f = open(newfile, "w")
    f.write(str(arr))
    f.write("\n")
    f.write(str(len(arr)))
    f.close

def createBasicLabel():
    os.chdir(bird_label_dir)
    arr = os.listdir(os.getcwd())
    for file in arr:
        temp = os.path.join(os.getcwd(),file)
        f = open(temp, "w")
        f.write("0 0.500000 0.500000 1.000000 1.000000")
    f.close()
createBasicLabel()
# handleImages()
# handleNames()