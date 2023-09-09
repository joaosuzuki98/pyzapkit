<h1>What is Pyzapkit?</h1>

<p>Do you waste countless hours sending messages though Whatsapp? Do you need to send the same file over and over again to different contacts? Say no more. Pyzapkit lets you automate all of your Whatsapp messages!</p>

<p>Using <b>selenium</b> and <b>pyautogui</b>, Pyzapkit lets you send text messages or files, instantly or at a certain time of the day</p>

<h1>How to use it</h1>

<p>
First, install pyzapkit:
</p>

```python
pip install pyzapkit
```
<br>

<p>
Import the Pyzap class:
</p>

```python
from pyzapkit.main import Pyzap
```
<br>

<p>
Now, you need to check which Google Chrome profile has your whatsapp web account, to do this, go to:
</p>

<h3>
On linux
</h3>

```
/home/your_user/.config/google-chrome
```

<h3>
On windows
</h3>

```
C:\Users\your_user\AppData\Local\Google\Chrome\User Data
```

<p>Inside those folders will be your chrome profiles. Usually, they will be named as 'Profile 1', 'Profile 2', 'Profile 3' and so on, but they can also be named as 'Default' or your chrome user name. Choose the one that has your whatsapp web account login.</p>
<br>

<p>
Instantiate Pyzap with your Chrome profile as an argument:
</p>

```python
whatsapp = Pyzap('Profile 2')
```
<br>

<p>
From there, you can:
</p>

<h4>Send text messages</h4>

```python
whatsapp.send_message('123456789', 'a message')
```

<p>To send text messages at a given time</p>

```python
whatsapp.send_message('123456789', 'a message', False, '14', '15')
```

* Use 24-hour format
* You can use an int or a str as the phone number
* It is not needed to start the phone number with the plus (+) sign

<p>A Chrome browser will be opened and the message will be sent.</p>
<br>

<h4>Send images or videos</h4>

```python
whatsapp.send_file('123456789', 'path/to/your/file.png')
```

* You can send both images (jpg, jpeg or png) or videos (mp4).

<p>You can also send a file at a certain time.</p>

```python
whatsapp.send_file('123456789', 'path/to/your/file.png', instantly=False, hour='14', min='15')
```

<p>You can also specify how long the browser will wait for the file to upload</p>

```python
whatsapp.send_file('123456789', 'path/to/your/file.png', '5', False, '14', '15')
```

<p>When using this method, a browser will be opened, then a dialog box will be opened, when this happens, don't move your mouse nor use your keyboard, because they will be used to automate the file sending process.</p>
<br>

<h4>Send document files</h4>

```python
whatsapp.send_doc('123456789', 'path/to/your/doc.pdf')
```

<p>As always, you can schedule it</p>

```python
whatsapp.send_doc('123456789', 'path/to/your/doc.pdf', instantly=False, hour='14', min='15')
```

<p>Just like with files, you can choose a upload waiting time</p>

```python
whatsapp.send_doc('123456789', 'path/to/your/doc.pdf', '5', False, '14', '15')
```
<br>

<h1>Requirements</h1>

* Google Chrome version 115
* On linux, use xorg display server
* before running the script, download the following pyautogui dependencies:

```bash
sudo apt install scrot
sudo apt install python3-tk 
sudo apt install python3-dev 
```
<br>

<h1>Recommendations</h1>

* When using send_file or send_doc methods, make sure that your directories or files do not have any accent, like ã, ê, ñ etc.
* Before using this script, open your browser with your whatsapp web account logged in and let it load your messages. Whatsapp web almost always backup your messages and this time loading the messages can break the script.
