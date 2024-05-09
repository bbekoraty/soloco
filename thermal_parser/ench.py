from thermal_parser import Thermal
import numpy as np
from PIL import Image, ImageEnhance
import os

def enhance_image(image, brightness_factor=1.2, contrast_factor=2):
    # Enhance brightness and contrast
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)
    
    return image

def test_parse_dirp2():
    thermal = Thermal()
    for filepath_image in os.listdir('DJI_202405071302_003_Site-H1/T_sort/'):
        temperature = thermal.parse_dirp2(
            filepath_image="DJI_202405071302_003_Site-H1/T_sort/" + str(filepath_image),
            object_distance=12,
            relative_humidity=55,
            emissivity=0.95,
            reflected_apparent_temperature=37
        )
        print(filepath_image)
        
        assert isinstance(temperature, np.ndarray)
        im = Image.open("DJI_202405071302_003_Site-H1/T_sort/" + filepath_image)
        
        # Enhance the image
        enhanced_im = enhance_image(im)
        
        # Convert the image to grayscale
        enhanced_im = enhanced_im.convert("L")
        
        # Save the enhanced image
        enhanced_im.save("DJI_202405071302_003_Site-H1/thermal/" + filepath_image)
        print(filepath_image)

test_parse_dirp2()
