import os
import os.path
import sys



w = "/Users/guilhermeluftmendes/Desktop/Python"

for raiz, diretorios, arquivos in os.walk(w):
    print ("\nCaminho:", raiz)
    for d in diretorios:
        space = os.path.getsize(os.path.join(raiz, d))
        print (" %s/ (%d bytes)" % (d, space))
    for f in arquivos:
        space = os.path.getsize(os.path.join(raiz, d, f))
        print (os.path.join(raiz, d, f))
        #print ("  %s (%d bytes)" % (f, space))
        
