from linebot.models import (
    TextSendMessage, ImageSendMessage, LocationSendMessage, TemplateSendMessage, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

faq = {
    'Splendid View': ImageSendMessage(
        original_content_url='https://c4.wallpaperflare.com/wallpaper/688/7/649/beautiful-halong-bay-vietnam-wallpaper-preview.jpg',
        preview_image_url='https://c4.wallpaperflare.com/wallpaper/688/7/649/beautiful-halong-bay-vietnam-wallpaper-preview.jpg'
    ),
    'Standard Hill View': ImageSendMessage(
        original_content_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2019/10/28081930/Standard-Hill-View_Twin-Beds-4.jpg',
        preview_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2019/10/28081930/Standard-Hill-View_Twin-Beds-4.jpg'
    ),
    'Superior Bay View': ImageSendMessage(
        original_content_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2019/10/28090504/1P4A2232-2.jpg',
        preview_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2019/10/28090504/1P4A2232-2.jpg'
    ),
    'Executive Bay View': ImageSendMessage(
        original_content_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2019/10/28093645/b-1.jpg',
        preview_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2019/10/28093645/b-1.jpg'
    ),
    'The Square': ImageSendMessage(
        original_content_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Restaurants_Bars-Section-1st-Restaurant-Detail-The-Square-restaurant.jpg',
        preview_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Restaurants_Bars-Section-1st-Restaurant-Detail-The-Square-restaurant.jpg'
    ),
    'Lobby Lounge Bar': ImageSendMessage(
        original_content_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Bars-Outlet-Section-1st-Outlet-Detail-Lobby-Lounge-Bar.jpg',
        preview_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Bars-Outlet-Section-1st-Outlet-Detail-Lobby-Lounge-Bar.jpg'
    ),
    'Poolside Bar': ImageSendMessage(
        original_content_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Bars-Outlet-Section-2nd-Outlet-Detail-Pool-Bar.jpg',
        preview_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Bars-Outlet-Section-2nd-Outlet-Detail-Pool-Bar.jpg'
    ),
    'Getting to Halong Bay!': TextSendMessage(text='All Transporation Options Available to You!',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="Train", text="Train")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="Public Bus", text="Public Bus")
                              )
                          ])
                          ),
    'Train': TextSendMessage(
        text="Recently the railway between Hanoi and Halong Bay reopened allowing tourists to take the train to Halong Bay. You can expect a ticket to be a bit less than 80.000 VND (4 USD). Information as follows: https://vietnamrailwaycorp.com/?gclid=Cj0KCQjw2_OWBhDqARIsAAUNTTGwtX_F5OqwxgKHYM2beGTAz6_wzLCx_wLM6uRPCM55I9nDwbwMd34aAqeGEALw_wcB"
    ),
    'Public Bus': TextSendMessage(
        text="One of the cheapest and most convenient ways to get from Hanoi to Halong bay is by public buses through the Hanoi-Hai Phong highway. These buses take about 2-2.5 hours and cost about 230,000 VND (~ 10 USD). Information as follows: https://rail.cc/hanoi/my-dinh-hanoi-bus-station/l6631"
    ),

    'Address': LocationSendMessage(
        title='Novotel Ha Long Bay',
        address='160 Ha Long Road, Bai Chay Ward Ha Long City, Quang Ninh, Vietnam Ha Long City, 200000, Vietnam',
        latitude=20.95210,
        longitude=107.04205
    ),
    'Service': TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2019/10/28082147/Untitled.jpg',
                    title='Rooms',
                    text='Click The Button Below Now',
                    actions=[
                        MessageAction(
                            label='Standard Hill View',
                            text='Standard Hill View'
                        ),
                        MessageAction(
                            label='Superior Bay View',
                            text='Superior Bay View'
                        ),
                        MessageAction(
                            label='Executive Bay View',
                            text='Executive Bay View'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Restaurants_Bars-Section-1st-Restaurant-Detail-The-Square-restaurant.jpg',
                    title='Restaurants & Bars',
                    text='Click The Button Below Now',
                    actions=[
                        MessageAction(
                            label='The Square',
                            text='The Square'
                        ),
                        MessageAction(
                            label='Lobby Lounge Bar',
                            text='Lobby Lounge Bar'
                        ),
                        MessageAction(
                            label='Poolside Bar',
                            text='Poolside Bar'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Home-Section-Background-Facade-.jpg',
                    title='Book',
                    text='Click The Button Below Now',
                    actions=[
                        URIAction(
                            label='Official Website',
                            uri='https://www.youtube.com/watch?v=fAS29vl-RPY'
                        ),
                        URIAction(
                            label='Book a Room',
                            uri='https://novotelhalongbay.com/rooms/'
                        ),
                        URIAction(
                            label='Youtube',
                            uri='https://www.youtube.com/channel/UCqM7VC8Fuc7ryrWBoh5A8JQ'
                        )
                    ]
                )
            ]
        )
    )
}

menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://c4.wallpaperflare.com/wallpaper/870/346/374/vietnam-halong-bay-0543681-wallpaper-preview.jpg',
                title='Hạ Long Bay',
                text='Click The Button Below Now',
                actions=[
                    MessageAction(
                        label='Transporation',
                        text='Getting to Halong Bay!'
                    ),
                    MessageAction(
                        label='Image',
                        text='Splendid View'
                    ),
                    URIAction(
                        label='Video Tour',
                        uri='https://www.youtube.com/watch?v=fAS29vl-RPY'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/81/2016/12/02071700/Rooms-_-Suites-Section-Rooms.jpg',
                title='Novotel Ha Long Bay',
                text='Click The Button Below Now',
                actions=[
                    MessageAction(
                        label='Service',
                        text='Service'
                    ),
                    URIAction(
                        label='Contact Us',
                        uri='https://novotelhalongbay.com/the-hotel/contact-us/'
                    ),
                    MessageAction(
                        label='Address',
                        text='Address'
                    )
                ]
            )
        ]
    )
)
