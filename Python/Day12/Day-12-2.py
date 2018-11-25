
dtree = dm.parse('note.xml')

root_n = dtree.documentElement

def parse(node):
    if node.nodeType == 3:
        print node.parentNode.nodeName," : ",node.nodeValue
    else:
        for ch in node.childNodes:
            parse(ch)


parse(root_n)



#------------------------------------------------------------------------------


import xml.dom.minidom as dm

def parse(file1):

    dtree = dm.parse(file1)
    rn = dtree.documentElement

    for bn in rn.childNodes:
        print(bn.nodeName, bn.nodeValue)
        for tn in bn.childNodes:
            print(tn.nodeName,bn.nodeValue)
            for tx in tn.childNodes:
                print(tx.nodeValue,bn.nodeValue)


parse('note.xml')
