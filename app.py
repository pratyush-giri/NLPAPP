from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPapp:

    def __init__(self) :
        #creating object of database clas
        self.dbo = Database()
        self.root = Tk()
        self.apio = API()
        self.root.title("NLPAPP")
        # self.root.iconbitmap("path of the image") to set user defined icons
        self.root.geometry("350x600")
        self.root.configure(bg='#889E9B')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        #heading of login
        heading = Label(self.root,text="NLPAPP",bg="#889E9B",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        # email input
        email_label = Label(self.root,text="enter email",bg="#889E9B",fg="white")
        email_label.pack(pady=(10,10))
        email_label.configure(font=('verdana',10,'bold'))
        self.email_entry = Entry(self.root,width=50)
        self.email_entry.pack(pady=(5,10),ipady=4)
        # password input
        password_label = Label(self.root,text="enter password",bg="#889E9B",fg="white")
        password_label.pack(pady=(10,10))
        password_label.configure(font=('verdana',10,'bold'))
        self.password_entry = Entry(self.root,width=50,show='*')
        self.password_entry.pack(pady=(5,10),ipady=4)

        #login button
        login_btn = Button(self.root,text="login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(20,10))

        #redirect button
        red_label = Label(self.root,text="not a member?",bg="#889E9B",fg="black")
        red_label.pack(pady=(10,10))

        redirect_btn = Button(self.root,text="register",width=30,height=2,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()
    
         #heading of login
        heading = Label(self.root,text="NLPAPP",bg="#889E9B",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        # name input
        name_label = Label(self.root,text="enter name",bg="#889E9B",fg="white")
        name_label.pack(pady=(10,10))
        name_label.configure(font=('verdana',10,'bold'))
        self.name_entry = Entry(self.root,width=50)
        self.name_entry.pack(pady=(5,10),ipady=4)
        # email input
        email_label = Label(self.root,text="enter email",bg="#889E9B",fg="white")
        email_label.pack(pady=(10,10))
        email_label.configure(font=('verdana',10,'bold'))
        self.email_entry = Entry(self.root,width=50)
        self.email_entry.pack(pady=(5,10),ipady=4)
        # password input
        password_label = Label(self.root,text="enter password",bg="#889E9B",fg="white")
        password_label.pack(pady=(10,10))
        password_label.configure(font=('verdana',10,'bold'))
        self.password_entry = Entry(self.root,width=50,show='*')
        self.password_entry.pack(pady=(5,10),ipady=4)

        #register button
        register_btn = Button(self.root,text="register",width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(20,10))

        #redirect button
        red_label = Label(self.root,text="already a member?",bg="#889E9B",fg="black")
        red_label.pack(pady=(10,10))

        login_btn = Button(self.root,text="login",width=30,height=2,command=self.login_gui)
        login_btn.pack(pady=(10,10))


    #clearing the gui 
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()



    #fetching registration details
    def perform_registration(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','registration successful ,you can login now')
        else:
            messagebox.showerror('Error','email aleady exists')
    #checking login credentials
    def perform_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success','login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','login failed')

    def home_gui(self):
        self.clear()
        heading = Label(self.root,text="NLPAPP",bg="#889E9B",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        #sentiment analysis button
        sentiment_btn = Button(self.root,text="Sentiment Analysis",width=30,height=4,command=self.sentiment_analysis_gui)
        sentiment_btn.pack(pady=(10,10))
        # named entity recognition
        ner_btn = Button(self.root,text="Named Entity Recognition",width=30,height=4,command=self.ner_analysis_gui)
        ner_btn.pack(pady=(20,10))

        emotion_btn = Button(self.root,text="emotion Analysis",width=30,height=4,command=self.emotion_analysis_gui)
        emotion_btn.pack(pady=(20,10))

        logout_btn = Button(self.root,text="Logout",width=30,height=4,command=self.login_gui)
        logout_btn.pack(pady=(20,10))
    def sentiment_analysis_gui(self):

        self.clear()
        heading = Label(self.root,text="NLPAPP",bg="#889E9B",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading2 = Label(self.root,text="Sentiment Analysis",bg="#889E9B",fg="white")
        heading2.pack(pady=(20,20))
        heading2.configure(font=('verdana',20))

        sentiment_label = Label(self.root,text="enter the text")
        sentiment_label.pack(pady=(10,10))
        self.sentiment_entry = Entry(self.root,width=50)
        self.sentiment_entry.pack(pady=(5,10),ipady=4)

        analyze_btn = Button(self.root,text="analyze sentiment",width=30,height=2,command=self.do_sentiment_analysis)
        analyze_btn.pack(pady=(20,10))

        self.sentiment_result = Label(self.root,text=" ",bg="#889E9B",fg="white")
        self.sentiment_result.pack(pady=(10,20))
        self.sentiment_result.configure(font=('verdana',16))

        goback_btn = Button(self.root,text="go back",width=30,height=2,command=self.home_gui)
        goback_btn.pack(pady=(20,10))




    def ner_analysis_gui(self):

        self.clear()
        heading = Label(self.root,text="NLPAPP",bg="#889E9B",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading2 = Label(self.root,text="NER Analysis",bg="#889E9B",fg="white")
        heading2.pack(pady=(20,20))
        heading2.configure(font=('verdana',20))

        NER_label = Label(self.root,text="enter the text")
        NER_label.pack(pady=(10,10))
        self.NER_entry = Entry(self.root,width=50)
        self.NER_entry.pack(pady=(5,10),ipady=4)

        analyze_btn = Button(self.root,text="analyze NER",width=30,height=2,command=self.do_ner_analysis)
        analyze_btn.pack(pady=(20,10))

        self.NER_result = Label(self.root,text=" ",bg="#889E9B",fg="white")
        self.NER_result.pack(pady=(10,20))
        self.NER_result.configure(font=('verdana',16))

        goback_btn = Button(self.root,text="go back",width=30,height=2,command=self.home_gui)
        goback_btn.pack(pady=(20,10))
        
    def emotion_analysis_gui(self):
        pass


    def do_sentiment_analysis(self):
        text = self.sentiment_entry.get()
        result = self.apio.sentiment_analysis(text)
        txt =''
        for i in result['sentiment']:
            txt = txt + i + "->" + str(result['sentiment'][i]) + '\n'
        self.sentiment_result['text'] = txt


    def do_ner_analysis(self):
        text = self.NER_entry.get()
        result = self.apio.ner_analysis(text)
        # print(result)
        txt =''
        for i in result['entities']:
            txt = txt + 'name' + '->' + i['name'] + " " + 'category' + '->' + i['category'] + '\n'

        self.NER_result['text'] = txt
nlp = NLPapp()  