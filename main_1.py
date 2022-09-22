import os
from tkinter import *

import mysql.connector
from PIL import ImageTk, Image


loginWin = Tk()
loginWin.geometry('800x700')
loginWin.title("Credit Card Fraud Detection")
loginWin.state('zoomed')


def login():
    if user_name.get() == "" or passwd.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=loginWin)
    else:
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="",
                                          database="credit_card_fraud_detection")
            cur = con.cursor()

            cur.execute("select * from user_info where user_name = %s and password = %s",
                        (user_name.get(), passwd.get()))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=loginWin)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=loginWin)
                close()
                passMain()
                # close()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=loginWin)


def clear():
    uEntry.delete(0, END)
    pEntry.delete(0, END)


def close():
    loginWin.destroy()


bg_frame = Image.open('detection.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(loginWin, image=photo)
bg_panel_image = photo
bg_panel.place(x=100, y=150)

Label(loginWin, text="Credit Card Fraud Detector ", width=30, fg='Dark green', font='Verdana 30 bold').place(x=1, y=40)

heading = Label(loginWin, text="Sign In", width=20, fg='Dark green', font='Verdana 30 bold')
heading.place(x=800, y=150)

# Entry Box
user_name = StringVar()
passwd = StringVar()

uname = Label(loginWin, text="User Name", bg='pale green', fg='black', font='Verdana 12', width=15)
uname.place(x=800, y=300)

uEntry = Entry(loginWin, textvariable=user_name, width=25, background='white', font='Verdana 15')
uEntry.focus()
uEntry.place(x=1000, y=300)

passWD = Label(loginWin, text="Password", bg='pale green', fg='black', font='Verdana 12', width=15)
passWD.place(x=800, y=400)

pEntry = Entry(loginWin, show='*', textvariable=passwd, width=25, background='white', font='Verdana 15')
pEntry.place(x=1000, y=400)

Button(loginWin, text='Login', width=13, bg='spring green', fg='black', font='Verdana 12 bold',
       activeforeground='white',
       activebackground='blue', command=login).place(x=880,
                                                     y=550)

Button(loginWin, text='Clear', width=13, bg='spring green', fg='black', font='Verdana 12 bold',
       activeforeground='white',
       activebackground='blue', command=clear).place(x=1130, y=550)




def signup():
    def action():
        if email_id.get() == "" or username.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=regWin)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=regWin)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="",
                                              database="credit_card_fraud_detection")
                cur = con.cursor()
                sql = "INSERT INTO user_info (email_id, user_name, password) VALUES (%s,%s,%s)"
                val = (email_id.get(),
                       username.get(),
                       password.get())

                cur.execute(sql, val)
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration Successfull", parent=regWin)
                clear()
                switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=regWin)

    def switch():
        regWin.destroy()

    def clearform():
        email_id.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    regWin = Tk()
    regWin.geometry('600x600')
    regWin.title("Credit Card Fraud Detector")
    regWin.state('zoomed')

    # heading label
    Label(regWin, text='', width=70, fg='white', bg='aquamarine', font='Verdana 25 bold').place(x=0, y=0)
    Label(regWin, text="Credit Card Fraud Detector ", width=30, fg='black', bg='aquamarine',
          font='Verdana 30 bold').place(
        x=0, y=45)
    Label(regWin, text=' ', width=40, fg='aquamarine', bg='aquamarine',
          font='Verdana 30 bold').place(x=830, y=45)
    Label(regWin, text='', width=70, fg='white', bg='aquamarine', font='Verdana 25 bold').place(x=0, y=97)

    heading = Label(regWin, text="Sign Up", width=20, fg='black', font='Verdana 30 bold')
    heading.place(x=500, y=150)

    emailid = Label(regWin, text="Email ID", bg='aquamarine', fg='black', font='Verdana 12', width=15)
    emailid.place(x=500, y=250)

    email_id = StringVar()
    email_id = Entry(regWin, width=25, background='white', font='Verdana 15', textvariable=email_id)
    email_id.place(x=700, y=250)

    username = Label(regWin, text="User Name", bg='aquamarine', fg='black', font='Verdana 12', width=15)
    username.place(x=500, y=320)

    username = Entry(regWin, width=25, background='white', font='Verdana 15')
    username.place(x=700, y=320)

    password = Label(regWin, text="Password", bg='aquamarine', fg='black', font='Verdana 12', width=15)
    password.place(x=500, y=390)

    password = Entry(regWin, width=25, background='white', font='Verdana 15', show="*")
    password.place(x=700, y=390)

    very_pass = Label(regWin, text="Verify Password", bg='aquamarine', fg='black', font='Verdana 12', width=15)
    very_pass.place(x=500, y=460)

    very_pass = Entry(regWin, width=25, background='white', font='Verdana 15', show="*")
    very_pass.place(x=700, y=460)

    # button login and clear
    btn_signup = Button(regWin, text="Signup", width=13, bg='spring green', fg='black', font='Verdana 12 bold',
                        activeforeground='white',
                        activebackground='blue', command=action)
    btn_signup.place(x=570, y=560)

    btn_login = Button(regWin, text="Clear", width=13, bg='spring green', fg='black', font='Verdana 12 bold',
                       activeforeground='white',
                       activebackground='blue', command=clearform)
    btn_login.place(x=800, y=560)

    Label(regWin, text='Already on Credit Card Fraud Detector?', width=35, font='Verdana 12', fg='black').place(x=500,
                                                                                                                y=660)
    sign_in_btn = Button(regWin, text="Sign In Now", bg='spring green', fg='black', font='Verdana 10 bold',
                         activebackground='blue', activeforeground='white', width=15, command=switch)
    sign_in_btn.place(x=850, y=660)

    regWin.mainloop()


