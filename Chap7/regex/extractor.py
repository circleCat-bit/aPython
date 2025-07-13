import pyperclip, re
#create 2 regexes for phone and email
phone_regex = re.compile(r"(?:09|02|03|05)\d{8}")
gmail_regex = re.compile(r"[\w+%.-]+@[0-9A-Za-z.-]+\.(?:com|edu|vn|org)")
text = pyperclip.paste()

pn_text = ""
g_text = ""
if pns := phone_regex.findall(text):  
    pn_text = "\n".join(pns) 
    pn_text = "Phone Number: \n" + pn_text + "\n"
    
if gmails := gmail_regex.findall(text):
    g_text = "\n".join(gmails)
    g_text = "Gmail: \n" + g_text + "\n"

pn_gmail_text = pn_text + g_text
if pn_gmail_text:
    pyperclip.copy(pn_gmail_text)
    print("Copy successfully")
else:
    print("Can't copy")