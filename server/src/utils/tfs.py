# Serie de Fourier, con n coeficientes
# Ref.Chapra 5ed Ejemplo 19.2 p548/pdf572
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO
T = 2*np.pi

t = sym.Symbol('t')
ft = sym.Piecewise((-1,t <-T/2),
                   (-1,t <-T/4),
                   ( 1,t < T/4),
                   (-1,t < T/2),
                   (-1,True),)
# intervalo
a = -T/2
b = T/2

# número de coeficientes
n = 11
# Evaluación para gráfica
muestras = 101
digitos  = 4    # numpy set_print_options 
casicero = 1e-15

# PROCEDIMIENTO
k  = sym.Symbol('k')
w0 = 2*np.pi/T

# Términos ak para coseno
enintegral  = ft*sym.cos(k*w0*t)
yaintegrado = sym.integrate(enintegral,(t,a,b))
ak = (2/T)*yaintegrado
ak = sym.simplify(ak)

# Términos bk para seno
enintegral = ft*sym.sin(k*w0*t)
yaintegrado = sym.integrate(enintegral,(t,a,b))
bk = (2/T)*yaintegrado
bk = sym.simplify(bk)

print(' expresión ak:')
sym.pprint(ak)
#print('\n ak formato latex')
#print(sym.latex(ak))

print('\n expresión bk:')
sym.pprint(bk)
#print('\n bk formato latex')
#print(sym.latex(bk))

# evalua los coeficientes
a0  = ak.subs(k,0)/2
b0  = bk.subs(k,0)
aki = [a0]
bki = [b0]
n_i = [0]
i = 1
while not(i>=n):
    avalor = ak.subs(k,i)
    bvalor = bk.subs(k,i)
    aki.append(avalor)
    bki.append(bvalor)
    n_i.append(i)
    i = i+1
    
##print('\n coeficientes ak: ')
##print(aki)
##print('\n coeficientes bk: ')
##print(bki)



# tabla de valores ak, Bk
tabla = np.concatenate([[np.array(n_i,dtype = int)],
                        [np.array(aki,dtype = float)],
                        [np.array(bki,dtype = float)]],
                       axis=0)
tabla = np.transpose(tabla)
np.set_printoptions(precision=digitos)
print('\n coeficientes: \n [ k, \t\t ak, \t  bk ] ')
print(tabla)

# serie de Fourier expresión
serieF = a0 + 0*t 
i = 1
while not(i>=n):
    serieF = serieF + aki[i]*sym.cos(i*w0*t)
    serieF = serieF + bki[i]*sym.sin(i*w0*t)
    i = i+1
# serie = sym.simplify(serie)

print('\n serie de Fourier fs(t): ')
# sym.pprint(serieF)
print(a0)
for i in range(1,n,1):
    termino = '+ '
    if aki[i]<0:
        termino = '- '
    aki_str = str(abs(aki[i]))
    if abs(aki[i])<casicero:
        aki_str = '0'
    termino = termino + aki_str+' cos('+str(i*w0)+' t)'
    if bki[i]>=0:
        termino = termino + '+ '
    else:
        termino = termino + '- '
    bki_str = str(abs(bki[i]))
    if abs(bki[i])<casicero:
        bki_str = '0'
    termino = termino + bki_str+' sin('+str(i*w0)+' t)'
    print(termino)


# Grafica - Para evaluacion numerica
fsn = sym.lambdify(t,serieF)
ftn = sym.lambdify(t,ft)

# Evaluacion para grafica
ti = np.linspace(a,b,muestras)
fi = ftn(ti)
fsi = fsn(ti) 

# SALIDA
# Grafica f(t) y Fourier en t
figura, graf_ftT0 = plt.subplots()
graf_ftT0.plot(ti,fi,label = 'f(t)')
etiqueta = 'coeficientes = '+ str(n)
graf_ftT0.plot(ti,fsi,label = etiqueta)
graf_ftT0.set_xlabel('t')
graf_ftT0.set_ylabel('f(t)')
graf_ftT0.legend()
graf_ftT0.grid()
graf_ftT0.set_title('Serie de Fourier de f(t)')
#plt.show()

# espectro de frecuencia Amplitud y fase
k_i = np.arange(0,n,1,dtype=float)
ak_i = np.array(aki,dtype=float)
bk_i = np.array(bki,dtype=float)

ck_i = np.sqrt(ak_i**2 + bk_i**2)
cfs_i = np.zeros(len(ak_i))
condicion = (abs(ak_i)>=casicero)
pendiente = -bk_i[condicion]/ak_i[condicion]
cfs_i[condicion] = np.arctan(pendiente)

tabla = np.concatenate([tabla,
                        np.transpose([ck_i]),
                        np.transpose([cfs_i])
                        ],
                       axis=1)
np.set_printoptions(precision=4)
print('\n coeficientes magnitud y fase: ')
print(' [k,\t\t ak,\t   bk,\t\t Ck,\t   fase_k ]')
print(tabla)

# grafica de espectro de frecuencia
figura, graf_Fw = plt.subplots(2,1)
graf_Fw[0].stem(k_i,ck_i,label='Ck_magnitud')
graf_Fw[0].set_ylabel('Ck')
graf_Fw[0].set_title('Espectro de frecuencia')
graf_Fw[0].legend()
graf_Fw[0].grid()

graf_Fw[1].stem(k_i,cfs_i,label='Ck_fase')
graf_Fw[1].legend()
graf_Fw[1].set_ylabel('Ck_fase')
graf_Fw[1].set_xlabel('k')
graf_Fw[1].grid()

plt.show()