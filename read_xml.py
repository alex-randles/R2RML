import xml.etree.cElementTree as et

parsedXML = et.parse("peoples.xml")
for part in parsedXML:
    print(parsedXML)