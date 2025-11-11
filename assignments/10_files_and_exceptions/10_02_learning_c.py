from pathlib import Path
'''For this program I had to use a specific code to find the file since it was not working by just putting in file name'''

path = Path('10_files_and_exceptions/learning_python.txt')
content = path.read_text()
content = content.rstrip()
update = content.replace('Python','C')
print(update)

from pathlib import Path 

path = Path('10_files_and_exceptions/learning_python.txt')
content = path.read_text()
update = content.replace('Python','C')

lines = update.splitlines()
for line in lines:
    print(line)
