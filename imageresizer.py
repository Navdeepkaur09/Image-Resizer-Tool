from PIL import Image
import os

output_folder="thumbnails"
os.makedirs(output_folder,exist_ok=True)
files=os.listdir(".")
for file in files:
    if file.lower().endswith(".jpg"):
        try:
            image=Image.open(f"{file}")
            image.thumbnail((640,400))
            base_name=os.path.splitext(file)[0]
            output_path=os.path.join(output_folder,f"{base_name}_thumbnail.jpg")
            image.save(output_path)
            print(f"Saved : {output_path},Size :{image.size}")
        except Exception as e:
            print(f"Error processing {file} : {e}")