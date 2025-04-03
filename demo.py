import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen2.5-vl-7b-instruct",
    messages=[
        {
            "role": "user",
            "content": "请用一段话介绍一下你自己，100字，一个字不能少。",
        }
    ],
)

print(response)

print(response.choices[0].message.content)