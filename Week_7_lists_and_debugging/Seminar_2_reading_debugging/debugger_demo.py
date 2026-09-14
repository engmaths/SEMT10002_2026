from math import cosh

xhi = 0.0
xlo = 1.0
a = -3.165
yhi = cosh(xhi+a)
ylo = cosh(xlo+a)

for ii in range(20):
    if yhi<ylo:
        xtmp = xhi
        ytmp = yhi
        xhi = xlo
        yhi = ylo
        xlo = xtmp
        ylo = ytmp
    else:
        xnew = xlo+(xlo-xhi)
        ynew = cosh(xnew+a)
        if ynew<ylo:
            xhi = xlo
            yhi = ylo
            xlo = xnew
            ylo = ynew
        else:
            xhi = 0.5*(xhi+xlo)
            yhi = cosh(xhi+a)
    print(xlo,ylo)