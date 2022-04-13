import dynet as dy
import numpy as np
import tqdm
from pprint import pprint
from typing import Any, Callable, Iterable, List

class NAryTreeLSTM:
    """Recursive neural network with arbitrary number of children per node."""
    def __init__(
        self, 
        input: Iterable[Iterable[float]], 
        word_shape: Iterable[int], 
        # phrase_shape: Iterable[int], 
        # sent_shape: Iterable[int]
    ):

        # validity checks
        if(len(word_shape) != 1)
            raise ValueError(f'word_shape ({word_shape}) must have exactly one element.')
        #  if(len(phrase_shape) != 1)
        #     raise ValueError(f'word_shape ({phrase_shape}) must have exactly one element.')
        #  if(len(sent_shape) != 1)
        #     raise ValueError(f'word_shape ({sent_shape}) must have exactly one element.')
        
        self.pc = dy.ParameterCollection()
        self.input = input
        self.word_shape = tuple(word_shape)
        self.W_words = None
        self.phrases = None
        # self.phrase_shape = phrase_shape
        # self.sent_shape = None

    def build(self, ph: Callable[[Iterable[str]], Iterable[str]]):
        self.phrases = phrase_gen(self.words)
        self.W_words = np.random.rand()
        for word in tqdm.tqdm(iterable=self.words):
            self.pc.add_parameters

W = m.add_parameters((8,2))
V = m.add_parameters((1,8))
b = m.add_parameters((8))

# dy.renew_cg()

# print(W.value())


# trainer = dy.SimpleSGDTrainer(m)

# loss = dy.binary_log_loss(x=x, y=y)

# total_loss = 0
# seen_instances = 0
# # for question, answer in zip(questions, answers):
# #     x.set(question)
# #     y.set(answer)
# #     seen_instances += 1
# #     total_loss += loss.value()
# #     loss.backward()
# #     trainer.update()
# #     if (seen_instances > 1 and seen_instances % 100 == 0):
# #         print("average loss is:",total_loss / seen_instances)

# loss.backward()
# trainer.update()

dy.Model()
