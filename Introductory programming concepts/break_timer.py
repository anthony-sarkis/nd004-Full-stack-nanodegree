
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

total_breaks = 30
break_count = 0
wait_time = 1800 * 1.5

print("This program started on " + time.ctime())
# Test
# webbrowser.open("https://www.youtube.com/watch?v=Odeys-B-ViY")

while(break_count < total_breaks):
    time.sleep(wait_time)
    webbrowser.open("https://www.youtube.com/watch?v=Odeys-B-ViY")
    break_count = break_count + 1
