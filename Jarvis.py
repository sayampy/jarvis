def login():
    import random
    password = []
    for i in range(5):
        pd = random.randint(0,9)
        password.append(pd)
    pd=str(password).replace("[","]").replace("]",",").replace(",","'").replace("'"," ").replace(" ","")
    import sqlite3 as sql
    db = sql.connect('jarvis_database.db')
    hello = db.execute("insert into jarvis VALUES('name',00, 'favourite', :id, 10)",{'id':pd})
    db.commit()
    db.close()
    print("Remember your password- "+pd)
def my_name(name,password):
    import sqlite3 as sql
    db = sql.connect('jarvis_database.db')
    db.execute("update jarvis set name = '"+name+"' where password = "+str(password))
    if 'None' in name:
        quit()
    else:
        print("\nok,you are "+name.title())
    db.commit()
    db.close()

def my_age(age,password):
    import sqlite3 as sql
    db = sql.connect('jarvis_database.db')
    db.execute("update jarvis set age = "+str(age)+" where password="+str(password))
    if age is None:
        quit()
    else:
        print("\nok,you are ",age,"years old")
    db.commit()
    db.close()
    if age >= 18:
        print("\nyou are now 🧑🏻 or 👩🏻")
    elif (age <= 17) and (age >= 15):
        print("\nokk you are in"+age)
def my_fav(fav,password):
    import sqlite3 as sql
    db = sql.connect('jarvis_database.db')
    db.execute("update jarvis set favourite = '"+fav+"' where password = " + str(password))
    if 'None' in fav:
        quit()
    else:
        print("\nok,you say, you love "+fav)
    db.commit()
    db.close()
def intro():
      white = 'https://'
      sg = ()
      hello='r',"are"
      usl = ('https://youtube.com/results?q=')
      url = 'https://google.com/search?q='
      nope=('nothing','no one','bla bla','i don''t no','idk','hxhjsisichhc','ayzgfghxuxuhxv gis','j2jwi8dudhdhdhskodi','sljfgchdkx','')
      name_reply=("so are no one!?","nothing!!","don't joke with me","Are you kidding me!","Are you blank!!")
      def remove(string):
          str(string).replace("(",")").replace(")",",").replace(",","")
      import sqlite3 as sql
      import time,random
      import webbrowser
      import datetime
      from time import strftime
      import sys, wikipedia
      from datetime import date
      def primt(str):
            for letter in str:
                  sys.stdout.write(letter)
                  sys.stdout.flush()
                  time.sleep(0.04)
      db = sql.connect('jarvis_database.db')
      name = db.execute("select name from jarvis")
      name = name.fetchone()
      name = str(name).replace("(",")").replace(")",",").replace(",","'").replace("'","")
      
      primt("\nHELLO"+", I Am JARVIS")
      db.close()
      primt("   \n      ask me by typing")
      time.sleep(.61)

