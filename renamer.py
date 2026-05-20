def prefix_rename(file,prefix):
    new_name = prefix +"_" + file.name
    new_path = file.parent / new_name
    if new_path.exists() :
        return None

    else:
        return new_path
    
def suffix_rename(file, suffix):
    new_name = file.stem + "_" + suffix + file.suffix
    new_path = file.parent / new_name
    if new_path.exists() :
        return None

    else:
        return new_path   
    
def find_replace(file, find, replace):
    new_name = file.name.replace(find, replace)
    new_path = file.parent / new_name
    if new_path.exists():
        return None
    
    else:
        return new_path
    
def upper(file):
    new_name = file.name.upper()
    new_path = file.parent / new_name

    if new_path.exists() :
        return None
    
    else:
        return new_path
    
def lower(file):
    new_name = file.name.lower()
    new_path = file.parent / new_name

    if new_path.exists() :
        return None
    
    else:
        return new_path
    
def title(file):
    new_name = file.stem.title() + file.suffix
    new_path = file.parent / new_name

    if new_path.exists() :
        return None
    
    else:
        return new_path
    
def rename_extension(file, new):
    new_path = file.with_suffix(new)
    

    if new_path.exists():
        return None
    
    else :
        return new_path
    
def specific_type_rename(file,type, new):
    if file.suffix == type :
        new_path = file.with_suffix(new)
    

        if new_path.exists():
            return None
    
        else :
            return new_path