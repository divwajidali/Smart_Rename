from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("path")
parser.add_argument("--prefix")
parser.add_argument("--suffix")
parser.add_argument("--numbering", action="store_true")
parser.add_argument("--replace", nargs=2)
parser.add_argument("--upper", action="store_true")
parser.add_argument("--lower", action="store_true")
parser.add_argument("--title", action="store_true")
parser.add_argument("--extension")
parser.add_argument("--type" , nargs=2)
parser.add_argument("--yes", action="store_true")
parser.add_argument("--recursive", action="store_true")

args = parser.parse_args()

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
    found = False
    if args.prefix :
        from renamer import prefix_rename
        prefix = args.prefix
        changes = []
        for file in files :
            if file.is_file() :
                found = True
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
                found = True
                old = file
                new = suffix_rename(file,suffix)
                if new is not None :
                    changes.append((old , new))
             
    elif args.numbering :
        changes = []
        for number, file in enumerate(files, start=1):
            if file.is_file():
                found = True
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
                found = True
                old = file
                if find in file.name:
                    new = find_replace(file, find, replace)

                    if new is not None:
                        changes.append((old, new))

    elif args.upper:
        from renamer import upper
        changes = []
        for file in files :
            if file.is_file() :
                found = True
                old = file
                new = upper(file)
                if new is not None:
                    changes.append((old, new))


    elif args.lower:
        from renamer import lower
        changes = []
        for file in files :
            if file.is_file() :
                found = True
                old = file
                new = lower(file)
                if new is not None:
                    changes.append((old, new))

    elif args.title:
        from renamer import title
        changes = []
        for file in files :
            if file.is_file() :
                found = True
                old = file
                new = title(file)
                if new is not None:
                    changes.append((old, new))

    elif args.type:
        from renamer import specific_type_rename
        type = args.type[0]
        new = args.type[1]
        changes = []
        for file in files :
            if file.is_file() :
                found = True
                old = file
                new_name = specific_type_rename(file, type, new)
                if new is not None:
                    changes.append((old, new_name))
                                   

    if not found:
        print("Files do not exist.") 

    if changes :
        from preview import preview
        preview(changes)

    else:
        print("No changes to preview.")
        
    if args.yes :
        for old, new in changes :
            
            old.rename(new)
        print("Files renamed successfully.")

    else: 
        print("Preview only. Use --yes to apply changes.")

    

