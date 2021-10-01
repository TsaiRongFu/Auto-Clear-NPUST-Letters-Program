from tkinter import messagebox
from selenium import webdriver
from icon import img
import tkinter as tk
import math as math
import base64
import time
import os

window = tk.Tk()
window.title('Auto-Clean-NPUST-Mail-Program')
window.geometry('500x300')
icon = open("Auto-Clean-NPUST-Mail-Program-Icon.ico","wb+")
icon.write(base64.b64decode(img))
icon.close()
window.iconbitmap('Auto-Clean-NPUST-Mail-Program-Icon.ico')
os.remove("Auto-Clean-NPUST-Mail-Program-Icon.ico")


def PopUpWindow(message):
    if (message.split(',')[0] == "Info"):
        messagebox.showinfo("系統提醒：", message.split(',')[1])
    elif (message.split(',')[0] == "Error"):
        messagebox.showerror("系統提醒：", message.split(',')[1])
    elif (message.split(',')[0] == "Warning"):
        messagebox.showwarning("系統提醒：", message.split(',')[1])

def AutoLogin():
    global browser
    HideLable()
    accountContent = account_entry.get()
    passwordContent = password_entry.get()
    if (len(accountContent) == 0 and len(passwordContent) == 0):
        message = "Warning,帳號密碼不能為空！"
        PopUpWindow(message)
        password_or_account_no_value_label.grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.E+tk.W)
    elif (len(accountContent) == 0):
        message = "Warning,帳號不能為空！"
        print(message)
        PopUpWindow(message)
        account_no_value_label.grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.E+tk.W)
    elif (len(passwordContent) == 0):
        message = "Warning,密碼不能為空！"
        print(message)
        PopUpWindow(message)
        password_no_value_label.grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.E+tk.W)
    else:
        browser = webdriver.Firefox()
        browser.get('https://mail.npust.edu.tw/')
        browser.find_element_by_name("USERID").send_keys(accountContent)
        time.sleep(0.5)
        browser.find_element_by_name("PASSWD").send_keys(passwordContent)
        time.sleep(0.5)
        browser.find_element_by_name("Submit").click()
        time.sleep(1)
        try:
            (browser.find_element_by_class_name("msg").text).split(' ')[0]
            Error = True
        except:
            Error = False
        if (Error):
            browser.quit()
            message = "Warning,輸入帳號或密碼錯誤，請重新輸入！"
            PopUpWindow(message)
            password_or_account_error_label.grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.E+tk.W)
        else:
            login_success_label.grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.E+tk.W)
            message = "Info,登入成功"
            PopUpWindow(message)
            manual_login_button['state'] = tk.DISABLED
            
def ManualLogin():
    global browser
    browser = webdriver.Firefox()
    browser.get('https://mail.npust.edu.tw/')
    
def LockAutoButton():
    auto_login_button['state'] = tk.DISABLED

def HideLable():
    login_success_label.grid_forget()
    account_no_value_label.grid_forget()
    password_no_value_label.grid_forget()
    password_or_account_error_label.grid_forget()
    password_or_account_no_value_label.grid_forget()

def DeleteAllEmail():
    try:
        global browser
        try:
            iframe1 = browser.find_element_by_xpath('//iframe[contains(@name, "m2k")]')
            browser.switch_to.frame(iframe1)
        except:
            pass
        aText = browser.find_elements_by_class_name("TreeNode")[1].text
        browser.find_element_by_link_text(aText).click()
        while True:
            UnText = browser.find_elements_by_class_name("TreeNode")[1].text
            if (UnText == '收信匣'):
                DeleteEmailReturn = 'Info,刪除完畢！'
                PopUpWindow(DeleteEmailReturn)
                return
            try:
                browser.find_element_by_id("lvMsgList_hchkbox").click()
                browser.execute_script("MsgFuncObj.MailDel(1);")
            except:
                pass
            time.sleep(0.5)
    except:
        systemMessage = 'Error,清空資源回收桶失敗！可能原因：\n\n1.程式偵測到您未啟的動瀏覽器：\n       1-1.您如果是自動登入可能是登入失敗或是您關閉了瀏覽器\n       1-2.您如果是手動登入可能是尚未登入成功或是您關閉了瀏覽器\n\n2.如以上瀏覽器啟動正常，可能為網路延遲，請再一次嘗試Delete\n\n3.如以上均不成功請到以下網址回報Issues給作者：\n\n                     https://git.io/JOuYU'
        PopUpWindow(systemMessage)
        
def CleanRecycleBin():
    try:
        global browser
        try:
            iframe1 = browser.find_element_by_xpath('//iframe[contains(@name, "m2k")]')
            browser.switch_to.frame(iframe1)
        except:
            pass
        aText = browser.find_elements_by_class_name("TreeNode")[5].text
        browser.find_element_by_link_text(aText).click()
        time.sleep(1)
        browser.execute_script("MsgFuncObj.MBoxPurge(null, true);")
        browser.switch_to.alert.accept()
        cleanRecycleBinMessage = 'Info,回收桶清除完畢！'
        PopUpWindow(cleanRecycleBinMessage)
    except:
        systemMessage = 'Error,清空資源回收桶失敗！可能原因：\n\n1.程式偵測到您未啟的動瀏覽器：\n       1-1.您如果是自動登入可能是登入失敗或是您關閉了瀏覽器\n       1-2.您如果是手動登入可能是尚未登入成功或是您關閉了瀏覽器\n\n2.如以上瀏覽器啟動正常，可能為網路延遲，請再一次嘗試Recycling Bin\n\n3.如以上均不成功請到以下網址回報Issues給作者：\n\n                     https://git.io/JOuYU'
        PopUpWindow(systemMessage)

