import requests
from bs4 import BeautifulSoup
import tkinter as tk

target_url = "https://news.ycombinator.com/"

"""
rsp = requests.get(target_url)

soup = BeautifulSoup(rsp.text, "html.parser")

titles = soup.find_all('span', class_="titleline")

title_array = []

for title in titles:
    title_array.append(title.text)
"""


def req_titles(array1):
    rsp = requests.get(target_url)
    soup = BeautifulSoup(rsp.text, "html.parser")
    titles = soup.find_all('span', class_="titleline")

    for title in titles:
        array1.append(title.text)

    return array1


def get_titles():
    array_titles = []
    req_titles(array_titles)
    if listbox_titles.size() == 0:
        for array in array_titles:
            listbox_titles.insert(tk.END, array)
    else:
        listbox_titles.delete(0, tk.END)
        get_titles()


windows1 = tk.Tk()
windows1.title("GetHackerNews")

lbl_title = tk.Label(windows1, text="Get Trend News from HackerNews")
lbl_title.config(font=('Verdana', 10, 'bold'), bg='yellow')
lbl_title.pack(padx=10, pady=10)

btn_get = tk.Button(windows1, text="GET", command=get_titles)
btn_get.config(font=('Verdana', '10', 'normal'), bg='green', fg='white')
btn_get.pack(padx=10, pady=10)

listbox_titles = tk.Listbox(windows1)
listbox_titles.config(width=100, height=20)
listbox_titles.pack(padx=10, pady=10)

windows1.mainloop()
