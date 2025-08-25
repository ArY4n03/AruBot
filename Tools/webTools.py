import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }


def get_response(url):
    response = requests.get(url,headers=headers)

    if response.status_code != 200:
        print("Something went wrong")
        return None
    return response
def search_wiki(topic:str):
    url = "https://en.wikipedia.org/wiki/" + topic.capitalize().replace(" ","_")
    print("Scrapping ",url)
    response = get_response(url)

    soup = BeautifulSoup(response.text,"html.parser")

    content_div = soup.find("div",{"id":"mw-content-text","class":"mw-body-content"})
    div = content_div.find('div',{"class":"mw-content-ltr mw-parser-output"})
    paragraphs = div.find_all('p')
    content = ""
    for paragraph in paragraphs:
        content += paragraph.get_text()
    
    return content

def download_imgFromWeb(url):
    response = get_response(url)

    soup = BeautifulSoup(response.text,"html.parser")
    images = soup.find_all('img')
    img_count = 1
    for img in images:
        if img_count > 100:
            break
        src = img.get('src')
        if "http" in src:
            print(src)
        
        # if src:
        #     try:
        #         img_data = requests.get(src,headers=headers).content

        img_count += 1

@tool
def get_TopAnime():

    """Returns Top 50 Anime of all time"""
    url = "https://myanimelist.net/topanime.php"
    response = get_response(url)
    soup = BeautifulSoup(response.text,'html.parser')
    ranking_table = soup.find('table',{"class":"top-ranking-table"})#.find('tbody')
    anime = ranking_table.find_all('tr',{"class":"ranking-list"})

    content = ""
    for a in anime:
         div1 = a.find('div',{'class':"di-ib clearfix"})
         link = div1.find('a').get('href')
         title = div1.find('a').get_text()
         content += title + " : " + link
         info = a.find('div',{'class':"information di-ib mt4"}).get_text()
         content += "\n" + info + '\n'
    
    return content

if __name__ == "__main__":
    #download_imgFromWeb(r"https://www.geeksforgeeks.org/websites-apps/static-vs-dynamic-website/")
    pass