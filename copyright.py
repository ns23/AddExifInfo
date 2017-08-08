import piexif
import os


# modify exif data and add CopyRight & artist  information

# get names of image files in a folder
def get_images(path):
    os.chdir(path)
    return [f for f in os.listdir(path) if os.path.isfile(f)]
    pass

#get existing exif data of image file
def get_exif_data(image_file):
    try:
        exif_dict = piexif.load(image_file)
        return exif_dict
    except Exception as e:
        return 0


# Single threaded code

path = raw_input("Enter the path: ")

Copyright = "" #add name of copyright holder
Artist = "" #add name of attist

image_files = get_images(path)
file_count = len(image_files)
count = 0

#modify exif data for each image in file
for image in image_files:
    image_path = path + '/' + image
    exif_dict = get_exif_data(image_path)

    if exif_dict is not 0:
        exif_dict['0th'][piexif.ImageIFD.Copyright] = Copyright
        exif_dict['0th'][piexif.ImageIFD.Artist] = Artist

        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, image_path)
    else:
        print("Was not able to open " + image)

    count = count + 1
    print("Processed: " + str(count) + "/" + str(file_count))
