[English](README_EN.md)

StableDelight is a cutting-edge solution for specular reflection removal from textured surfaces.

Note: According to my tests, the objects will change a lot, especially semi transparent objects such as light bulbs and glass in the sample. Looking forward to future improvements.

## Preview
![save api extended](example/workflow_base.png)

## Install

- Manual
```shell
    cd custom_nodes
    git clone https://github.com/lldacing/ComfyUI_StableDelight_ll.git
    cd ComfyUI_StableDelight_ll
    # restart ComfyUI
```
    

## Model
From [HuggingFace](https://huggingface.co/Stable-X/yoso-delight-v0-4-base/tree/main) download all files to `ComfyUI/models/diffusers/Stable-X--yoso-delight-v0-4-base` directory.

Suggest using huggingface-cli to download
```
# Start the command line in the ComfyUI/models/diffusers directory and execute the following command
huggingface-cli download Stable-X/yoso-delight-v0-4-base --local-dir Stable-X--yoso-delight-v0-4-base
```
目录结构如下：
```
ComfyUI
  └─models
      └─diffusers
          └─Stable-X--yoso-delight-v0-4-base
```


## Thanks

Original Project [Stable-X/StableDelight](https://github.com/Stable-X/StableDelight)


