# import modules
import zipfile
import pathlib
# from pathlib import Path
import shutil
import tkinter as tk

# project info
__version__ = "0.1.0"

# main program
def logger(input_txt, box=0):
    if box == 0:
        txt_log.insert(tk.END, input_txt + "\n")
    elif box == 1:
        txt_arch.insert(tk.END, input_txt + "\n")

def clearlog():
    txt_arch.delete('1.0', tk.END)

def main():        
    path_from_entry = pathlib.Path(entry.get())
    dir_zip = pathlib.Path(ent_zip.get())    
    dir_start = path_from_entry
    if dir_zip.is_dir():        
        logger("Directory already exists")
    else:        
        logger("Directory didn't exists")
        pathlib.Path.mkdir(dir_zip)   
    
    for path in dir_start.rglob('*.zip'):
        if path.parent != dir_zip:            
            try:
                zf = zipfile.ZipFile(path)
                zf.extractall(path.parent)
                zf.close()            
                source = str(path)                  
                logger(source, 1)
                destination = str(dir_zip.joinpath(path.name))
                logger(destination)
                shutil.move(source, destination)
            except:                
                logger("Failed to unpack the archive: " + path.name)            
  
def listThis():
    path_from_entry = pathlib.Path(entry.get())
    dir_dest = pathlib.Path(ent_zip.get())    
    dir_start = path_from_entry
    clearlog()
    for path in dir_start.rglob('*.zip'):
        if path.parent != dir_zip:            
            try:
                source = str(path)                  
                logger(source, 1)
                destination = str(dir_dest.joinpath(path.name))
                logger(destination)                
            except:                
                logger("Failed to list archives " + path.name)     

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
    button = tk.Button(
                 text="List zips!",
                 master=frame,
                 command=listThis
                 )
    button.grid(row=2, column=1, padx=5, pady=5) 

    lbl_zip = tk.Label(text="Select directory to run store ZIPs: ", master=frame)
    lbl_zip.grid(row=2, column=0, padx=5, pady=5)
    ent_zip = tk.Entry(master=frame, width=60)
    ent_zip.grid(row=3, column=0, padx=5, pady=5)
    ent_zip.insert(0, dir_zip)

    lbl_log = tk.Label(text="Program log: ", master=frame)
    lbl_log.grid(row=4, column=0, padx=5, pady=5)
    txt_log = tk.Text(master=frame)
    txt_log.grid(row=5, column=0, padx=5, pady=5)

    lbl_arch = tk.Label(text="Archives found: ", master=frame)
    lbl_arch.grid(row=4, column=1, padx=5, pady=5)

    txt_arch = tk.Text(master=frame)
    txt_arch.grid(row=5, column=1, padx=5, pady=5)
    window.mainloop()