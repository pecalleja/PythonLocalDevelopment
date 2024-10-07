class Codec:
    def encode(self, s: list):
        return "π".join(s)

    def decode(self, s: str):
        return s.split("π")
