a = input('Введите слово: ').lower()
b= reversed(a)

if list(a) == list(b):
    print(True)
else:
    print(False)
