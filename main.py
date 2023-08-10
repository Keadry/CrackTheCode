from numbersManager import number

numberGame = number()
numberGame.numberGen()
print("Seçilen sayılar:", numberGame.trueNumbers)

numberGame.notCorrect()
numberGame.twoCorrectFalsePlace()
numberGame.oneCorrectFalsePlace(1)
numberGame.oneCorrectTruePlace()
numberGame.oneCorrectFalsePlace(0)
for _ in range(3):
    guess = numberGame.getUserGuess()
    result = numberGame.evaluateGuess(guess)
    print(result)
    if "Doğru tahmin" in result:
        break
    else:
        print("Üzgünüm, doğru tahmin yapamadınız. Doğru cevap:", numberGame.trueNumbers)