# hitchhikers-guide-to-the-galaxy

A small, unofficial tribute to Douglas Adams.

## Why

TL;DR: `42`. It's the answer to everything :)

I've audited the state of vibe coding.

Every tutorial. Every Colab. Every "quick seed for reproducibility"
Stack Overflow answer that somehow has 47k upvotes.

They all use `42`.

Not 7. Not 1337. Not your birthday. Forty. Two.

We've been paying silent homage to Douglas Adams this whole time and
calling it "best practice."

So this package stops pretending that is science and makes it official:
one import, one enum, one joke that outlived the radio series and every
model that will confidently invent a paper about why 42 maximizes entropy.

Don't panic. Just import the Answer.

(And if your PR reviewer asks why -- tell them Deep Thought approved the API.)

## Usage

```python
from hitchhikers_guide_to_the_galaxy import Answer
import random

random.seed(Answer.FORTY_TWO)
```

Or, if you prefer the full ceremony:

```python
from hitchhikers_guide_to_the_galaxy import TheAnswerToLifeTheUniverseAndEverything

assert TheAnswerToLifeTheUniverseAndEverything.FORTY_TWO == 42
```

One package. One file. One enum.

## Install

```bash
pip install hitchhikers-guide-to-the-galaxy
```

## References

**The joke (Adams / 42)**

- [Phrases from The Hitchhiker's Guide to the Galaxy -- The number 42](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#Answer_to_the_Ultimate_Question_of_Life,_the_Universe,_and_Everything_(42)) (Wikipedia)
- [For Math Fans: A Hitchhiker's Guide to the Number 42](https://www.scientificamerican.com/article/for-math-fans-a-hitchhikers-guide-to-the-number-42/) (Scientific American) -- includes Adams explaining he just picked an ordinary smallish number
- [Douglas Adams and the cult of 42](https://www.theguardian.com/books/2011/feb/03/douglas-adams-42-hitchhiker) (The Guardian)

**The seed convention (ML / docs / folklore)**

- [sklearn.model_selection.train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) -- official examples use `random_state=42`
- [Common pitfalls -- scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html) -- same pattern in recommended practices
- [In machine learning why most guys using random_state=42?](https://stackoverflow.com/questions/48940148/in-machine-learning-why-most-guys-using-random-state-42) (Stack Overflow)
- [What is the origin of magic number 42, indispensable in coding?](https://stackoverflow.com/questions/16236182/what-is-the-origin-of-magic-number-42-indispensable-in-coding) (Stack Overflow)
- [The story behind random.seed(42) in machine learning](https://medium.com/geekculture/the-story-behind-random-seed-42-in-machine-learning-b838c4ac290a) (Nazia Nafis, Geek Culture)
- [The number 42 shows up all over ML](https://milesmurdocca.com/42-2/index.html) (Miles Murdocca)

Any fixed seed is fine for reproducibility. `42` is culture, not statistics.

## Disclaimer

Unofficial fan tribute. Not affiliated with, endorsed by, or connected to
the Douglas Adams estate, or any rights holders of *The Hitchhiker's Guide
to the Galaxy*.

## License

MIT -- share freely across the galaxy (and your `random.seed` calls).

