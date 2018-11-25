import xml.dom.minidom as dm

book = dm.parse('book.xml')

root = book.documentElement

bNode = root.getElementsByTagName('book')



for bn in bNode:
    if bn.hasAttribute('category'):
       
        f= bn.getAttribute('category')
    
    
    tNode= bn.getElementsByTagName('title')
    for tn in tNode:
        print "This book", tn.childNodes[0].nodeValue


    aNode= bn.getElementsByTagName("author")
    for an in aNode:
        print 'belongs to',f, 'category and is written by', an.childNodes[0].nodeValue

    yNode= bn.getElementsByTagName("year")
    for yn in yNode:
        print 'This Book is published in the year', yn.childNodes[0].nodeValue


    pNode= bn.getElementsByTagName("price")
    for pn in pNode:
        print 'with a price of ', pn.childNodes[0].nodeValue

    print '---------------------------------------------------------'



