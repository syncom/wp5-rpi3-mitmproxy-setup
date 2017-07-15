from netlib.http import decoded
import pprint

def response(flow):
    if flow.response.headers.get('Content-Type','').startswith("text/html"):
       with decoded(flow.response):
	  flow.response.content = flow.response.content.replace(
	       "</body>",
               "<div style=\"font-size:400%;text-align:center;color:red;\">HACKED!!!</div></body>")
