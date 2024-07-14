# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import authorized_users_only
from VCPlayBot.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from VCPlayBot.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Hoş Geldiniz, Saygılarımla 🥰 {query.message.from_user.mention}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ➻ Hızlı & Muhteşem Özelliklere Sahip En İyi Telegram Müzik Botu!**

💡 **๏ YARDIM & KOMUTLAR BUTONU İLE BOT HAKKINDA YARDIM ALABİLİRSİNİZ » 📚 𝚈𝚊𝚛𝚍ı𝚖° & 𝙺𝚘𝚖𝚞𝚝𝚕𝚊𝚛° !**

❓ **YARDIM MENÜSÜNÜ PM'DE BAŞLATIN /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ 𝙱𝚎𝚗𝚒 𝙶𝚛𝚞𝚋𝚞𝚗𝚊 𝙴𝚔𝚕𝚎° ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❓ 𝚈𝚊𝚛𝚍ı𝚖°", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 𝙺𝚘𝚖𝚞𝚝𝚕𝚊𝚛°", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 𝐒𝐀𝐇𝐈̇𝐏°", url=f"https://t.me/AdanaliMuhendis")
                ],[
                    InlineKeyboardButton(
                        "👥 𝐀𝐋𝐄𝐌°", url=f"https://t.me/SohbetAlemi"
                    ),
                    InlineKeyboardButton(
                        "📣 𝓐𝓵𝓮𝓶𝓬𝓲𝔂𝓲𝔃°", url=f"https://t.me/Alemciyiz")
                ],[
                    InlineKeyboardButton(
                        "🧪 𝓒𝓮𝓭𝓻𝓲𝓬° 🧪", url="https://t.me/ByCedric"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Merhaba, Yardım Menüsüne Hoş Geldiniz !</b>

**Bu menüde mevcut çeşitli komut menülerini açabilirsiniz. Her komut menüsünde ayrıca her komutun kısa bir açıklaması vardır.**

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Temel Kmt", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Gelişmiş Kmt", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Yönetici Kmt, callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Yetkili Kmt", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Sahip Kmt", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Eğlence Kmt", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Temel Komutlar Burada</b>

🎧 [ GROUP SESLİ KMT ]

- /play, /oynat (Parça İsmi) - İstenilen parçayı görüntülü sohbette yayınlamaya başlar
- /ytpplay (Parça İsmi) - İstenilen parçayı youtube üzerinden sohbette yayınlamaya başlar 
- /playlist - Parça listesini gösterir
- /song (Parça İsmi) - Parça indirir Youtube üzerinden
- /search (video İsmi) - Youtube üzerinden video bulur
- /video (video İsmi) - Youtube üzerinden video indirir
- /lyrics - (Parça İsmi) Şarkı sözleri oluşturur

🎧 [ KANAL SESLİ KMT ]

- /cplay - İstenilen parçayı görüntülü sohbette yayınlamaya başlar
- /cplayer - Yayınlanan parça ayrıntılarını gösterir
- /cpause - Mevcut oynatma akışını duraklatır
- /cresume - Duraklatılan akışı devam ettirir
- /cskip - Mevcut oynatma akışını atla ve sıradaki parçayı oynatmaya başlar
- /cend - Listeyi temizler ve mevcut oynatma akışını sonlandırır
- /admincache - Yönetici listesini yeniler
- /userbotjoin: @{ASSISTANT_NAME} Asistanı Gruba Davet Eder

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Gelişmiş Komutlar Burada</b>

/start (Grup İçerisinde) - Botun Aktifliği Kontrol Edilir
/reload - Botlar ve Yönetici Listesi Yenilenir
/admincache - Yönetici Listesi Yenilenir
/ping - Bot Ping İstatistikleri Getirilir
/uptime - Kullanım süresi kontrol edilir

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Yönetici Komutları Burada</b>

/player - Parça ayrıtıları gösterilir
/pause, /dur - Mevcut oynatma akışını duraklatır
/resume, /devam - Duraklatılan akışı devam ettirir
/skip, /atla, /lehaaa - Mevcut oynatma akışını atlar
/end, /son - Listeyi temizler ve mevcut oynatma akışını sonlandırır
/userbotjoin - Asistanı gruba davet eder
/auth - Bot üzerinde kullanıcı yetkilendirilir
/deauth - Bot üzerinde kullanıcı yetkisi silinir
/control - Müzik Botu ayarları
/delcmd (on | off) - Gelişmiş Komutları Aç-Kapa
/musicplayer (on / off) - Müzik Çalar Aç-Kapa
/b and /tb (ban / temporary ban) - Grup içerisinde kullanıcıyı banlar
/ub - Grup içerisinde kullanıcı banı açılır
/m and /tm (mute / temporary mute) - Grup içerisinde kullanıcıyı sessize alır
/um - Grup içerisinde sessize alınan kullanıcı tekrar konuşabilir

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Yetkili Kullanıcı Komutları Burada</b>

/userbotleaveall - Asistan bütün gruplardan çıkış yapar
/gcast - Asistan üzerinden mesaj yayınlar
/stats - Bot istatistiklerini gösterir
/rmd - İndirme dosyaları silinir
/clean - Ön bellek temizlenir

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Sahip Komutları Burada</b>

/stats - Bot istatistiklerini gösterir
/broadcast - Bot üzerinden mesaj yayınlar
/block (user id - duration - reason) - Kullanıcı bottan banlanır
/unblock (user id - reason) - Kullanıcı banı açılır
/blocklist - Bot üzerinden banlananların listesini gösterir

📝 Not: Bu botun sahip olduğu tüm komutlar, istisnasız olarak botun sahibi tarafından değiştirilebilir...

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Eğlence Komutları Burada</b>

/chika - Kendinizi Kontrol Ediniz
/wibu - Kendinizi Kontrol Ediniz
/asupan - Kendinizi Kontrol Ediniz
/truth - Kendinizi Kontrol Ediniz
/dare - Kendinizi Kontrol Ediniz

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ BU BOT NASIL KULLANILIR:

1.) Öncelikle beni grubunuza ekleyin.
2.) Daha sonra beni yönetici olarak tanıtın ve anonim yönetici dışındaki tüm izinleri verin.
3.) @{ASSISTANT_NAME} Grubunuza ekleyin veya onu davet etmek için /userbotjoin yazın.
4.) Müzik çalmaya başlamadan önce sesli sohbeti açın.

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 𝙺𝚘𝚖𝚞𝚝𝚕𝚊𝚛°", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 𝐊𝐀𝐏𝐀𝐓°", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 Botun kontrol menüsü burada :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ dur", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ devam", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ atla", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ son", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ anti kmt", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 grup araçları", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 𝐊𝐀𝐏𝐀𝐓°", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Gelişmiş Özellik Bilgisi :</b>

