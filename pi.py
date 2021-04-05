import request

var = "abcd"
link = "https://api.kreditbee.in"
req = request.get(link)
print(req.text)
