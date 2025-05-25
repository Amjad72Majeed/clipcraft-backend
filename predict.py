import torch
from diffusers import DiffusionPipeline
from PIL import Image
import moviepy.editor as mpy
import os
from datetime import datetime

# Load model (load once, globally)
pipe = DiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16,
    revision="fp16"
)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def predict_video(prompt: str) -> str:
    # Create a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_dir = "static"
    os.makedirs(output_dir, exist_ok=True)
    video_path = os.path.join(output_dir, f"{timestamp}_output.mp4")

    # Generate 8 images from the prompt
    images = []
    for i in range(8):
        image = pipe(prompt).images[0]
        images.append(image)

    # Convert images to video using MoviePy
    clip = mpy.ImageSequenceClip([img for img in images], fps=2)
    clip.write_videofile(video_path, codec='libx264')

    return video_path