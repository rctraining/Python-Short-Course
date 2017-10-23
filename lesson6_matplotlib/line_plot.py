##################################################################
# Example:  Creating a line plot
# To begin with, we import the pyplot package from matplotlib
# Common practice is to alias pyplot as plt
# We also import numpy

import matplotlib.pyplot as plt
import numpy as np

###############################################
# Let's generate some sample data to plot
# We will plot two functions of x
pi = np.pi
npts = 64
mydt='float64'
x  = np.linspace(0,2*pi,npts,dtype=mydt)

y1 = x
y2 = x*x
y3 = np.cos(2*x)
###############################################

plt.figure(1)
plt.plot(x,y1)        # Simple line plot
# Matplotlib choose default colors based on the ordering of the plots.
# The first plot is blue, the second is orange, etc.
# We can control the color using a single-character string corresponding
# to the first letter of the color we want to use.
# We can also add additional characters that indicate the linestyle we would like to adopt.
# For other available symboles and linestyles, see 
#  https://matplotlib.org/api/markers_api.html

plt.plot(x,y2,'go')   # green circles (first letter g = green; second letter o = filled circle)
plt.plot(x,y3,'r--')  # red dashed lines (first letter r = red; second characters indicate line pattern)

# The xlabel, ylabel, and title functions control the axes and plot title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Title')


#To view the plot in our web browser, we use the "show" function.
plt.show()

# Alternatively, we can save the figure in a number of formats
# Try uncommenting the savefig and one of the ext's below 
#ext='png'
#ext='pdf'
#ext='jpeg'
#plt.savefig('sample_figure.'+ext)


