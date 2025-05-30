import sys
import matplotlib.pyplot as plt
from numpy import loadtxt, mean, linspace


def load_txt(name):
	file = loadtxt(name)
	hjd, mag= file[:,0], file[:,1]
	HJD, MAG = [], []
	for h, m in zip(hjd, mag):
		if m < 90:
			HJD.append(h)
			MAG.append(m)
	return HJD, MAG

def prumerny_rozdil(prvni, druha):
	max_posun = min([prvni[0][1] - prvni[0][0], druha[0][1] - druha[0][0]])
	rozdily = []
	for h1, m1 in zip(prvni[0], prvni[1]):
		for h2, m2 in zip(druha[0], druha[1]):
			if abs(h2 - h1) < max_posun:
				rozdily.append(abs(m2 - m1))
	rozdil = mean(rozdily)
	print("Průměrný rozdíl {0:.3f}".format(rozdil))

	#x = linspace(1, len(rozdily), len(rozdily))
	#plt.plot(x, rozdily)
	#plt.show()

def rozdil_prumeru(prvni, druha):
	rozdil = mean(prvni) - mean(druha)
	print("Rozdíl průměru {0:.3f}".format(rozdil))



#rozdil_prumeru(load_txt("V.lc")[1], load_txt("R.lc")[1])

if __name__ == "__main__":
	print(sys.argv[1][0] + " - " + sys.argv[2][0])
	try:
		rozdil_prumeru(load_txt(sys.argv[1])[1], load_txt(sys.argv[2])[1])
		prumerny_rozdil(load_txt(sys.argv[1]), load_txt(sys.argv[2]))
	except:
		print("{0}".format("Usage: python3 color_index.py curve1.lc curve2.lc"))
		sys.exit(0)
