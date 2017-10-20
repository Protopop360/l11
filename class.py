class Cars: #классы это тип данных кооторый мы саи объявляем
	wheels = 4
	engine = True

	def ride(self): #метод класса или егоо функция ну или дейстовие объекта
		print("wroom wroom mfk")


volga = Cars()

# print(volga)
print(volga.wheels)
print(volga.engine)
volga.ride()
volga.wheels +=6
print(volga.wheels)
