
import webbrowser
import time

"""
Infinite loop

while True:
    time.sleep(5)
    webbrowser.open("http://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7")
"""


"""
Set variable
for x in range (0, 3):
    time.sleep(5)
    webbrowser.open("http://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7")
"""

total_breaks = 3
break_count = 0
wait_time = 7200

print("This program started on "+time.ctime())

while(break_count < total_breaks):
    time.sleep(wait_time)
    webbrowser.open("http://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7")
    break_count = break_count + 1
