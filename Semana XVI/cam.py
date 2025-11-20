import cv2 as cv

cap = cv.VideoCapture()
if not cap.isOpened():
    raise Exception("ERROR! No se pudo abrir la cámara")

# chicky = cv.imread("/Users/miguelcamargorojas/Documents/UP/PDI-Ago-dic25/Grupo A/images/chicky_512.png")
# cv.imshow("TEST", chicky)
# key = cv.waitKey()
is_gray = False
is_blurred = False
while True:
    _, frame = cap.read()
    if is_gray:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if is_blurred:
        frame = cv.blur(frame, (11, 11))

    key = cv.waitKey(17)
    if key == ord("q"):
        exit()
    elif key == ord("g"):
        is_gray = not is_gray
    elif key == ord("b"):
        is_blurred = not is_blurred

    cv.imshow("frame", frame)

cap.release()
cv.destroyAllWindows()
# print(key)
# print(ord("h"))