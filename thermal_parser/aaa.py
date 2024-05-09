from thermal_parser  import Thermal
import numpy as np
import matplotlib.pyplot as plt 
import os

from PIL import Image

def test_parse_dirp2():
        thermal = Thermal()
        for filepath_image in os.listdir('test_pic/') :
    

            temperature = thermal.parse_dirp2(filepath_image="test_pic/"+str(filepath_image),
    object_distance = 22,
    relative_humidity = 55,
    emissivity = 0.95,
    reflected_apparent_temperature = 37,)
   
            assert isinstance(temperature, np.ndarray)
            im = Image.fromarray(temperature)
            plt.imshow(temperature)
            plt.show()
            print(temperature)
            if im.mode != 'RGB':
                im = im.convert('RGB')
            # im.save("DJI_202405071302_003_Site-H1/"+filepath_image)
            print(filepath_image);
            
test_parse_dirp2()
