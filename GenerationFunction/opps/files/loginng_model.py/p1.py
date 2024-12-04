import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("this is my first log") 
logging.info("this is my second log")
logging.error("this is my third log")
logging.critical("this is my fourth log")
logging.warning("this is my fifth log")
#logging means it will print in the file
# logging Level means it will print only the info level
#thereare 6 levels in logging NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
 

 #logging.debug("this is my first log") and logging.notset("this is my first log")
 #ye print nahi hoga as it is not in the info level
 # eske allawa baki sab level print hoga
