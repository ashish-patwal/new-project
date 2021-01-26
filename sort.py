from pathlib import Path
import shutil

path = Path('/home/lucifer/Downloads')


for file in path.glob('*.jpg'):
    shutil.move(file, '/home/lucifer/Downloads/images')


for file in path.glob('*.jpeg'):
    shutil.move(file, '/home/lucifer/Downloads/images')


for file in path.glob('*.png'):
    shutil.move(file, '/home/lucifer/Downloads/images')


for file in path.glob('*.gif'):
    shutil.move(file, '/home/lucifer/Downloads/images')
