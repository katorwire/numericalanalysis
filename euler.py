'''
we solve for y' = f(x, y) = x + y
this code can be modified for different 
ODE's
'''


def euler(x0=0, y0=1, h=0.1):
    '''
    in this function; it accepts the inital values 
    x0 which is 0 and y0 is 1, and the step factor
    h which is 0.1

    '''
    y_prime = x0 + y0  # this gets the first value for yprime

    '''
    a for loop is used to iterate over it to get our values
    of yn from 1 to 10
    '''
    for i in range(1, 11):
        # this is the formula for finding the next value after the step
        y_N = y0 + h * (y_prime)
        next_x = round(x0 + h, 2)  # i used this to geet the next x
        x0 += 0.1  # i had to increment or i will still be left with x0 =0.1 which will be bad

        y_prime = next_x + y_N
        y0 = y_N  # we also have to change our y0
        # we pass the arguement y_n to the print function to print our values to the screen
        print('the values after ', i, 'are {:.3f}'.format(y_N))


euler()  # we call the function here
