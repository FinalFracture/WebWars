import sorter
import splitter

inputing = 'Sunday. Sunday: Rain likely before 8am, then a chance of showers after 8am.'
sentence = []
unit = []
sorter = sorter.Sorter(2)
splitter = splitter.Splitter(2)

sentence = splitter.generate()



for word in sentence:
	unit.append(sorter.create_unit(word))
	for index in unit:
		print(f'{unit[0]} \n')
	unit.pop()
print(sorter.accepted_letters)