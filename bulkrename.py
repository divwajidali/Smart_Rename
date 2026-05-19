from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("path")
parser.add_argument("--prefix")
parser.add_argument("--suffix")
parser.add_argument("--yes", action="store_true")

args = parser.parse_args()

path = Path(args.path)

if not path.exists() :
    print("Folder does not exist.")

elif not path.is_dir() :
    print("This is not folder.")

else :
    files = path.iterdir()
    found = False
    from renamer import rename_file
    if args.prefix :
        prefix = args.prefix
        changes = []
        for file in files :
            if file.is_file() :
                found = True
                old = file
                new = rename_file(file,prefix)
                if new is not None :
                    changes.append((old , new))
            
    if not found:
        print("Files do not exist.")        
            
    from preview import preview
    preview(changes)
    if args.yes :
        for old, new in changes :
            
            old.rename(new)
        print("Files renamed successfully.")

    else: 
        print("Preview only. Use --yes to apply changes.")

    

