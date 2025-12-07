book = {}
book['tom'] = {
    'rocket' : 'bugatti',
    'food':'coffee',
    'phone': 56755757578
    
}


book['bob'] = {
    'run': 'too bad',
    'fruit':'dragon',
    'pin':4545317592
}

print(book)

import json

s=json.dumps(book)

with open(r"P:\AI Engineer\book.txt", "w") as f:
    f.write(s)
