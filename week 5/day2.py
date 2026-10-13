# import requests

# r = requests.get('https://jsonplaceholder.typicode.com/posts/12')

# # print(r.status_code)
# # print(r.json())
# # print(r.headers)
# # print(r.text)

# # r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# # r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# # r = requests.delete('https://httpbin.org/delete')


# import requests

# response = requests.patch(
#     'https://jsonplaceholder.typicode.com/posts/6',
#     json={'title': 'Just changed the title'},
#     headers={'Content-type': 'application/json; charset=UTF-8'}
# )

# response.raise_for_status()
# result = response.json()
# print(result)


# import requests

# response = requests.post(
#     'https://jsonplaceholder.typicode.com/posts',
#     json={
#         'title': 'foo',
#         'body': 'bar',
#         'userId': 1,
#     },
#     headers={'Content-type': 'application/json; charset=UTF-8'}
# )

# response.raise_for_status()
# result = response.json()
# print(result)


import requests

# response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# response.raise_for_status()
# result = response.json()
# print(result)

# No timeout → hangs forever
url =  "https://jsonplaceholder.typicode.com/posts"

request = requests.get(url, timeout=10)
request.raise_for_status()
print(request.json())