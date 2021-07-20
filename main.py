import time

phrases = ["The quick brown fox jumps over the lazy dog", "Whatever you are, be a good one.",
           "Be the change you wish to see in the world.", "Try and fail, but never fail to try."]


def main():
    index = 1
    print("Choose a phrase from the list to measure typing speed or choose 5 to enter a custom phrase: ")
    for i in phrases:
        print(index, i)
        index += 1
    print("5 Custom Phrase")
    user_input = input("Choose an option: ")
    menu(user_input)


def menu(user_input):
    while user_input:
        if user_input == "1":
            test_phrase = phrases[0]
            type_test(test_phrase)
        elif user_input == "2":
            test_phrase = phrases[1]
            type_test(test_phrase)
        elif user_input == "3":
            test_phrase = phrases[2]
            type_test(test_phrase)
        elif user_input == "4":
            test_phrase = phrases[3]
            type_test(test_phrase)
        elif user_input == "5":
            newPhrase = str(input("Please enter a custom phrase: "))
            phrases.append(newPhrase)
            print("Added new phrase to array")
            test_phrase = phrases[4]
            type_test(test_phrase)
        else:
            print("Please enter a valid selection from the menu.")
            main()


def type_test(test_phrase):
    t0 = time.time()  # start time
    inputText = str(input('Enter the phrase: "%s" as fast as possible: ' % test_phrase))
    t1 = time.time()  # stop time
    timeTaken = (t1-t0)/60
    grossWPM = ((len(inputText)/5)/timeTaken)
    timeTakenSeconds = timeTaken*60
    timeTakenSeconds = "{:.2f}".format(timeTakenSeconds)
    print('Time taken: ', timeTakenSeconds, "seconds")
    wpmFormatted = round(grossWPM)
    print('WPM', wpmFormatted)


main()