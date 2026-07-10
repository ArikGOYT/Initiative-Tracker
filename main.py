from logic import addCombatant, showCombatants, delCombatant, changeHp, clearAll
from storage import saveCombat, readCombat

readCombat()
while True:
    try:
        userInput=int(input(f"1. Добавить    \n2. Показать   \n3. Урон/Хил   \n4. Удалить    \n5. Очистить поле  \n6. Выход  \n"))
        if userInput == 1:
            addCombatant()
        elif userInput == 2:
            showCombatants()
        elif userInput == 3:
            showCombatants()
            changeHp()
        elif userInput == 4:
            delCombatant()
        elif userInput == 5:
            clearAll()
            saveCombat()
            print("Поле боя очищено.\n")
        elif userInput == 6:
            break
        else:
            print(f"Введите цифру из предложенного списка...\n")
    except (IndexError, ValueError, TypeError) as e:
        print(f"Что-то пошло не так...{e}\n")

