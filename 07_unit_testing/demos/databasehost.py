#!/usr/bin/env python

import os
  
key = 'HOME'
value = os.getenv(key)
mysql = "mysql://"
concat = mysql+value
  
# Print the value of 'DATABASE_HOST'
# environment variable
print(concat)
