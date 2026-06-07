import requests
from pathlib import Path

P=Path()

post_dict={}
for p in list(P.glob("*.jpg"))+list(P.glob("*.webp")):
    print(p.stem)
    post_dict[p.stem]=open(p,"rb")
# print(post_dict)

resp= requests.post("http://127.0.0.1:5000/upload",files=post_dict)
for p in post_dict.values():
    p.close()

print(list(post_dict.keys()))
print(resp.text)