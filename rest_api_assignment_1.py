#Stateless

Statelessness means that every HTTP request happens in complete isolation. When the client makes an HTTP request, it includes all information necessary for the server to fulfill the request.
The server never relies on information from previous requests from the client.

#Status Codes

#403 :
The HTTP 403 Forbidden response status code indicates that the server understands the request but refuses to authorize it.

#503 :
An HTTP 503 status code (Service Unavailable) typically indicates a performance issue on the origin server. In rare cases, it indicates that CloudFront temporarily can't satisfy a request because of resource constraints at an edge location.

#301 :
The HTTP 301 status response code indicates that the requested resource has been definitively moved to the URL given by the Location headers.



#HTTP Methods
import requests
import json

# Post
ulr = "https://jsonplaceholder.typicode.com/todos"
todo = {"name": "via", "age": 28, "profession": "wanderer"}
print(type(todo))
response = requests.post(ulr, json=todo)
print(response)
print(response.json())


#Get
url2 = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(url2)
print(response.json())


#Put
todo = {"name": "via", "age": 28, "profession": "wanderer"}
response = requests.put(url2, json=todo)
print(response)
print(response.json())


#Patch
todo = {"title" : "Tsumugi"}
response = requests.patch(url2, json=todo)
print(response)
print(response.json())


#Delete 
response = requests.delete(url2)
print(response)
print(response.json())
