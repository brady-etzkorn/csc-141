from pathlib import Path 

filenames = ['10_files_and_exceptions/mycat.txt','10_files_and_exceptions/dog.txt']
for filename in filenames:
    path = Path(filename)
    try:
        names = path.read_text()
        print(names)
    except FileNotFoundError:
        pass