from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from datetime import datetime, timedelta

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

my_url= 'https://ssl.smn.gob.ar/mensajes/index.php?observacion=metar&operacion=consultar&89055=on'

uClient = uReq(my_url)
page_html =uClient.read()
uClient.close()
page_soup=soup(page_html, "html.parser")

containers =page_soup.findAll("tr",{"class":"result"})
#print(len(containers))
#print(soup.prettify(containers[0]))

dateTimeObj = datetime.now()
dateObj = dateTimeObj.date()

container= containers[0]
print(container.input["value"])

append_new_line('89055.txt', container.input["value"] + ' , ' + str(dateObj))