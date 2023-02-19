# -*- coding: utf-8 -*-
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

truth = split_into_sentences("Would you rather once a day touch a child or murder a man , for the rest of your life. Would you rather curb stomp a child or eat a human eyeball? Would you rather stab a newborn baby in the head or a pregnant woman in the stomach? What was the worst thing you did while drunk? When was the last time you lied? What's the worst thing you've ever done at work? When was the last time you cried? What's your biggest fear? What's your biggest fantasy? Do you have any fetishes? Who's the last person you searched on Instagram? What's something you're glad your family doesn't know about you? Have you ever cheated on someone? Where's the weirdest place you peed? What's the worst thing you've ever done? What's the strangest thing you've ever eaten? What's your relationship dealbreaker? What's a secret you've never told anyone? Do you have a hidden talent? Who was your first celebrity crush? What are your thoughts on polyamory? What's the worst intimate experience you've ever had? What's the best intimate experience you've ever had? Have you ever cheated in an exam? If you were going to be on a reality TV show, which would it be? What's the drunkest you've ever been? Have you ever broken the law? What's the most embarrassing thing you've ever done? What's your biggest insecurity? Have you ever stayed friends with someone because it benefitted you beyond just the friendship? What's the biggest mistake you've ever made? What's the most disgusting thing you've ever done? Who would you like to kiss in this room? What's one thing you hate people knowing about you? What's the worst thing anyone's ever done to you? What's the best thing anyone's ever done for you? Have you ever had a run in with the law? What's your worst habit? What's the most embarrassing thing you've done in a taxi? What's the worst thing you've ever said to anyone? Have you ever peed in the shower? What's the strangest dream you've had? Have you ever been caught doing something you shouldn't have? What's the worst date you've been on? What's the best date you've been on? What happened on the latest night out you've ever had? What's your biggest regret? What's the biggest misconception about you? Have you ever said something you regret about someone in this room? What's one thing you wish people knew about you? Where's the weirdest place you've had sex? Why did your last relationship break down? Have you ever lied to get out of a bad date? What's the most trouble you've been in?  When did you last have sex outside? What's the worst thing you've lied about? What's one thing you wish you'd lied about? What's the best piece of advice you've been given? What's the most you've spent on a night out? Have you ever returned or re-gifted a present? Name a time you think you were a bad partner What's your guilty pleasure? What's one thing you only do when you're alone? If you had to get back with an ex, who would you choose? If you had to cut one friend out of your life, who would it be? Do you have a favourite friend? Do you have a favourite sibling? What's the strangest rumour you've heard about yourself? What's your biggest turn on? What's your favorite gross food combination? What's the silliest reason you've left a club early? What have you purchased that's been the biggest waste of money?If you could swap lives with someone in this room, who would it be? Tell me about your first kiss What was the most inappropriate time you farted? What's something you really hope your family never finds out about? What's the weirdest lie you've ever told? Do you have any fake social media accounts? Have you ever peed in the pool? Who do you think is the worst-dressed person in this room? Have you ever practiced kissing in a mirror? How would you rate your looks on a scale of 1 to 10? What gives you the ick? Have you ever told a lie about your BFF to make yourself look better? What's your worst fashion moment? What's your biggest pet peeve? What TV character do you relate to the most? What celebrity do you look up to? Who do you like best - Kris, Kourtney, Kim, Khloé, Kendall or Kylie? If you could be one celebrity for a day, who would it be? Have you ever dined and dashed? What's the weirdest thing you've ever eaten? If you could do any job in the world, what would it be? What's your dream life? What do you value the most - money, fame, success,  friends, family, etc?")
dare = split_into_sentences("Pull a moonie. Attempt to break dance for 30 seconds. Serenade the person to your right. Dance like your life depends on it with no music for 2 whole minutes. Give a personalised insult to everyone in the room. Tell everyone your most embarrassing story about yourself. Show the most embarrassing photo on your phone. Attempt to impersonate everyone in the room. Let the group text your mum on your phone something embarrassing.  Quack like a duck until your next turn. Call a random phone number and talk to them for as long as you can. Using only your elbows, upload a Facebook status. Close your eyes, sit on someone’s lap and guess who it is. Argue with a wall and pretend like it talks back for one minute. Call one of your parents and tell them you’ve pooped today.")
#import radom
import random
import sys
import time


#animated typing (rpg style)
def type(text):
  words = text
  for char in words:
    time.sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

def the_game():
    #printing the game
    print("\ntruth or dare?")

    #user input
    user_input = input()


    #truth, dare or other user input
    if user_input == "truth":
      type(random.choice(truth))
    elif user_input == "dare":
      type(random.choice(dare))
    else:
      type("its either truth or dare. check your spelling.")

loop_variable = 10

while loop_variable ==10:
    the_game()
