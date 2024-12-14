from TPNumbeer import TPNumber
def main():
    
        number = TPNumber("E0.53333333", 16, 8)
        number2 = TPNumber("-A.B.", 16, 8)
        now = number2 - number
        print(f"{number.number:.20f}\t{number.number_string}")
        print(f"{number2.number:.20f}\t{number2.number_string}")
        now.setBase(10)
        print(f"{now.number:.20f}\t{number2.number_string}")
        now.Invert()

if __name__ == "__main__":
    main()

else:
    print("Ошибка: Неподобразимый объект float")