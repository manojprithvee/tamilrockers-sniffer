import requests,re
import lxml.html as lh
import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print os.getcwd()
def notify(title1,message,try1=1,pri=0):
    if try1>=4:
        print "4 Retries failed"
        return
    try:
        a=requests.post('https://api.parse.com/1/push', data=json.dumps({
       "where": {
         "deviceType": "android"
       },
       "data": {
         "alert": message,
         "title":title1,
         "flag":"watchseries"
       }
     }), headers={
       "X-Parse-Application-Id": "fMB6piQyYMpDbCnkJFrlfPZVS5nihQfADGqycvTH",
       "X-Parse-REST-API-Key": "jiBr1uM5ip7oSYzwNYlL9QzI6eM62xfKxR3y5u3b",
       "Content-Type": "application/json"
     })
    except:
        notify(title1,message,try1+1)
a=requests.get("http://www.tamilrockers.com/")
doc=lh.fromstring(a.text)
span=doc.xpath('//*[@id="content"]/div[4]/div[2]/div/div[1]/div/strong[1]//span/text()')
link=doc.xpath('//*[@id="content"]/div[4]/div[2]/div/div[1]/div/strong[1]/span/a[@class="bbc_url"]/@href')
temp=list()
f=open("data.json","r")
data=json.loads(f.read())
f.close()
j=0
x=0
string=""
for i in span:
	if i[0]!="[" and i[-1]!="]" and i!=" - ":
		string=i
		data[string]=dict()
	else:
		if i!=" - ":
			data[string][i]=link[x]
			x=x+1
f=open("data.json","w")
f.write(json.dumps(data,sort_keys=True,indent=4))
f.close()
for i in data:
	if i.lower().find("thanga magan")!=-1 and i.lower().find("hd")!=-1:
		notify("tamilrockers sniffer",i+" has come")



