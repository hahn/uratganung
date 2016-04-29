#main.py
from usabperning import fUsabPerning
import webapp2, suku, os
from google.appengine.ext.webapp import template
import cgi, urllib
import wsgiref.handlers


class HomePage(webapp2.RequestHandler):
	def get(self):
		xxx = self.request.get('h')
		template_values = {
			'hasilnya' : xxx,
		}
		# print "template_values: " + xxx
		path = os.path.join(os.path.dirname(__file__), 'template/index.html')
		self.response.out.write(template.render(path, template_values))
	
		
class UratGanung(webapp2.RequestHandler):
	def post(self):
		hasil =''
		kata = self.request.get('kata')
		kata = str(kata)
		x = len(kata)
		# self.response.write("Kata yang akan diterjemahkan:<br/> " + kata)
		perning = kata.split();
		for i in range(0,len(perning)):
			hasil += fUsabPerning(perning[i])
			hasil += ' '
		
		# print "ini hasilnya : ", hasil		
		self.redirect('/?' + urllib.urlencode({'h': hasil}))
		# self.redirect('/')

class TentangApp(webapp2.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'template/naonatuh.html')
		self.response.out.write(template.render(path,''))

application = webapp2.WSGIApplication([
		('/input', UratGanung),
		('/', HomePage),
		('/naonsih', TentangApp),
	], debug = True)



def main():
	application.RUN()


if __name__ == '__main__':
	main()