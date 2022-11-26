import os, urllib.request
from serpapi import GoogleSearch

img_res = list()

params = {
        "engine": "google",               
        "q": "wedding rings",             # search query
        "tbm": "isch",                    # image results
        "num": "100",                     # number of images per page
        "ijn": 0,                         # page number: 0 -> first page, 1 -> second...
        "api_key": os.getenv("API_KEY")       
    }

search = GoogleSearch(params)

images_present = True
while images_present:
    results = search.get_dict()     # returns JSON result
    
    if "error" not in results:
        for image in results["images_results"]:
            if image["original"] not in img_res:
                print(image["original"])
                img_res.append(image["original"])
        
        params["ijn"] += 1
    else:
        images_present = False
        print(results["error"])


    # Downloading images
    for i, img in enumerate(results["images_results"]):
        print("Downloading {} image...".format(i))
        
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.102 Safari/537.36 Edge/18.19582')]
        urllib.request.install_opener(opener)

        urllib.request.urlretrieve(img["original"], "images/{}.jpg".format(i))
