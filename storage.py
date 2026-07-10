from models import Creature

fileName = "combatants.txt"
combatants = []
def saveCombat():
    with open(fileName, "w", encoding="utf-8") as f:
        for c in combatants:
            f.write(f"{c.name}|{c.init}|{c.ac}|{c.hp}\n")

def readCombat():
    global combatants
    try:
        combatants.clear()
        with open(fileName, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    name, init, ac, hp = line.split("|")
                    combatants.append(Creature(name, int(init), int(ac), int(hp)))
    except FileNotFoundError:
        pass
