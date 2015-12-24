import importlib
import flashcards_back as back
import flashcards_front as front
import sys

if __name__ == "__main__":
    s = """
    program.py <arg1> <arg2>
    arg1: [help]|[int between 1 and 100]
    arg2: [front]|[back]
    """
    importlib.reload(front)
    importlib.reload(back)
    length = 2
    side = "front"
    if len(sys.argv) >= 2:
        if sys.argv[1].strip().lower() == "help":
            print(s)
        else:
            try:
                length = int(sys.argv[1])
                if length < 1 or length > 100:
                    raise ValueError("length too long: {}".format(length))
            except Exception as e:
                print(e)
    if len(sys.argv) >= 3:
        side = sys.argv[2].strip().lower()
        if side == "front" or side == "back":
            pass
        else:
            raise ValueError("This ({}) is an inappropriate value for side.".format(side))
    if side == "front":        
        front.main("front.txt", length)
    else:
        back.main("back.txt", length)
