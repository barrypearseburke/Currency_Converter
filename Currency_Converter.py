__author__ = 'Barry'
""" A Simple project that will ask the user how much he wants to convert. From What and to what.
Branch idea in the future is to use pygame and make the  program to use a graphical user interface
Program will query google currency converter and display value to the user in real time

Author: Barry Burke
Date started 10th of Febuary 2015
GNU V2 Public licencse applys

"""

import string

class Currency():
    def __init__(self,Amount,Currency_Have ,Currency_Want):

        self.Amount = 3 #float(Amount)
        self.Currency_Have = USD# Currency_Have
        self.Currency_Want = EUR#Currency_Want


    def request(self):
        urlstart = "www.google.com/finance/converter?a=1&from="
        urlmid = "&to="
        url = "{}{}{}{}".format(urlstart,self.Currency_Have,urlmid,self.Currency_Want)
        print(url)
    def __str__(self):
        pass
    def __repr__(self):
        pass





