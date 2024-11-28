import os
import torch
from comfy import model_management
import folder_paths
from .libs.YosoDelightPipe import YosoDelightPipeline

deviceType = model_management.get_torch_device().type


class LoadStableDelightModel:

    @classmethod
    def INPUT_TYPES(cls):
        paths = []
        for search_path in folder_paths.get_folder_paths("diffusers"):
            if os.path.exists(search_path):
                for root, subdir, files in os.walk(search_path, followlinks=True):
                    if "model_index.json" in files:
                        paths.append(os.path.relpath(root, start=search_path))
        return {
            "required": {
                "model": (paths,),
                "device": (["AUTO", "CPU"], )
            }
        }

    RETURN_TYPES = ("DelightMODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "load_model"
    CATEGORY = "stableX/delight"

    def load_model(self, model, device):
        for search_path in folder_paths.get_folder_paths("diffusers"):
            if os.path.exists(search_path):
                path = os.path.join(search_path, model)
                if os.path.exists(path):
                    model = path
                    break

        if device == "AUTO":
            device_type = deviceType
        else:
            device_type = "cpu"
        # Stable-X/yoso-delight-v0-4-base
        pipe = YosoDelightPipeline.from_pretrained(model,
                                                   cache_dir=folder_paths.get_folder_paths("diffusers")[0],
                                                   safety_checker=None,
                                                   variant="fp16",
                                                   torch_dtype=torch.float16 if device_type == "cuda" else None,
                                                   t_start=0,
                                                   local_files_only=True).to(device_type)
        # 启用 xformers
        if model_management.XFORMERS_IS_AVAILABLE and device_type == "cuda":
            pipe.enable_xformers_memory_efficient_attention()

        return (pipe, )


class ApplyStableDelight:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("DelightMODEL",),
                "images": ("IMAGE",),
                "strength": ("FLOAT",
                             {
                                 "default": 1,
                                 "min": 0.01,
                                 "max": 5.0,
                                 "step": 0.1
                             }),
                "resolution": ("INT",
                               {
                                   "default": 1024,
                                   "step": 8,
                                   "min": 0,
                                   "max": 4096,
                                   "tooltip": "Preprocess the resolution of the image, if eq 0, using image original size"
                               }),
                "upscale_method": (["nearest-exact", "bilinear", "area", "bicubic", "lanczos"], {"default": "bilinear"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "delight"
    CATEGORY = "stableX/delight"

    def delight(self, model, images, strength, resolution, upscale_method):
        _images = []
        _masks = []

        for image in images:
            h, w, c = image.shape
            # h, w, c -> c, h, w
            im_tensor = image.permute(2, 0, 1)

            with torch.no_grad():
                result_image = model(im_tensor,
                                     controlnet_conditioning_scale=strength,
                                     skip_preprocess=resolution == 0,
                                     processing_resolution=resolution,
                                     resample_methodinput=upscale_method,
                                     resample_method_output=upscale_method,
                                     output_type="pt"
                                     ).prediction.cpu()

            # 归一化
            result_image = (result_image.clamp(-1, 1) + 1) / 2
            # b, c, h, w -> b, h, w, c
            result_image = result_image.permute(0, 2, 3, 1)

            _images.append(result_image)

        out_images = torch.cat(_images, dim=0)

        return out_images,


NODE_CLASS_MAPPINGS = {
    "LoadStableDelightModel": LoadStableDelightModel,
    "ApplyStableDelight": ApplyStableDelight,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadStableDelightModel": "LoadStableDelightModel",
    "ApplyStableDelight": "ApplyStableDelight",
}
