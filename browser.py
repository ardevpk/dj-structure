import webbrowser
import os
envPath = os.path.join(os.getcwd(), 'env/Scripts/activate')

webUrl = 'http://127.0.0.1:8000'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'

webbrowser.get(chrome_path).open_new(webUrl)
os.system(f'{envPath} & python manage.py runserver --skip-checks')
