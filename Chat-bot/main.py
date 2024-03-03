import telebot
from telebot import types


bot = telebot.TeleBot('6692662161:AAFO43MklaENKhglMu7ptViXP_7QQu_zI80')


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Привіт, я твій помічник з хімії! Обери що тобі цікаво:")
    bot.send_message(message.chat.id, "/element - Все про хімічні елементи")
    bot.send_message(message.chat.id, "/test - Зіграй в хімічний тест")
    bot.send_message(message.chat.id, "/facts - Дізнайся про нові факти з хімії")


@bot.message_handler(commands=["element"])
def element(message):
    bot.send_message(message.chat.id, "Введіть хімічний елемент(символ):")


@bot.message_handler(commands=["test"])
def test(message):
    bot.send_message(message.chat.id, "Оберіть ваш клас:")


@bot.message_handler(commands=["facts"])
def facts(message):
    bot.send_message(message.chat.id, "Виберіть число від 1 до 40:")


@bot.message_handler()
def tabl(message):
    if message.text.lower() == "h":
        bot.send_message(message.chat.id, "Гідроген (H) — хімічний елемент з атомним номером 1, який належить до 1-ї групи (за старою класифікацією — головної підгрупи 1-ї групи), 1-го періоду періодичної системи хімічних елементів, та є першим і найпростішим представником усіх хімічних елементів взагалі. Найбільш розповсюджений елемент Всесвіту. Належить до неметалів.")
    elif message.text.lower() == "he":
        bot.send_message(message.chat.id, "Гелій (He) — хімічний елемент з атомним номером 2, який належить до 18-ї групи (за старою класифікацією — головної підгрупи 8-ї групи), 1-го періоду періодичної системи хімічних елементів, та є першим представником благородних газів.")
    elif message.text.lower() == "li":
        bot.send_message(message.chat.id, "Літій (Li) — хімічний елемент з атомним номером 3, який належить до 1-ї групи (за старою класифікацією — головної підгрупи I групи), 2-го періоду періодичної системи хімічних елементів, та є першим представником лужних металів.")
    elif message.text.lower() == "be":
        bot.send_message(message.chat.id, "Берилій (Be) — хімічний елемент з атомним номером 4, який належить до 2-ї групи (за старою класифікацією — головної підгрупи II групи), 2-го періоду періодичної системи хімічних елементів, та є першим представником лужноземельних металів.")
    elif message.text.lower() == "b":
        bot.send_message(message.chat.id, "Бор (B) — хімічний елемент з атомним номером 5, який належить до 13-ї групи (за старою класифікацією — головної підгрупи III групи) 2-го періоду періодичної системи хімічних елементів та є першим представником напівметалів.")
    elif message.text.lower() == "c":
        bot.send_message(message.chat.id, "Вуглець (C) — хімічний елемент з атомним номером 6, що належить до 4-ї групи, 2-го періоду періодичної системи хімічних елементів; представник поліатомних неметалів.")
    elif message.text.lower() == "n":
        bot.send_message(message.chat.id, "Азот (N) — хімічний елемент з атомним номером 7, що належить до 15-ї групи, 2-го періоду періодичної системи хімічних елементів; представник неметалів.")
    elif message.text.lower() == "o":
        bot.send_message(message.chat.id, "Кисень(Оксиген) (O) — хімічний елемент з атомним номером 8, що належить до головної підгрупи (або підгрупи кисню) VI групи періодичної системи елементів (16-ї групи за номенклатурою IUPAC), 2-го періоду. Його простими речовинами є гази кисень (O2)та озон (O3) Примітка. В українській мові протягом 1994 — 2019 рр., в рамках реформи хімічної термінології, діяв стандарт ДСТУ 2439-94, згідно з яким хімічний елемент мав назву «Оксиген». З 2019 року назву «Оксиген» скасовано, рекомендовано «кисень» як єдину назву хімічного елемента і найпоширенішої його простої речовини, але дозволено для елемента назву «оксиґен».")
    elif message.text.lower() == "f":
        bot.send_message(message.chat.id, "Фтор (F) — хімічний елемент з атомним номером 9, галоген, що належить до 7-ї групи, 2-го періоду періодичної системи хімічних елементів. Так само назву фтор має відповідна проста речовина, яка є отруйним і хімічно-активним жовто-зеленим газом.")
    elif message.text.lower() == "ne":
        bot.send_message(message.chat.id, "Неон (Ne) — хімічний елемент вісімнадцятої групи другого періоду періодичної системи хімічних елементів із атомним номером 10. П'ятий за поширеністю елемент у Всесвіті після водню, гелію, кисню і вуглецю. Його проста речовина — неон — прозорий одноатомний інертний газ без кольору і запаху. Для неону характерне червоне світіння при електричному розряді, чим зумовлене його використання в рекламі.")
    elif message.text.lower() == "na":
        bot.send_message(message.chat.id, "Натрій (Na) — хімічний елемент з атомним номером 11 та відповідна проста речовина — лужний сріблясто-білий м'який метал, хімічно дуже активний, на повітрі швидко окиснюється. Густина 0,968; tплав 97,83 °С; tкип 882,9 °С; коефіцієнт твердості за Моосом 0,5.")
    elif message.text.lower() == "mg":
        bot.send_message(message.chat.id, "Магній (Mg) — хімічний елемент.Атомний номер — 12; атомна маса — 24,312. Відкритий англійським хіміком Гемфрі Деві у 1808 році")
    elif message.text.lower() == "al":
        bot.send_message(message.chat.id, "Алюмі́ній (Al)— хімічний елемент 3 групи періодичної системи, його атомний номер 13, відносна атомна маса 26,9815. В природі існує єдиний стабільний ізотоп 27Al. Третій за вмістом елемент (і найпоширеніший метал) земної кори (після кисню і кремнію), що становить приблизно 8% від її маси.")
    elif message.text.lower() == "si":
        bot.send_message(message.chat.id, "Кремній (Si) — хімічний елемент з атомним номером 14, що належить до 4-ї групи, 3-го періоду періодичної системи хімічних елементів.Проста речовина — кре́мній, утворює темно-сірі зі смолистим блиском крихкі кристали з гранецентрованою кубічною ґраткою типу алмазу.")
    elif message.text.lower() == "p":
        bot.send_message(message.chat.id, "Фосфор (P) — хімічний елемент 15-ї групи (згідно із застарілою класифікацією — головної підгрупи п'ятої групи) третього періоду періодичної системи хімічних елементів; неметал; атомний номер 15. Атомна маса 30,97376. Один з найпоширеніших елементів земної кори: 0,08-0,09% її маси. У вільному стані не зустрічається через високу хімічну активність. У природі відомий один стабільний ізотоп — 31Р. Відомі оксиди фосфору P2O5, P2O3, пероксид P2O6, карбід РС3. Утворює близько 190 мінералів, найважливішими з яких є апатит Ca5(PO4)3(F, Cl, OH), фосфорит та інші. Фосфор міститься у всіх частинах зелених рослин, ще більше його в плодах і насінні (див. фосфоліпіди). Міститься в тканинах тварин, входить до складу білків та інших найважливіших органічних сполук (аденозинтрифосфат (АТФ), дезоксирибонуклеїнова кислота (ДНК)), є біогенним елементом.")
    elif message.text.lower() == "s":
        bot.send_message(message.chat.id, "Сірка (S) — хімічний елемент з атомним номером 16, що належить до 16-ї групи, 3-го періоду періодичної системи хімічних елементів.Проста речовина — сі́рка, неметал, жовта кристалічна речовина. Трапляється в природі в самородному стані та у вигляді сульфідів важких металів, піриту та інших. Сірку застосовують переважно у хімічній промисловості для виробництва сірчаної кислоти, синтетичного волокна, сірчистих барвників, димного пороху, у гумовій промисловості, також у сільському господарстві, фармацевтиці тощо.")
    elif message.text.lower() == "cl":
        bot.send_message(message.chat.id, "Хлор (Cl) — елемент 7-ї групи періодичної таблиці хімічних елементів (за застарілою класифікацією — елемент головної підгрупи VII групи) з атомним номером 17.Позначається символом Cl (лат. Chlorum). Хімічно активний неметал. У природі існує два стабільних ізотопи: 35Cl i 37Cl. Науковцям вдалось синтезувати нестабільні ізотопи хлору, зокрема, з атомною масою 52Входить у групу галогенів (спочатку назву «галоген» використовував німецький хімік Швейгер для хлору [дослівно «галоген» перекладається як солерід], але воно не прижилося, і згодом стало загальним для VII групи елементів, у яку входить і хлор.")
    elif message.text.lower() == "ar":
        bot.send_message(message.chat.id, "Аргон (Ar) — хімічний елемент з атомним номером 18, а також його проста речовина, інертний газ, без кольору і запаху. Вважається, що він не вступає в реакції з іншими елементами, проте недавно встановлено, що він може з'єднуватися з фторидом бору. Міститься в атмосфері Землі (1 %).")
    elif message.text.lower() == "k":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "ca":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "sc":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "ti":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "v":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "cr":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "mn":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "fe":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "co":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "ni":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, "")
    elif message.text.lower() == "1":
        bot.send_message(message.chat.id, "Для забезпечення польоту середнього пасажирського літака потрібно до 80 тонн кисню. Таку кількість кисню виробляє 40 000 гектарів лісу.")
    elif message.text.lower() == "2":
        bot.send_message(message.chat.id, "З 1 тонни морської води можна отримати 7 мг золота.")
    elif message.text.lower() == "3":
        bot.send_message(message.chat.id, "Серед усіх відомих матеріалів граніт вважається найкращим провідником звуку.")
    elif message.text.lower() == "4":
        bot.send_message(message.chat.id, "Цікавий факт, що мильна бульбашка лопається всього за 0,001 секунди.")
    elif message.text.lower() == "5":
        bot.send_message(message.chat.id, "В одному літрі морської води міститься приблизно 20 г солі.")
    elif message.text.lower() == "6":
        bot.send_message(message.chat.id, "Найбільш рідкісним хімічним елементом в атмосфері є радон.")
    elif message.text.lower() == "7":
        bot.send_message(message.chat.id, "Згідно розрахункам учених, за останні 5 століть маса Землі збільшилася приблизно на 1 млрд тонн.")
    elif message.text.lower() == "8":
        bot.send_message(message.chat.id, "Залізо переходить у газоподібний стан при температурі 5000 ⁰С.")
    elif message.text.lower() == "9":
        bot.send_message(message.chat.id, "Якщо 100 млн атомів водню скласти в одну лінію, то вона буде становити 1 див.")
    elif message.text.lower() == "10":
        bot.send_message(message.chat.id, "Чи знаєте ви, що за 1 хвилину Сонце виділяє таку кількість енергії, якої б вистачило нашій планеті на цілий рік?")
    elif message.text.lower() == "11":
        bot.send_message(message.chat.id, "Людина на 75% складається з води")
    elif message.text.lower() == "12":
        bot.send_message(message.chat.id, "Найважчий платиновий самородок важить понад 7 кг.")
    elif message.text.lower() == "13":
        bot.send_message(message.chat.id, "Петро Столипін здавав іспит з хімії у самого Дмитра Менделєєва.")
    elif message.text.lower() == "14":
        bot.send_message(message.chat.id, "Водень є найлегшим серед усіх відомих газів.")
    elif message.text.lower() == "15":
        bot.send_message(message.chat.id, "Той же водень вважається найпоширенішим хімічним елементом у світі.")
    elif message.text.lower() == "16":
        bot.send_message(message.chat.id, "Вушна сірка захищає наш організм від шкідливих бактерій та мікроорганізмів.")
    elif message.text.lower() == "17":
        bot.send_message(message.chat.id, "Всього за 1 секунду в головному мозку людини відбувається 100 000 хімічних реакцій.")
    elif message.text.lower() == "18":
        bot.send_message(message.chat.id, "Цікавий факт, що Ернест Резерфорд був першою людиною, який удостоївся Нобелівської премії з хімії.")
    elif message.text.lower() == "19":
        bot.send_message(message.chat.id, "Далеко не всі знають про те, що срібло володіє бактерицидними властивостями, які допомагають очищати воду від вірусів і шкідливих бактерій.")
    elif message.text.lower() == "20":
        bot.send_message(message.chat.id, "Спочатку вартість платини була нижче срібла, з причини її тугоплавкості.")
    elif message.text.lower() == "21":
        bot.send_message(message.chat.id, "Першовідкривачем антибіотиків був відомий хімік Олександр Флемінг.")
    elif message.text.lower() == "22":
        bot.send_message(message.chat.id, "Чи знаєте ви, що гаряча вода швидше перетворюється у лід, ніж холодна?")
    elif message.text.lower() == "23":
        bot.send_message(message.chat.id, "Станом на сьогодні, найчистіша вода знаходиться у Фінляндії.")
    elif message.text.lower() == "24":
        bot.send_message(message.chat.id, "Щоб полум’я набуло зелений колір, у нього достатньо додати бор.")
    elif message.text.lower() == "25":
        bot.send_message(message.chat.id, "Азот здатний спровокувати помутніння розуму.")
    elif message.text.lower() == "26":
        bot.send_message(message.chat.id, "Для зміцнення сталі застосовується такий хімічний елемент, як – ванадій.")
    elif message.text.lower() == "27":
        bot.send_message(message.chat.id, "Якщо через неон пропустити електрика, він почне світитися червоним кольором.")
    elif message.text.lower() == "28":
        bot.send_message(message.chat.id, "При виготовленні сірників використовується не тільки сірка, але і фосфор.")
    elif message.text.lower() == "29":
        bot.send_message(message.chat.id, "За допомогою вуглекислого газу можна отримати безліч різних речовин.")
    elif message.text.lower() == "30":
        bot.send_message(message.chat.id, "Найбільша кількість кальцію міститься в молочних продуктах.")
    elif message.text.lower() == "31":
        bot.send_message(message.chat.id, "Цікавий факт, що марганець може викликати інтоксикацію організму.")
    elif message.text.lower() == "32":
        bot.send_message(message.chat.id, "При виробництві магнітів використовують кобальт.")
    elif message.text.lower() == "33":
        bot.send_message(message.chat.id, "Серед захоплень відомого хіміка Дмитра Менделєєва було виготовлення валіз.")
    elif message.text.lower() == "34":
        bot.send_message(message.chat.id, "Цікаво, що ложки в складі яких присутній галій, можуть плавитися в гарячій воді.")
    elif message.text.lower() == "35":
        bot.send_message(message.chat.id, "При різкому згинанні, хімічний елемент індій видає різкий звук.")
    elif message.text.lower() == "36":
        bot.send_message(message.chat.id, "Цезій вважається самим активним металом")
    elif message.text.lower() == "37":
        bot.send_message(message.chat.id, "Одним з найбільш тугоплавких металів є вольфрам. Саме з нього роблять спіралі в лампах розжарювання.")
    elif message.text.lower() == "38":
        bot.send_message(message.chat.id, "Ртуть володіє найнижчою температурою плавлення.")
    elif message.text.lower() == "39":
        bot.send_message(message.chat.id, "Незначна кількість метанолу може призвести до втрати зору.")
    elif message.text.lower() == "40":
        bot.send_message(message.chat.id, "Виявляється, в гарячій воді неможливо відіпрати плями про білкових продуктів.")


bot.polling(non_stop=True)

