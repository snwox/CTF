mappings = {
    "00":" ",
    "04":"a",
    "05":"b",
    "06":"c",
    "07":"d",
    "08":"e",
    "09":"f",
    "0a":"g",
    "0b":"h",
    "0c":"i",
    "0d":"j",
    "0e":"k",
    "0f":"l",
    "10":"m",
    "11":"n",
    "12":"o",
    "13":"p",
    "14":"q",
    "15":"r",
    "16":"s",
    "17":"t",
    "18":"u",
    "19":"v",
    "1a":"w",
    "1b":"x",
    "1c":"y",
    "1d":"z",
    "1e":"1",
    "1f":"2",
    "20":"3",
    "21":"4",
    "22":"5",
    "23":"6",
    "24":"7",
    "25":"8",
    "26":"9",
    "27":"0",
    "28":"\n",
    "29":"esc",
    "2a":"back",
    "2b":"tab",
    "2c":" ",
    "2d":"_",
    "2e":"=",
    "2f":"{",
    "30":"}",
    "31":"\\",
    "32":"Non-US",
    "33":";",
    "34":"'",
    "35":"test1",
    "36":",",
    "37":".",
    "38":"/",
    "39":"Capslock",
    "3a":"F1",
    "3b":"F2",
    "3c":"F3",
    "3d":"F4",
    "3e":"F5",
    "3f":"F6",
    "40":"F7",
    "41":"F8",
    "42":"F9",
    "43":"F10",
    "44":"F11",
    "45":"F12",
    "46":"PrintScreen",
    "47":"ScrollLock",
    "48":"Pause",
    "49":"Insert",
    "4a":"Home",
    "4b":"PageUp",
    "4c":"DeleteForward",
    "4d":"End",
    "4e":"PageDown",
    "4f":"RightArrow",
    "50":"LeftArrow",
    "51":"DownArrow",
    "52":"UpArrow",
}
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
f = open("data.txt","r")
data = f.readlines()
re = ""
for l in data:
    point = l[4]+l[5]
    if point in mappings:
        re += mappings[point]
    if l[0]+l[1]=='20' and re[len(re)-1] in alphabet:
        re=re[:len(re)-1]+chr(ord(re[len(re)-1])-32)

print(re)
