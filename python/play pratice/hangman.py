#secret word
#letter input
#letter checker
#user progress
#number of guesses

def UpdateUserProgress(userProgress, secretWord, guess):
    x = len(secretWord)#prepares variables
    userProgress = list(userProgress)
    secretWord = list(secretWord)

    for i in range(x):#replaces ? with correct letters
        if guess in secretWord[i]:
            userProgress[i] = guess


    output ="" # converts to string
    for i in range(x):
        output = output + userProgress[i]
    return output

def GetGuess():#gets input
    print("what letter will you guess?")
    return input()

def PlayGame():
    print("whats the word?")
    secretWord = input()
    userProgress = "?" * len(secretWord)
    lives = 10
    guess = " " # handles spaces
    if guess in secretWord:  # handles spaces
        userProgress = UpdateUserProgress(userProgress, secretWord, guess)
    print(userProgress)

    while (lives != 0) and ("?" in userProgress):#runs loop and checks for an end
        guess = GetGuess()
        if guess in secretWord: #checks for correct guess
            userProgress = UpdateUserProgress(userProgress, secretWord, guess)
            print(userProgress)
        else: #takes a life
            print("nope")
            lives = lives -1
            print("you have", lives, "lives left")

    if(lives == 0):#finishing remarks
        print("you lose!")
    else:
        print("you win!")




PlayGame()
