import os
import sys


def main(args):


    if args[0]=="setup":

        name = args[1] if len(args)>1 else "rename_pls"
        path = args[2] if len(args)>2 else os.getcwd()
        combined_path = os.path.join(path, name)
        dirs = ["data/external", "data/raw", "data/interim", "data/processed", "src/data", "src/features", "src/models",
                "src/visualization", "notebooks", "reports", "models"]
        files = ["README.md",".gitignore",'Requirements.txt',"src/__init__.py","setup.py"]

        for dir in dirs:
            if not os.path.isdir(os.path.join(combined_path, dir)):
                print(dir, "created")
            os.makedirs(os.path.join(combined_path, dir), 0o666,exist_ok=True)

        for file in files:
            file_path=os.path.join(combined_path,file)
            if not os.path.exists(file_path):
                print(file_path," added")
                with open(file_path, 'w'): pass


    # if args[0] == "ignore":

        #for roots, dirs, files in os.walk(combined_path):
        #check if exists is a file or a dir add command to .gitignore



if __name__ == "__main__":
    main(sys.argv[1:])


