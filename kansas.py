from random import choice

capital = "Delhi"
bird = "Peacock"
flower = "Lotus"
song = "Jai Shree Krishna"
def randomfunfact():
    funfacts = [
        "Delhi is the capital of India, and it is very beautiful city , It hold the world's largest number of monuments.",
        "Peacock is the national bird of India, and it is very beautiful bird.",
        "Lotus is the national flower of India, and it is very beautiful flower.",
        "Jai Shree Krishna is the national song of India, and it is very beautiful song."
    ]
    index = choice("0123")

    print(funfacts[int(index)])
