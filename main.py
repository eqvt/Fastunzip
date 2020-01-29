# import modules
import zipfile
import pathlib
import shutil

# project info
__version__ = "0.1.0"

# main program

def main():    
    print(f"Your current directory is: {dir_start}")    
    for path in dir_start.rglob('*.zip'):
        if path.parent != dir_zip:            
            try:
                zf = zipfile.ZipFile(path)
                zf.extractall(path.parent)
                zf.close()            
                source = str(path)  
                print(source)          
                destination = str(dir_zip.joinpath(path.name))
                print(destination)
                shutil.move(source, destination)                
            except:
                print(f"Failed to unpack the archive: {path.name}")
  
if __name__ == "__main__":   
    dir_start = pathlib.Path.cwd().joinpath('test')
    dir_zip = pathlib.Path.cwd().joinpath('zip')
    main()