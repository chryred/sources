from zipfile import *

def extractZip(zipname):
	with ZipFile(zipname, "r") as ziph:
		ziph.extractall()
		print("압축 풀기 성공")

extractZip("D:\Lecture\Python\python.zip")