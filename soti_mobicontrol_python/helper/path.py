import urllib.parse

# Quute the path
def quote_path(path:str):
    path = path.lstrip('/')
    path = "//" + path
    path = urllib.parse.quote(path)
    return path

# clean path
def clean_path(path:str):
    # Remove any leading or trailing slashes
    # Replace backslashes with forward
    return path.strip('\\').strip('/').replace('\\', '/')