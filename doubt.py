Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="saishankar mantramurthy"
>>> l=list(s)
>>> l.reverse()
>>> print(l)
['y', 'h', 't', 'r', 'u', 'm', 'a', 'r', 't', 'n', 'a', 'm', ' ', 'r', 'a', 'k', 'n', 'a', 'h', 's', 'i', 'a', 's']
>>> ss=str(l)
>>> print(ss)
['y', 'h', 't', 'r', 'u', 'm', 'a', 'r', 't', 'n', 'a', 'm', ' ', 'r', 'a', 'k', 'n', 'a', 'h', 's', 'i', 'a', 's']
>>> ss.split()
["['y',", "'h',", "'t',", "'r',", "'u',", "'m',", "'a',", "'r',", "'t',", "'n',", "'a',", "'m',", "'", "',", "'r',", "'a',", "'k',", "'n',", "'a',", "'h',", "'s',", "'i',", "'a',", "'s']"]
>>> ss.group()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ss.group()
AttributeError: 'str' object has no attribute 'group'
>>> 
