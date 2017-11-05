import os, glob

folder = "D:\\Lecture"
file_list = os.listdir(folder)

print(file_list)

pdir = os.getcwd(); print(pdir)
os.chdir(folder); print(os.getcwd())
os.chdir(pdir)

files = "*.txt"
file_list = glob.glob(files)
print(file_list)