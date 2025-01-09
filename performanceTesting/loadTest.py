import requests
import time
import matplotlib.pyplot as plt
import random
import string

url_get = "http://localhost:4000/0"
url_put = "http://localhost:4000/?short={}&long={}"
short_length = 20
long_length = 50
num_requests = 1000

def generate_random_url(length):
    characters = string.ascii_letters + string.digits  # letters (lowercase + uppercase) and digits
    return ''.join(random.choice(characters) for _ in range(length))

def cache():
    response_times = []
    for i in range(num_requests):
        start_time = time.time()
        response = requests.get(url_get)
        end_time = time.time()
        response_times.append(end_time - start_time)
    
    plt.figure(figsize=(10, 6))
    plt.plot(response_times, marker='o')
    plt.title('Response Times for Cache Requests')
    plt.xlabel('Request Number')
    plt.ylabel('Response Time (seconds)')
    plt.grid()
    plt.savefig('cache.png')
    plt.close()

def get():
    response_times = []
    for i in range(num_requests):
        url = url_get + generate_random_url(short_length)
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(response_times, marker='o')
    plt.title('Response Times for GET Requests')
    plt.xlabel('Request Number')
    plt.ylabel('Response Time (seconds)')
    plt.grid()
    plt.savefig('get.png')
    plt.close()
    
def put():
    response_times = []
    for i in range(num_requests):
        url = url_put.format(generate_random_url(short_length), generate_random_url(long_length))
        start_time = time.time()
        response = requests.put(url)
        end_time = time.time()
        response_times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(response_times, marker='o')
    plt.title('Response Times for PUT Requests')
    plt.xlabel('Request Number')
    plt.ylabel('Response Time (seconds)')
    plt.grid()
    plt.savefig('put.png')
    plt.close()

if __name__ == "__main__":
    cache()
    get()
    put()
