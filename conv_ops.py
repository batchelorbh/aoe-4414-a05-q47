#!/usr/bin/env python
# conv_ops.py
#
# Calculates the output shape and operation count of a convolution layer
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Parameters:
#    c_in                input channel count
#    h_in                input height count
#    w_in                input width count
#    n_filt              number of filters in the convolution layer
#    h_filt              filter height count
#    w_filt              filter width count
#    s                   stride of convolution layers
#    p                   amount of padding on each of the four input map sides
#
# Output:
#    Print output values to screen, including the output channel count,
#    height count, width count, number of additions performed, number of
#    multiplications performed, and number of divisions performed
#
# Revision history:
#    10/22/2024          Script created
#
###############################################################################

#Import relevant modules
import sys
from math import floor

#Define constants
const1 = 0

#User-defined functions
def user_function(param1, param2):
   return param1 + param2

#Pre-initialize input parameters
c_in = float('nan') #Input channel count
h_in = float('nan') #Input height count
w_in = float('nan') #Input width count
n_filt = float('nan') #Number of filters in the convolution layer
h_filt = float('nan') #Filter height count
w_filt = float('nan') #Filter width count
s = float('nan') #Stride of convolution filters
p = float('nan') #Amount of padding on each of the four input map sides

#Arguments are strings by default
if len(sys.argv) == 9:
   c_in = float(sys.argv[1])
   h_in = float(sys.argv[2])
   w_in = float(sys.argv[3])
   n_filt = float(sys.argv[4])
   h_filt = float(sys.argv[5])
   w_filt = float(sys.argv[6])
   s = float(sys.argv[7])
   p = float(sys.argv[8])
else:
   print('Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p')
   sys.exit()

#Main body of script

#Calculate the number of output channels
c_out = n_filt

#Calculate the height and width of the output map
h_out = floor(((h_in + 2 * p - h_filt) / s) + 1)
w_out = floor(((w_in + 2 * p - w_filt) / s) + 1)

#Calculate total number of additions, multiplications, and divisions
muls = n_filt * h_out * w_out * c_in * h_filt * w_filt
adds = n_filt * h_out * w_out * c_in * h_filt * w_filt
divs = 0 #Zero for standard convolutions

#Print output to the screen
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
