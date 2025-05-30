import sys
import matplotlib.pyplot as plt
from numpy import loadtxt, mean, std, linspace


def load_txt(name):
	file = loadtxt(name)
	hjd, mag, err = file[:,0], file[:,1], file[:,2]
	HJD, MAG, ERR = [], [], []
	for h, m, e in zip(hjd, mag, err):
		if m < 90:
			HJD.append(h)
			MAG.append(m)
			ERR.append(e)
	return HJD, MAG, ERR

def prumerny_rozdil(prvni, druha):
	max_posun = prvni[0][1] - prvni[0][0]
	rozdily = []
	for h1, m1 in zip(prvni[0], prvni[1]):
		for h2, m2 in zip(druha[0], druha[1]):
			if abs(h2 - h1) < max_posun:
				rozdily.append(abs(m2 - m1))
	rozdil, err = mean(rozdily), std(rozdily)
	print("Průměrný rozdíl {0:.3f} +/- {1:.3f}".format(rozdil, err))

	#x = linspace(1, len(rozdily), len(rozdily))
	#plt.plot(x, rozdily)
	#plt.show()

def rozdil_prumeru(prvni, druha):
	rozdil = mean(prvni[1]) - mean(druha[1])
	err = (mean(prvni[2])**2 + mean(druha[2])**2)**(1/2)
	print("Rozdíl průměrů {0:.3f} +/- {1:.3f}".format(rozdil, err))


if __name__ == "__main__":
	print(sys.argv[1][0] + " - " + sys.argv[2][0])
	try:
		rozdil_prumeru(load_txt(sys.argv[1]), load_txt(sys.argv[2]))
		prumerny_rozdil(load_txt(sys.argv[1]), load_txt(sys.argv[2]))
	except:
		print("{0}".format("Usage: python3 color_index.py curve1.lc curve2.lc"))
		sys.exit(0)
