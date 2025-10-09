import time
import requests
def benchmark(func):
    def wrapper (*args, **kwargs):
        start_time = time.perf_counter()
        return_vallue = func(*args, **kwargs)
        end_time = time.perf_counter()
        processing_time = end_time - start_time
        print(f'Время выполнение запроса {processing_time: .4f} секунд')
        return return_vallue
    return wrapper

@benchmark
def fetch_webpage(url):
    web_page = requests.get(url, verify=False)
    return web_page

web_page = fetch_webpage('https://google.com')
print(web_page)