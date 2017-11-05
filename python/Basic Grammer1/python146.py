from os.path import getsize

file1 = "test_2.txt"
file2 = "test_2_copy.txt"

file_size1 = getsize(file1)
file_size2 = getsize(file2)

print("File Name: %s \tFile Size %d" %(file1, file_size1))
print("File Name: %s \tFile Size %d" %(file2, file_size2))