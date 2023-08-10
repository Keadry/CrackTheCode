import random

class number:
    def __init__(self):
        self.numbers = list(range(1, 10))
        self.wrongNumber = list(range(1,10))
        self.trueNumbers = []
        self.hintNumbers = []

    def numberGen(self):
        for _ in range(3):
            rastgeleSayi = random.choice(self.wrongNumber)
            self.trueNumbers.append(rastgeleSayi)
            self.wrongNumber.remove(rastgeleSayi)


    def hintMaker(self,hint):
        userGuess = hint

        correctDigits = sum([1 for x in userGuess if x in self.trueNumbers])
        correctPositions = sum([1 for x, y in zip(self.trueNumbers, userGuess) if x == y])

        print(f"Sayı : {self.hintNumbers} | Sonuç: {correctDigits} doğru rakam, {correctPositions} doğru pozisyon.")

    def twoCorrectFalsePlace(self):
        x = 1
        correct_number_1 = self.trueNumbers[x]
        y = 2
        correct_number_2 = self.trueNumbers[y]
        wrong_number = random.choice(self.wrongNumber)
        if  (x==0 and y == 1):
                self.hintNumbers = [wrong_number,correct_number_1, correct_number_2]
        elif x==1 and y==0:
                self.hintNumbers = [wrong_number,correct_number_2, correct_number_1]
        elif (x == 0 and y == 2):
                self.hintNumbers = [correct_number_2, wrong_number, correct_number_1]
        elif x == 2 and y == 0:
                self.hintNumbers = [correct_number_1, wrong_number, correct_number_2]
        elif (x == 1 and y == 2):
                self.hintNumbers = [correct_number_1, correct_number_2, wrong_number]
        elif x == 2 and y == 1:
                self.hintNumbers = [correct_number_2, correct_number_1, wrong_number]
    
        self.hintMaker(self.hintNumbers)

    def oneCorrectFalsePlace(self,x):
        correct_number = self.trueNumbers[x]
        wrong_numbers = random.sample([num for num in self.wrongNumber], 2)
        if(x == 0):
            y = random.randint(1,2)
            if y == 1:
                hint = [wrong_numbers[0], correct_number, wrong_numbers[1]]
            else:
                hint = [wrong_numbers[1], wrong_numbers[0], correct_number]
        elif(x==1):
            y = random.randint(1,2)
            if y == 1:
                hint = [correct_number, wrong_numbers[0], wrong_numbers[1]]
            else:
                hint = [wrong_numbers[1], wrong_numbers[0], correct_number]
        else:
            y = random.randint(1,2)
            if y == 1:
                hint =[correct_number, wrong_numbers[0], wrong_numbers[1]]
            else:
                hint = [wrong_numbers[0], correct_number, wrong_numbers[1]]

        self.hintNumbers = hint
        self.hintMaker(self.hintNumbers)
    
    def oneCorrectTruePlace(self):
        x = random.randint(0, 2)
        correct_number = self.trueNumbers[x]
        wrong_numbers = random.sample([num for num in self.wrongNumber], 2)
        if(x == 0):
                hint = [correct_number,wrong_numbers[0] , wrong_numbers[1]]
        elif(x==1):
                hint = [wrong_numbers[0], correct_number, wrong_numbers[1]]
        else:
                hint =[wrong_numbers[1], wrong_numbers[0], correct_number]
        self.hintNumbers = hint
        self.hintMaker(self.hintNumbers)
    def notCorrect(self):
        for _ in range(3):
            rastgeleSayi = random.choice(self.wrongNumber)
            self.hintNumbers.append(rastgeleSayi)
            self.wrongNumber.remove(rastgeleSayi)
        self.hintMaker(self.hintNumbers)
        self.hintNumbers.clear()

    def evaluateGuess(self, guess):
        correctPositions = sum([1 for x, y in zip(self.trueNumbers, guess) if x == y])

        if correctPositions == 3:
            return "Doğru tahmin! Tebrikler!"
        else:
            return " "

    def getUserGuess(self):
        while True:
            try:
                guess = input("Tahmininizi girin (virgül (',') ile ayırarak): ")
                guess = guess.replace(" ", "").split(",")
                guess = [int(num) for num in guess]
                if len(guess) == 3:
                    return guess
                else:
                    print("Lütfen 3 rakam girin.")
            except ValueError:
                print("Geçerli rakamlar girin.")

    def play(self):
        self.numberGen()
        print("Seçilen sayılar:", self.trueNumbers)

        self.notCorrect()
        self.twoCorrectFalsePlace()
        self.oneCorrectFalsePlace(1)
        self.oneCorrectTruePlace()
        self.oneCorrectFalsePlace(0)

        for _ in range(3):
            guess = self.getUserGuess()
            result = self.evaluateGuess(guess)
            print(result)
            if "Doğru tahmin" in result:
                break
        else:
            print("Üzgünüm, doğru tahmin yapamadınız. Doğru cevap:", self.trueNumbers)