import requests, json, re, os
from parsel import Selector

params = {
    "q": "shoes",
    "hl": "en",
    "gl": "us",
    "tbm": "shop"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" 
}

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
selector = Selector(html.text)

def get_original_images():
    all_script_tags = "".join(
        [
            script.replace("</script>", "</script>\n")
            for script in selector.css("script").getall()
        ]
    )

    image_urls = []

    for result in selector.css(".Qlx7of .sh-dgr__grid-result"):
        # https://regex101.com/r/udjFUq/1
        url_with_unicode = re.findall(rf"var\s?_u='(.*?)';var\s?_i='{result.attrib['data-pck']}';", all_script_tags)

        if url_with_unicode:
            url_decode = bytes(url_with_unicode[0], 'ascii').decode('unicode-escape')
            image_urls.append(url_decode)

    # download_original_images(image_urls)  

    return image_urls

def get_suggested_search_data():
    google_shopping_data = []
