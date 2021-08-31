from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.india.gov.in/topics/industries/micro-small-medium-enterprises'
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("li", {"class":"views-row"})

file_name = "msme.csv"
f = open(file_name, "w")

headers = "artical_name , info \n"
f.write(headers)



for container in containers:
    print("_____________________________________________________________________________________________________________")
    artical = ""
    for a in container.find_all('a',{"class":"ext-link"}, text=True): 
        artical = a.text
    print(artical)

    alpha = ""
    for para in container.find_all("p"):
        alpha = para.get_text()
    print(alpha)
    print("_____________________________________________________________________________________________________________")




    f.write(artical.replace(",","|") + "," + artical + "," + alpha.replace(",",".") + "\n")

f.close()