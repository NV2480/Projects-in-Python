# pip install xlrd
import pandas as pd
import datetime
import smtplib
import os
os.chdir(r"C:\Users\dell\PycharmProjects\Python\automaticWishes")

GMAIL_ID=''
GMAIL_PSWD=''


def sendMsg(to,sub,msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s= smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to, f"Subject: {sub}\n\n{msg}")
    s.quit()




if __name__=="__main__":
    sendMsg(GMAIL_ID,"subject","test message")
    exit()
    df=pd.read_excel("data.xlsx",engine='openpyxl')

    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%y")

    writeInd=[]
    for index,item in df.iterrows():
        bday= item['Bday'].strftime("%d-%m")
        if (today==bday) and  yearNow not in str(item['Year']):
            sendMsg(item['Email'], "Happy Bday", item['Wishes'])
            writeInd.append(index)

    print(writeInd)
    for i in writeInd:
        yr=df.loc[i,'Year']
        print(yr)
        df.loc[i, 'Year']= str(yr) +', ' +str(yearNow)
        print(df.loc[i,'Year'])
    print(df)
    df.to_excel('data.xlsx',index=False)
