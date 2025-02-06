from openai import OpenAI
client = OpenAI(    
    api_key="", # ModelScope Token    
    base_url="https://api-inference.modelscope.cn/v1"
)

response = client.chat.completions.create(    
    model="Qwen/Qwen2.5-VL-72B-Instruct", # ModleScope Model-Id 
    messages = [      
        {  
            "role": "user",      
            "content": [    
                {
                    "type": "image_url",
                    # "image_url": {"url": "https://modelscope.oss-cn-beijing.aliyuncs.com/demo/images/bird-vl.jpg"}   
                    "image_url": {"url": "https://raw.githubusercontent.com/invisible30/test-qwen_vl-2.5/main/qwen_vl2.5_try.jpg"} 
                    # 在github网页上直接复制过来的网址是https://github.com/invisible30/test-qwen_vl-2.5/blob/main/qwen_vl2.5_try.jpg
                    # 需要改成代码中的形式  
                }, 
                {   "type": "text",    
                    # "text": "Count the number of birds in the figure, including those that are only showing their heads. To ensure accuracy, first detect their key points, then give the total number."                
                    "text": "Describe this picture"                
                },      
            ], 
        } 
    ], 
    stream=True 
    )

for chunk in response:   
    print(chunk.choices[0].delta.content, end='', flush=True)

"""
The picture shows a room with a gaming setup. In the foreground, there is a custom-made arcade-style controller with various buttons and joysticks, featuring artwork of characters from an anime or manga series. The controller is connected to a television screen displaying a basketball video game, likely NBA 2K, as indicated by the 
on-screen graphics and player models.

The room appears to be a living space with a white wall decorated with floral patterns near the ceiling. Below 
the TV, there is a shelf filled with various items, including bottles, containers, and other miscellaneous objects. The overall lighting in the room is dim, with some light coming from the TV screen and the illuminated buttons on the controller. The scene suggests a dedicated gaming area within a home environment.
"""