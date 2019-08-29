def take_inputs(*cities, sentence="I have been to"):
    for city in cities:
        print(sentence, city)


take_inputs("test","test", "hello", "there")