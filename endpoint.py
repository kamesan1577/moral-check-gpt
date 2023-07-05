import openai

#ModerationAPIの呼び出し
def get_moderation(msg):
    with open("key.secret", "r") as f:
        openai.api_key = f.read().strip()
    openai.api_base = "https://api.openai.iniad.org/api/v1"

    msg = msg
    response = openai.Moderation.create(input=msg)
    return (msg,response["results"][0])

#英語に翻訳してから呼び出すバージョン
def get_moderation_after_translate(msg):
    #普通にChatGPTに翻訳させる
    msg_translated = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user", "content":f"Translate this message to English(return only translation result): {msg}"},
            ],
    )["choices"][0]["message"]["content"]

    return get_moderation(msg_translated)
