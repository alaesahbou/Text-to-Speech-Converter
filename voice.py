import sys
import pyttsx3
import getopt

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def main(argv):
    text = ""
    try:
        opts, args = getopt.getopt(argv,"ht:f:",["text=","file="])
    except getopt.GetoptError:
        print(f'{sys.argv[0]} -t <text> or {sys.argv[0]} -f <file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(f'{sys.argv[0]} -t <text> or {sys.argv[0]} -f <file>')
            sys.exit()
        elif opt in ("-t", "--text"):
            text = arg
        elif opt in ("-f", "--file"):
            text = read_file(arg)
    if text == "":
        print(f"No text or file provided. Please provide text or file name with -t or -f options.")
        sys.exit()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main(sys.argv[1:])
