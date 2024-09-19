#   Yanni Klironomos
#   261233238

#Brief Description:

#This program determines whether a response online was written by a human
#or a chatbot by evaluating key features: message hour, response time,
#words per minute (WPM), number of typos and the 'eeooeotetto' test

#It uses the Comp 202 lecture material at McGill from Lectures 1-4

#Code Below: 

RESPONSE_TIME_THRESHOLD_MIN = 0.15
#The response time threshold of 9 seconds converted to minutes (9/60 = 0.15 min)

WPM_THRESHOLD = 66
#The word-per-minute (WPM) threshold 

CORRECT_NB_OF_T_WANG = 3
#The correct number of t's in 'eeooeotetto'

TWO_AM = 2.0
#The value for 2 am in 24-hour format

FIVE_AM = 5.0
#The value for 5 am in 24-hour format

print("Bot or Human? Let's figure this out!")

message_hour = float(input(
    "When did you receive your response " \
    "(type a float between 0 and 24)? "))
#The hours are in a 24-hour format (1 means 1 AM and 13 means 1 PM)

if message_hour >= TWO_AM and message_hour <= FIVE_AM:
    print("You just talked to a bot")
else:
    response_time = float(input(
        "How long did it take to get your response (in min)? "))
    if response_time < RESPONSE_TIME_THRESHOLD_MIN:
        print("You just talked to a bot")
    else:
        number_of_words = int(input(
            "How many words in your response? "))
        wpm = number_of_words / response_time #Compute WPM for the next conditional
        if wpm < WPM_THRESHOLD:
                print("You just talked to a fellow human")
        else:
            number_of_typos = int(input(
                "How many typos in the response "\
                "(grammatical errors, misspelled words, etc.)? "))
            if number_of_typos > 0:
                print("You just talked to a fellow human")
            else:
                number_of_t = int(input(
                    "Ask the responder how many 't' there are "\
                    "in 'eeooeotetto' and type their answer? "))
                if number_of_t == CORRECT_NB_OF_T_WANG:
                    print("You just talked to a fellow human")
                else:
                    print("You just talked to a bot")
