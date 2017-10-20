# Описываем участников 
# их скорость, топливо, нитро, бак, расход топлива, имя, пройденный путь 
# На выбор есть различная скорость, нитро-расход топлива в 3 раза - Каждый ход, 
# побеждает тот кто приехал первым либо тот у кого позже закончилось топливо.


def easy(car):
	car["distance"]+= car["speed"]
	car["fuel"]-=car["expen"]


def nitro(car):
	car["distance"] += car["nitro"]
	car["fuel"]-= car["expen"] * 3

def stats(car):
	print("\nТекущее состояние"+
		" Топливо: "+ str(car["fuel"])+
		" Расстояние "+ str(car["distance"]) + "/" + str(track),
		sep = "\n"
		)


def step(car):
	choose = input("Твой ход, "+ car["name"]+ ". Выбирай с умом"+
			" 1- просто едем \n"+
			"2- топим \n"
			)

	if choose == "1":
		easy(car)
	elif choose == "2":
		nitro(car)
	else:
		print("Ты совершил ошибку")

	stats(car)

track = 50




car1 = {
	"name": "Бетмобиль",
	"speed": 6,
	"fuel": 30,
	"expen": 3,
	"nitro": 9,
	"distance":0
}
car2 = {
	"name": "Черная молния",
	"speed": 8,
	"fuel": 25,
	"expen": 4,
	"nitro":13,
	"distance":0
}


while True:
	step(car1)
	step(car2)
	input()