import urllib.parse

# Quute the path
def quote_path(path:str):
    path = path.lstrip('/')
    path = "//" + path
    path = urllib.parse.quote(path)
    return path