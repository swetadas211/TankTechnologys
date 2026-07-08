#test file contains only the test flow,Test methods,Method calls

import pytest

from pages.verticalpage import vertical  #perticular page import the class

@pytest.mark.smoke         #This is a marker

def test_vertical(page):   #test method.
    v1=vertical(page)      #Creates an object of the vertical page class.
    v1.mouse_hover()       #Performs the test by calling the method.

def test_trading(page):
    v2=vertical(page)
    v2.trading_click() 

def test_retails(page):
    v3=vertical(page)
    v3.retail_click()
    
def test_healthcare(page):
    v4=vertical(page)
    v4.healthcare_click()

def test_finetech(page):
    v4=vertical(page)
    v4.fintech_click()

def test_customApp(page):
    v5=vertical(page)
    v5.customApp_click()


  
  