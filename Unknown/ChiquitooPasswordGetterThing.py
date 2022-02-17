import urllib.request, urllib.error, urllib.parse

link = "http://www.chiquitooenterprise.com/password"
code = link
response = urllib.request.urlopen(code)
response = response.read()
response = response.decode('utf-8')

print(response)

response = response[::-1]

answer = "http://www.chiquitooenterprise.com/password?code=" + response
print(answer)
response2 = urllib.request.urlopen(answer)
response2 = response2.read()
print(response2.decode('utf-8'))