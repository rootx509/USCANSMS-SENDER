
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import time
import os
KEY='textbelt'

def main():
    while True:
        with open('message.txt','r') as f:
            message=f.read()
        try:
            response=requests.get('https://www.receivesms.co/us-phone-numbers/us/',headers=Headers().generate())
            numbers=[]
            try:
                soup=BeautifulSoup(response.text,'html.parser')
                a_tags = soup.find_all('a',attrs={'data-clipboard-text':True})
                if a_tags:
                    for a_tag in a_tags:
                        numbers.append(a_tag['data-clipboard-text'])
            except:
                pass
            response=requests.get('https://anonymsms.com/',headers=Headers().generate())    
            try:
                soup=BeautifulSoup(response.text,'html.parser')
                tags=soup.find_all('tr')
                if tags:
                    for tag in tags:
                        td=tag.find_all('td')   
                        if td:
                            print(td)
                            number=td[0].text
                            country=td[2].text
                            if country=='United States' or country=='Canada':
                                numbers.append(number)
            except:
                pass
            print(f'Found {len(numbers)} numbers')
            if numbers:
                for number in numbers:
                    print(f'Sending message to {number}')
                    resp = requests.post('https://textbelt.com/text', {
                'phone': f'{number}',
                'message': f'{message}',
                'key': f'{KEY}',
            })
                    print(resp.json())
        except:
            pass
        print('Sleeping for 1 hour')
        time.sleep(3600)

if __name__ == '__main__':

    main()  

