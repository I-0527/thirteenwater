import http.client
from receive import token 
conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")


import cal
userid,card=cal.main()

payload = "{\"id\"400,\"card\":[\"*2 $10 $J\",\"&4 $4 *7 &7 #6\",\"&A $A $5 #5 #3\"]}"#%(userid,card[12],card[11],card[10],
                                                                                             #card[9],card[8],card[7],card[6],card[5],
                                                                                    #card[4],card[3],card[2],card[1],card[0])

headers = {
    'content-type': "application/json",
    'x-auth-token': token
    }

conn.request("POST", "/game/submit", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
