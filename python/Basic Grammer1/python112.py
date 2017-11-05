solarsys = ["태양", "수성", "금성", "지구", "화성", "목성", "토성", "천왕성", "해왕성"]
solarsys.remove("해왕성")
del solarsys[1:3]

print(solarsys)
print(len(solarsys))
print(solarsys.count("태양"))

del solarsys
#print(solarsys)