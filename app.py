
# import flask module
from flask import Flask, request, abort
# import linebit module
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from modules.reply import faq, menu

from linebot.models import (
    MessageEvent,
    TextMessage,
    StickerMessage,
    StickerSendMessage,
)


app = Flask(__name__)


CHANNEL_ACCESS_TOKEN = 'ABCDEFG'
CHANNEL_SECRET = '1234567'


line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
@app.route("/", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']


    body = request.get_data(as_text=True)
    print("[app.route]information to X-Line-Signature in validation process")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    print('*'*30)
    print('[User Sends Text Message]')

    user_msg = event.message.text
    if user_msg in faq:
        reply = faq[user_msg]
    else:
        reply = menu
    line_bot_api.reply_message(
        event.reply_token,
        reply)
 
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    print('*'*30)
    print('[User Sends Sticker]')
    print(str(event))

    reply = StickerSendMessage(package_id='2', sticker_id='149')

    line_bot_api.reply_message(
        event.reply_token,
        reply)


import os
if __name__ == "__main__":
    print('[Server starts working]')

    port = int(os.environ.get('PORT', 5500))

    print(f'[Flask connect to the port:{port}]')

    app.run(host='127.0.0.1', port=port, debug=True)
