# Aquí programa una función que resuelva el problema 1 FizzBuzz

def fizzbuzz(n):
    """
        func que recibe un numero n y retorna una lista de numeros del 1 al n
        reemplazando los multiplos de 3 por Fizz, los multiplos de 5 por Buzz
        y los multiplos de 3 y 5 por FizzBuzz
    """
    arr = [x for x in range(1, n + 1)]
    for i in range(len(arr)):
        x = arr[i]
        if x % 5 == 0 and x % 3 == 0:
            arr[i] = 'FizzBuzz'
        elif x % 3 == 0:
            arr[i] = 'Fizz'
        elif x % 5 == 0:
            arr[i] = 'Buzz'
    return arr

if __name__ == '__main__':
    print(fizzbuzz(100))
