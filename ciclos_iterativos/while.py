from PIL import Image


cont = 0
while cont != 200:  #contador hasta 200 
    print(cont)
    cont = cont + 1

#mostrar una imagen cualquiera 
    
img = Image.open("D:\Documentos Danny\Platzi\Git y Github\proyecto1\ciclos_iterativos\Danny_bici.jpg")
img.show()


