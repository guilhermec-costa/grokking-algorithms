"""
hashtables are nothing more than a group of key-value pairs stored in a array
the key-value pair is possible because of a hash function

A hash function, in its first execution, tells where it is possible to store that string correspondent in the array. In this way, it maps a string to a index permanently
In the next time, passing that string as parameter to the hash function, it will return the correspodent imediatelly, because the hash function knows exactly where the value is stored

The ideal hash function is the one that maps exactly one key to one value

Colision: a problem, when different keys are indicated to be at the same index in the array
- 1st solution: start a linked list in that index. Long linked lists worsen the perfomance of the hashtable
"""
notebook = {}

notebook["apple"] = 0.67

apple_price = notebook.get("apple")
print(apple_price)


page_cache = {}
def get_server_data(url):
    pass


def get_page(url):
    if page_cache.get(url):
        return page_cache[url]
    else:
        dados = get_server_data(url)
        page_cache[url] = dados
        return dados;

