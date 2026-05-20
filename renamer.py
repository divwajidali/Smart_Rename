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
    
def to_uppercase(file):

    new_name = file.name.upper()
    if new_name == file.name:
        return None

    return file.parent / new_name
    
def to_lowercase(file):
    new_name = file.name.lower()
    

    if new_name == file.name :
        return None
    
    
    return file.parent / new_name
    
def to_titlecase(file):
    new_name = file.stem.title() + file.suffix
    new_path = file.parent / new_name

    if new_name == file.name :
        return None
    

    return new_path
    
def rename_extension(file, new):
    if not new.startswith("."):
        new = "." + new
    new_path = file.with_suffix(new)
    

    if new_path.exists():
        return None
    
    else :
        return new_path
    
def specific_type_rename(file,file_type, new):
    if not new.startswith("."):
    
        new = "." + new
    if file.suffix == type :
        new_path = file_type.with_suffix(new)
    

        if new_path.exists():
            return None
    
        else :
            return new_path
    return None