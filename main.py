
import random

print("                        BIBLE QUIZ")
print("                    CREATIVE COMPUTING")
print("                  MORRISTOWN, NEW JERSEY")

print("THIS GAME IS A QUIZ WHICH TESTS ")
print ("YOUR KNOWLEDGE OF BIBLICAL EVENTS, PLACES, ")
print ("AND PERSONS.")

print ()

print ('I WILL ASK YOU A QUESTION AND THEN WAIT ')
print ('FOR YOUR ANSWER.  IF YOUR ANSWER IS CORRECT ')
print ('I WILL PROCEED TO THE NEXT QUESTION.  IF YOUR ')
print ('ANSWER IS INCORRECT I WILL GIVE YOU THE ')
print ('CORRECT ANSWER AND THEN PROCEED TO THE  ')
print ('NEXT QUESTION. ')

print ()

print ('ALL ANSWERS ARE ONE WORD. ')
print ('ALL ANSWERS MUST BE CORRECTLY SPELLED. ')
print ('THERE IS A TOTAL OF 25 QUESTIONS. ')
print ('HOW MANY QUESTIONS DO YOU WISH TO TRY? ')

n = int(input())

A=list(range(1,26)) # создадим массив, после чего будем использвать его в качестве выбора вопроса

random.shuffle(A)# рандомно переставляем порядок в массиве для создания уникальности каждой игры
C=0
CA =0
N1 = 0
X = int



