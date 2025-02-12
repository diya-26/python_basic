import requests
import time

urls=["http://www.example.com/nonexistentpage",  
    "http://httpstat.us/404",                  
    "http://httpstat.us/500",                  
    "https://www.google.com/" ]

while True:
    print("\nChecking urls...\n"+ "-"*50)

    for url in urls:
        try:
            response=requests.get(url,timeout=5)
            status=response.status_code
            message=f"{url} - {status}"
            if 400 <= status <=500:
                message+="error"
            elif 500 <= status <=600:
                message+="error again"
            print(message)
        except requests.exceptions.RequestException:
            print(f"{url}-Unable to reach")
    print("\nWaiting for 10 sec before checking again\n")
    time.sleep(10)