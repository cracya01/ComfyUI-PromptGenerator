import os
import json
import requests
import re
from typing import Dict, Any

class CracyaOpenAIAPIConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "api_key": ("STRING", {"default": "", "placeholder": "输入你的 OpenAI API Key"}),
                "api_base": ("STRING", {"default": "https://api.openai.com/v1", "placeholder": "API 基础 URL"}),
                "model": ("STRING", {"default": "gpt-3.5-turbo", "placeholder": "模型名称"}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0, "step": 0.1}),
                "max_tokens": ("INT", {"default": 2000, "min": 50, "max": 4000, "step": 50}),
            }
        }

    RETURN_TYPES = ("OPENAI_CONFIG",)
    RETURN_NAMES = ("api_config",)
    FUNCTION = "configure"
    CATEGORY = "提示词生成"
    DESCRIPTION = "配置 OpenAI API 参数"

    def configure(self, api_key, api_base, model, temperature, max_tokens):
        if not api_key:
            print("警告: 未提供 API Key")
        
        config = {
            "api_key": api_key,
            "api_base": api_base,
            "model": model,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        return (config,)

class CracyaPromptGenerator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "system_prompt": ("STRING", {"multiline": True, "default": "你作为世界顶尖的视觉艺术家、顶尖摄影师和AIGC提示词专家，你需要充分发挥想象力，为我写出精彩绝伦的AI绘画或者AI视频提示词，我给了你参考词，你先充分思考后再写提示词，我只需要你提供一整段英文提示词，不要提供多余的内容。", "placeholder": "输入系统提示"}),
                "prompt": ("STRING", {"multiline": True, "default": "生成一个美丽的风景图像", "placeholder": "输入你想要生成的图像/视频描述"}),
                "api_config": ("OPENAI_CONFIG", ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated_text",)
    FUNCTION = "generate_text"
    CATEGORY = "提示词生成"
    DESCRIPTION = "使用 OpenAI API 生成提示词"

    def generate_text(self, system_prompt, prompt, api_config):
        api_key = api_config.get("api_key", "")
        api_base = api_config.get("api_base", "https://api.openai.com/v1")
        model = api_config.get("model", "gpt-3.5-turbo")
        temperature = api_config.get("temperature", 0.7)
        max_tokens = api_config.get("max_tokens", 2000)
        
        if not api_key:
            return ("请提供 OpenAI API Key",)
        
        # 调用 OpenAI API
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            # 修复 URL 构建，确保不会重复路径段
            endpoint = api_base.rstrip('/')
            if endpoint.endswith('/chat/completions'):
                api_url = endpoint
            else:
                api_url = f"{endpoint}/chat/completions"
                
            print(f"调用 API URL: {api_url}")  # 调试信息
            
            response = requests.post(api_url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            content = result["choices"][0]["message"]["content"].strip()
            return (content,)
        except Exception as e:
            error_msg = f"API 调用错误: {str(e)}"
            print(error_msg)  # 打印详细错误信息到控制台
            return (error_msg,)

class CracyaRegexFilter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),  # 使用空字典作为第二个参数
                "pattern": ("STRING", {"default": "^[\\s\\S]*</think>\\s*", "placeholder": "输入正则表达式模式"}),
            },
            "optional": {
                "mode": (["RegEx", "Strict"], {"default": "RegEx"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filtered_text",)
    FUNCTION = "filter_text"
    CATEGORY = "提示词生成"
    DESCRIPTION = "使用正则表达式过滤文本"

    def filter_text(self, text, pattern, mode="RegEx"):
        if mode == "RegEx":
            try:
                filtered = re.sub(pattern, '', text, flags=re.DOTALL)
                return (filtered,)
            except Exception as e:
                print(f"正则表达式错误: {str(e)}")
                return (f"正则表达式错误: {str(e)}",)
        elif mode == "Strict":
            # Strict 模式下，只有完全匹配的部分会被替换
            try:
                filtered = re.sub(pattern, '', text)
                return (filtered,)
            except Exception as e:
                print(f"正则表达式错误: {str(e)}")
                return (f"正则表达式错误: {str(e)}",)
        else:
            return (text,)



# 节点列表
NODE_CLASS_MAPPINGS = {
    "cracyaOpenAIAPIConfig": CracyaOpenAIAPIConfig,
    "cracyaPromptGenerator": CracyaPromptGenerator,
    "cracyaRegexFilter": CracyaRegexFilter,
}

# 节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "cracyaOpenAIAPIConfig": "cracya OpenAI API 配置",
    "cracyaPromptGenerator": "cracya 提示词生成器",
    "cracyaRegexFilter": "cracya 正则过滤器",
}