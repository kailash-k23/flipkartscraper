from ssl import OP_NO_COMPRESSION
from typing import Text
from urllib.request import urlopen 
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from flask.globals import request
from googlesearch import search
import csv
from mailing import mailto
import io, os

base = "www.flipkart.com"


def get_target_url(results):
    
    for result in results:
        domain = urlparse(result).netloc       
        if base in domain:                      
            target_url = result
    return target_url



def get_details(user_input):
    result = []         
    search_term = base + user_input


    search_results = search(search_term, num=1, stop=1)

    targetUrl = get_target_url(search_results)

    
    page = urlopen(targetUrl)

    pageContent = page.read()

    pageSoup = BeautifulSoup(pageContent, "html.parser")

    products = pageSoup.findAll('div', {'style':'width:25%'})
    if products != []:
        for product in products:                #every product
            title = product.find('a', {'class':'s1Q9rs'})
            name = title.get("title")
            link = title.get("href")
            cost = product.find('div', {'class': '_30jeq3'})
            amount = cost.text.strip()
            if (name, cost) not in result:
                each_item = (name, amount)
                result.append(each_item)
    else:
        product_two = pageSoup.findAll('div', {'style': 'width:100%'})
        for product in product_two:
            nametag = product.find('div', {'class': '_4rR01T'})
            
            name = nametag.text
            costtag = product.find('div', {'class': '_30jeq3 _1_WHN1'})
            cost = str(costtag.text)
            if (name,cost) not in result:
                each_item = (name,cost)
                result.append(each_item)

    return result


def return_result(input, mail):
    result_list = get_details(input)
    result_dict  = dict(result_list)
    data = str(result_dict)
    if os.path.isfile('send.txt'):
        pass
    else:
        file = open('send.txt', 'x')
    with io.open('send.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(data)
    mailto(mail, 'send.txt')





    




