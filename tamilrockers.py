import requests,re
import lxml.html as lh
import json
import os,boto3
os.environ["aws_access_key_id"] = 'AKIAIATTEJBNHASYUK7Q'
os.environ["aws_secret_access_key"] = 'yHabSLmW+BYJFJPOZviP3oLpotejDMIvCC35X7zah'
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
data=json.loads(requests.get("http://tamilrockersdump.s3-website-ap-southeast-1.amazonaws.com/").text)
j=1
x=0
string=""
for i in span:
  print "("+str(j)+"/"+str(len(span))+")"
  if i[0]!="[" and i[-1]!="]" and i!=" - ":
    string=i
    data[string]=dict()
  else:
    if i!=" - ":
      a = requests.get(link[x])
      doc=lh.fromstring(a.text)
      urls=doc.xpath('//a/@href')
      for b in urls:
        if b.find("magnet:?") != -1:
          urls = b
          break
      data[string][i]=urls
      x=x+1
  j=j+1
f=open("data.json","w")
f.write(json.dumps(data,sort_keys=True,indent=4))
f.close()
session = boto3.session.Session(aws_access_key_id='AKIAIE77JWLUJPBLUBMA',
                  aws_secret_access_key='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',
                  region_name='ap-southeast-1')
s3_client = session.client('s3')
s3_client.upload_file('data.json', 'tamilrockersdump', 'data.json')
for i in data:
	if i.lower().find("thanga magan")!=-1 and i.lower().find("hd")!=-1:
		notify("tamilrockers sniffer",i+" has come")



