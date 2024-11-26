[ENGLISH](README_EN.md)

StableDelight 是一种从纹理表面去除镜面反射的尖端解决方案。

注：实测下来，物体变化有点大，特别是半透明的物体，如样例中的灯泡、玻璃。期待原项目的后期改进。

## 预览
![save api extended](example/workflow_base.png)

## 安装

- 手动安装
```shell
    cd custom_nodes
    git clone https://github.com/lldacing/ComfyUI_StableDelight_ll.git
    cd ComfyUI_StableDelight_ll
    # 重启comfyUI
```
    

## 模型
从[HuggingFace](https://huggingface.co/Stable-X/yoso-delight-v0-4-base/tree/main)下载所有文件放到目录`ComfyUI/models/diffusers/Stable-X--yoso-delight-v0-4-base`

建议使用huggingface-cli下载
```
# 设置代理，按需设置，也可开全局代理
set https_proxy=http://127.0.0.1:7890
# 在ComfyUI/models/diffusers/目录下启动命令行执行下面的命令，如果找不到huggingface-cli，huggingface-cli在${python_home}/Scripts目录下，使用全路径
huggingface-cli download Stable-X/yoso-delight-v0-4-base --local-dir Stable-X--yoso-delight-v0-4-base
```
目录结构如下：
```
ComfyUI
  └─models
      └─diffusers
          └─Stable-X--yoso-delight-v0-4-base
```

## 感谢

原项目 [Stable-X/StableDelight](https://github.com/Stable-X/StableDelight)

