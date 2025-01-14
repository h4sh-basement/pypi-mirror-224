# %%
import time, os
import numpy as np
import pandas as pd
import string
import colorsys
from PIL import Image, ImageDraw, ImageFont

# %%
class ModelDispatch_Paddle:
    def __init__(self,
                device='cpu',
                auto_load=False,
                log_telemetry=False,
                lang='en',
                ):
        assert device in ['cpu', 'cuda']
        self.device = device
        self.use_gpu = self.device in ['cuda']
        self.lang = lang
        self.paddle_ocr = None
        self.loaded = False
        self.running = False
        self.log_telemetry = bool(log_telemetry)
        self.telemetry = {
            'load_time': None,
            'forward_time': [],
        }
        if auto_load:
            self._load()
    
    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
    
    def _load(self):
        from paddleocr import PaddleOCR
        self.paddle_ocr = PaddleOCR(
            lang=self.lang,
            use_gpu=self.use_gpu,
            use_angle_cls=True,
            show_log=False,
        )
        self.loaded = True
    
    def _unload(self):
        del self.paddle_ocr
        self.paddle_ocr = None
        self.loaded = False
    
    def forward(self, *args, **kwargs):
        self.running = True
        if not self.loaded:
            self._load()
        
        time_start = time.perf_counter()
        
        _output = self._forward(*args, **kwargs)
        
        if self.log_telemetry:
            time_elapsed = time.perf_counter() - time_start
            self.telemetry['forward_time'].append(time_elapsed)
            self.telemetry['forward_time'] = self.telemetry['forward_time'][-20:]
        
        self.running = False
        return _output
    
    def _forward(self, image:Image.Image, detection_only=False) -> pd.DataFrame:
        image_feed = np.array(image.convert('RGB'))
        
        if detection_only:
            results = self.paddle_ocr.ocr(image_feed, rec=False)
            boxes_8_np = np.array(results).reshape(-1, 8)
            boxes_np = boxes_8_np[:, [0, 1, 2, 5]]
            data = [
                {
                    'text': '',
                    'score': 0.,
                    'box': [int(v) for v in box],
                }
                for box in boxes_np
            ]
        else:
            results = self.paddle_ocr.ocr(image_feed, cls=True)
            data = [
                {
                    'text': d[1][0],
                    'score': d[1][1],
                    'box': [int(v) for v in [*d[0][0], *d[0][2]]],
                }
                for res in results
                for d in res
            ]
        
        result_df = pd.DataFrame(
            data=data,
            columns=['text', 'score', 'box'],
        )
        return result_df

# %%