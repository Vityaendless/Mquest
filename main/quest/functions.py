import datetime as dt
from .hero import Hero

day = 1
hero = Hero(100, 10)

def currentTime():
    time = dt.datetime.utcnow() - dt.timedelta(days=365000) + dt.timedelta(days=day)
    return time.strftime('%A - %d %B %Y')

def dayInWeek():
    weekday = (dt.datetime.today().isoweekday() + day) % 7
    return weekday

def WeekDay():
    weekday = dayInWeek()
    weekday_list = [
        'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'
    ]
    writtenDayInWeek = weekday_list[weekday]
    return writtenDayInWeek

def daysCounter():
    global day
    day += 1

def introText():
    global day
    wd = WeekDay()
    text = f'Солнце встает, петухи орут, начинается утро. Сегодня {wd}, {day}-го дня моего существования здесь, а значит я могу заняться следующими делами:'
    return text

def aboutHero():
    global hero
    return hero

def actions():
    current_day = dayInWeek()
    if current_day < 5:
        actions = {
            'Спрячусь где-нибудь. Пусть кто-нибудь другой поработает!': '1',
            'Попрошусь работать в поле, там свежий воздух и относительно спокойно...': '2',
            'Займусь тяжелой работой. Что там нужно господину? Новую помойную яму?': '3',
            'Никуда не пойду, буду спать, я так устал': '4',
            'Лучше и вкуснее всего у господина на кухне, надо пробиться туда!': '5'
        }
    else:
        actions = {
            'Вот уж в выходной день я точно буду спать и отдыхать!': '6',
            'Пойду в таверну. Там и выпить можно и девку пощипать!': '7',
            'Говорят, в город цирк приехал. Вот ведь загляденье будет...': '8',
            'Сегодня открыты бойцовские ямы, сейчас я всем покажу свою силищу!': '9',
            'У господина намечается пир, побуду обслугой и постараюсь что-нибудь урвать...': '10'
        }
    return actions

def actionsDetails(event_number, happens):
    chosen_event = quests(event_number, happens)
    return chosen_event

def randomActionsDetails(random_number):
    chosen_event = random_event(random_number)
    return chosen_event

