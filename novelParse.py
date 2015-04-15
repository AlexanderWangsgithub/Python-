import urllib2
from sgmllib import SGMLParser
 
class ListName(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_h2 = ""
		self.name = []
	def start_h2(self, attrs):
		self.is_h2 = 1
	def end_h2(self):
		self.is_h2 = ""
	def handle_data(self, text):
		if self.is_h2 == 1:
			self.name.append(text)
class ListContent(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_p = ""
		self.content = []
	def start_p(self, attrs):
		self.is_p = 1
	def end_p(self):
		self.is_p = ""
	def handle_data(self, text):
		if self.is_p == 1:
			self.content.append(text) 
#下面的是个邪恶的小说网站
url = str('http://www.xincuiweiju.com/files/article/html/0/92/')  
begin_page = int(25756)  
end_page = int(26738) 
txtName = 'test.txt'
f =open(txtName,'a+')
for i in range(begin_page, end_page+1):
	longurl = str(url + str(i)+'.html')
	try: 
		content = urllib2.urlopen(longurl).read()


		listname = ListName()
		listname.feed(content)
		for item in listname.name:
			f.write(item)
		f.write('\n')
		f.write('\n')

		listcontent = ListContent()
		listcontent.feed(content)
		for item in listcontent.content:
			f.write(item)
		f.write('\n')
		f.write('\n')
		print i

	except urllib2.URLError, e:
		print e.reason

f.close()


