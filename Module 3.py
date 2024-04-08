Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Part 1: Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge forthe food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.
>>>
>>> # I prefer using a real world problem for this, so I added a few sandwiches to show my skills on making a dictionary baked on the employee lunch order I took care of last week.
>>>  subway_Sandwiches = {
  File "<stdin>", line 1
    subway_Sandwiches = {
IndentationError: unexpected indent
>>> subway_Sandwiches = {'Spicy Italian': 6.50,'Steak & Cheese': 8.50,'Tuna'
: 8.50,'Veggie Delight': 6.50,'B.L.T.': 5.25}
>>> # All of these sandwiches were not picked by accident, this was an order I was told to place for my team for a company lunch one day. From here, I willnow apply tip and tax for all the sandwiches I ordered for my team to let HR know how much I should be reimbursed for this order. But first, the total of the sandwiches must be calculated before knowing tax and tips is calculated on top.
>>>
>>> # Here is the sum of the Subway sandwich order:
>>> sum(subway_Sandwiches)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(subway_Sandwiches.values())
35.25
>>> # Now, the user can calculate the percentages for tip and tax on the order.
>>> tax = * 0.07
  File "<stdin>", line 1
SyntaxError: can't use starred expression here
>>> # Wait, before continuing, the sum of the sandwiches should be calculated as its own value that will be called 'order'.
>>> order = sum(subway_Sandwiches.values())
>>> # Good, now to go back to fixing and adding the calculations for tax and tip.
>>> tax = order * 0.07
>>> print('The tax will be: $', tax)
The tax will be: $ 2.4675000000000002
>>> print("The tax will be: $', '{.2f}'.format(tax))
  File "<stdin>", line 1
    print("The tax will be: $', '{.2f}'.format(tax))
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print('The tax will be: $', {tax:.2f})
  File "<stdin>", line 1
    print('The tax will be: $', {tax:.2f})
                                      ^
SyntaxError: invalid decimal literal
>>> print('The tax will be: $', f{tax:.2f})
  File "<stdin>", line 1
    print('The tax will be: $', f{tax:.2f})
                                       ^
SyntaxError: invalid decimal literal
>>> print('The tax will be: $', f'{tax:.2f}')
The tax will be: $ 2.47
>>>  tip = (order + tax) * 0.18
  File "<stdin>", line 1
    tip = (order + tax) * 0.18
IndentationError: unexpected indent
>>> tip = (order + tax) * 0.18
>>> print('The tip will be: $', f'{tip:.2f}')
The tip will be: $ 6.79
>>> # Finally, the total amount can be calculated.
>>> total = order + tip + tax
>>> print('The entire cost for the employee lunch will be:', total)
The entire cost for the employee lunch will be: 44.50665
>>> print('The entire cost for the employee lunch will be:', f'{total:.2f}')

The entire cost for the employee lunch will be: 44.51
>>>
>>>
>>>
>>> # Part 2: Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on a 24-hour clock when the alarm goes off.
>>> # User is asked what the current time is:
>>> current_Time = int(14)
>>> # User is asked how long they would like to set the alarm for:
>>> setting_Alarm = int(127)
>>> # Calculating when the alarm will go off:
>>> alarm = (current_Time + setting_Alarm) % 24
>>>  print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 00.')
  File "<stdin>", line 1
    print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', currprint('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 00.')                     IndentationError: un, it will go off at', alarm,': 00.') print('On a 24-hour clock,if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at' print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', cur print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at',
ck, if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it wilting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 0rm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 00.')
  File "<stdin>", line 1
    print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 00.') print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 00.') print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 00.')
Inde
>>> print('On a 24-hour clock, if I set a', setting_Alarm, 'hour alarm at', current_Time, ': 00, it will go off at', alarm,': 00.')
On a 24-hour clock, if I set a 127 hour alarm at 14 : 00, it will go off at 21 : 00.
>>>
