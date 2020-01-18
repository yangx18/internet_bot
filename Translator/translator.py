import requests
import time
import js2py
import random
import hashlib
import re
import js
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton



'''
Yang, 
Translate api:
Translator From:
	Youdao
'''
class youdao():
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
						'Referer': 'http://fanyi.youdao.com/',
						'Cookie': 'OUTFOX_SEARCH_USER_ID=-481680322@10.169.0.83;'
					}

		self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
	def translate(self, word):
		ts = str(int(time.time()*10000))
		salt = ts + str(int(random.random()*10))
		sign = 'fanyideskweb' + word + salt + '97_3(jkMYg@T[KZQmqjTK'
		sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
		bv = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
		bv = hashlib.md5(bv.encode('utf-8')).hexdigest()
		self.data = {
            'i': word,
            'from': 'AUTO','to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,'bv': bv,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
		res = requests.post(self.url, headers=self.headers, data=self.data)
		return [res.json()['translateResult'][0][0].get('tgt')]





class Window(QWidget):
	def __init__(self, parent=None):
		super().__init__()
		self.setWindowTitle('yangx18, Enlish<->Chinese')
		self.setWindowIcon(QIcon('YoudaoDict.jpg'))
		self.Label1 = QLabel('input')
		self.Label2 = QLabel('output')
		self.LineEdit1 = QLineEdit()
		self.LineEdit2 = QLineEdit()

		self.translateButton = QPushButton()


		self.translateButton.setText('Youdao Translate')

		self.grid = QGridLayout()
		self.grid.setSpacing(12)
		self.grid.addWidget(self.Label1, 1, 0)
		self.grid.addWidget(self.LineEdit1, 1, 1)
		self.grid.addWidget(self.Label2, 2, 0)
		self.grid.addWidget(self.LineEdit2, 2, 1)

		self.grid.addWidget(self.translateButton, 1, 2)

		self.setLayout(self.grid)
		self.resize(600, 225)

		self.translateButton.clicked.connect(lambda : self.translate(api='youdao'))

		self.yd_translate = youdao()

	def translate(self, api='youdao'):
		word = self.LineEdit1.text()
		if not word:
			return
	
		if api == 'youdao':
			results = self.yd_translate.translate(word)

		else:
			raise RuntimeError('Api should be  <youdao> ...')
		self.LineEdit2.setText(';'.join(results))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())