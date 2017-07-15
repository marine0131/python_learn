from sys import argv

script, user_name=argv
prompt ='> '

print "Hi %s, I'm the %s script." %(user_name, script)
print "Do you like me %s?"%user_name
likes = raw_input(prompt)

print "where do you live %s?"% user_name
lives=raw_input(prompt)

print """
alright, so you said %r about like me.
and, you said %r about where you live.
"""%(likes,lives)
