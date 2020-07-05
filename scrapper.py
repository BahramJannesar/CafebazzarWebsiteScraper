import requests
from bs4 import BeautifulSoup
import json
import time

base_url = 'https://cafebazaar.ir'
file_path_name = 'cafebazzar_category_link.txt'


# def category_link_scrapper(base_url):

#     response = requests.get(base_url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     links = soup.find_all('a')
#     for link in links:
#         if link.get('href') is None:
#             pass
#         elif 'cat' in link.get('href'):
#             with open(file_path_name, 'a') as file:
#                 file.write(base_url + link.get('href') + '\n')


# def app_link_scrapper(file_path_name):
#     with open(file_path_name, 'r') as file:
#         category_link = file.readlines()

#     app_link_list = []

#     for link in category_link:
#         link = link.strip()
#         time.sleep(10)
#         response = requests.get(link)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         all_app_links = soup.find_all('a')
#         for app_link in all_app_links:
#             if app_link.get('href') is None:
#                 pass
#             elif 'app' in app_link.get('href')[0:4]:
#                 if app_link.get('href') in app_link_list:
#                     pass
#                 else:
#                     app_link_list.append(base_url + app_link.get('href'))

#         app_link_dict = {
#             'app_category': link[26:-1] + link[-1],
#             'links': app_link_list
#         }

#         app_link_js = json.dumps(app_link_dict, indent=4)
#         with open('app_link.json', 'a') as file:
#             file.write(app_link_js + ',')
#             print('Category ' + link[26:-1] + link[-1] + ' Done!')


# if __name__ == "__main__":

#     category_link_scrapper(base_url)

#     app_link_scrapper(file_path_name)



# with open('app_link.json', 'r') as file :
#     app_links = json.loads(file.read())
#     for each in app_links:
#         print(each['links'])

response = requests.get('https://cafebazaar.ir/app/org.mozilla.focus')

soup = BeautifulSoup(response.content , 'html.parser')
application_name = soup.find('h1')
developer_name = soup.find('div' , attrs={'class':'cover-header__title-subtitle'})
developer_link_page = developer_name.find('a')
application_version = soup.find('div' , attrs={'class':'app-details__version app-details__version--linked'})
application_price = soup.find('div' , attrs={'class':'cover-header__btn-area'})
active_installed_number = soup.find('div' , attrs={'class':'info-cube__content info-cubes__installs'})
rating_cube = soup.find('div' , attrs={'itemprop':'aggregateRating'})
application_rating = rating_cube.find('div'  , attrs={'itemprop':'ratingValue'})



print(application_name.text)
print(developer_name.text)
print( 'https://cafebazaar.ir' + developer_link_page.get('href'))
print(application_version.text.strip())
print(application_price.text.strip())
print(active_installed_number.text)
print(application_rating.text)

