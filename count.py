import cv2 as cv
import os
import csv

def load_filename_from_folder(folder):
    return [filename for filename in os.listdir(folder)]


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def write(filename, data):
    csv_file = open(filename, "w", newline='')
    writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
    for data in data:
        writer.writerow(data)
    csv_file.close()



def main():
    path = "notblur"
    data = [["filename", "width", "height"]]
    filename = load_filename_from_folder(path)

    elem = 0
    for img in load_images_from_folder(path):
        width = img.shape[0]
        height = img.shape[1]
        data_for_append = [filename[elem], str(width), str(height)]
        data.append(data_for_append)
        elem += 1
        print(elem)

    write("notblur.csv", data)


main()
