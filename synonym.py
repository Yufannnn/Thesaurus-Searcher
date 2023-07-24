class Synonym:
    def __init__(self, origin_word, term, pos, similarity, is_informal, is_vulgar):
        self.origin_word = origin_word
        self.term = term
        self.pos = pos
        self.similarity = int(similarity)  # Convert similarity to an integer
        self.is_informal = bool(int(is_informal))  # Convert is_informal to a boolean
        self.is_vulgar = bool(int(is_vulgar))  # Convert is_vulgar to a boolean

    def __repr__(self):
        return f"Origin Word: {self.origin_word}, Term: {self.term}, POS: {self.pos}, Similarity: {self.similarity}, Informal: {self.is_informal}, Vulgar: {self.is_vulgar}"
    def __eq__(self, other):
        return self.term == other.term and self.origin_word == other.origin_word and self.pos == other.pos

    def is_similar_enough(self, required_similarity):
        return self.similarity >= required_similarity

    def is_different_enough(self, required_difference):
        return self.similarity <= required_difference