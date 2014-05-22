from Products.Five import BrowserView

class georss(BrowserView):
    def getrss(self):
       import feedparser
       p = self.request["param"]
       pp = p.replace(' ','%20')
       url = "http://193.206.192.120:8080/geoportalserver1_2_2/rest/find/document?searchText="+str(pp)
       codice=""
       feed = feedparser.parse (url)
       for item in feed["items"]:
              codice += '<h2>'+item["title"]+'</h2>'+item["description"]
       if codice=="":
              codice="<h2>Non sono stati trovati dati</h2>"
       return codice
