import os

def required_folder(*parts):
    """joins the args and creates the folder if not exists"""
    path = os.path.join(*parts)
    if not os.path.exists(path):
        os.makedirs(path)
    assert os.path.isdir(path), "%s is not a folder as required" % path
    return path