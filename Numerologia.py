nombre = input("Escriba su nombre completo ")
total = 0
count_spaces = 0

for letter in nombre:
        if letter.isalpha():
            letter_int = ord(letter)
            total += letter_int

print("El valor ASCII de su nombre es: ", total)

str_pseudo = str(total)

while (len(str_pseudo) != 1):

    secreto = 0
    for str_number in str_pseudo:
            number_again = int(str_number)
            secreto += number_again
    str_secreto = str(secreto)
    str_pseudo = str_secreto # para que el str_pseudo se update

print("El numero secreto es", secreto)
