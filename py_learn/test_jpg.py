
import os
from PIL import Image

def resize_images(input_dir: str, output_dir: str, size: tuple) -> None:
    """
    将输入目录中的所有图片文件调整为指定大小并保存到输出目录中。

    Args:
        input_dir (str): 输入目录的路径。
        output_dir (str): 输出目录的路径。
        size (tuple): 调整后的图片大小，格式为 (width, height)。

    Returns:
        None
    """
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        with Image.open(input_path) as img:
            img_resized = img.resize(size)
            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)
