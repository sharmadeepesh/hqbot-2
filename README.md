# hqbot-2
Just a script to automate HQTrivia answers, but FAST

This script is just an extension to my previous HQBot script. The reason why I created a new repo is that this one has a different approach than the previous one.

The main mechanism of the script is same. However, there is one big difference in this one. Instead of using local machine's interpreter, the script takes help of online Jupyter Notebook Binder to execute some part of the code. This saves a lot of time and makes the script more efficient.

The script OCRs the live game broadcast and passes the generate strings to Jupyter Notebook. The rest of the code is executed on that environment. This saves us approximately 7-8 seconds of processing time.
<h3>How To Use This Script</h3>
I have provided some steps to inform you how to use this script.
1. First of all, open this link on your browser.
2. Shift the browser windows on Right Side of your screen since it's gonna be a little messy.
3. Watch the video "How To Use The Script.mp4" to get an idea of the setup.
4. Shift your HQ trivia game broadcast to the Left Side of your screen.
5. When Jupyter Notebook is opened, close all the unnecessary tabs as shown in the video, and open a Python3 Interpreter. 
6. Start a new Console to install necessary modules on the notebook.
7. Enter <code>pip install google requests</code> in the console and press Shift+Enter to execute it.
8. Open your terminal and shift it to lower right part of the screen. Minimize it as much as possible.
9. Execute the script on your terminal and BAAM! you would see the answer on Jupyter Notebook in a couple of seconds.

<strong>Note : THE PREDEFINED COORDINATES WORK FOR ME AND SHOULD WORK FOR YOU AS WELL. HOWEVER IF NOT, FIX THEM ACCORDING TO YOUR SCREEN. </strong>

For those who do not know about my previous script, here's a little intro to it.

<h3>What Is HQ Trivia</h3>
HQ Trivia is an online game that resembles the concept of "Who wants to be a Millionaire" and its various derivatives. 

The game airs on the official HQ Trivia smartphone application at specific timings. 

<h3>How It Works</h3>
This script OCRs the game real time for question and answers. Parses the generated strings for better processing. And, then uses web scraping to predict the most probable answer. It also uses the concept of Multithreading to improve the time efficiency of the script.

The script is still in making and takes more time to process than needed. This bot is  approximately 50-60% efficient in answering the questions.

What it basically does is that it counts the number of times each answer appears in the top Five results in Google SERP. The script returns the possible answer for each result.

<h3>REQUIREMENTS</h3>
<ol>
  <li>pyautogui</li>
  <li>Pillow / PIL</li>
  <li>Pytesseract</li>                                                                                    
  <li>googlesearch</li>
</ol>

<strong>Note</strong> - The script is developed to run on a Windows Machine. However, the script is still compatible with Unix. Just change the directory of the Pytesseract OCR.

Add all the modules by entering "pip install -r Requirements.txt" in the terminal.

Windows users need to install PyTesseract as a standalone executable. <underline>(Add the module + Install as exe too)</underline>
Linux users need to download "tesseract-ocr" package using their system's package manager. </br>
<code>sudo apt-get install tesseract-ocr</code></br>
Linux users must also comment out the "Pytesseract Path Line from the code" otherwise it would raise an error.
