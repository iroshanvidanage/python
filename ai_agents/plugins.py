import os, glob, datetime, stat

def search_files(pattern, path):
    print(path)
    return [f for f in glob.glob(os.path.join(path, pattern), recursive=True)]

def get_file_meta(file_path):
    stats = os.stat(file_path)
    size = stats.st_size
    modified_date = datetime.fromtimestamp(stats.st_mtime).isoformat()
    permissions = stat.filemode(stats.st_mode)

if __name__ == '__main__':
    file_path = r'../'
    print(search_files("*.py", file_path))