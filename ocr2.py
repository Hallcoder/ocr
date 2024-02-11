from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Autopsy-4.21.0\autopsy\Tesseract-OCR\tesseract.exe'
# Load the image
img_path = r'C:\Users\Admin\Documents\projects\embedded\ocr\ocr_image.png'
img = Image.open(img_path)

# Image preprocessing
# img = img.resize((int(img.width * 0.5), int(img.height * 0.5)))  # Resize image
# img = img.convert('L')  # Convert to grayscale
# img = img.point(lambda x: 0 if x < 128 else 255)  # Apply thresholding

# # Save the preprocessed image (optional)
# img.save('preprocessed_image.png')

# Use Tesseract OCR
text = pytesseract.image_to_string(img, config='--psm 6 -l eng')

# Print the extracted text
print(text)
