import sys
import requests
import threading
import time

success_build_api = "https://api-travis-build.herokuapp.com/api/v1/mcu/actions/success"
failed_build_api = "https://api-travis-build.herokuapp.com/api/v1/mcu/actions/running"
running_build_api = "https://api-travis-build.herokuapp.com/api/v1/mcu/actions/failed"

def post_url(url):     
    r = requests.post(url)   
    print(r) 
    if r.status_code != 200:
        requests.post(url)


def main(argv):
    status = argv   
    if status == "success":
        post_url(success_build_api)
    elif status == "failure":
        post_url(failed_build_api)
    elif status == "building":
        post_url(running_build_api)
        time.sleep(5.4)
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python error [success/failure/building]')
        exit(1)    
    main(sys.argv[1])