def numeroprimo(a):
    if a < 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True            
def app():
    a = int(input("escribe un numero:    "))
    result = numeroprimo(a)

    if result is True:
        print(" el numero es primo")
    else:
        print(" el numero no es primo")
if __name__ == "__main__":
    app()
