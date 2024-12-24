
import gradio as gr
import time
from pathlib import Path 
import requests  
import json
import os
from dotenv import load_dotenv  
import io 
import base64  
import time  
import asyncio 
# 加载.env文件  
load_dotenv("en1.env")  

os.environ["OPENAI_API_TYPE"] = os.environ["Azure_OPENAI_API_TYPE1"]
os.environ["OPENAI_API_BASE"] = os.environ["Azure_OPENAI_API_BASE1"]
os.environ["OPENAI_API_KEY"] = os.environ["Azure_OPENAI_API_KEY1"]
os.environ["OPENAI_API_VERSION"] = os.environ["Azure_OPENAI_API_VERSION1"]
BASE_URL=os.environ["OPENAI_API_BASE"]
API_KEY=os.environ["OPENAI_API_KEY"]
Chat_Deployment=os.environ["Azure_OPENAI_Chat_API_Deployment"]
Whisper_key=os.environ["Azure_Whisper_API_KEY"]
Whisper_endpoint = os.environ["Azure_Whisper_API_Url"]
Azure_speech_key= os.environ["Azure_speech_key"]
Azure_speech_region= os.environ["Azure_speech_region"]
Azure_speech_speaker= os.environ["Azure_speech_speaker"]
os.environ["AZURE_API_KEY"] =API_KEY
os.environ["AZURE_API_BASE"] =BASE_URL
os.environ["AZURE_API_VERSION"] =os.environ["Azure_OPENAI_API_VERSION1"]
import os  
import subprocess  
  
  
def extract_audio(input_file, output_file):  
    # 检查输出文件是否存在，如果存在则删除  
    if os.path.exists(output_file):  
        os.remove(output_file)  
        
    command = [  
        'ffmpeg',  
        '-i', input_file,  
        '-q:a', '0',  
        '-map', 'a',  
        output_file  
    ]  
      
    try:  
        subprocess.run(command, check=True)  
        print(f"音频成功提取并保存为 {output_file}")  
    except subprocess.CalledProcessError as e:  
        print(f"错误：{e}")  

messages = []

prompt_input = ''

messages_text =[{"role":"system","content":"你是解答问题的助手，总是能深入的剖析问题的根本，并给出解决问题的方法。即使不能解决也能提供思路，引导用户挖掘更多信息。"}]
import requests  
import json  
  
def update_video_translation(resource_key, operation_id, display_name, description,   
                             video_source_locale, translation_target_locale,   
                             voice_kind, speaker_count,   
                             subtitle_max_char_count_per_segment,   
                             export_subtitle_in_video,   
                             video_file_url, speech_region, translation_id):  
      
    url = f"https://{speech_region}.api.cognitive.microsoft.com/videotranslation/translations/{translation_id}?api-version=2024-05-20-preview"  
      
    headers = {  
        "Ocp-Apim-Subscription-Key": resource_key,  
        "Operation-Id": operation_id,  
        "Content-Type": "application/json"  
    }  
      
    data = {  
        "displayName": display_name,  
        "description": description,  
        "input": {  
            "sourceLocale": video_source_locale,  
            "targetLocale": translation_target_locale,  
            "voiceKind": voice_kind,  
            "speakerCount": speaker_count,  
            "subtitleMaxCharCountPerSegment": subtitle_max_char_count_per_segment,  
            "exportSubtitleInVideo": export_subtitle_in_video,  
            "videoFileUrl": video_file_url  
        }  
    }  
      
    response = requests.put(url, headers=headers, data=json.dumps(data),verify=False)  
      
    if response.status_code == 201 or response.status_code == 200:  
        print("Translation updated successfully.")  
        return response.json()  
    else:  
        print(f"Failed to update translation. Status code: {response.status_code}")  
        print(f"Response: {response.text}")  
        return None  
  
def update_translation_iteration(resource_key, operation_id, speaker_count,   
                                 subtitle_max_char_count_per_segment,   
                                 export_subtitle_in_video, webvtt_kind,   
                                 webvtt_url, speech_region, translation_id,   
                                 iteration_id):  
      
    url = f"https://{speech_region}.api.cognitive.microsoft.com/videotranslation/translations/{translation_id}/iterations/{iteration_id}?api-version=2024-05-20-preview"  
      
    headers = {  
        "Ocp-Apim-Subscription-Key": resource_key,  
        "Operation-Id": operation_id,  
        "Content-Type": "application/json"  
    }  
      
    data = {  
        "input": {  
            "speakerCount": speaker_count,  
            "subtitleMaxCharCountPerSegment": subtitle_max_char_count_per_segment,  
            "exportSubtitleInVideo": export_subtitle_in_video
            
        }  
    }  
    ''',  
            "webvttFile": {  
                "Kind": webvtt_kind,  
                "url": webvtt_url  
            }  
            '''  
    response = requests.put(url, headers=headers, data=json.dumps(data), verify=False)  
      
    if response.status_code == 201 or response.status_code == 200:  
        print("Translation iteration updated successfully.")  
        return response.json()  
    else:  
        print(f"Failed to update translation iteration. Status code: {response.status_code}")  
        print(f"Response: {response.text}")  
        return None  
        
