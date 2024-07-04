import cv2
import pytesseract

image = cv2.imread('op2.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

custom_config = r'--oem 3 --psm 6 outputbase digits'
extracted_text = pytesseract.image_to_string(thresh, config=custom_config)

lines = extracted_text.split('\n')

ic_types = {
    '76': 'Integrated-Circuit J-K Flip-Flop',
    '11': 'AND 3 GATE',
    '22': 'NAND GATE',
    '02': 'AND GATE',
}

ic_type = 'Unknown IC'
for line in lines:
    for pattern, ic_name in ic_types.items():
        if pattern in line:
            ic_type = ic_name
            break
    if ic_type != 'Unknown IC':
        break 

print("Identified IC Type:", ic_type)

