from numpy import loadtxt, polyfit, linspace
import matplotlib.pyplot as plt


def func(name):
	file = loadtxt(name)
	hjd, mag, err = file[:,0], file[:,1], file[:,2]
	n = 0
	for h, m in zip(hjd, mag):
		n += 1
		if m == max(mag):
			center = n
	k = 20
	a0, a1, a2 = polyfit(hjd[center - k:center + k], mag[center - k:center + k], 2)
	x = linspace(center - 20, center + 20)

	plt.plot(hjd, mag, 'o')
	#plt.plot(x, a2 + x * a1 + x**2 * a0)
	plt.show()

for i in ["r.lc"]:
	func(i)
