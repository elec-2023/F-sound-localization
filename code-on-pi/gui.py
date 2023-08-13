import tkinter as tk
import threading
import time,wave
import serial,pyaudio
import tensorflow as tf
import numpy as np
import pandas as pd
import os

videoout=0
Log = 'log begin:\n'
audio_file_path = 'sound.wav'  # 替换为您的音频文件路径
sample_rate = 196000
x = 7
y = 7

def play_audio(audio_file, sample_rate):
    chunk = 1024

    wf = wave.open(audio_file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=sample_rate,
                    output=True)

    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()
def play():
    try:
        global videoout
        while videoout:
            play_audio(audio_file_path, sample_rate)
    except:
        pass
def load_data(csv_path):
    data = pd.read_csv(csv_path, header=None)
    return data.iloc[:, 200:500].values


def guibegin():
    def toggle_fullscreen(event=None):
        state = not root.attributes("-fullscreen")
        root.attributes("-fullscreen", state)

    def show_test_window():
        def playvideo():
            global videoout
            videoout=1
            play_audio(audio_file_path, sample_rate)
            print(1)

        def closevideo():
            global videoout
            videoout = 0
            print(0)
        def reback():
            global videoout
            videoout = 0
            print(0)
            test_window.destroy()


        test_window = tk.Toplevel(root)
        test_window.attributes('-fullscreen', True)
        test_window.title("测试窗口")
        tk.Button(test_window, text="返回", command=reback,font=("Courier", 60)).pack()
        tk.Button(test_window, text="播放音频", command=playvideo,font=("Courier", 60)).pack()
        tk.Button(test_window, text="结束音频", command=closevideo, font=("Courier", 60)).pack()
        # 在此添加测试窗口的内容

    def show_basic_requirements_window():
        def begin_test():
            global x, y, current_content
            x = 7
            y = 7
            current_content="物体位置：（--，--）"
            while 1:
                label.config(text=current_content)
                print(x)
                print(y)
                time.sleep(0.1)
                if x == 7 and y == 7:
                    continue
                else:
                    if x == 1:
                        s1 = 'AB'
                    elif x == 2:
                        s1 = 'CD'
                    elif x == 3:
                        s1 = 'EF'
                    elif x == 4:
                        s1 = 'GH'
                    elif x == 5:
                        s1 = 'IJ'
                    elif x == 6:
                        s1 = 'KL'
                    else:
                        current_content = "物体位置：（--，--）"
                        continue
                    if y == 1:
                        s2 = '0102'
                    elif y == 2:
                        s2 = '0304'
                    elif y == 3:
                        s2 = '0506'
                    elif y== 4:
                        s2 = '0708'
                    elif y == 5:
                        s2 = '0910'
                    elif y == 6:
                        s2 = '1112'
                    else:
                        current_content = "物体位置：（--，--）"
                        continue
                    current_content = f"物体位置：（{s1}，{s2}）"
        def begin1():
            threading.Thread(target=begin_test).start()
        current_content = "物体位置：（--，--）"
        basic_window = tk.Toplevel(root)
        label = tk.Label(basic_window, text=current_content, font=("Courier", 60))
        label.pack()
        basic_window.attributes('-fullscreen', True)
        basic_window.title("基本要求第二部分窗口")
        tk.Button(basic_window, text="返回", command=lambda: basic_window.destroy(),font=("Courier", 60)).pack()
        pbt = tk.Button(basic_window, text="开始测试", command=begin1,font=("Courier", 60))

        pbt.pack()
        basic_window.mainloop()
        # 在此添加基本要求第二部分窗口的内容

    def show_exercise_part_one_window():
        def begin_test():
            global x, y, current_content
            x = 7
            y = 7
            current_content = "物体位置：（--，--）"
            while 1:
                label.config(text=current_content)
                print(x)
                print(y)
                time.sleep(0.1)
                if x == 7 and y == 7:
                    continue
                else:
                    if x == 1:
                        s1 = 'B'
                    elif x == 2:
                        s1 = 'C'
                    elif x == 3:
                        s1 = 'E'
                    elif x == 4:
                        s1 = 'H'
                    elif x == 5:
                        s1 = 'J'
                    elif x == 6:
                        s1 = 'L'
                    else:
                        current_content = "物体位置：（-，-）"
                        continue
                    if y == 1:
                        s2 = '01'
                    elif y == 2:
                        s2 = '04'
                    elif y == 3:
                        s2 = '05'
                    elif y == 4:
                        s2 = '08'
                    elif y == 5:
                        s2 = '09'
                    elif y == 6:
                        s2 = '12'
                    else:
                        current_content = "物体位置：（-,-）"
                        continue
                    current_content = f"物体位置：（{s1}，{s2}）"

        def begin1():
            threading.Thread(target=begin_test).start()

        current_content = "物体位置：（-，-）"
        exercise_part_one_window = tk.Toplevel(root)
        label = tk.Label(exercise_part_one_window, text=current_content, font=("Courier", 60))
        label.pack()
        exercise_part_one_window.attributes('-fullscreen', True)
        exercise_part_one_window.title("发挥部分第一部分窗口")
        tk.Button(exercise_part_one_window, text="返回", command=lambda: exercise_part_one_window.destroy(), font=("Courier", 60)).pack()
        pbt = tk.Button(exercise_part_one_window, text="开始测试", command=begin1, font=("Courier", 60))

        pbt.pack()
        exercise_part_one_window.mainloop()
        # 在此添加发挥部分第一部分窗口的内容

    def show_exercise_part_two_window():
        exercise_part_two_window = tk.Toplevel(root)
        exercise_part_two_window.attributes('-fullscreen', True)
        exercise_part_two_window.title("发挥部分第二部分窗口")
        tk.Button(exercise_part_two_window, text="返回", command=lambda: exercise_part_two_window.destroy(),font=("Courier", 60)).pack()
        # 在此添加发挥部分第二部分窗口的内容

    root = tk.Tk()
    root.geometry("800x600")  # Set the initial window size (optional)

    # Bind the F11 key to toggle full-screen mode
    root.bind("<F11>", toggle_fullscreen)

    # Bind the Escape key to exit full-screen mode
    root.bind("<Escape>", toggle_fullscreen)
    root.attributes('-fullscreen', True)
    root.title("全屏GUI示例")

    test_button = tk.Button(root, text="测试", command=show_test_window,font=("Courier", 60))
    test_button.pack()

    basic_requirements_button = tk.Button(root, text="基本要求第二部分", command=show_basic_requirements_window,font=("Courier", 60))
    basic_requirements_button.pack()

    exercise_part_one_button = tk.Button(root, text="发挥部分第一部分", command=show_exercise_part_one_window,font=("Courier", 60))
    exercise_part_one_button.pack()

    exercise_part_two_button = tk.Button(root, text="发挥部分第二部分", command=show_exercise_part_two_window,font=("Courier", 60))
    exercise_part_two_button.pack()

    root.mainloop()


