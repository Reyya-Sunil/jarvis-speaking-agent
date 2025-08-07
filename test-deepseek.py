import os
from PIL import Image

gif_path = r"C:\Users\reyya\OneDrive\Desktop\jarvis\ai-speaking-jarvis\AI Animation.gif"

if os.path.exists(gif_path):
    gif = Image.open(gif_path)
    # proceed with displaying or using the gif
else:
    print("[⚠ Warning] Animation file not found. Skipping animation.")
