import urllib.request, urllib.error, urllib.parse

link = "https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D"
response = urllib.request.urlopen(link)
response = response.read()
response = response.decode('utf-8')

link2 = "https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D"
response2 = urllib.request.urlopen(link2)
response2 = response2.read()
response2 = response2.decode('utf-8')

link3 = "https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D"
response3 = urllib.request.urlopen(link3)
response3 = response3.read()
response3 = response3.decode('utf-8')

link4 = "https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D"
response4 = urllib.request.urlopen(link4)
response4 = response4.read()
response4 = response4.decode('utf-8')

link5 = "https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D"
response5 = urllib.request.urlopen(link5)
response5 = response5.read()
response5 = response5.decode('utf-8')

result = response+response2+response3+response4+response5

answer = "https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string=" + result
print(answer)
response2 = urllib.request.urlopen(answer)
response2 = response2.read()
print(response2.decode('utf-8'))