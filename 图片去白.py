from PIL import Image
import os


class TXQB(object):
	def __init__(self,rpath,wpath,value):
		super(TXQB, self).__init__()
		self.rpath = rpath
		self.wpath = wpath
		self.value = value

	def DELETETXQB(self):     #  将不是白色的设为透明
		self.rpath1 = self.rpath + "/"
		self.wpath = self.wpath + "/"

		
		for filename in os.listdir(self.rpath):
			img = Image.open(self.rpath1+filename)
			img = img.convert("RGBA")
			print(self.rpath1 + filename)
			pixdata = img.load()


			for y in range(img.size[1]):
				for x in range(img.size[0]):
					if pixdata[x,y][0]>self.value and pixdata[x,y][1]>self.value and pixdata[x,y][2]>self.value:
						pixdata[x, y] = (255, 255, 255, 0)
			filename = filename + ".png"
			img.save(self.wpath + filename, "PNG")



	def UPDAYOTXQB(self):     #  将不是白色的设为透明，且黑色设为纯黑
		self.rpath1 = self.rpath + "/"
		self.wpath = self.wpath + "/"

		
		for filename in os.listdir(self.rpath):
			img = Image.open(self.rpath1+filename)
			img = img.convert("RGBA")
			print(self.rpath1 + filename)
			pixdata = img.load()


			for y in range(img.size[1]):
				for x in range(img.size[0]):
					if pixdata[x,y][0]>self.value and pixdata[x,y][1]>self.value and pixdata[x,y][2]>self.value:
						pixdata[x, y] = (255, 255, 255, 0)
					else :
						pixdata[x, y] = (0, 0, 0, 255)
			filename = filename + ".png"
			img.save(self.wpath + filename, "PNG")



rpath = "D:/下载辅助/测试"
wpath = "D:/下载辅助/测试1"


value = input('是否进入超级除黑模式，不是 直接回车，是 521后回车(英文输入法下回车！！！)')
if value == '521':
	value =20
else :
	value = 120



TXQB = TXQB(rpath,wpath,value)


zif = input('是否进入存有 原暗色，不是 直接回车，是 666 回车')

if zif == '666':
	TXQB.DELETETXQB()
else :
	TXQB.UPDAYOTXQB()