💡 **Özellik:** Bu özellik, grubunuzdaki kullanıcıları yasaklayabilen, sessize alabilen, yasağını kaldırabilen ve sesini açabilen işlevler içerir.

Ayrıca grubunuzdaki üyelerin yasaklama ve susturma cezaları için bir süre belirleyerek belirlenen süre içerisinde cezadan kurtulmalarını sağlayabilirsiniz.

❔ **Kullanım:**

1️⃣ Kullanıcıyı grubunuzdan yasaklayın yada geçici olarak yasaklayın:
   » `/b kullanıcı adı/mesajı yanıtla` kalıcı olarak yasaklayın
   » `/tb kullanıcı adı/mesajı yanıtla/süre' kullanıcıyı geçici olarak yasakla
   » `/ub kullanıcı adı/mesajı yanıtla` Kullanıcının yasağını kaldırır

2️⃣ Grubunuzdaki kullanıcıyı sessize alın veya geçici olarak sessize alın:
   » '/m kullanıcı adı/mesajı yanıtla' kalıcı olarak sessize alın
   » `/tm kullanıcı adı/mesajı yanıtla/süre' kullanıcıyı geçici olarak sessize alın
   » `/um kullanıcı adı/mesajı yanıtla' Kullanıcının sesini açar

📝 Not: cmd /b, /tb ve /ub, grubunuzdaki kullanıcıyı yasaklayan/yasağı kaldıran işlevdir; /m, /tm ve /um ise grubunuzdaki kullanıcının sesini kapatmaya/sesi açmaya yönelik komutlardır.

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Gelişmiş Özellik Bilgisi :</b>
        
**💡 Özellik:** Gruplarda spam'ı önlemek için kullanıcılar tarafından gönderilen tüm komutları silin!

❔ Kullanım:**

 1️⃣ Özelliği açmak için:
     » `/delcmd on`
    
 2️⃣ Özelliği kapatmak için:
     » `/delcmd off`
      
⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Temel Kmt", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Gelişmiş Kmt", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Yönetici Kmt", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Yetkili Kmt", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Sahip Kmt", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Eğlence Kmt", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ BU BOT NASIL KULLANILIR:

1.) Öncelikle beni grubunuza ekleyin.
2.) Daha sonra beni yönetici olarak tanıtın ve anonim yönetici dışındaki tüm izinleri verin.
3.) @{ASSISTANT_NAME} Grubunuza ekleyin veya onu davet etmek için /userbotjoin yazın.
4.) Müzik çalmaya başlamadan önce sesli sohbeti açın.

⚡ __ {BOT_NAME} Tarafından desteklenmektedir__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐆𝐄𝐑𝐢°", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
