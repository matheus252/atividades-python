import openai

def jarvis (pergunta):
    resposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role':'system', 'content':'você é um assitente inteligente chamado JARVIS.'},
        {'role': 'user',' content': pergunta}])
    return resposta['choices'][0]['message']['content']

while True:
        pergunta= input("você: ")
        if pergunta.lower() == 'sair':
             break
        reposta = jarvis(pergunta)
        print(f'jarvis:{reposta}')