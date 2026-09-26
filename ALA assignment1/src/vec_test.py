import sys
from typing import Self
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from vec.vec import Vec as Vector
from w2v import get_word_vector,load_model

class TestVec(unittest.TestCase):

    def test_mean_word(self):
        model = load_model("ala2026/src/word2vec/glove50/glove_50_fast.wordvectors")
        word_vec = get_word_vector(model, "quick")
        v=Vector([float(x) for x in word_vec])
        expected_mean = sum(v.elements) / len(v.elements)
        self.assertAlmostEqual(v.mean(), expected_mean, places=5, msg="Vector mean mismatch.")
        print(expected_mean,v.mean())

    def test_demean_word(self):
        model = load_model("ala2026/src/word2vec/glove50/glove_50_fast.wordvectors")
        word_vec = get_word_vector(model, "quick")
        v = Vector([float(x) for x in word_vec])

        self.assertAlmostEqual(v.demean(), 0.0 , places=5, msg="Demeaned vector mismatch.")
        print("Demean:" ,v.demean())

    def test_std_word(self):
        model = load_model("ala2026/src/word2vec/glove50/glove_50_fast.wordvectors")
        word_vec = get_word_vector(model, "quick")
        v = Vector([float(x) for x in word_vec])

        expected_std = (sum((x - v.mean()) ** 2 for x in v.elements) / len(v.elements)) ** 0.5
        self.assertAlmostEqual(v.std(), expected_std, places=5, msg="Vector standard deviation mismatch.")
        print("Std:",v.std())
    

if __name__ == "__main__":
    unittest.main()