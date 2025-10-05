# Sample Python code to run the fit_black_box Python code relatively easily
import sys, math
import matplotlib.pyplot as plt

sys.path.insert(0,r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj")
import fit_black_box as bb

# Loading from a file like a CSV file.
# NOTE: The CSV file should not have commas to separate things! Spaces or tabs are fine.

# Again, start with a fitting function. This time it is quadratic.

def quadratic(theta, period, b, c):
    return period*(1 + b*theta + c*theta**2)

def sinusoidal(time, tau, phi, T):
    return .262 * bb.np.e**(-time/tau) * bb.np.cos(((2*bb.np.pi/T) * time)+phi)

def expon(time, tau):
    return .262 * bb.np.e**(-time/tau)
# Now load the data from the file. The file should be in the same directory as this Python code.
# Some chance you will need an absolute path

pVSa = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\Period vs Angle.txt"
aVSt = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\Amplitude vs. Time.txt"
aVStExt = r"C:\Users\jings\Downloads\EngSciY1\Physics\PendulumProj\Amplitude vs. Time ext.txt"
x, y, xerr, yerr = bb.load_data(aVSt)

# This time, let's use every single possible option available to bb.plot_fit()

font_size = 20
xlabel="Time (s)"
ylabel="Amplitude (rad)"
title=""

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
x, y, xerr, yerr = bb.load_data(pVSa)
bb.plot_fit(quadratic, x, y, xerr, yerr, init_guess=(-0.5, 0, +0.5), font_size=font_size, xlabel="Release Angle (rad)", ylabel="Period (s)", title=title, color="blue", labelA="Equation 3")

x, y, xerr, yerr = bb.load_data(aVSt)
bb.plot_fit(sinusoidal, x, y, xerr, yerr, init_guess=(100, 0, 1.26), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="Equation 1")

x, y, xerr, yerr = bb.load_data(aVStExt)
bb.plot_fit(expon, x, y, xerr, yerr, init_guess=(110), font_size=font_size, xlabel=xlabel, ylabel=ylabel, title=title, color="blue", labelA="Equation 2")

# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical