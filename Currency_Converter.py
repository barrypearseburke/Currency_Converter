__author__ = 'Barry'
""" A Simple project that will ask the user how much he wants to convert. From What and to what.
Branch idea in the future is to use pygame and make the  program to use a graphical user interface
Program will query google currency converter and display value to the user in real time

Author: Barry Burke
Date started 10th of Febuary 2015
GNU V2 Public licencse applys

"""

import string
import urllib.request

class Currency():
    def __init__(self,Amount,Currency_Have ,Currency_Want):

        self.Amount = Amount #float(Amount)
        self.Currency_Have = Currency_Have# Currency_Have
        self.Currency_Want = Currency_Want#Currency_Want
        Currency.request(self)


    def request(self):
        urlstart = "http://www.google.com/finance/converter?a="
        urlmid = "&from="
        urlend = "&to="
        url = "{}{}{}{}{}{}".format(urlstart,self.Amount,urlmid,self.Currency_Have,urlend,self.Currency_Want)
        #alternative
        #url = urlstart + self.Amount + urlmid + self.Currency_Have + urlend,self.Currency_Want
        #this downloads the the html source and put its all into a string called HTML_SOURCE
        web = urllib.request.urlopen(url)
        HTML_SOURCE = str(web.read())
        #TODO find the section of the html source where the value is given
    def __str__(self):
        pass
    def __repr__(self):
        pass
myCur = Currency(100,"USD","EUR")


