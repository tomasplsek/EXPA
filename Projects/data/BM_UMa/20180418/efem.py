from numpy import loadtxt, polyfit, linspace
import matplotlib.pyplot as plt


def func(name):
	file = loadtxt(name)
	hjd, mag, err = file[len(file[:,0])//2:,0], file[len(file[:,0])//2:,1], file[len(file[:,0])//2:,2]
	hjd = hjd - 2458000
	n = 0
	for h, m in zip(hjd, mag):
		n += 1
		if m == max(mag):
			center = n
			cen = h
	k = 10
	a7, a6, a5, a4, a3, a2, a1, a0 = polyfit(hjd[center - k:center + k], mag[center - k:center + k], 7)
	#a4, a3, a2, a1, a0 = polyfit(hjd[center - k:center + k], mag[center - k:center + k], 4)

	x = linspace(cen - 0.03, cen + 0.03)
	plt.plot(hjd[center - k:center + k], mag[center - k:center + k], 'o')
	#plt.plot(hjd, mag, 'o')
	y = a0 + x * a1 + x**2 * a2 + x**3 * a3 + x**4 * a4 + x**5 * a5 + x**6 * a6 + x**7 * a7
	#y = a0 + x * a1 + x**2 * a2 + x**3 * a3 + x**4 * a4
	plt.plot(x, y)
	plt.show()

	for X, Y in zip(x, y):
		if Y == max(y):
			print((2458227.412870 - 2458227.54781)*2)

for i in ["r.lc"]:
	func(i)