def start(password):
      import sqlite3 as sql
      import time,random
      import webbrowser
      import datetime
      from time import strftime
      import sys, wikipedia
      from datetime import date
      white = 'https://'
      sg = ()
      hello='r',"are"
      usl = ('https://youtube.com/results?q=')
      url = 'https://google.com/search?q='
      nope=('nothing','no one','bla bla','i don''t no','idk','hxhjsisichhc','ayzgfghxuxuhxv gis','j2jwi8dudhdhdhskodi','sljfgchdkx','')
      name_reply=("so are no one!?","nothing!!","don't joke with me","Are you kidding me!","Are you blank!!")
      welcome_command=('are you fine','how are you')
      well_reply=("I am fine,How about you?","not bad","well,and you?")
      name_ask=("who are you","what is your name","your name","who are you?","what is your name?","your name?")
      name_introduce=("I am Jarvis","My name is Jarvis")
      doing_what=("what are you doing")
      jarvis_doing=("chatting","typing","chat with you")
      idk_command = ("idk","i don't know","nope","no")
      sad_word=("sad","hopeless","depressed","mournful","despairing","miserable","downcast","gloomy","heartbroken","my heart is broke")
      support_word=("Hang in there","Don't give up","Keep fighting!","Stay strong.","Never give up","Never say 'die'.","Come on! You can do it!.")
      my_name=("who am i?","who am i","what is my name","what is my name?")
      my_favourite=("what is my favourite","what is my fav","my favourite?","what is my fav?")
      db = sql.connect('jarvis_database.db')
      name = db.execute("select name from jarvis where password = " + str(password))
      name = name.fetchone()
      name = str(name).replace("(",")").replace(")",",").replace(",","'").replace("'","")
      if 'None'in name:
          quit()


      def primt(str):
            for letter in str:
                  sys.stdout.write(letter)
                  sys.stdout.flush()
                  time.sleep(0.04)
      choice=random.choice
      ran_support_word=choice(support_word)
      random_reply=random.choice(name_reply)
      sg = input('\nyou: ')
      sg2 = sg.lower()
      if 'good' in sg2:
             sat = sg2.replace('good', '\n')
             primt(sat)
      elif (sg2 in name_ask):
             primt(choice(name_introduce))
      elif 'bengali' in sg2:
            primt('\nঠিক আছে।\tদ্যাখো আমি বা‌ংলা বলছি☺️,%s!')
      elif sg2 in my_name:
            db = sql.connect('jarvis_database.db')
            name = db.execute("select name from jarvis where password = " + str(password))
            name = name.fetchone()
            name = str(name).replace("(",")").replace(")",",").replace(",","'").replace("'","")
            primt("You told me, you are "+name+" 😄😃😀")
            db.close()
      elif 'hack' in sg2:
            print('\n\n'+' hack😜'*990)
      elif 'are you a girl' in sg2:
            primt ("\nNope, I am a boy")
      elif 'who made you' in sg2:
            primt(" \n\tI made by—\n      SAYAM GOSWAMI")
      elif ('google' in sg2) and ('search' in sg2) or ('google' in sg2):
                 sayam = sg2.replace('google', '')
                 asmi = sayam.replace('search', '')
                 primt(" \nopening..")
                 webbrowser.open(url + asmi)
      elif ("hello" == sg2):
            primt(" Hello,")
      elif ('youtube' in sg2) and ('search' in sg2) or ('youtube' in sg2):
                init = sg2.replace('youtube', '')
                initi= init.replace('search', '')
                webbrowser.open(usl + initi)
      elif('time' in sg2):
            primt(strftime('\n\t %H:%M:%S %p'))
      elif 'site'in sg2:
                 primt('\nWhich site ::'), input ("")
                 webbrowser.open(white + hat + '.com')
      elif sg2 in welcome_command:
            primt(random.choice(well_reply))
            #this is not for anyone
            #LOCK SAYAM
      elif 'my repl.it' in sg2:
            webbrowser.open('https://repl.it/')
      elif sg2 in sad_word:
            primt(ran_support_word)
      elif ('quit' in sg2 or 'stop' in sg2 or 'bye' in sg2):
                 time.sleep(1)
                 primt("\nok,\n\tbye😭")
                 quit()
      elif doing_what in sg2:
                  primt(choice(jarvis_doing))
                  
      elif "help" in sg2:
                  primt(" \n\ntry this commands\n")
                  time.sleep(1)
                  print("\n☞can  you hack me\n\n☞hack me\n\n☞are you a girl?\n\n☞speak in bengali\n\n☞what is your name?\n\n☞good morning\n\n☞who made you?\n\n☞open google\n\n☞open youtube\n\n☞time")
      elif( "date" in sg2) or ("today" in sg2):
           primt("\ntoday is:"),print(date.today())
      elif sg2 in idk_command:
           primt("\nIn which topic you talking about?\n I skipped it")
      elif ("i am "or "my name is ")in sg2:
          primt("\nplease change your name with this function-- jarvis2.my_name('your name', your password)")
      elif sg2 in my_favourite:
          db = sql.connect('jarvis_database.db')
          fav = db.execute("select favorite from jarvis where password = "+str(password))
          fav = fav.fetchone()
          fav = str(fav).replace("(",")").replace(")",",").replace(",","'").replace("'","")
          primt("your favourite is " + fav +"😁😉")
          db.close()
      elif "my age" in sg2:
          db = sql.connect('jarvis_database.db')
          age = db.execute("select age from jarvis where password = " +str(password))
          age = age.fetchone()
          age = str(age).replace("(",")").replace(")",",").replace(",","'").replace("'","")
          primt("your age is "+ age +"😉")
          db.close()
      elif ("am i"and "older"or "elder"and " than you")in sg2:
          db = sql.connect('jarvis_database.db')
          age = db.execute("select age from jarvis where password = " + str(password))
          age = age.fetchone()
          age = str(age).replace("(",")").replace(")",",").replace(",","'").replace("'","")
          if int(age) >=12:
              primt("I think yes")
          else:
              primt("I think my boss is elder than you😁")
      else:
                 time.sleep(1)
                 primt(" Can search from wikipedia?(y/n)\n")
                 com = input("")
                 come = com.lower()
                 if 'y' in come:
                       primt(" \n found from wikipedia--\n\t")
                       primt(wikipedia.summary(sg2,sentences=2))
                 else:
                       primt("\nI don't know what you mean!!")
def add(command,function):
      import time,random
      import webbrowser
      import datetime
      from time import strftime
      import sys, wikipedia
      from datetime import date
      def primt(str):
            for letter in str:
                  sys.stdout.write(letter)
                  sys.stdout.flush()
                  time.sleep(0.04)
      sg4=input("\nyou: ").lower()
      if command in sg4:
                  primt(function)
      else:
                  primt("your add func is not available")
def info():
      def primt(str):
            for letter in str:
                  sys.stdout.write(letter)
                  sys.stdout.flush()
                  time.sleep(0.04)
      import sys,time
      primt("Hey,I am the owner of this module.\nthis is a very simple text commanding bot with multi functions-- like YouTube,google searches.\nFor help you can type help after run this.\n\nIf any mistake or any function you want, feel free to email me at—\n\tsujata.howrah.belgachia@gmail.com")
