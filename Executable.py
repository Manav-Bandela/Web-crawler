from tkinter import *
import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
from login import *
from PIL import Image, ImageTk

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Web Crawler")
        master.geometry("850x477")
        master.resizable(0, 0)
        master.load = Image.open("C:\\Users\\Manav\\Downloads\\MP\\MP-1\\web.jpg")
        master.render = ImageTk.PhotoImage(master.load)
        self.p_name = StringVar()
        self.u_link = StringVar()

        self.l = Label(master,image=master.render)
        self.l.place(x=0, y=0)
        self.label = Label(master, text="Welcome to our Web Crawler!!", bg="#c8c1b7", width="300", height="2",
                           font=("Times new Roman", 13))
        self.label.pack()
        self.label = Label(master, text="", bg="#c8c1b7").pack()

        self.label1 = Label(master, text="Enter Project Name * ", bg="#c8c1b7").pack()
        self.label1 = Entry(master, bd=1, textvariable=self.p_name)
        self.label1.pack()
        self.label1 = Label(master, text="", bg="#c8c1b7").pack()

        self.label2 = Label(master, text="Enter base url only * ", bg="#c8c1b7").pack()
        self.label2 = Entry(master, bd=1, textvariable=self.u_link)
        self.label2.pack()
        self.label2 = Label(master, text="", bg="#c8c1b7").pack()

        self.button = Button(master, text="RUN", width=10, height=1, command=self.project, bg="#c8c1b7").pack()

    def project(self):
        self.label1 = self.p_name.get()
        print(self.label1)

        self.label2 = self.u_link.get()
        print(self.label2)

        root.destroy()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
PROJECT_NAME = my_gui.label1
HOMEPAGE = my_gui.label2
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
