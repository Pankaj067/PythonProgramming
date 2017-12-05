import io
from google.cloud import vision

vision_client = vision.Client()
filename = "C:/Users/pankaj.kumar1/Desktop/PythonLib/Images/TextImage.PNG"
#filename = "C:/Users/pankaj.kumar1/Desktop/PythonLib/Images/Steve.jpg"
with io.open(filename,'rb') as image_file:
	content = image_file.read()
	image = vision_client.image(content = content)

labels = image.detect_labels()

print("-----------------")
for label in labels:
	print(label.description , " -> confidence: " , label.score)
	print("")

print("-----------------")


for text in image.detect_text():
	print(text.description,)