def Reset():
    try:
        browser.quit()
    except:
        pass
    try:
        HideLable()
    except:
        pass
    try:
        if (manual_login_button['state'] != "normal"):
            manual_login_button['state'] = tk.NORMAL
        if (auto_login_button['state'] != "normal"):
            auto_login_button['state'] = tk.NORMAL
    except:
        pass
    try:
        if (len(password_entry.get()) != 0):
            password_entry.delete(0,'end')
        if (len(account_entry.get()) != 0):
            account_entry.delete(0,'end')
    except:
        pass
    RestSuccess = 'Info,重置成功！'
    PopUpWindow(RestSuccess)

auto_caption_row_frame = tk.LabelFrame(window, text='如果您要交由程式自動執行登入請填入資料',labelanchor='n',font=('DFKai-SB', 12))
auto_caption_row_frame.pack(side=tk.TOP)

account_label = tk.Label(auto_caption_row_frame, text='       帳號：',font=('DFKai-SB', 12))
account_label.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.E+tk.W)
account_entry = tk.Entry(auto_caption_row_frame, width=15)
account_entry.grid(column=1, row=1, ipadx=5, pady=5, sticky=tk.E+tk.W)

password_label = tk.Label(auto_caption_row_frame, text='       密碼：',font=('DFKai-SB', 12))
password_label.grid(column=0, row=2, ipadx=5, pady=5, sticky=tk.E+tk.W)
password_entry = tk.Entry(auto_caption_row_frame, show="*", width=15)
password_entry.grid(column=1, row=2, ipadx=5, pady=5, sticky=tk.E+tk.W)

password_or_account_error_label = tk.Label(auto_caption_row_frame, text='帳號密碼輸入錯誤！', fg='red' ,font=('DFKai-SB', 10))
password_or_account_no_value_label = tk.Label(auto_caption_row_frame, text='帳號密碼欄位不能為空！', fg='red' ,font=('DFKai-SB', 10))
password_no_value_label = tk.Label(auto_caption_row_frame, text='密碼欄位不能為空！', fg='red' ,font=('DFKai-SB', 10))
account_no_value_label = tk.Label(auto_caption_row_frame, text='帳號欄位不能為空！', fg='red' ,font=('DFKai-SB', 10))
login_success_label = tk.Label(auto_caption_row_frame, text='登入成功', fg='blue' ,font=('DFKai-SB', 10))

auto_login_button = tk.Button(auto_caption_row_frame, text='登入', fg='black', command=AutoLogin ,font=('DFKai-SB', 12, 'bold'))
auto_login_button.grid(column=3, row=3, ipadx=5, pady=5, sticky=tk.E+tk.W)

manual_caption_row_frame = tk.LabelFrame(window, text='如果您要手動登入請按以下按鈕',labelanchor='n',font=('DFKai-SB', 12))
manual_caption_row_frame.pack(side=tk.TOP)

manual_login_label = tk.Label(manual_caption_row_frame, text='         ',font=('DFKai-SB', 12))
manual_login_label.grid(column=1, row=1, ipadx=5, pady=5, sticky=tk.E)
manual_login_button = tk.Button(manual_caption_row_frame, text='登入', fg='black', command=lambda:[LockAutoButton(),ManualLogin()] ,font=('DFKai-SB', 12, 'bold'))
manual_login_button.grid(column=2, row=1, ipadx=5, pady=5, sticky=tk.E)

delete_letter_caption_row_frame = tk.LabelFrame(window, text='刪除全部信件',labelanchor='n',font=('DFKai-SB', 12))
delete_letter_caption_row_frame.pack(side=tk.RIGHT)

delete_letter_label = tk.Label(delete_letter_caption_row_frame, text=' ',font=('DFKai-SB', 12))
delete_letter_label.grid(column=0, row=5, ipadx=5, pady=5, sticky=tk.E)
delete_letter_button = tk.Button(delete_letter_caption_row_frame, text='Delete', fg='red', command=DeleteAllEmail)
delete_letter_button.grid(column=1, row=5, ipadx=5, pady=5, sticky=tk.W+tk.N)

empty_letter_caption_row_frame = tk.LabelFrame(window, text='清空資源回收桶的信件',labelanchor='n',font=('DFKai-SB', 12))
empty_letter_caption_row_frame.pack(side=tk.LEFT)

empty_letter_label = tk.Label(empty_letter_caption_row_frame, text='   ',font=('DFKai-SB', 12))
empty_letter_label.grid(column=0, row=5, ipadx=5, pady=5, sticky=tk.E)
empty_letter_button3 = tk.Button(empty_letter_caption_row_frame, text='Recycling Bin', fg='red', command=CleanRecycleBin )
empty_letter_button3.grid(column=1, row=5, ipadx=5, pady=5, sticky=tk.W+tk.N)

reset_caption_row_frame = tk.LabelFrame(window, text='重置網頁及恢復按鈕',labelanchor='n',font=('DFKai-SB', 12))
reset_caption_row_frame.pack(side=tk.LEFT, padx=30)

empty_letter_label = tk.Label(reset_caption_row_frame, text='    ',font=('DFKai-SB', 12))
empty_letter_label.grid(column=0, row=5, ipadx=5, pady=5, sticky=tk.E)
empty_letter_button3 = tk.Button(reset_caption_row_frame, text='Reset', fg='red', command=Reset )
empty_letter_button3.grid(column=1, row=5, ipadx=5, pady=5, sticky=tk.W+tk.N)

window.mainloop()