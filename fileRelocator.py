# going to file relocation script.
import os
import argparse
import shutil
import logging

logger = logging.getLogger("relocator")
logger.setLevel(logging.DEBUG)

format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
stream.setFormatter(format)

file_log = logging.FileHandler("relocator.log")
file_log.setLevel(logging.INFO)
file_log.setFormatter(format)

logger.addHandler(stream)
logger.addHandler(file_log)


IMG_EXTENSIONS = ['.jpg', '.png', '.svg', '.jpeg']
DOC_EXTENSIONS = ['.docx', '.pdf', '.DOCX', '.PDF', '.doc', '.ppt', '.pptx']

def hasExtension(filename, extension):
    return any(filename.lower().endswith(ext) for ext in extension)

def findFiles(directory, extension):
    return [f for f in os.listdir(directory) if hasExtension(f, extension)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default = 'images', choices=['images', 'documents'])
    parser.add_argument('--search_dir', default = "C:/Users/kensu/Downloads", help="where this script will be searching for files.")
    parser.add_argument('--save_dir', default='C:/Users/kensu/OneDrive/Pictures', help="where files get sent")
    parser.add_argument('--preview', action='store_true', help='showing where the files will be relocated.')
    
    args = parser.parse_args()

    extensions = IMG_EXTENSIONS if args.mode == 'images' else DOC_EXTENSIONS

    destination = args.save_dir
    source = args.search_dir

    files = findFiles(source, extensions)
    
    if args.preview: 
        for file in files:
            # print(os.path.join(source, file) + " will be moved to " + os.path.join(destination, file))
            logger.debug(f'Preview: {file} will be moved to {os.path.join(destination, file)}.')
        print("File relocation preview finished.")
    else:
        for file in files:
            shutil.move(os.path.join(source, file), os.path.join(destination, file))
            logger.info(f'Moved {os.path.join(source, file)} to {os.path.join(destination, file)}.')
        print("\nFile relocation done. Please check the source and destination folders.")
    
    