def get_video_translation_operation(resource_key, operation_id, speech_region):  
    url = f"https://{speech_region}.api.cognitive.microsoft.com/videotranslation/operations/{operation_id}?api-version=2024-05-20-preview"  
      
    headers = {  
        "Ocp-Apim-Subscription-Key": resource_key  
    }  
      
    response = requests.get(url, headers=headers,verify=False)  
      
    if response.status_code == 200:  
        print("Operation details retrieved successfully.")  
        return response.json()  
    else:  
        print(f"Failed to retrieve operation details. Status code: {response.status_code}")  
        print(f"Response: {response.text}")  
        return None 

def get_video_translation_iteration(resource_key, translation_id, iteration_id, speech_region):  
    url = f"https://{speech_region}.api.cognitive.microsoft.com/videotranslation/translations/{translation_id}/iterations/{iteration_id}?api-version=2024-05-20-preview"  
      
    headers = {  
        "Ocp-Apim-Subscription-Key": resource_key  
    }  
      
    response = requests.get(url, headers=headers,verify=False)  
      
    if response.status_code == 200:  
        print("Iteration details retrieved successfully.")  
        return response.json()  
    else:  
        print(f"Failed to retrieve iteration details. Status code: {response.status_code}")  
        print(f"Response: {response.text}")  
        return None  

import random  
  
def generate_random_number():  
    # 生成一个 6 位的随机数  
    random_number = random.randint(100000, 999999)  
    return random_number  
    
# 可选的语言列表  
language_options = {  
    "English": "en-US",  
    "Chinese": "zh-CN",
    "Japanese":"ja-JP",
    "French": "fr-FR",  
    "Spanish": "es-ES",  
    "German": "de-DE"  
}  

myfile=''
def handle_video(audio, source_language, target_language):
    global messages_text,myfile
    print(source_language)
    cont=None
    sourceLc = language_options[source_language]
    targetLc = language_options[target_language]
    if audio is None:
        error_html = """  
    <div style="position: relative; width: 600px;">  
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 24px; background: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px;">  
            Please choose video first!
        </div>  
    </div>  
    """  
        yield error_html
        return error_html
        
    # 返回“正在加载...”的HTML  
    loading_html = """  
    <div style="position: relative; width: 600px;">  
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 24px; background: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px;">  
            Processing...  
        </div>  
    </div>  
    """  
    yield loading_html
    if audio is not None:
        myfile=Path(audio)
        blob_name = os.path.basename(myfile)  
        video_url=uploadVideo()
        

  
        # 示例调用  
        random_number = generate_random_number()  
        operation_id=f"{blob_name}_opr_{random_number}"
        translation_id=f"{blob_name}_tran_{random_number}"
        iteration_id=f"{blob_name}_iter_{random_number}"
        resource_key=os.environ["Azure_translate_key"]
        video_source_locale=sourceLc
        translation_target_locale=targetLc
        speech_region=os.environ["Azure_translate_region"]
        video_file_url=video_url
            
        # 用实际参数调用  
        result = update_video_translation(  
            resource_key=resource_key,  
            operation_id=operation_id,  
            display_name="videotrans001",  
            description="videotrans001des",  
            video_source_locale=video_source_locale,  
            translation_target_locale=translation_target_locale,  
            voice_kind="PlatformVoice",  
            speaker_count=1,  
            subtitle_max_char_count_per_segment=30,  
            export_subtitle_in_video=True,  
            video_file_url=video_file_url,  
            speech_region=speech_region,  
            translation_id=translation_id 
        )    
        
        result = get_video_translation_operation(  
            resource_key=resource_key,  
            operation_id=operation_id,  
            speech_region=speech_region
        )  
        while result["status"]!='Succeeded':
            # 暂停 1 秒钟  
            time.sleep(1) 
            result = get_video_translation_operation(  
                resource_key=resource_key,  
                operation_id=operation_id,  
                speech_region=speech_region
            )
            yield loading_html
            
        result = update_translation_iteration(  
            resource_key=resource_key,  
            operation_id=operation_id+"01",  
            speaker_count=1,  
            subtitle_max_char_count_per_segment=30,  
            export_subtitle_in_video=True,  # 注意这里使用 True 而非 true  
            webvtt_kind="en-US",  # 根据您的需求调整  
            webvtt_url=f"{os.environ['Azure_storage_endpoint']}/video/azure_ai_001.mp4?{os.environ['Azure_storage_sgs']}",  
            speech_region=speech_region,  
            translation_id=translation_id,  
            iteration_id=iteration_id
        )     
        result = get_video_translation_iteration(  
            resource_key=resource_key,  
            translation_id=translation_id,  
            iteration_id=iteration_id,  
            speech_region=speech_region
        )  
        while result["status"]!='Succeeded':
            print(result)
            # 暂停 1 秒钟  
            time.sleep(1) 
            
            result = get_video_translation_iteration(  
                    resource_key=resource_key,  
                    translation_id=translation_id,  
                    iteration_id=iteration_id,  
                    speech_region=speech_region
                )  
            yield loading_html
            
        print(result["result"]["translatedVideoFileUrl"])   
        result = get_video_translation_iteration(  
                resource_key=resource_key,  
                translation_id=translation_id,  
                iteration_id=iteration_id,  
                speech_region=speech_region
            )  
        
        video_url=result["result"]["translatedVideoFileUrl"]
        print(video_url)
        # 使用 HTML 的 <video> 标签来嵌入视频  
    video_html = f"""  
    <video width="600" controls>  
        <source src="{video_url}" type="video/mp4">  
        Your browser does not support the video tag.  
    </video>  
    """  
    yield video_html
    return video_html  
    #return v

