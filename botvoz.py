import telebot
from gtts import gTTS

chave_API = 'TOKEN dado pelo suporte de BOT do Telegram'
bot = telebot.TeleBot(chave_API)


@bot.message_handler(commands=["voz"])
def voz(mensagem):
    bot.send_message(mensagem.chat.id, f' {mensagem.chat.first_name},\n'
                                       f'Infome o texto que você quer que seja lida.')
    bot.register_next_step_handler(mensagem, falando)


def falando(mensagem):
    # aguardando mensagem
    resposta = (mensagem.text)
    voz = gTTS(resposta, lang='pt-br')
    voz.save(f'{mensagem.chat.id}.mp3')
    bot.send_voice(chat_id=mensagem.chat.id, voice=open(f'{mensagem.chat.id}.mp3', 'rb'))
    bot.send_message(mensagem.chat.id, 'Lerei o texto informado\n'
                                       'Após isso, volte ao inicio: /Inicio.\n'
                                       'Muito Obrigado por testar esse BOT\n'
                                       f'{mensagem.chat.first_name}, você me ajudou muito.')


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    text = '''
    Olá, tudo bem? Vamos testar a voz? (Clique na opção desejavel)
        /voz = Ouvir o texto informado
    Obrigado pela compreenção[...]
    '''
    bot.reply_to(mensagem, text)
bot.polling()
