import xml.sax

class XMLclass(xml.sax.ContentHandler):
    def __init__(self):
        self.title=""
        self.author=""
        self.year=""
        self.price=""
        self.curtag=""
        self.string="The book"
    def startElement(self, tagname,attrs):
        self.curtag= tagname
        if tagname=="book":
            print "----------------------------------------"
            
            p=attrs["category"]
            global p    

    def characters(self,content):
        if self.curtag=="title":
            self.title=content
        
        if self.curtag=="author":
            self.author=content
            
        if self.curtag=="year":
            self.year=content
            
        if self.curtag=="price":
            self.price=content

        
    def endElement(self, tag):
        if tag=="title":
            print "The book ",self.title,"belongs to category",p
        if tag=="author":
            print"and is written by ",self.author
        if tag=="year":
            print"This book is published in the year",self.year
        if tag=="price":
            print "with a price of",self.price
        
pobj=xml.sax.make_parser()
obj=XMLclass()
pobj.setContentHandler(obj)
pobj.parse("/home/ai1/My_Files/Python/Day11/book.xml")

            
