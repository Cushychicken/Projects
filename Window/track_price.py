#!/usr/bin/env python

import json
import urllib2
from time import sleep, localtime, strftime

class Tracker:
    def __init__(self, stock):
        self.stock = stock
        self.prices = []
        self.times  = []
        self.loop()

    def loop(self):
        while True:
            self.update()
            self.redraw()
            sleep(1)

    def update(self):
        first = 'http://finance.yahoo.com/webservice/v1/symbols/'
        last = '/quote?format=json'
        data = urllib2.urlopen(first+self.stock+last).read()
        data = json.loads(data)
        if len(self.prices) == 10:
            self.prices.pop(0)
            self.times.pop(0)
        self.prices.append(data[u'list'][u'resources'][0][u'resource'][u'fields'][u'price'])
        self.times.append(localtime())
        print self.stock,' ', self.prices[-1], ' ', strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
                       
    def redraw(self):
        if len(self.prices) == 10 and len(self.times) == 10:
            plot(self.times, self.prices)
        else:
            pass

if __name__ == '__main__':
    t = Tracker('AAPL')
