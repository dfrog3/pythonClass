def vowel():

    print("give me a string")
    userString = input()
    x = 0

    vowels = "aeiou"

    for letter in userString.lower():
        if letter in vowels:
            x = x + 1
        else:
            continue
    print(x)
main()