#!/usr/bin/python2
import Skype4Py, time
import sqlite3 as lite

s = Skype4Py.Skype()

s.Attach()
con = lite.connect('skype.sqlite')
cur = con.cursor()

print "Bot running..."
mutewords = ["yolo",
             "y o l o"] # Add your own mutewords (words that trigger chat muting) in the format 
             # "word",

responses = {'hello, bot':  "Hi, %user%!",
            } # To add your own responses, add in the format
            # 'Message from user': "Bots response",

chat = s.Chat('CHAT_ID') # Find the skype conversation's ID and replace CHAT_ID with the value
mutes = {}

def send (msg):
    global chat
    try:
        chat.SendMessage(msg)
    except:
		pass

def is_message_done (msgid):
    cur.execute('SELECT * FROM skype WHERE mid=' + str(msgid))
    i = 0
    for c in cur.fetchall():
        i = i + 1
    if i == 0:
        #try:
            cur.execute('INSERT INTO skype VALUES (' + str(msgid) + ')')
            con.commit()
            return True;
        #except:
        #    pass
    else: return False;

def toggle_listener (chat, handle):
    global mutes
    for member in chat.MemberObjects:
        if member.Handle == handle:
            if member.Role == "USER":
                send("Muting " + m.Sender.Handle + " for 30 seconds!")
                try:
                    member.Role = "LISTENER"
                except:
                    pass
                mutes[handle] = 30
            else:
                try:
                    member.Role = "USER"
                except:
                    pass
                send("Unmuting " + handle + "!")
                try:
                    del mutes[handle]
                except:
                    pass

def check_mutes (chat):
    global mutes
    for m, t in mutes.items():
        mutes[m] = mutes[m] - 1
        #print "Unmuting " + m + " in " + str(t)
        if t < 1:
            toggle_listener(chat, m)

while True:
    check_mutes(chat)
    for m in chat.RecentMessages:
        if is_message_done(m.Id):
            print m.Sender.Handle + ": " + m.Body;
            for word in mutewords:
                if word in m.Body.lower():                
                    #try:
                        if m.Sender.Handle not in mutes:
                            print("muting (id " + str(m.Id) + ") : " + m.Sender.Handle)
                            toggle_listener(chat, m.Sender.Handle)
                    #except: pass
            for listen, say in responses.iteritems():
                if listen in m.Body.lower():
                    say = say.replace("%user%", m.FromDisplayName);
                    send(say);
    time.sleep(1)