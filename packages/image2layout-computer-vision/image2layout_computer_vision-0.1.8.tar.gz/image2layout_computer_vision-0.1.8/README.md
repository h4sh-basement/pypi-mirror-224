# image2layout_computer_vision

An image processing module for some computer vision tasks (public module for image2layout)

Package Page: [pypi](https://pypi.org/project/image2layout-computer-vision/)

Features:

1. Text Detection and Recognition (OCR)
2. Color extraction (background and main foreground)

## Installations

### Install with `python`/`conda` [Linux]

1. (Optional) Conda

```bash
curl https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh -o ~/conda.sh
bash ~/conda.sh -b -f -p /opt/conda
rm ~/conda.sh
conda init --all --dry-run --verbose

conda create -n cv python=3.10 -y
conda activate cv
```

3. Python libraries (python>=3.8)

> CPU
```bash
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
python -m pip install paddleocr paddlepaddle

python -m pip install datasets transformers scikit-learn Pillow numpy pandas chardet
python -m pip install --upgrade image2layout-computer-vision
```

> GPU
```bash
# python -m pip install 'torch>=2.0' torchvision torchaudio
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
python -m pip install paddleocr paddlepaddle-gpu

python -m pip install datasets transformers scikit-learn Pillow numpy pandas chardet
python -m pip install --upgrade image2layout-computer-vision
```

### Install with `docker`
For running with CPU on Ubuntu
```bash
sudo docker build --tag cv -f Dockerfile_cpu .

sudo docker run -it -p 0.0.0.0:8000:8000 -p 0.0.0.0:8001:8001 -v $(pwd):/app cv bash

```

From inside container
```bash
cd deployment
conda activate cv
python api_serve.py -n CV -p 8000
```

## Usage

Note: Input image/images expects a filepath, an Image.Image object, or a numpy array

1. Run this python code to pre-download model weights

```python
from image2layout_computer_vision import OCR
OCR._load()
```

2. Recognize texts

```python
from image2layout_computer_vision.ocr as OCR

# [A] no text, box only, 2 lists of dicts with keys [text (empty), box, score (empty)]
data_merged, data_raw = OCR.detect_text_data('path/to/image.png', recognition=False)

# [B] text + box from multiple images -> list of list of dicts with keys [text, box, score]
data_raw_multi = OCR.detect_text_elements(['path/to/image.png', 'path/to/image2.png'])

```

3. Extract colors
```python
import image2layout_computer_vision as icv

# [A] list [ tuples [ 2 rgb-color tuples ] ] for background and foreground
# sample output: [((2, 2, 2), (4, 4, 4)), ((6, 6, 6), (8, 8, 8))]
colors_all = icv.extract_colors(['path/to/image.png', 'path/to/image2.png'])

# [B] 2 rgb-color tuples for background and foreground
# sample output: ((9, 9, 9), (6, 6, 6))
color_bg, color_fg = icv.extract_colors('path/to/image.png')

```

4. Detect elements [work-in-progress]
```python
import image2layout_computer_vision.yolov6 as Detection

# pd.DataFrame with columns [box, score, class_index, class_name]
df_element = Detection.detect_element('path/to/image.png')

```


## Build
(for building and uploading this package)
```bash
python -m pip install --upgrade pip
python -m pip install --upgrade build twine "keyring<19.0"

rm -rf dist
python -m build
python -m twine upload dist/* --verbose
```
