#!/usr/bin/env python

from Tkinter import *
import json
import urllib2

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.stocks = [] 

        self.button = Button(
            frame, text='QUIT', fg='red', command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text='HELLO', command=self.get_field)
        self.hi_there.pack(side=LEFT)

	self.watch = Button(frame, text='WATCH', command=self.watch_stock)
        self.watch.pack(side=LEFT)

	self.field = Entry(frame)
        self.field.pack(side=BOTTOM)

    def get_field(self):
        stocks = self.field.get()
        stocks = stocks.split(',')
        for s in stocks:
            data = urllib2.urlopen('http://finance.yahoo.com/webservice/v1/symbols/'+s+'/quote?format=json').read()
            data = json.loads(data)
	    #print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            for i in data[u'list'][u'resources']:
		print i[u'resource'][u'fields'][u'name'], ':', i[u'resource'][u'fields'][u'price']

    def watch_stock(self):
        stocks = self.field.get()
        stocks = stocks.split(',')
        for s in stocks:
            self.stocks.append(s)
	print self.stocks

    def watch_update(self):
        for s in self.stocks:
            data = urllib2.urlopen('http://finance.yahoo.com/webservice/v1/symb$
            data = json.loads(data)
            #print json.dumps(data, sort_keys=True, indent=4, separators=(',', $
            for i in data[u'list'][u'resources']:
                print i[u'resource'][u'fields'][u'name'], ':', i[u'resource'][u'fields'][u'price']

root = Tk()

app = App(root)

root.mainloop()
