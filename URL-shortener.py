#!/usr/bin/python3
import tkinter as tk
import requests
import validators



class UrlShortApp:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_frame = tk.Frame(self.main_window)
        self.lbl_app_name = tk.Label(self.main_frame)
        self.lbl_app_name.configure(
            background="#0080ff",
            font="{Arial Narrow} 24 {bold}",
            foreground="#ffffff",
            text="URL Shortner",
        )
        self.lbl_app_name.pack(pady=30, side="top")
        self.entry1 = tk.Entry(self.main_frame)
        self.long_url = tk.StringVar(value="Enter a URL")
        self.entry1.configure(
            font="{Berlin Sans FB} 12 {}",
            justify="center",
            relief="groove",
            takefocus=False,
        )
        self.entry1.configure(textvariable=self.long_url, validate="none", width=70)
        _text_ = "Enter a URL"
        self.entry1.delete("0", "end")
        self.entry1.insert("0", _text_)
        self.entry1.pack(side="top")
        self.btn_shorten = tk.Button(self.main_frame)
        self.btn_shorten.configure(
            activeforeground="#e1031e",
            background="#ebebeb",
            cursor="hand2",
            font="{Britannic Bold} 12 {}",
            foreground="#0080ff",
        )
        self.btn_shorten.configure(
            relief="flat", takefocus=True, text="Generate short URL"
        )
        self.btn_shorten.pack(pady=100, side="top")
        self.btn_shorten.configure(command=self.make_short_link)
        self.output_short_url = tk.StringVar()
        self.btn_shorten.bind("<Enter>", self.on_enter, add="")
        self.btn_shorten.bind("<Leave>", self.on_leave, add="")
        self.short_url = tk.Entry(self.main_frame)
        self.short_url.configure(
            background="#0080ff",
            borderwidth=0,
            font="{Arial Baltic} 12 {}",
            justify="center",
        )
        self.short_url.configure(
            readonlybackground="#0080ff", state="readonly", validate="all", width=50, textvariable=self.output_short_url
        )
        self.short_url.pack(side="top")
        self.main_frame.configure(background="#0080ff", height=480, width=800)
        self.main_frame.pack(side="top")
        self.main_window.configure(background="#0080ff", height=200, width=200)
        self.main_window.geometry("800x480")
        self.main_window.overrideredirect("False")
        self.main_window.resizable(False, False)
        self.main_window.title("URL Shortner")

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def on_enter(self, event=None):
        self.btn_shorten["background"]="#ffffff"

    def on_leave(self, event=None):
        self.btn_shorten["background"]="#ebebeb"

    def make_short_link(self):

        valid_url=validators.url(self.long_url.get())
        if valid_url:
            headers = {
                'Authorization': 'Bearer 1001207f811dd5b5dfee51da77445642edd7131e',
                'Content-Type': 'application/json',
            }

            data = '{ "long_url": "'+self.long_url.get()+'", "domain": "bit.ly"}'

            response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
            try:
                link = response.json()['link']
                self.output_short_url.set(link)
            except KeyError:
                self.output_short_url.set("Error in generating URL")
        else:
            self.output_short_url.set("Invalid long URL")
            
if __name__ == "__main__":
    app = UrlShortApp()
    app.run()
