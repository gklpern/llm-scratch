import json

class Tokenizer:
    def __init__(self, vocab_file):
        with open(vocab_file, "r") as f:
            self.vocab = json.load(f)  # subword -> id
        self.reverse_vocab = {v: k for k, v in self.vocab.items()}  # id -> subword

    def encode(self, text):
        tokens = []
        for word in text.split():
            i = 0
            # Örnek: "states"
            # "state" => 4
            # "s" => 58
            while i < len(word):
                found_match = False
                # En uzun subword match arama (geriye doğru)
                for j in range(len(word), i, -1):
                    sub_word = word[i:j]
                    if sub_word in self.vocab:
                        tokens.append(self.vocab[sub_word])
                        i = j
                        found_match = True
                        break
                if not found_match:
                    # Bilinmeyen token (<unk>)
                    tokens.append(self.vocab["<unk>"])
                    i += 1
            # Kelime bitişi için boşluk token
            tokens.append(self.vocab[" "])
        return tokens

    def decode(self, ids):
        return "".join([self.reverse_vocab[id] for id in ids])
