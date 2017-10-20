import os
# print(list("список"))

# i = []
# l = ["N","a","me"]
# print(i)
# print(l)

# t = [" Света","sdf","rf","rf"]
# t.count(2)
# print(t)
i = 0
print(os.getcwd())
while True:
	os.chdir(r"C:\Users\Администратор\Desktop\lop")
	os.mkdir("stupidman32" + str(i))
	i+=1