from models import Creature
from storage import saveCombat
from storage import combatants

def addCombatant():
    fields = [("имя", False), ("инициативу", True), ("КД", True), ("ХП", True)]
    data = []

    for label, is_num in fields:
        while True:
            val = input(f"Введите {label}: ")
            if val == "-":
                print("Добавление отменено.\n")
                return

            if is_num:
                try:
                    data.append(int(val))
                    break
                except ValueError:
                    print("Введите число.\n")
            else:
                data.append(val)
                break
    hero = Creature(*data)
    combatants.append(hero)
    combatants.sort(key=lambda x:x.init, reverse=True)
    saveCombat()
    print(f"Персонаж {hero.name} добавлен!\n")
def showCombatants():
    if not combatants:
        print("Список участников пуст.\n")
    for c in combatants:
        print(f"⚔️   {c.name} (Инициатива: {c.init}, КД: {c.ac}, ХП: {c.hp})\n")
def delCombatant():
    if not combatants:
        print("Список участников пуст, удалять нечего.\n")
        return
    while True:
        try:
            showCombatants()
            userInput = input("Введите номер удаляемого участника (начиная с 0. '-' для отмены):...")
            if userInput == "-":
                break
            combatants.pop(int(userInput))
            saveCombat()
            print("Участник успешно удалён!\n")
            break
        except (ValueError, IndexError):
            print(f"Введите цифру из предложенного списка...\n")
def changeHp():
    try:
        if not combatants:
            print("Список участников пуст, урон наносить некому.\n")
            return
        idx = int(input("Номер цели:    "))
        amount = int(input("Число (положительное или отрицательное) "))
        if not combatants[idx].modifyHp(amount):
            print(f"{combatants[idx].name} мёртв. Удаление из списка.\n")
            combatants.pop(idx)
            saveCombat()
        elif amount >= 0:
            print(f"{combatants[idx].name} получил лечение в размере {amount}.\n")
        else:
            print(f"{combatants[idx].name} получил урон в размере {amount}.\n")
        saveCombat()
    except (ValueError, IndexError):
        print(f"Введите цифру из предложенного списка...\n")
def clearAll():
    combatants.clear()