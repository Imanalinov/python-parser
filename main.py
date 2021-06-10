import requests
from json2html import *
import time

#Your url
url = ""

while(True):
    responce = requests.get(url)
    responceJson = responce.json()

    html = f'''
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    {json2html.convert(json = responceJson)}
    <script src="./script.js"></script>
    </html>
    '''

    with open("index.html", "w", encoding="utf-8") as file: 
        file.write(html)

    time.sleep(5)