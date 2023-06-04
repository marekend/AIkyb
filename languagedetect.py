from langdetect import detect, detect_langs, DetectorFactory
from langcodes import *

DetectorFactory.seed = 0

def lang_detect(text, method = "single"):
    if(method != "single"):
        result = detect_langs(text)
        print("Detected Languages: ")
        for item in result:
           langlabel = Language.make(language=item.lang).display_name()
           print(langlabel)
    else:
        result = detect(text)
        langlabel = Language.make(language=result).display_name()
        print("Detected Language: " + langlabel)


text = input("Enter text: ")
method = input("Enter method single/multiple: ")


if method == "single":
    lang_detect(text)
elif method == "multiple":
    lang_detect(text, method)
else:
    print("Wrong method")
