class Bookshelf:
    def __init__(self,bname,bauthor,bprice,byear):
        self.bname=bname
        self.bauthor=bauthor
        self.bprice=bprice
        self.byear=byear
        
    def display(self):
        print("Book Name:"+self.bname)
        print("Book Author:"+self.bauthor)
        print("Book Price:"+str(self.bprice))
        print("This book was published in :"+str(self.byear))
        print("Book Added")
        
        
    def publish(self):
        years=2022-self.byear
        print("This book was published "+str(years)+" years ago.")
        
        
book1 = Bookshelf("To Kill a Mockingbird","Harper Lee",10,1960)
book1.display()
book1.publish()