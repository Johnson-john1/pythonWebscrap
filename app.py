from flask import Flask
import requests
from bs4 import BeautifulSoup
import json

//app = Flask(__name__)




final_data = []


def saveAsJson(data, path='./firstPage.json'):
    with open(path, mode='w',  encoding="utf-8") as f:
        f.write(json.dumps(data))

def save(data, path='./anroo_firstRt.txt'):
    with open(path, mode='w',  encoding="utf-8") as f:
        f.write(str(data))


final_data = []
for x in range(1, 2):
    print(x, 2)
    req_url = f"https://androeed.store/index.php?m=android&f=games&mod=1&page={x}"
    req_result = requests.get(req_url)
    html = req_result.text
    soup = BeautifulSoup(html, 'html.parser')

    app_list = soup.find(class_ = 'apps_list')
    all_a_tags = app_list.find_all('a')

    # print(all_a_tags['href'] )
    for list in all_a_tags:
        temp_dict = {}
        link = list['href']
        # print(list)
        img_link = list.find('img')['src']
        title = list.find(class_ = 'title').string
        temp_dict['title'] = title
        temp_dict['imgLink'] = img_link
        temp_dict['pageLink'] = f"https://androeed.store{link}"
        final_data.append(temp_dict)

# print(list_arr)
# save(app_list)
print('final')
saveAsJson(final_data)
 

 
