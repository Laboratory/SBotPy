SBotPy
======

A simple Skype bot, written in Python.

This is a Skype bot I wrote one evening to kick people who say "YOLO" from a group skype chat.  I've modified the logic a bit so that it mutes the user for 30 seconds instead, and it can do basic reponses when it hears a string.  As this was written relatively quickly, the code is far from perfect, and I intend to go through, clean things up and write some documentation when I get a chance (I am aware the code is fairly messy). The current use of the database is not thought out all that well either, and I hope to move all the bad words and responses to the database, as well as potentially implementing chat logging and a web interface (although those are a long way off).

Requirements
------------

* Python 2.7+
* Skype4Py