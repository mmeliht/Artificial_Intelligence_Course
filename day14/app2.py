import ollama
res=ollama.chat(model='llama3.2-vision:11b',
                messages=[
                    {'role':'user',
                     'content':'Extract the exact text as it appears on this image, nothing less nothing more',
                     'images':['typewritten.png']
                     }
                    
                ])
print(res['message']['content'])