def handle_gpt(input):
    if input is None:
        return ""
    completion=chatgpt(messages_text[-20:])
    cont=completion["choices"][0]["message"]["content"]

    #if cont is not None:
    #    speak(cont)
    return cont
    
def handle_conv(cont):
    if cont:
        assistant_msg={"role": "assistant", "content":cont}
        messages_text.append(assistant_msg)
    print(assistant_msg)    
    dialogue_string = ""  
    for message in messages_text: 
        role = message["role"]  
        if role=="system":
            continue
        content = message["content"]
        avatar="🤖"
        if role=="user":
            avatar="👨"
        dialogue_string += f"{avatar} {role}: {content}\n"
    return dialogue_string
    
def whisper(myfile):
    url = Whisper_endpoint
    headers = {'api-key': Whisper_key}  
    files = {  
        "file": open(myfile, "rb")  
    }  

    response = requests.post(url, headers=headers, files=files,verify=False)
    return response


    
def Reset():
    global messages_text
    messages_text =[{"role":"system","content":"你是解答问题的助手。"}]
    return ""
    
def CreateIndex(text):
    global myfile
    video_url = uploadVideo()
    print('create index...')
    blob_name = blob_name = os.path.basename(myfile)   
    b64FileName = convert_to_base64(blob_name)

    return "index done sucessfully!"
    
def uploadVideo():
    global myfile
    print('upload video...')
    from azure.storage.blob import BlobServiceClient  
    import os  
    # Azure Storage Account 信息  
    connection_string = os.environ['Azure_storage_connectionstring']  # 替换为您的连接字符串  
    container_name = "video"          # 替换为您的容器名称  
    file_path =myfile             # 替换为您的本地文件路径  
    blob_name = os.path.basename(file_path)          # 使用文件名作为 Blob 名称  
      
    # 创建 BlobServiceClient 实例  
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)  
      
    # 获取容器客户端  
    container_client = blob_service_client.get_container_client(container_name)  
      
    # 上传文件  
    with open(file_path, "rb") as data:  
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)  
      
    print(f"文件 {file_path} 已成功上传到 Azure Blob 存储中的 {blob_name}")  
    vedio_url = f"{os.environ['Azure_storage_endpoint']}/video/{blob_name}?{os.environ['Azure_storage_sgs']}"
    print(vedio_url)
    return vedio_url

def convert_to_base64(original_string):  
    # 将字符串编码为字节  
    string_bytes = original_string.encode('utf-8')  
      
    # 转换为Base64  
    base64_bytes = base64.b64encode(string_bytes)  
      
    # 将Base64字节转换为字符串  
    base64_string = base64_bytes.decode('utf-8')  
      
    return base64_string  
    
import requests  
  



out_speak=gr.Video(label="⚡ Translated ⚡:",visible=True)

# 创建 Gradio 接口  
with gr.Interface(  
    title="💎Translate Video💎",  
    description="This is demo by 🚩Azure speech🎤Azure Video Translate⚡Azure AI🚀",  
    fn=handle_video,  
    outputs=gr.HTML(),  
    inputs=[gr.Video(sources=["upload"], label="Video Input 🎥"),gr.Dropdown(label="Source", choices=list(language_options.keys())),  gr.Dropdown(label="Target", choices=list(language_options.keys()))  ],  
    live=True,
    allow_flagging="never",
) as demo:  
    btn = gr.Button("🕗 Create Index",visible=False)


if __name__ == "__main__":
    demo.launch(share=True)


