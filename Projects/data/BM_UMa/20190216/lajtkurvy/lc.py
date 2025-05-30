from numpy import loadtxt


def func(name):
	file = loadtxt(name)
	hjd, mag, err = file[:,0], file[:,1], file[:,2]
	with open(name.lower(), "w") as file:
		for h, m, e in zip(hjd, mag, err):
			if m < 20:
				file.write("{0:.6f} {1:.5f} {2:.5f}\n".format(h, m, e))

for i in ["B.lc", "V.lc", "R.lc"]:
	func(i)
