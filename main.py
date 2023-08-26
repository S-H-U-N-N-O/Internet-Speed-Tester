from tkinter import *
import speedtest_cli

def speeder():
    speed = speedtest_cli.Speedtest()
    speed.get_servers()
    down = str( round(speed.download()/(10**6),3))+" Mbps"
    up = str( round(speed.upload()/(10**6),3))+" Mbps"
    title2.config(text=down)
    title4.config(text=up)


root = Tk()
root.geometry("1366x768")

title = Label(root,justify="center", text="Internet Speed Tester", font=("Times New Roman", 40, "bold"))
title.place(x=40, y=40)

title1 = Label(root,justify="center", text="Download Speed", font=("Times New Roman", 20, "bold"))
title1.place(x=40, y=120)

title2 = Label(root,justify="center", text="00", font=("Times New Roman", 18, "bold"))
title2.place(x=40, y=160)

title3 = Label(root,justify="center", text="Upload Speed", font=("Times New Roman", 20, "bold"))
title3.place(x=40, y=240)

title4 = Label(root,justify="center", text="00", font=("Times New Roman", 18, "bold"))
title4.place(x=40, y=280)

button = Button(root, text="Check Speed", font=("Times New Roman", 18, "bold"), relief=RAISED, bg="cyan", command=speeder)
button.place(x=40, y=330)

root.mainloop()