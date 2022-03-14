# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import tkinter as tk
from playsound import playsound
from PIL import ImageTk, Image
from tkinter import *

window = tk.Tk()
window_prop = []

window_height = 250
window_width = 350

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
count = 0
positions = ["350x250+0+" + str(y_coordinate), "350x250+" + str(x_coordinate) + "+0",
             "350x250+" + str(screen_width - 350) + "+" + str(y_coordinate),
             "350x250+" + str(x_coordinate) + "+" + str(screen_height - 250),
             "350x250+0+0", "350x250+" + str(screen_width - 350) + "+0",
             "350x250+" + str(screen_width - 350) + "+" + str(screen_height - 250),
             "350x250+0+" + str(screen_height - 250),
             "350x250+" + str(175) + "+" + str(125),
             "350x250+" + str(screen_width - 350 - 175) + "+" + str(125),
             "350x250+" + str(screen_width - 350 - 175) + "+" + str(screen_height - 125 - 250),
             "350x250+" + str(175) + "+" + str(screen_height - 125 - 250)]
windows = []

text = """啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊

        """
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def birthday_scene():
        # set all background back to white...
        window.config(bg='white')
        window_prop[0].delete("1.0", "end")
        window_prop[0].configure(bg='white', font=("Times", 32))
        window_prop[0].insert(tk.END, "镟镟镟镟镟镟镟镟！生日快乐呀呀！<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")
        for x in range(12):
            windows[x].destroy()
        windows.clear()
        for x in range(8):
            windows.append(tk.Toplevel(window))
            windows[x].geometry(positions[x])
            if x == 0 or x == 4 or x == 7:
                bg = tk.PhotoImage(file='./popper.png')
            else:
                bg = tk.PhotoImage(file='./popperf.png')
            my_label = tk.Label(windows[x], image=bg)
            my_label.image = bg
            my_label.place(x=0, y=0, relwidth=1, relheight=1)
        windows[1].destroy()
        windows[3].destroy()
        window.after(500, func=play_music)

    def play_music():
        playsound('birth.mp3')


    def change_center():
        window_prop[0].delete("1.0", "end")
        window_prop[0].configure(font=("Times", 165, "bold"))
        window_prop[0].insert(tk.END, "!!!!!!!")
        window.after(2000, func=birthday_scene)


    def more_windows1():
        windows.append(tk.Toplevel(window))
        windows[8].geometry(positions[8])
        windows[8].config(bg='red')
        tk.Label(windows[8]).pack()
        aa_text = tk.Text(windows[8], height=200, width=200, bg="red", font=("Times", 165, "bold"))
        aa_text.pack()
        aa_text.insert(tk.END, "你")
        window.after(1000, func=more_windows2)


    def more_windows2():
        windows.append(tk.Toplevel(window))
        windows[9].geometry(positions[9])
        windows[9].config(bg='red')
        tk.Label(windows[9]).pack()
        aa_text = tk.Text(windows[9], height=200, width=200, bg="red", font=("Times", 165, "bold"))
        aa_text.pack()
        aa_text.insert(tk.END, "要")
        window.after(1000, func=more_windows3)


    def more_windows3():
        windows.append(tk.Toplevel(window))
        windows[10].geometry(positions[10])
        windows[10].config(bg='red')
        tk.Label(windows[10]).pack()
        aa_text = tk.Text(windows[10], height=200, width=200, bg="red", font=("Times", 165, "bold"))
        aa_text.pack()
        aa_text.insert(tk.END, "完")
        window.after(1000, func=more_windows4)


    def more_windows4():
        windows.append(tk.Toplevel(window))
        windows[11].geometry(positions[11])
        windows[11].config(bg='red')
        tk.Label(windows[11]).pack()
        aa_text = tk.Text(windows[11], height=200, width=200, bg="red", font=("Times", 165))
        aa_text.pack()
        aa_text.insert(tk.END, "啦")
        window.after(1000, func=change_center)


    def window_a():
        aa_text = tk.Text(window, height=200, width=200, bg="red", font=("Times", 10))
        aa_text.pack()
        aa_text.insert(tk.END, text)
        window_prop.append(aa_text)
        window.after(2000, func=windows_a)


    def windows_a():
        for x in windows:
            a_text = tk.Text(x, height=200, width=200, bg="red", font=("Times", random.randint(5, 32)))
            a_text.pack()
            a_text.insert(tk.END, text)
        window.after(1000, func=more_windows1)


    def change_button():
        global count
        if count == 0:
            button['text'] = "都说了不要按我！"
        if count == 1:
            button.pack_forget()
            window.config(bg='red')
            for x in range(8):
                windows.append(tk.Toplevel(window))
                windows[x].geometry(positions[x])
                windows[x].config(bg='red')
                tk.Label(windows[x]).pack()
                windows[x].after(1000)
            window.after(3000, func=window_a)
        count += 1


    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    button = tk.Button(window, text="不要按我！", command=change_button)
    button.pack()
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
