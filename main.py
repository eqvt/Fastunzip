# import modules
import zipfile
import pathlib
# from pathlib import Path
import shutil
import tkinter as tk

# project info
__version__ = "0.1.0"

# main program

def main():        
    path_from_entry = pathlib.Path(entry.get())
    dir_zip = path_from_entry.joinpath('zip')
    dir_start = path_from_entry
    if dir_zip.is_dir():
        print("Directory already exists")
    else:
        print("Directory didn't exists")
        pathlib.Path.mkdir(dir_zip)
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
    # main()
    window = tk.Tk()
    window.title("GUI")    
    frame = tk.Frame(master=window)
    frame.pack()
    #Create Label
    label = tk.Label(text="Select directory to run Fastunzip: ", master=frame)
    entry = tk.Entry(master=frame, width=60)
    label.grid(row=0, column=0, padx=5, pady=5)
    entry.grid(row=1, column=0, padx=5, pady=5)
    entry.insert(0, dir_start)
    button = tk.Button(
                 text="Unzip!",
                 master=frame,
                 command=main
                 )
    button.grid(row=1, column=1, padx=5, pady=5) 

    lbl_zip = tk.Label(text="Select directory to run store ZIPs: ", master=frame)
    lbl_zip.grid(row=2, column=0, padx=5, pady=5)
    ent_zip = tk.Entry(master=frame, width=60)
    ent_zip.grid(row=3, column=0, padx=5, pady=5)
    ent_zip.insert(0, dir_zip)


    window.mainloop()