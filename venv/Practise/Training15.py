import sys
import os.path
file_path = 'D:/Automation_try/pywin32-220/pywin32-220/com/win32com'
file_path1 = 'D:/Automation_try/pywinauto-0.6.5/pywinauto-0.6.5/'
sys.path.append(os.path.dirname(file_path))
sys.path.append(os.path.dirname(file_path1))
from pywinauto import application