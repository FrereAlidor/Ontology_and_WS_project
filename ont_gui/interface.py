from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote

HOST = ''
PORT = 8080
server = (HOST, PORT)

def make_list(s):
	return '<li>%s</li>\n' % s


class BallHandler(BaseHTTPRequestHandler):
	def success(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

	def do_GET(self):
		if self.path == '/':
			self.success()
			with open('base.html') as fp:
				page = fp.read()
				self.wfile.write(page)

		elif self.path.startswith('/?search='):
			self.success()
			query = unquote(self.path[9:]).decode('utf8')
			with open('base.html') as fp:
				page = fp.read().split('<!--##PEWPEW##-->')
				self.wfile.write(page[0])
				self.wfile.write('<ul>\n\n')
				
				# Processing query
				result = query
				for r in result:
					self.wfile.write(make_list(r))

				# End processing
				self.wfile.write('\n</ul>\n')
				self.wfile.write(page[1])


try:
	s = HTTPServer((HOST, PORT), BallHandler)
	s.serve_forever()
except KeyboardInterrupt:
	print ('\b\bBye Bye  signed by Groupe1&6;)')
