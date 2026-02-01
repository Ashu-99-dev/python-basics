def hello(name , lang):
    greeting = {
        "english": "Hello",
        "hindi": "Namaste",
        "punjabi": "Namaste",
        "gujarati": "Namaste",
        "marathi": "Namaste",
        "telugu": "Namaste",
        "tamil": "Namaste",
        "kannada": "Namaste",
        "odia": "Namaste",
        "assamese": "Namaste",
        "bengali": "Namaste",
    }
    msg = f"{greeting[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This program greets the person")
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet")
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["english","hindi","punjabi","gujarati","marathi","telugu","tamil","kannada","odia","assamese","bengali"],help="The language of the person to greet")
    args = parser.parse_args()
    hello(args.name,args.lang)