from tkinter import *
from tkinter import messagebox



#
#
def passMain():
    root = Tk()
    root.title('Credit Card Fraud Detector')
    root.geometry('800x1000')
    root.state('zoomed')

    from tkinter import filedialog

    def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.ipynb*"),
                                                         ("all files",
                                                          "*.*")))

        # Change label contents
        dataset.configure(text="File Selected: " + filename)

    def prediction():
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        from matplotlib import gridspec

        # In[2]:

        # load dataset
        data = pd.read_csv("creditcard.csv")

        # In[3]:

        data.head(10)

        # In[4]:

        # describing the data
        print(data.shape)
        print(data.describe())

        # In[5]:

        # imbalance in the data
        fraud = data[data['Class'] == 1]
        valid = data[data['Class'] == 0]
        outlierFraction = len(fraud) / float(len(valid))
        print(outlierFraction)
        print('Fraud Cases: {}'.format(len(data[data['Class'] == 1])))
        print('Valid Transactions: {}'.format(len(data[data['Class'] == 0])))

        # In[6]:

        # the amount details for fraudulent transaction
        fraud.Amount.describe()

        # In[7]:

        # the amount details for normal transaction
        valid.Amount.describe()

        # In[8]:

        # plotting the correlation matrix
        corrmat = data.corr()
        fig = plt.figure(figsize=(12, 9))
        sns.heatmap(corrmat, vmax=.8, square=True)
        plt.show()

        # In[9]:

        # separating the X and the Y values
        X = data.drop(['Class'], axis=1)
        Y = data["Class"]
        print(X.shape)
        print(Y.shape)
        # getting just the values for the sake of processing
        # (its a numpy array with no columns)
        xData = X.values
        yData = Y.values

        # In[10]:

        # training and testing data bifurcation
        from sklearn.model_selection import train_test_split

        # split the data into training and testing sets
        xTrain, xTest, yTrain, yTest = train_test_split(xData, yData, test_size=0.2, random_state=42)

        # In[11]:

        # building the Random Forest Classifier
        from sklearn.ensemble import RandomForestClassifier

        # random forest model creation
        rfc = RandomForestClassifier()
        rfc.fit(xTrain, yTrain)
        # predictions
        yPred = rfc.predict(xTest)

        # In[12]:

        # building all kinds of evaluating parameters
        from sklearn.metrics import classification_report, accuracy_score
        from sklearn.metrics import precision_score, recall_score
        from sklearn.metrics import f1_score, matthews_corrcoef
        from sklearn.metrics import confusion_matrix

        n_outliers = len(fraud)
        n_errors = (yPred != yTest).sum()
        print("The model used is Random Forest classifier")

        acc = accuracy_score(yTest, yPred)
        print("The accuracy is {}".format(acc))

        prec = precision_score(yTest, yPred)
        print("The precision is {}".format(prec))

        rec = recall_score(yTest, yPred)
        print("The recall is {}".format(rec))

        f1 = f1_score(yTest, yPred)
        print("The F1-Score is {}".format(f1))

        MCC = matthews_corrcoef(yTest, yPred)
        print("The Matthews correlation coefficient is{}".format(MCC))

        # In[13]:

        # visulalizing the confusion matrix
        LABELS = ['Normal', 'Fraud']
        conf_matrix = confusion_matrix(yTest, yPred)
        plt.figure(figsize=(12, 12))
        sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d")
        plt.title("Confusion matrix")
        plt.ylabel('True class')
        plt.xlabel('Predicted class')
        plt.show()

        # In[ ]:

        # os.system(filename)
        # os.startfile(filename, operation='open')

    Label(root, text='', width=70, fg='white', bg='aquamarine', font='Verdana 25 bold').place(x=0, y=0)
    Label(root, text="Credit Card Fraud Detector ", width=25, fg='black', bg='aquamarine',
          font='Verdana 30 bold').place(x=0, y=45)
    Label(root, text=' ', width=40, fg='aquamarine', bg='aquamarine', font='Verdana 30 bold').place(x=670, y=45)
    Label(root, text='', width=70, fg='white', bg='aquamarine', font='Verdana 25 bold').place(x=0, y=97)

    heading = Label(root, text="Upload Credit Card DataSet", width=30, fg='black', font='Verdana 20 bold')
    heading.place(x=500, y=200)



    dataset = Label(root, text="Upload DataSet", bg='aquamarine', fg='black', font='Verdana 12', width=15)
    dataset.place(x=600, y=390)


    dataset = Button(root,
                     text="Browse File",
                     command=browseFiles, bg='white', width=20)
    dataset.place(x=800, y=390)


    btn_login = Button(root, text="PREDICT", width=13, bg='spring green', fg='black', font='Verdana 12 bold',
                       activeforeground='white',
                       activebackground='blue', command=prediction)
    btn_login.place(x=700, y=560)
    root.mainloop()


Label(loginWin, text='New to Credit Card Fraud Detector?', width=35, font='Verdana 12', fg='black').place(x=780, y=650)
sign_up_btn = Button(loginWin, text="Sign Up Now", command=signup, bg='spring green', fg='black',
                     font='Verdana 10 bold',
                     activebackground='blue', activeforeground='white', width=15)
sign_up_btn.place(x=1120, y=650)

loginWin.mainloop()
