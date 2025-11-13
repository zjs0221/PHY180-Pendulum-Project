# Sample Python code to run the fit_black_box Python code relatively easily
import sys, math
import matplotlib.pyplot as plt

sys.path.insert(0,r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02")
import fit_black_box as bb

# Loading from a file like a CSV file.
# NOTE: The CSV file should not have commas to separate things! Spaces or tabs are fine.

# Again, start with a fitting function. This time it is quadratic.

def quadratic(theta, period, b, c):
    return period*(1 + b*theta + c*theta**2)

def sinusoidal(time, tau, phi, T,a):
    return -.175 * bb.np.e**(-time/tau) * bb.np.cos(((2*bb.np.pi/T) * time)+phi)+a

def radical(length, k, n):
    return k * length**n

def expon(time, tau):
    return .262 * bb.np.e**(-time/tau)
# Now load the data from the file. The file should be in the same directory as this Python code.
# Some chance you will need an absolute path

aVSt1 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 01.txt"
aVSt2 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 02.txt"
aVSt3 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 03.txt"
aVSt4 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 04.txt"
aVSt5 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 05.txt"
aVSt6 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 06.txt"
aVSt7 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 07.txt"
aVSt8 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 08.txt"
aVSt9 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 09.txt"
aVSt10 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 10.txt"
aVSt11 = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Amplitude vs Time 11.txt"
pVSl = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Period vs Length.txt"
qVSl = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\report02\Qfactor vs Length.txt"

# This time, let's use every single possible option available to bb.plot_fit()

font_size = 20
xlabel="Time (s)"
ylabel="Amplitude (rad)"
title=""

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
x, y, xerr, yerr = bb.load_data(pVSl)
bb.plot_fit(radical, x, y, xerr, yerr, init_guess=(2, .5), font_size=font_size, xlabel="Length", ylabel="Period", title=title, color="blue", labelA="Radical Regression")

x, y, xerr, yerr = bb.load_data(aVSt1)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, .6, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.0944m")

x, y, xerr, yerr = bb.load_data(aVSt2)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, .723, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.1297m")

x, y, xerr, yerr = bb.load_data(aVSt3)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 0.821, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.1685m")

x, y, xerr, yerr = bb.load_data(aVSt4)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, .95, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.2129m")

x, y, xerr, yerr = bb.load_data(aVSt5)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.026, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.2610m")

x, y, xerr, yerr = bb.load_data(aVSt6)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.15, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.3040m")

x, y, xerr, yerr = bb.load_data(aVSt7)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.2, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.3375m")

x, y, xerr, yerr = bb.load_data(aVSt8)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.229, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.3720m")

x, y, xerr, yerr = bb.load_data(aVSt9)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.3, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.4090m")

x, y, xerr, yerr = bb.load_data(aVSt10)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.4, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.4445m")

x, y, xerr, yerr = bb.load_data(aVSt11)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.416, 0), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="L= 0.5015m")

'''
x, y, xerr, yerr = bb.load_data(pVSa)
bb.plot_fit(quadratic, x, y, xerr, yerr, init_guess=(-0.5, 0, +0.5), font_size=font_size, xlabel="Release Angle (rad)", ylabel="Period (s)", title=title, color="blue", labelA="Equation 3")

x, y, xerr, yerr = bb.load_data(aVStExt)
bb.plot_fit(expon, x, y, xerr, yerr, init_guess=(110), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="Equation 2")'''

# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical