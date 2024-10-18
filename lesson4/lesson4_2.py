import tkinter as tk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('這是我的第一個視窗!')
        self.geometry('800x300')
        message = tk.Label(self, text='hello,這是第一個視窗')
        message.pack()

def main():

    # root = tk.Tk()
    Window = Window()
    Window.mainloop()
    
if __name__ == "__main__":
    main()
