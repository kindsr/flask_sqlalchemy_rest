import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 10, "name": "kindsr", "views": 9900000},
#         {"likes": 78, "name": "Joe", "views": 10000000},
#         {"likes": 10000, "name": "How to make REST API", "views": 80000},
#         {"likes": 35, "name": "Time", "views": 2000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

#response = requests.get(BASE + "helloworld/kindsr")
#response = requests.put(BASE + "video/3", {"likes": 10, "name": "kindsr", "views": 10000000})
#print(response.json())

#input()
#response = requests.delete(BASE + "video/0")
#print(response)

# input()
# response = requests.get(BASE + "video/6")
# print(response.json())

response = requests.patch(BASE + "video/2", {"views":99})
print(response.json())
