import logging
#logging.basicConfig(filename="test.log",level=logging.INFO)
logging.basicConfig(filename="test.log",level=logging.DEBUG,format='%(asctime)s %(message)s' )
logging.info("this is my first log") 
logging.info("this is my second log")
logging.error("this is my third log")
logging.critical("this is my fourth log")
#logging.warning("this is my fifth log")
#logging.debug("This is my msg")