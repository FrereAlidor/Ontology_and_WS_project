from http.server import *
from urllib.parse import unquote_plus
import Search
import Preprocessing
import Spell

HOST = '127.0.0.1'
PORT = 8080
server = (HOST, PORT)

def make_list(s):
    return '<li>%s</li>\n' % s

def make_href(s):
    return '<a href="/?search={0}">{0}</a>'.format(s)


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
                self.wfile.write(page.encode())

        elif self.path.startswith('/?search='):
            self.success()
            query = unquote_plus(self.path[9:])
            with open('base.html') as fp:
                page = fp.read().split('<!--##PEWPEW##-->')
                self.wfile.write(page[0].encode())
                self.wfile.write(b'<ul>\n\n')

                # Processing query
                results = Search.search(query)
                if not results:
                    self.wfile.write(b"<p>Qu'est ce que vous voulez  dire?</p>")

                    sw = Spell.SearchWord()
                    words = Preprocessing.Clean(query)
                    spelled = []
                    for word in words:
                        spelled.append(sw.spell(word))
                    for list in spelled:
                        for document in list:
                            self.wfile.write(make_list(make_href(document)).encode())
                else:
                    for r in results:
                        list = results[r]
                    for document in list:
                        self.wfile.write(make_list(document).encode())

                # End processing
                self.wfile.write(b'\n</ul>\n')
                self.wfile.write(page[1].encode())


try:
    s = HTTPServer((HOST, PORT), BallHandler)
    s.serve_forever()
except KeyboardInterrupt:
    print('\b\bByebye have a nice day ;)')
