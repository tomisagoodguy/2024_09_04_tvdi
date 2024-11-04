from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title('登入')
        #self.geometry('600x400')
        
        #================style==========
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=("Helvetica",20))
        #===============end style========
        
        
        #==============top Frame========
        
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='多選鈕',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
    
        #==============end top Frame=====
        #===============bottomFrame==========
        bottomFrame= ttk.Frame(self)
        self.agreement = tk.StringVar()
        
        # 在 bottomFrame 中添加複選框
        ttk.Checkbutton(bottomFrame,text='我同意條款和條件',
        variable=self.agreement,
        onvalue='同意',
        offvalue='不同意',
        command=self.agreement_changed).pack()
        # 設置 bottomFrame 的布局
        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)

    #================end bottle Frame=====
    
    def agreement_changed(self):
        showinfo(
            title='Agreement',
            message=self.agreement.get()
            
        )
        message =self.agreement.get()
    
def main():
    window = Window(theme='arc')
    window.mainloop()
    
if __name__ == '__main__':
    main()
    