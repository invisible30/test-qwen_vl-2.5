# Qwen-VL 2.5 图像描述示例

这是一个使用 **Qwen-VL 2.5** 模型进行图像描述的 Python 示例代码。代码通过 ModelScope 的 API 调用 Qwen-VL 2.5 模型，支持输入图片 URL 并生成对图片内容的描述。

## 项目简介

本项目展示了如何使用 OpenAI 客户端与 ModelScope 的 API 进行交互，调用 Qwen-VL 2.5 模型对图片进行描述。代码支持流式输出，适合处理大图片或需要实时响应的场景。

## 环境要求

- Python 3.7 或更高版本
- `openai` 包
- ModelScope API Token
[ModelScope API获取](https://modelscope.cn/my/myaccesstoken)

## 安装依赖

在运行代码之前，请确保已安装 `openai` 包。可以通过以下命令安装：

```bash
pip install openai
```
---
### 说明：
1. **API Token**：请确保将 `your-modelscope-token` 替换为你的实际 ModelScope API Token。
2. **图片 URL**：示例中使用了 GitHub 的 `raw.githubusercontent.com` 格式 URL，确保图片是公开可访问的。

## 示例
<img src="qwen_vl2.5_try.jpg" alt="results" width="400"/>

输出
```
The picture shows a room with a gaming setup. In the foreground, there is a custom-made arcade-style controller with various buttons and joysticks, featuring artwork of characters from an anime or manga series. The controller is connected to a television screen displaying a basketball video game, likely NBA 2K, as indicated by the 
on-screen graphics and player models.

The room appears to be a living space with a white wall decorated with floral patterns near the ceiling. Below 
the TV, there is a shelf filled with various items, including bottles, containers, and other miscellaneous objects. The overall lighting in the room is dim, with some light coming from the TV screen and the illuminated buttons on the controller. The scene suggests a dedicated gaming area within a home environment.
```

