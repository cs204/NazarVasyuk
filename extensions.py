text = input("File name: ")
ext = text.split('.')[-1]
if text.endswith(".gif"):
	print("image/gif")
if text.endswith(".jpg"):
	print("image/jpeg")
if text.endswith(".jpeg"):
	print("image/jpeg")
if text.endswith(".png"):
	print("image/png")
if text.endswith(".pdf"):
	print("application/pdf")
if text.endswith(".txt"):
	print("text/plain")
if text.endswith(".zip"):
	print("application/zip")
"""Не могу сделать окончание application/octet-stream. Пробовал через match name.
В обоих вариантах выдает два ответа, например: text/plain и application/octet-stream сразу. Подскажите, пожалуйста, как это исправить?"""