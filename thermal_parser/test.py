from thermal_parser  import Thermal
import numpy as np
import matplotlib.pyplot as plt 
import os

from PIL import Image

def test_parse_dirp2():
        thermal = Thermal()
        for filepath_image in os.listdir('DJI_202405071302_003_Site-H1/T_sort/') :
    

            temperature = thermal.parse_dirp2(filepath_image="DJI_202405071302_003_Site-H1/T_sort/"+str(filepath_image),
    object_distance = 22,
    relative_humidity = 62,
    emissivity = 0.95,
    reflected_apparent_temperature = 34,)
            
            fig, ax = plt.subplots()
            
            im = plt.imshow(temperature,cmap="gray")
            
            ax.axis("off")

            assert isinstance(temperature, np.ndarray)
            # im = Image.fromarray(temperature*1.2)
            # if im.mode != 'RGB':
            #     im = im.convert('RGB')
            
            
                
            plt.savefig("DJI_202405071302_003_Site-H1/thermal/"+filepath_image, format = "png", bbox_inches='tight',pad_inches=0.0 )
            plt.close(fig)
            
test_parse_dirp2()
