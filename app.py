from time import time

from flask import Flask, render_template, request, url_for, redirect

def whatsapp_message_sender(phone_number, message, time_hour, time_minute, repeat_count=1):
    import pywhatkit
    from datetime import time
    the_time= time(hour=time_hour, minute=time_minute, second=0)
    pywhatkit.sendwhatmsg(phone_no= phone_number, message= message, time_hour= the_time.hour, time_min=the_time.minute, tab_close=True, close_time=4)
    if repeat_count >1:
        for i in range(repeat_count-1):
            pywhatkit.sendwhatmsg_instantly(phone_no= phone_number, message= message, wait_time=10, tab_close=True)
def message_everywhere_sender(message, repeat_count=1, delay_time=0):
    import pyautogui
    import time
    for i in range(repeat_count):
        pyautogui.typewrite(message=message)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(delay_time)

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        from_type= request.form['auto_sender']
        if from_type == 'whatsapp_sender':

            phone_number= request.form['phone']
            message=request.form['message']
            time_hour= int(request.form['hour'])
            time_minute= int(request.form['minute'])
            repeat_count= int(request.form['repeat'])
            whatsapp_message_sender(phone_number, message, time_hour, time_minute, repeat_count)
        elif from_type=="everywhere_sender":
            message_everywhere=request.form['message']
            repeat_count_everywhere= int(request.form['repeat'])
            delay_time_everywhere= int(request.form.get('delay') or 1)

            message_everywhere_sender(message_everywhere, repeat_count_everywhere, delay_time_everywhere)

        return render_template('index.html')

    return render_template('index.html')
        

app.run(debug=True)