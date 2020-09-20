from pytube import *        
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0

def progress(stream = None, chunk = None, remaining = None):
    file_downloaded = (file_size - remaining)
    per = (file_downloaded/file_size) * 100
    dbtn.config(text="{:10.0f} % downloaded".format(per))

def startDownload():
    global file_size
    try:
        url = urlfield.get()

        dbtn.config(text="Please wait...")
        dbtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if(path_to_save_video) is None:
            return
        ob = YouTube(url, on_progress_callback=progress)
        strm = ob.streams.first()   
        file_size = strm.filesize
        vtitle.config(text = strm.title)
        vtitle.pack(side=TOP)
        strm.download(path_to_save_video)
        dbtn.config(text="Done!")
        dbtn.config(text="start download")
        dbtn.config(state=NORMAL)
        showinfo("Download finished","Downloaded Successfully!")
        urlfield.delete(0, END)
        vtitle.pack_forget()
    except Exception as e:
        print(e)
        print("Error")


def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()

main = Tk()

main.title("Youtube Downloader")
main.iconbitmap('youtube-squared.ico')

main.geometry("500x600")

file = PhotoImage(file='youtube.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP, pady=40)
urlfield = Entry(main, font=("verdana", 18), justify=CENTER)
urlfield.pack(side=TOP, fill = X, padx = 20)
dbtn = Button(main, text="start download", font=("verdana", 12), relief="ridge", command=startDownloadThread)
dbtn.pack(side=TOP,pady=10)
vtitle= Label(main, text="")
main.mainloop()