threading.Thread(target=guibegin).start()
loaded_model = tf.keras.models.load_model('model_93.keras')
ser = serial.Serial('/dev/ttyS0', 115200)
k = 0
while 1:
    print('---------------------------------------------------')
    data = ser.readline()
    while 1:
        try:
            if data.decode()[0] == 'a' and data.decode()[1] == '1':
                break
        except:
            pass
        data = ser.readline()

    print(data.decode().strip())
    data = ser.readline()
    s1 = [int(x) for x in data.decode().strip().replace(',.', '').split(',')]
    print(f'max is {max(s1)},at frame {s1.index(max(s1))}')
    for i in range(500):
        if abs(s1[i + 1] - s1[i]) > 20:
            print(f'start at frame {i}')
            break
    data = ser.readline()
    print(data.decode().strip())
    data = ser.readline()
    s2 = [int(x) for x in data.decode().strip().replace(',.', '').split(',')]
    print(f'max is {max(s2)},at frame {s2.index(max(s2))}')
    for i in range(500):
        if abs(s2[i + 1] - s2[i]) > 20:
            print(f'start at frame {i}')
            break
    data = ser.readline()
    print(data.decode().strip())
    data = ser.readline()
    s3 = [int(x) for x in data.decode().strip().replace(',.', '').split(',')]
    print(f'max is {max(s3)},at frame {s3.index(max(s3))}')
    for i in range(500):
        if abs(s3[i + 1] - s3[i]) > 20:
            print(f'start at frame {i}')
            break
    if max(s3) + max(s2) + max(s1) > 1000:
        data_matrix = np.vstack((s1, s2, s3))
        # 将数据保存到 CSV 文件
        np.savetxt(f'target-{k}.csv', data_matrix, delimiter=',', fmt='%d')
        print(f'the {k}-th data saved')
        new_data = load_data(f'target-{k}.csv')
        # 使用加载的模型进行预测
        predictions = loaded_model.predict(np.array([new_data / 1024]))

        # 输出预测结果
        print(predictions)
        print(f'{6 - np.argmax(predictions) // 6},{np.argmax(predictions) % 6 + 1}')
        y = 6 - np.argmax(predictions) // 6
        x = np.argmax(predictions) % 6 + 1
        k = k + 1

