import os
import csv

import shutil
def define():
    path_input = r'C:\Users\Poott\OneDrive\Desktop\CN240\CN240\images\notblur'
    option = []
    for file in os.listdir(path_input): 
        option.append(file)
    check_in_list = []

    for imagePath_origin in option:

        imagePath =  imagePath_origin.split("_")
        
        
        check_in_temp =[]
        for i in imagePath:
            x = any(char.isdigit() for char in i)
            if x == False :
                check_in_temp.append(i)
        
        if check_in_temp in check_in_list:
            name_dir = ''
            for i in check_in_temp:
                if not name_dir:
                    name_dir = name_dir+ i
                else:
                    name_dir = name_dir+"_"+ i
            print("is in")
            shutil.move(r"C:\Users\Poott\OneDrive\Desktop\CN240\CN240\images\notblur"+"/"+imagePath_origin,r"C:\Users\Poott\OneDrive\Desktop\CN240\CN240\images\notblur"+"/"+name_dir)
        else:
            print("not in")
            check_in_list.append(check_in_temp)
            name_dir = ''
            for i in check_in_temp:
                if not name_dir:
                    name_dir = name_dir+ i
                else:
                    name_dir = name_dir+"_"+ i
            os.makedirs(r'C:\Users\Poott\OneDrive\Desktop\CN240\CN240\images\notblur'+'/'+name_dir)
            
            shutil.move(r"C:\Users\Poott\OneDrive\Desktop\CN240\CN240\images\notblur"+"/"+imagePath_origin,r"C:\Users\Poott\OneDrive\Desktop\CN240\CN240\images\notblur"+"/"+name_dir)


        #os.mkdir(path)
        #shutil.move(r"C:\Users\ANFIELD\Desktop\tu\cn240\example\bobi\face_detact\FaceDetect\data\move_notblur"+"/"+imagePath,"C:/Users/ANFIELD/Desktop/git,PASS/cn240/as1/image/facial_expressions/move_notblur/")


if __name__ == "__main__": 
    x=int(input("1>defin category"))
    if x == 1:
        define()
   