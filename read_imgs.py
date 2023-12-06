import cv2 as cv

# Leitura de imagens
img = cv.imread("images/foto_padrao.png") # matriz de pixels armazenada em img

cv.imshow('Tigre', img)

cv.waitKey(0)   # espera por uma tecla ser pressionada

### a imagem será aberta em uma outra janela 