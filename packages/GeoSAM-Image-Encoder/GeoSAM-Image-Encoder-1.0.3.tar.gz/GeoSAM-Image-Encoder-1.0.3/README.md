# GeoSAM-Image-Encoder

This package is part of [Geo-SAM](https://github.com/coolzhao/Geo-SAM) and is used to encode image data into features recognized by Geo-SAM.

## Installation

Installing `GeoSAM-Image-Encoder` directly will install the CPU version of `PyTorch`. Therefore, it is recommended to install the appropriate version of `PyTorch` before installing `GeoSAM-Image-Encoder` in your machine. You can install the corresponding version based on the official PyTorch website:
<https://pytorch.org/get-started/locally/>

After installing PyTorch, you can install `GeoSAM-Image-Encoder` via pip.

``` BASH
pip install GeoSAM-Image-Encoder
# or
pip install git+https://github.com/Fanchengyan/GeoSAM-Image-Encoder.git
```


## Usage

You can call this script in Python or Terminal.

### Using Python

After install GeoSAM-Image-Encoder, you can import it using `geosam`

```python
import geosam
from geosam import ImageEncoder
```

check the folder contains geosam and add it to environment if you want to run in terminal

```python
geosam.folder
```

check if gpu available

```python
geosam.gpu_available()
```

#### Run by specify parameters dirctly

```python
checkpoint_path = '/content/sam_vit_l_0b3195.pth'
image_path = '/content/beiluhe_google_img_201211_clip.tif'
feature_dir = './'

## init ImageEncoder
img_encoder = ImageEncoder(checkpoint_path)
```

```python
## encode image
img_encoder.encode_image(image_path, feature_dir)
```

#### Run by parameters from setting.json file

If you want to using settings.json file to provide the parameters

```python
setting_file = "/content/setting.json"
feature_dir = './'

### parse settings from the setting,json file
settings = geosam.parse_settings_file(setting_file)

### setting file not contains feature_dir, you need add it
settings.update({"feature_dir":feature_dir})

### split settings into init_settings, encode_settings
init_settings, encode_settings = geosam.split_settings(settings)

print(f"settings: {settings}")
print(f"init_settings: {init_settings}")
print(f"encode_settings: {encode_settings}")
```

Then, you can run image incoding by parrameters from setting.json file

```python
img_encoder = ImageEncoder(**init_settings)
img_encoder.encode_image(**encode_settings)
```

### Using Terminal


check the folder of geosam

```python
print(geosam.folder)
```

add this folder into environment of your machine. Then run in terminal:

```bash
image_encoder.py -i /content/beiluhe_google_img_201211_clip.tif -c /content/sam_vit_l_0b3195.pth -f ./
```

You can overwrite the settings from file by specify the parameter values. For Example

```bash
image_encoder.py -s /content/setting.json  -f ./ --stride 256 --value_range "10,255"
```

check all available parameters:

```bash
image_encoder.py -h
```
