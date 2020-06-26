import re
def find(s):
     charRe  = re.compile(r".*[0-9]$")
     if  charRe.match(s):
         return True
     else :
         return False   


s= input()
print (find(s) )