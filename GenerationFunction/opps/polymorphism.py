class data_science:
    def syllabus(self):
        print("this is syllabus for data science") 
class web_dev:
    def syllabus(self):
        print("this is syllabus for web dev")
def class_precer(class_obj):
    for i in class_obj:
        i.syllabus()
data_science=data_science()
web_dev=web_dev()
class_obj=[data_science,web_dev]
class_precer(class_obj)

