"""
Always the second function gets executed ignoring the first function
"""

class Browser:

    def make_https_request(self,url):
        print("HI, Let's make the http request")

    def make_https_request(self,url,auth):
        print("HI, Let's make the http request with auth", auth, url)

t = Browser()
t.make_https_request("google.com", "admin")