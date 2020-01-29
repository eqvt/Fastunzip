# import modules
import os

# project info
__version__ = "0.1.0"

# main program

def main():    
    print(f"Your current directory is: {dir_start}")
    action = input("Write 'Start' to proceed: ")
    if action == "Start"S:
        print("Sucessful")
    else:
        print("Quiting...")
        exit()

if __name__ == "__main__":
    # This is executed from the command line 
    dir_start = os.path.dirname(os.path.realpath(__file__))
    main()