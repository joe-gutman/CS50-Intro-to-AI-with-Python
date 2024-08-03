from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge_base = And( 
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Or(AKnave, AKnight),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    knowledge_base,

    Or(Not(AKnight), And(AKnight, AKnave)),
    Or(Not(AKnave), Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    knowledge_base,

    Or(Not(AKnight), And(AKnave, BKnave)),
    Or(Not(AKnave), Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    knowledge_base,

    Or(Not(AKnight), And(AKnight, BKnight)),
    Or(Not(AKnave), Not(And(AKnight, BKnight))),
    Or(Not(BKnight), And(AKnave, BKnight)),
    Or(Not(BKnave), And(AKnight, BKnave)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    knowledge_base,
    
    Not(AKnave),
    Or(AKnight, AKnave),
    Or(Not(BKnight), AKnave),
    Or(Not(BKnight), CKnave),

    Or(Not(BKnave), AKnight),
    Or(Not(BKnave), CKnight),

    Or(Not(CKnight), AKnight),
    Or(Not(CKnave), Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
