import sys, requests # pip install requests
import webbrowser
global nick # varivel nick como global
x = sys.argv # x recebe sys.argv

def ajuda():
	print("""
++++++++++++++++++++++++++++++++++++++++++++++++++
+ -all => PROCURA TUDO (exceto o -tu)
+ -f  => Facebook 									
+ -tw => Twitter
+ -i  => Instagram
+ -tu => Tumblr 
+ -fi => Filmow
++++++++++++++++++++++++++++++++++++++++++++++++++
--python SNSearch.py mary553 -tu
--python SNSearch.py algo -all


""")

def abra(url):
	webbrowser.open(url)

def facebook():
	url = 'https://m.facebook.com/'+nick
	r = requests.get(url) # faz a requisiçao
	checa = r.status_code # varivel para checar o status
	if checa == 200: # caso o status seja 200 ele retorna FOUND
		print('[+] FACEBOOK FOUND => {}\n'.format(url))
		abra(url)
	else:
		print('[-]FACEBOOK NOT FOUND => {}\n'.format(url))


def twitter():
	url = 'https://m.twitter.com/'+nick
	r = requests.get(url) # faz a requisiçao
	checa = r.status_code # varivel para checar o status
	if checa == 200: # caso o status seja 200 ele retorna FOUND
		print('[+] TWITTER FOUND => {}\n'.format(url))
		abra(url)
	else:
		print('[-]TWITTER NOT FOUND => {}\n'.format(url))


def instagram():
	url = 'https://www.instagram.com/'+nick
	r = requests.get(url)
	checa = r.status_code
	if checa == 200:
		print('[+] INSTAGRAM FOUND => {}\n'.format(url))
		abra(url)
	else:
		print('[-]INSTAGRAM NOT FOUND => {}\n'.format(url))

def tumblr():
	url = 'https://'+nick+'.tumblr.com'
	r = requests.get(url)
	checa = r.status_code
	if checa == 200:
		print('[+] TUMBLR FOUND => {}\n'.format(url))
		abra(url)
	else:
		print('[-]TUMBRL NOT FOUND => {}\n'.format(url))

def filmow():
	url = 'https://filmow.com/usuario/'+nick
	r = requests.get(url)
	checa = r.status_code
	if checa == 200:
		print('[+] FILMOW FOUND => {}\n'.format(url))
		abra(url)
	else:
		print('[-]FILMOW NOT FOUND => {}\n'.format(url))



########## MAIN
if len(x) == 3: # Se o tamanho da sys for 3 execute isso, ou seja : python Social-Media-Search.py exemplo -all
	nick = x[1]         													#1						#2		#3
	if x[2] == '-f': # Se o argumento 2 for -f chame a funçao facebook
		facebook()
	elif x[2] == '-fi': # Se Não se o argumento 2 for -fi chame a funçao filmow
		filmow()
	elif x[2] == '-tw': # Se Não se o argumento 2 for -tw chame a funçao twitter
		twitter()
	elif x[2] == '-tu': # Se Não se o argumento 2 for -tu chame a funçao tumblr
		tumblr()
	elif x[2] == '-all': # Se Não se o argumento 2 for -all chame todas as funçoes
		facebook()
		twitter()
		instagram()
		filmow()
	elif x[2] == '-i': # Se Não se o argumento 2 for -i chame a funçao instagram
		instagram()

else:
	ajuda()



