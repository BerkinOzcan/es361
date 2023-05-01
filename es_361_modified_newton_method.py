
import math
xi=2.5
M=2
'''
fx_term_1= pow(xi,3)
fx_term_2= pow(xi,2)*(math.exp(xi)-4)
fx_term_3=
fx_term_4=
'''
for i in range(10):
    # TODO: write code...
    print(i)
    f_x = (xi**3) + (xi**2)*(math.exp(xi)-4) - (4*xi*(math.exp(xi)-1)) + 4*math.exp(xi)
    fprime_x = 3*(xi**2) + 2*xi*(math.exp(xi)-4) + (xi**2)*math.exp(xi) - 4*(math.exp(xi)-1) - 4*xi*math.exp(xi) + 4*math.exp(xi)
#xi_pone=xi-(M*f_x/fprime_x)
    xi_pone=xi-(M*f_x/fprime_x)
    print("xi= " , xi)
    print("f(xi)= " , f_x)
    print("f'(xi)= " , fprime_x)
    print("xi+1" , xi_pone)
    xi=xi_pone

