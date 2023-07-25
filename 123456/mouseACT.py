import pyautogui
import keyboard
import pyperclip

def copy_mouse_position_to_clipboard():
    #獲取當前鼠标的坐標
    x, y = pyautogui.position()
    #轉化為字串
    pyperclip.copy(f'{x}, {y}')
    #複制到剪贴板
    print(f"当前鼠标坐标为：{x}, {y}")

def on_hotkey_triggered():
    copy_mouse_position_to_clipboard()

# 註冊熱鍵 'P'，按下时触发 on_hotkey_triggered函数
keyboard.add_hotkey('p', on_hotkey_triggered)
# 監聽熱鍵事件
keyboard.wait()