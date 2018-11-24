import threading
import urllib.request
import time

def download_image(image_path, file_name):
    print('Download Image From', image_path)
    urllib.request.urlretrieve(image_path, file_name)
    print("Completed Downlaod")

def execute_thread(i):
    image_name = "temp/image-" + str(i) + ".jpg"
    download_image('http://lorempixel.com/400/200/sports', image_name)

def main():
    s = time.time()
    threads = list()
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()

    e = time.time()
    total_time = e - s
    print("total execute time {}".format(total_time))

if __name__ == '__main__':
    main()