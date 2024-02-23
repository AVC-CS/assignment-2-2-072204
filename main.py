def main():
    
    celsius = int(input('Enter your celsius value:')) 

    fahrenheit = 9 / 5 * celsius + 32

    print(f'{celsius} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit.')

    return celsius, fahrenheit


if __name__ == '__main__':
    main()