for i in range (n): # выводим столько вопросов, сколько ввел пользователь на 31стрк.
    X = A[0]  # берем номер вопроса

    print('\nQUESTION № ' + str(C+1))
    C = C+1
    if X ==1:
        print("WHO SET FIRE TO THREE HUNDRED FOXES TAILS")
        Result = input()
        Answer ="SAMSON"

        A.pop(0)


        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 1 JUDGES 15:4,5")
            CA=CA+1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "SAMSON" + " 1 JUDGES 15:4,5")

    if X ==2:
        print("WHAT HEBREW SERVED A QUICK LUNCH UNDER A TREE")
        Result = input()
        Answer ="ABRAHAM"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ "GEN. 18:6-8")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ABRAHAM" + "GEN. 18:6-8")

    if X ==3:
        print("WHAT HUNGRY MAN CURSED A FRUITLESS FIG TREE")
        Result = input()
        Answer ="JESUS"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " MARK 11:12-14")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "JESUS" + " MARK 11:12-14")

    if X ==4:
        print("WHO KILLED HIS BROTHER FOR HUMBLING HIS SISTER")
        Result = input()
        Answer ="ABSALOM"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 2 SAM. 13")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ABSALOM" + " 2 SAM. 13")

    if X ==5:
        print("WHO KILLED HIS BROTHER FOR HUMBLING HIS SISTER")
        Result = input()
        Answer ="ABSALOM"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 2 SAM. 13")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ABSALOM" + " 2 SAM. 13")


    if X ==6:
        print("WHO HAD THREE HUNDRED CONCUBINES")
        Result = input()
        Answer ="SOLOMON"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 1 KINGS 11:1-3")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "SOLOMON" + " 1 KINGS 11:1-3")

    if X ==7:
        print("WHAT BOY HAD A VARIEGATED COAT")
        Result = input()
        Answer ="JOSEPH"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ "  GEN. 37:3")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "JOSEPH" + " GEN. 37:3")


    if X ==8:
        print("WHO HAD A SEAMLESS COAT")
        Result = input()
        Answer ="JESUS"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ "  JOHN 19:23")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "JESUS" + " JOHN 19:23")


    if X == 9:
        print("WHO TOOK OFF HIS SHOE TO BIND A CONTRACT")
        Result = input()
        Answer ="BOAZ"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ "  RUTH 4:7-9")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "BOAZ" + " RUTH 4:7-9")

    if X == 10:
        print("WHO SLEPT ON AN IRON BEDSTEAD OVER THIRTEEN FEET LONG")
        Result = input()
        Answer ="OG"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ "   DUET. 3:11")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "OG" + "  DUET. 3:11")

    if X == 11:
        print("WHO WAS THE FIRST CITY-BUILDER")
        Result = input()
        Answer ="CAIN"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " GEN. 4:17")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "CAIN" + " GEN. 4:17")

    if X == 12:
        print("WHAT PHYSICIAN WAS AN AUTHOR")
        Result = input()
        Answer ="LUKE"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " COL. 4:14")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "LUKE" + " COL. 4:14")

    if X == 13:
        print("WHAT SONG-COMPOSER IS CREDITED WITH 1005 SONGS")
        Result = input()
        Answer ="SOLOMON"

        A.pop(0)


        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 1 KINGS 4:32")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "SOLOMON" + " 1 KINGS 4:32")

    if X == 14:
        print("WHO WAS THE FIRST PERSON KILLED")
        Result = input()
        Answer ="ABEL"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " GEN. 4:8")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ABEL" + " GEN. 4:8")

    if X == 15:
        print("WHO WAS BURIED IN A CAVE WITH HIS WIFE")
        Result = input()
        Answer ="ABRAHAM"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " GEN. 25:9-10")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ABRAHAM" + " GEN. 25:9-10")

    if X == 16:
        print("WHO ACCIDENTLY HANGED HIMSELF IN A TREE")
        Result = input()
        Answer ="ABSALOM"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 2 SAM. 18:9")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ABSALOM" + " 2 SAM. 18:9")

    if X == 17:
        print("WHAT BLIND HAN KILLED THREE THOUSAND AT A RELIGOUS FEAST")
        Result = input()
        Answer ="SAMSON"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " JUDGES 16:23-30")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "SAMSON" + " JUDGES 16:23-30")

    if X == 18:
        print("WHAT WAS THE NAME OF THE FIRST CITY EVER BUILT")
        Result = input()
        Answer ="ENOCH"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " GEN. 4:17")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ENOCH" + " GEN. 4:17")

    if X == 19:
        print("WHO WAS A MIGHTY HUNTER")
        Result = input()
        Answer ="NIMROD"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " GEN. 10:9-12")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "NIMROD" + " GEN. 10:9-12")

    if X == 20:
        print("WHO DROVE FURIOUSLY")
        Result = input()
        Answer ="JEHU"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 2 KINGS 9:20")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "JEHU" + " 2 KINGS 9:20")

    if X == 21:
        print("WHO WAS THE FIRST CHRISTIAN MARTYR")
        Result = input()
        Answer ="STEPHEN"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " ACTS 7")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "STEPHEN" + " ACTS 7")

    if X == 22:
        print("WHO FELL ASLEEP DURING A LONG SERMON")
        Result = input()
        Answer ="EUTYCHUS"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " ACTS 20:9")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "EUTYCHUS" + " ACTS 20:9")

    if X == 23:
        print("WHAT CITY IS CALLED THE CITY OF PALM TREES")
        Result = input()
        Answer ="JERICHO"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " DUET. 34:3")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "JERICHO" + " DUET. 34:3")

    if X == 24:
        print("WHO CLIMBED A TREE TO SEE JESUS")
        Result = input()
        Answer ="ZACCHAEUS"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " LUKE 19:4")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "ZACCHAEUS" + " LUKE 19:4")

    if X == 25:
        print("WHO KILLED GOLIATH")
        Result = input()
        Answer ="DAVID"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " 1 SAM. 17:49")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "DAVID" + " 1 SAM. 17:49")

    if X == 26:
        print("WHO WAS CAST INTO A DEN OF LIONS")
        Result = input()
        Answer ="DANIEL"

        A.pop(0)

        if Result.upper() == Answer:
            print("CORRECT ANSWER--VERY GOOD! "+ " DAN. 6:16")
            CA = CA + 1
        else:
            print("INCORRECT ANSWER")
            print("THE CORRECT ANSWER IS " + "DANIEL" + " DAN. 6:16")
P = ((CA/n)*100)

print("OUT OF " + str(n) + " QUESTIONS YOU ANSWERED " + str(CA) + " CORRECTLY.")
print("YOUR PERCENTAGE FOR CORRECT ANSWERS IS "+ str(P) + "%")


print ()






