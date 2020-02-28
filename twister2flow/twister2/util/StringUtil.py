

class StringUtil:

    @staticmethod
    def get_words(sentence=None, delimiter=" "):
        words = None
        if sentence is None:
            raise Exception("No input to the function")
        else:
            if delimiter in sentence:
                words = sentence.split(" ")
            else:
                words = sentence

        return words