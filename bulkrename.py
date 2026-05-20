from pathlib import Path
import argparse
import json

parser = argparse.ArgumentParser(
    description="Cross-platform bulk file renaming tool"
)

parser.add_argument("path", help="Path to target folder")
parser.add_argument("--prefix", help="Add prefix to filenames")
parser.add_argument("--suffix", help="Add suffix to filenames")
parser.add_argument("--numbering", action="store_true", help="Add sequential numbering to filenames")
parser.add_argument("--replace", nargs=2, help="Find and replace text in filenames")
parser.add_argument("--upper", action="store_true", help="Convert filenames to uppercase")
parser.add_argument("--lower", action="store_true", help="Convert filenames to lowercase")
parser.add_argument("--title", action="store_true", help="Convert filenames to titlecase")
parser.add_argument("--extension", help="Change file extensions")
parser.add_argument("--type" , nargs=2, help="Rename only specific file types")
parser.add_argument("--yes", action="store_true", help="Apply changing without confirmation")
parser.add_argument("--recursive", action="store_true", help="Rename files recursively in subfolders")
parser.add_argument("--undo", action="store_true", help="Undo the previous rename operation")

args = parser.parse_args()

if not any([
    args.prefix,
    args.suffix,
    args.numbering,
    args.replace,
    args.upper,
    args.lower,
    args.title,
    args.extension,
    args.type,
    args.undo
]):
    print("Please provide a rename operation.")

path = Path(args.path)

if not path.exists() :
    print("Folder does not exist.")

elif not path.is_dir() :
    print("This is not folder.")


else :
    if args.recursive :
        files = sorted(path.rglob("*"))

    else:
        files = sorted(path.iterdir())

    changes = []
    if args.prefix :
        from renamer import prefix_rename
        prefix = args.prefix
        changes = []
        for file in files :
            if file.is_file() :
        
                old = file
                new = prefix_rename(file,prefix)
                if new is not None :
                    changes.append((old , new))

    
     
    elif args.suffix :
        from renamer import suffix_rename 
        suffix = args.suffix
        changes = []
        for file in files :
            if file.is_file() :
            
                old = file
                new = suffix_rename(file,suffix)
                if new is not None :
                    changes.append((old , new))
             
    elif args.numbering :
        changes = []
        for number, file in enumerate(files, start=1):
            if file.is_file():
                
                old = file
                padded_num = str(number).zfill(3)
                new = padded_num + file.suffix
                new_path = file.parent / new
                if new_path.exists():
                    continue
                changes.append((old,new_path))


    elif args.replace :
        from renamer import find_replace
        find = args.replace[0]
        replace = args.replace[1]
        changes = []
        for file in files :
            if file.is_file() :
                old = file
                if find in file.name:
                    new = find_replace(file, find, replace)

                    if new is not None:
                        changes.append((old, new))

    elif args.upper:
        from renamer import to_uppercase
        changes = []
        for file in files :
            if file.is_file():
                old = file
                new = to_uppercase(file)
                if new is not None:
                    changes.append((old, new))


    elif args.lower:
        from renamer import to_lowercase
        changes = []
        for file in files :
            if file.is_file() :
                old = file
                new = to_lowercase(file)
                if new is not None:
                    changes.append((old, new))

    elif args.title:
        from renamer import to_titlecase
        changes = []
        for file in files :
            if file.is_file() :
                old = file
                new = to_titlecase(file)
                if new is not None:
                    changes.append((old, new))

    elif args.type:
        from renamer import specific_type_rename
        file_type = args.type[0]
        new = args.type[1]
        changes = []
        for file in files :
            if file.is_file() :
                old = file
                new_name = specific_type_rename(file, file_type, new)
                if new_name is not None:
                    changes.append((old, new_name))

    elif args.extension:
        from renamer import rename_extension
        changes = []
        for file in files :
            if file.is_file() :
                old = file
                new = rename_extension(file, args.extension)
                if new is not None:
                    changes.append((old, new))
                                   
    def save_history(changes):
            data = []

            for old, new in changes:
                info = {
                    "old" : str(old),
                    "new" : str(new)
                }
                data.append(info)

            with open("undo.json", "w") as f:
                json.dump(data, f, indent=4)
 

    def preview(changes):
        print("\nPREVIEW\n")
        for old, new in changes:
            print(old.name , "->" , new.name)

    def undo (filename):
        history = []
        try:
            with open(filename, "r") as f:
                history = json.load(f)

        except FileNotFoundError:
            print("History not found.")
        
        if history:
            for item in history:

                current = Path(item["new"])

                original = Path(item["old"])

                if current.exists():

                    if original.exists():
                         if original.exists() and current.name.lower() != original.name.lower():

                            print(original.name, "already exists")

                    else:

                        current.rename(original)
            

            with open(filename, "w") as f:
                json.dump([], f)
            print("Undo completed successfully.")

    if args.undo:
        undo("undo.json")

    else:

        if changes :
            preview(changes)

        else:
            print("No changes to preview.")
        
        if args.yes :
            for old, new in changes :
            
                old.rename(new)
            save_history(changes)
            print("Files renamed successfully.")

        elif changes:
            print("Preview only. Use --yes to apply changes.")

    
    