 # File Organizer

This Python script organizes files in a specified directory into separate folders based on their file types. It helps in keeping your files well-arranged by moving them into designated directories like Images, PDFs, Videos, Audios, Documents, and Others.


## Features

-   **Automatic Directory Creation:** The script will automatically create the necessary directories if they do not exist.
-   **File Moving with Error Handling:** Files are moved to their respective directories with error handling to ensure no data is lost.
-   **Extension-Based Sorting:** Files are sorted and moved based on their extensions into specific folders.
-   **Support for Various File Types:** The script supports a wide range of file types, including images, PDFs, videos, audios, documents, and others.

##  Directory Structure

The script creates the following directories within the specified path:

-   `Images`
-   `Pdfs`
-   `Videos`
-   `Audios`
-   `Documents`
-   `Others`

## Usage

-   **Set the Path:** Modify the `path` variable in the script to the directory you want to organize.
  
    
    `path = "C:/Users/shivh/Downloads"` 
    
-   **Run the Script:** Execute the script. It will create the necessary directories and move the files accordingly.
    
 
    
    `python file_organizer.py`


## How It Works

1.  **Change Directory:** The script changes the working directory to the specified path.
    
  
    
    `os.chdir(path)` 
    
2.  **Create Directories:** The `create_directory` function ensures the necessary directories are created.
    
    
    
    `def create_directory(directory):
        if not os.path.exists(directory):
            os.mkdir(directory)` 
    
3.  **Move Files:** The `move_file` function handles moving the files to their respective directories.
    
   
    
    `def move_file(old_file, new_file):
        os.rename(old_file, new_file)` 
    
4.  **Check File Types and Move:** Functions like `checkForImages`, `checkForPdf`, `checkForVideo`, `checkForAudio`, and `checkForDocument` check the file extensions and move the files.
    
    
    
    `def checkForImages(ext, file_names):
        if ext in ["png", "jpg", "gif"]:
            move_file(old_file, new_file)` 
    
5.  **Organize Files:** The script goes through each file in the directory and moves it to the appropriate folder.
    
    
    `for file_names in mylist:
   ext = os.path.splitext(file_names)[1][1:]
        if not (checkForImages(ext, file_names) or
                checkForPdf(ext, file_names) or
                checkForVideo(ext, file_names) or
                checkForAudio(ext, file_names) or
                checkForDocument(ext, file_names)):
            move_file(old_file, new_file)`

