import pyautogui, time
time.sleep(5)
f = open("PizzaTime")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
print(range(10))









