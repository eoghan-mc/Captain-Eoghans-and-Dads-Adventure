# Captain-Eoghans-and-Dads-Adventure
Captain Eoghans and Dads Adventure

If on Windows, install python and open cmd.  You may need to install ipython

py -m pip install ipython

You may hten encounter -->

Traceback (most recent call last):
  File "C:\Users\mcmah\OneDrive\Desktop\Captain Eoghans and Dads Adventure.py", line 12, in <module>
    get_ipython().magic('clear')
    ^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'magic'

So apparently above is because matplotlib needs an environment.

py -m pip install jupyterlab

