from PyQt5.QtWidgets import QApplication,QWidget
import pyqtgraph.opengl as gl
from mpmath import mp

mp.depth=40

def bust(xx,yy):
    x=mp.mpf(xx)
    y=mp.mpf(yy)
    return mp.mpf('1')/mp.mpf('8')* (mp.mpf('6')*mp.exp(-((mp.mpf('2')/mp.mpf('3')*mp.fabs(x) - mp.mpf('1'))**mp.mpf('2') + (mp.mpf('2')/mp.mpf('3') *y)**mp.mpf('2')) - mp.mpf('1')/mp.mpf('3')*(mp.mpf('2')/mp.mpf('3')*y + mp.mpf('1')/mp.mpf('2'))**mp.mpf('3'))+ mp.mpf('2')/mp.mpf('3') *mp.exp(mp.mpf('-2.818')**mp.mpf('11')*((mp.fabs(mp.mpf('2')/mp.mpf('3')*x) - mp.mpf('1'))**mp.mpf('2')+ (mp.mpf('2')/mp.mpf('3') *y)**mp.mpf('2'))**mp.mpf('2')) + mp.mpf('2')/mp.mpf('3')*y - (mp.mpf('2')/mp.mpf('3')*x)**mp.mpf('4'))

def draw_oppai(x, y, distance,pxl=2):

    app = QApplication([])
    w = gl.GLViewWidget()
    w.resize(600,400)
    w.opts['distance'] = distance
    w.show()
    w.setWindowTitle('Oppai')

    p=[ [ xp,yp,bust(xp,yp)] for xp in x for yp in y]
    plt=gl.GLScatterPlotItem(pos=p,color=(1,1,1,1),size=pxl)
    w.addItem(plt)

    app.exec_()

def linspace(a,b,n):
    return [ a+i*((b-a)/n) for i in range(n+1)]

def main():
    nx=100
    ny=50
    x=linspace(-3.0,3.0,nx)
    y=linspace(-3.0,3.0,ny)
    draw_oppai(x,y,10,pxl=2)

if __name__=='__main__':
    main()

