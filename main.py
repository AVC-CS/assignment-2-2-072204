def main():
    
    celsius = int(input('Enter your fahrenheit celsius:')) 

    fahrenheit = 9 / 5 * celsius + 32

    print(f'Celcius: {celsius} \t Fahrenheit: {fahrenheit:.2f}')

    return celsius, fahrenheit


if __name__ == '__main__':
    main()
