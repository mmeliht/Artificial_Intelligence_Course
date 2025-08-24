import ollama
res=ollama.chat(model='llama3.2-vision:11b',
                messages=[
                    {'role':'user',
                     'content':'Bana kuantum bilgisayarlar hakkinda 1 paragraflik bilgi ver'
                     
                     }
                    
                ])
print(res['message']['content'])