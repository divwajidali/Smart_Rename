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