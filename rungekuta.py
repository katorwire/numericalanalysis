import math

'''
4 stage rungu kuta problem for 
value problem y'=3x^2y in the interval x€[0,1].
'''


def runge(y0, x0, h, int_val):  # in this function we collect certain set of parameters y0, x0, h
    '''
    to find the stepsize for the equation we use
    the above equation
    '''
    for n in range(11):
        print()
        print('after n = ', n)

        k1 = int_val * pow(x0, 2) * y0
        k2 = int_val * pow(x0 + h/2, 2) * (y0 + (h*k1)/2)
        k3 = int_val * pow(x0 + h/2, 2) * (y0 + (h*k2)/2)
        k4 = int_val * pow(x0 + h, 2) * (y0 + h*k3)
        print()  # printing spaces to make the work look neat

        # formula for calculating the y1, y2 y3, y4 value
        y_next_value = y0 + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        print(y_next_value)

        x0 += 0.1  # this increments the value of x0 by o.1 as n increases

        # this chnages the y0 value to the current value that has been calculated already
        y0 = y_next_value

        '''
        the respective formulas above for k1, k2, k3, k4
        '''

        true_value = math.e**((0.1*n)**2)

        print('the values of k1 at n = {} is {}'.format(n, k1))
        print('the values of k2 at n = {} is {}'.format(n, k4))
        print('the values of k3 at n = {} is {}'.format(n, k3))
        print('the values of k4 at n = {} is {}'.format(n, k4))

        print('the true values at the corresponding ',
              n, 'values are', true_value)

        
    print()


print(runge(1, 0, 0.1, 3))
