import inspect
 
def line_numb():
   return -1 * int(inspect.currentframe().f_back.f_lineno)
