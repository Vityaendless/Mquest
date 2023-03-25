class Hero():
    def __init__(self, health, gold):
        self.health = health
        self.gold = gold
        self.age = 3285

    def heroesAge(self):
        """Подсчет возраста героя"""
        self.age += 1

    def heroesHealth(self, n):
        """Подсчет здоровья"""
        self.health += n
        if self.health >= 100:
            self.health = 100

    def heroesGold(self, n):
        """Подсчет денег"""
        self.gold += n
        if self.gold <= 0:
            self.gold = 0

    def heroesClean(self):
        self.health = 100
        self.gold = 10
        self.age = 3285

    def printHeroesAge(self):
        """Выводим информацию о возрасте"""
        years = self.age // 365
        years_string = plural_years(years)
        days = self.age % 365
        days_string = plural_days(days)
        age_string = f'{years_string} и {days_string}'
        return age_string


"""вне класса - использую только для учета склонений возраста персонажа"""
def plural_days(n):
    days = ['день', 'дня', 'дней']
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2

    return str(n)+' '+days[p]

def plural_years(n):
    years = ['год', 'года', 'лет']
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2

    return str(n)+' '+years[p]