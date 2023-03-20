import cv2
classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

imagem = cv2.imread("imagens/pessoas1.jpg")
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.2, minSize=(41,41))
print(facesDetectadas)
for x, y, l, a in facesDetectadas:
    imagem = cv2.rectangle(imagem, (x,y), (x+l, y+a), (0, 255, 0), 2 )

cv2.imshow("pessoas1", imagem)
cv2.waitKey()