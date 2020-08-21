class College:
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept
    def display(self):
        print("NAME: %s \n DEPT: %s" % (self.name,self.dept))
c=College("santhosh kumar","CSE")
c.display()
