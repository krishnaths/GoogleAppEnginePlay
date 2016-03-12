import sys

print 'Content-Type: text/html'
print ''

print '<pre>'
#Read the form input
guess=-1
data=sys.stdin.read()
try:
   guess= int(data[data.find('=')+1:])
except:
   guess= -1
print 'Your guess is', guess
answer = 42
if guess < answer:
   print 'Your guess is too low'
if guess== answer:
   print 'Your guess is correct'
if guess > answer:
   print 'Your guess is too high'
print '</pre>'

print '''<form method="post" action="/">
Enter Guess:  <input type="text" name="guess"><br>
<input type="submit">
</form>'''
