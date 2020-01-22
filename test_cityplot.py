# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:06:30 2020

@author: Devendra Singh
"""


from cityfunc import *

class TestCity:
    
    def test_file(self):
        assert 0 == check_file("citydata.txt")
        
    def test_columns(self):
        assert 0 == check_columns("citydata.txt")
        
