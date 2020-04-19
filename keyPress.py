import keyboard, pyautogui, pickle

class keyPress():
    def __init__(self):
        self.recorded = ''

    def record(self):
        self.recorded = keyboard.record(until='esc')

    def play(self,record,time):
        keyboard.play(record,time,speed_factor=1)

    def save(self,PIK = 'pickle.dat'):
        data = self.getRecord()
        with open(PIK,'wb') as f:
            pickle.dump(data,f)

    def load(self,PIK = 'pickle.dat'):
        with open(PIK,'rb') as f:
            return pickle.load(f)

    def fight(self):
        enemy = pyautogui.locateOnScreen('enemy.png')#, region=(1735, 145, 30, 30))
        if hasattr(enemy, '__getitem__'):
            self.num1()

    def num1(self):
        keyboard.write('100')

    #getter/setters
    def getRecord(self):
        return self.recorded
    def setRecord(self,recorded):
        self.recorded = recorded

if __name__ == '__main__':
    k = keyPress()
    k.record()
    k.save()
    x = k.load()

    counter=0
    while(True):
        for i in range(0,len(x)-1):
            if i==0:
                k.play([x[i]],x[i].time)
            else:
                k.play([x[i]],x[i-1].time)

            if counter%5==0:
                k.fight()
            i=i+1
            counter=counter+1

