'''Importing all the necessary modules and libraries'''
import pyperclip
import pyautogui                                                                                                        
from PIL import Image, ImageFile, ImageDraw, ImageChops, ImageFilter, ImageEnhance                                      
from pytesseract import *                                                                                                                                                                                                      
import string  

#This function pastes the code in the notebook and executes it
def open_jupyter(copycode):
	pyperclip.copy(copycode)
	pyautogui.moveTo(1057, 198, duration=0.1)
	pyautogui.click()
	pyautogui.hotkey('ctrl','v')
	pyautogui.click()
	pyautogui.hotkey('shift', 'enter')

#This function parses the text into questions and answers
def ocr_text_parse():
	global text
	global question
	global answers
	clean_text=("".join([s for s in text.strip().splitlines(True) if s.strip()]))
	question = clean_text.split("?")[0]
	print(question)
	answers = clean_text.split("?")[1]
	answers=("".join([s for s in answers.strip().splitlines(True) if s.strip()]))
	answers = answers.split('\n')
	print(answers)
	copycode = ('''import requests
	\nimport string
	\nfrom googlesearch import *
	\n
	\ndef find_url():
	\turl=[]
	\tquestion = """{}"""
	\tanswers = {} 
	\tfor j in search(question, stop=5):
	\t\turl.append(j)
	\tcount_calc(answers, url[0], 0)
	\tcount_calc(answers, url[1],1)
	\tcount_calc(answers, url[2],2)
	\tcount_calc(answers, url[3],3)
	\tcount_calc(answers, url[4],4)
	\n
	\ndef count_calc(answers, url, number):
	\tcount=[1,1,1]
	\tfor i in range(3):
	\t\tcount[i]=requests.get(url).text.count(answers[i])
	\tmaxnumber = max(count)
	\tif count[0]==maxnumber:
	\t\tdraft_answer= answers[0]
	\telif count[1]==maxnumber:
	\t\tdraft_answer=answers[1]
	\telif count[2]==maxnumber:
	\t\tdraft_answer=answers[2]
	\tprint(draft_answer)   
	\n    
	\nfind_url()'''.format(question,answers))
	open_jupyter(copycode)

#This function captures screen in real time and processes it for OCR
def text_extraction():                                                                          
	global text
	screenshot = pyautogui.screenshot()
	cropped = screenshot.crop((81,261,597,719))
	contrasted = ImageEnhance.Contrast(cropped).enhance(5.0)
	text=image_to_string(contrasted)
	ocr_text_parse()
	             

if __name__ == '__main__':
	text_extraction()
      