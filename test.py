import os

imageDirectory = "Images"
pdfDirectory = "Pdfs"
videoDirectory = "Videos"
audioDirectory = "Audios"
documentDirectory = "Documents"
otherDirectory  = "Others"
path = "C:/Users/shivh/Downloads"

os.chdir(path)

# Create the needed directories with error handling
def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
            print(f"Directory {directory} created.")
        else:
            print(f"Directory {directory} already exists.")
    except Exception as e:
        print(f"Error creating directory {directory}: {e}")

create_directory(imageDirectory)
create_directory(pdfDirectory)
create_directory(videoDirectory)
create_directory(audioDirectory)
create_directory(documentDirectory)
create_directory(otherDirectory)


# Actually move the file with error handling

def move_file(old_file, new_file):
    try:
        if os.path.exists(old_file):
            os.rename(old_file, new_file)
            return True
        else:
            print(f"File {old_file} does not exist.")
            return False
    except Exception as e:
        print(f"Error moving file {old_file} to {new_file}: {e}")
        return False

# Functions to check for extensions and call the move_file function to run the move file move
def checkForImages(ext, file_names):
    if ext in ["png", "jpg", "gif"]:
        old_file = os.path.join(path, file_names)
        new_file = os.path.join(path, imageDirectory, file_names)
        return move_file(old_file, new_file)
    return False

def checkForPdf(ext, file_names):
    if ext == "pdf":
        old_file = os.path.join(path, file_names)
        new_file = os.path.join(path, pdfDirectory, file_names)
        return move_file(old_file, new_file)
    return False

def checkForVideo(ext, file_names):
    if ext in ["webm", "mkv", "flv", "vob", "ogv", "ogg", "rrc", "gifv", "mng", "mov", "avi", "qt", "wmv", "yuv", "rm", "asf", "amv", "mp4", "m4p", "m4v", "mpg", "mp2", "mpeg", "mpe", "mpv", "m4v", "svi", "3gp", "3g2", "mxf", "roq", "nsv", "flv", "f4v", "f4p", "f4a", "f4b", "mod"]:
        old_file = os.path.join(path, file_names)
        new_file = os.path.join(path, videoDirectory, file_names)
        return move_file(old_file, new_file)
    return False

def checkForAudio(ext, file_names):
    if ext in ["mp3", "wav", "aac", "flac", "alac", "wma", "ogg", "opus", "aiff", "dsd", "pcm", "ape", "m4a", "mpc", "amr", "au", "aif", "wv", "tta", "ac3", "ra", "dts", "mka", "caf"]:
        old_file = os.path.join(path, file_names)
        new_file = os.path.join(path, audioDirectory, file_names)
        return move_file(old_file, new_file)
    return False

def checkForDocument(ext, file_names):
    if ext in ["doc", "docx", "odt", "rtf", "txt", "html", "htm", "md", "markdown", "xml", "epub", "mobi", "azw", "azw3", "djvu", "fb2", "ibooks", "cbr", "cbz", "xps", "oxps", "ps", "dvi", "tex", "latex", "csv", "tsv", "xls", "xlsx", "ods", "ppt", "pptx", "odp", "key", "numbers", "pages"]:
        old_file = os.path.join(path, file_names)
        new_file = os.path.join(path, documentDirectory, file_names)
        return move_file(old_file, new_file)
    return False

mylist = os.listdir(path)

# Removing the directories from mylist if they exist
for directory in [imageDirectory, pdfDirectory, videoDirectory, audioDirectory, documentDirectory, otherDirectory]:
    if directory in mylist:
        mylist.remove(directory)

# Go through each file in my list of file names
for file_names in mylist:
    ext = os.path.splitext(file_names)[1][1:]

    # if the functons return false for all these types then move the file to the others folder
    if not (checkForImages(ext, file_names) or
            checkForPdf(ext, file_names) or
            checkForVideo(ext, file_names) or
            checkForAudio(ext, file_names) or
            checkForDocument(ext, file_names)):
        old_file = os.path.join(path, file_names)
        new_file = os.path.join(path, otherDirectory, file_names)
        move_file(old_file, new_file)

print("Done the script")
