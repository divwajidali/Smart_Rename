def rename_file(file,prefix):
    new_name = prefix +"_" + file.name
    new_path = file.parent / new_name
    if new_path.exists() :
        return None

    else:
        return new_path
    
    