def quests(event_number, after_smtng_happens):
    print(after_smtng_happens)
    if event_number == 1:
        if after_smtng_happens <= 85:
            smthng_happens = ['Один из охраников Вас заметил, Вам сильно досталось...', {
                '1': 'Ойойой. Как больно!'},
                'main/img/event_bad_relax.jpg']
            hero.heroesHealth(-20)
            hero.heroesGold(-20)
        else:
            smthng_happens = ['Все работали, а я хорошо отдохнул. Ура!', {
                '2': 'Иду в свою землянку. Мне повезло'},
                'main/img/event_good_relax.jpg']
            hero.heroesHealth(20)
            hero.heroesGold(1)
    elif event_number == 2:
        if after_smtng_happens <= 15:
            smthng_happens = ['Проколол ногу, очень больно!', {
                '3': 'Хромаю домой, надеюсь быстро заживет'},
                'main/img/event_bad_work.jpg']
            hero.heroesHealth(-10)
            hero.heroesGold(-5)
        else:
            smthng_happens = ['Поработал на славу, день прошел быстро, а усталась приятная', {
                '4': 'Да и погода была хорошая.'},
                'main/img/event_good_work.jpg']
            hero.heroesHealth(5)
            hero.heroesGold(3)
    elif event_number == 3:
        if after_smtng_happens <= 50:
            smthng_happens = ['Меня заставили копать каменистую землю. Даже не дали обед и воды...', {
                '5': 'Смиренно тружусь.'},
                'main/img/event_bad_hw.jpg']
            hero.heroesHealth(-10)
            hero.heroesGold(10)
        else:
            smthng_happens = ['Работа была не слишком сложной, да и покормили чуть-чуть.', {
                '6': 'Спасибо и на этом...'},
                'main/img/event_good_hw.jpg']
            hero.heroesHealth(5)
            hero.heroesGold(10)
    elif event_number == 4:
        if after_smtng_happens <= 95:
            smthng_happens = ['Естественно меня схватили и показательно выпороли...', {
                '7': 'Ну а на что я рассчитывал?'},
                'main/img/event_bad_out.jpg']
            hero.heroesHealth(-50)
            hero.heroesGold(-50)
        else:
            smthng_happens = ['Никто не обратил на меня внимания.', {
                '8': 'Ничего себе, бывает же такое!'},
                'main/img/event_good_out.jpg']
            hero.heroesHealth(30)
            hero.heroesGold(1)
    elif event_number == 5:
        if after_smtng_happens <= 75:
            smthng_happens = ['В поместье я попал, но только носить ночные горшки. Все на меня кричали и оскорбляли...', {
                '9': 'Столько услышал и узнал про себя, столько было угроз, что не смогу уснуть'},
                'main/img/event_bad_palace.jpg']
            hero.heroesHealth(-25)
            hero.heroesGold(5)
        else:
            smthng_happens = ['Накрывал на стол самому господину, да и объедочки мне достались.', {
                '10': 'Ням!'},
                'main/img/event_good_palace.jpg']
            hero.heroesHealth(15)
            hero.heroesGold(4)
    elif event_number == 6:
        if after_smtng_happens <= 30:
            smthng_happens = ['Схватили у дома и загребли чистить стойла.', {
                '11': 'Увы, отдых не удался.'},
                'main/img/event_bad_sleep.jpg']
            hero.heroesHealth(-10)
            hero.heroesGold(2)
        else:
            smthng_happens = ['Я поспал и восстановил силы.', {
                '12': 'Эх, как хорошо.'},
                'main/img/event_good_sleep.jpg']
            hero.heroesHealth(30)
            hero.heroesGold(1)
    elif event_number == 7:
        if after_smtng_happens <= 60:
            smthng_happens = ['Из таверны меня выгнали, говорят на место таким как я в ней!', {
                '13': 'Эх, очень жаль....'},
                'main/img/event_bad_tavern.jpg']
            hero.heroesHealth(-20)
            hero.heroesGold(-10)
        else:
            smthng_happens = ['Хорошо провел время. В картишки сыграл.А уж девки как плясали, загляденье!', {
                '14': 'Жизнь хороша'},
                'main/img/event_good_tavern.jpg']
            hero.heroesHealth(30)
            hero.heroesGold(2)
    elif event_number == 8:
        if after_smtng_happens <= 80:
            smthng_happens = ['Через маленькую щелочку ничего не увидел толком. Но кто был были в восторге!', {
                '15': 'Ну хоть что-то'},
                'main/img/event_bad_circus.jpg']
            hero.heroesHealth(-5)
            hero.heroesGold(-1)
        else:
            smthng_happens = ['Пролез сквозь навес и увидел тварей невиданных и красивые выступления...', {
                '16': 'Вот загляденье!'},
                'main/img/event_good_circus.jpg']
            hero.heroesHealth(10)
            hero.heroesGold(2)
    elif event_number == 9:
        if after_smtng_happens <= 50:
            smthng_happens = ['Я победил!', {
                '17': 'Как же я хорош!'},
                'main/img/event_good_fight.jpg']
            hero.heroesHealth(-10)
            hero.heroesGold(30)
        else:
            smthng_happens = ['Меня побили...', {
                '18': 'Ну а на что я рассчитывал?'},
                'main/img/event_bad_fight.jpg']
            hero.heroesHealth(-60)
            hero.heroesGold(-30)
    else:
        if after_smtng_happens <= 90:
            smthng_happens = ['Господин напился и стрелял в нас из арбалета', {
                '19': 'На всё его воля.'},
                'main/img/event_bad_meeting.jpg']
            hero.heroesHealth(-40)
            hero.heroesGold(-10)
        else:
            smthng_happens = ['Мне повезло, господин пожаловал объедки слугам. А еще был добр и разрешил поспать в хлеву при поместье.', {
                '20': 'Жизнь хороша!'},
                'main/img/event_good_meeting.jpg']
            hero.heroesHealth(20)
            hero.heroesGold(15)

    return smthng_happens

def random_event(random_number):
    if random_number == 1:
        smtng_random = ['По дороге к дому на меня напали хулиганы. Побили, все тело болит',
                        'main/img/random_attack.jpg']
        hero.heroesHealth(-30)
        hero.heroesGold(-25)
    elif random_number == 2:
        smtng_random = ['По пути мне встретилась блаженная бабка. Она прокляла меня. Так плохо, что не уснуть...',
                        'main/img/random_witch.jpg']
        hero.heroesHealth(-15)
        hero.heroesGold(-10)
    elif random_number == 3:
        smtng_random = ['Съел каких-то ягод, живот крутит что дай боже. Вся ночь на горшке ждет меня...',
                        'main/img/random_berries.jpg']
        hero.heroesHealth(-20)
        hero.heroesGold(-5)
    elif random_number == 4:
        smtng_random = ['Эх. Вроде как соседка втюрилась в меня. Дала мне пообнимать себя по пути домой.',
                        'main/img/random_girl.jpg']
        hero.heroesHealth(15)
        hero.heroesGold(5)
    else:
        smtng_random = ['Нашел монету в грязище. Куплю чего поесть нормального',
                        'main/img/random_food.jpg']
        hero.heroesHealth(10)
        hero.heroesGold(15)

    return smtng_random