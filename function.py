def get_vat (payment):
	try:
		payment = float(payment)
		vat = payment*0.18
		return vat
	except (TypeError, ValueError):
		print("Неверный тип данных")

user_payment = input ('Введите сумму платежа: ')
print ("НДС от указанного платежа составляет:", get_vat(user_payment))