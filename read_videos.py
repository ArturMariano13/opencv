import cv2 as cv

# Leitura de Vídeos

capture = cv.VideoCapture(0)
# se colocar 0,1 ou 2 como parâmetro da função, abrirá alguma webcam do computador
# coloca-se o caminho para o vídeo

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if (cv.waitKey(20) & 0xFF==ord('d')):   # encerrará o programa quando a tecla 'd' for pressionada
        break

capture.release()
cv.destroyAllWindows()
