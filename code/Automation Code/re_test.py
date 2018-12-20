# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:36:44 2018

@author: Michael Tonore
"""

import re

randomNum = re.compile(r'\d\d\d\d-\d\d\d')
it = randomNum.search('Call me at 4442-324')
print('Phone number found: ' + it.group())