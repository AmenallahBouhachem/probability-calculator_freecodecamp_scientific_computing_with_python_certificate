
import copy
import random
class Hat:
    def __init__(self, **kwargs):
        self.dict = kwargs
        self._get_contents()
    def _get_contents(self):
        self.contents = list()
        for i, j in self.dict.items():
            for k in range(0, j):
                self.contents.append(i)
    def draw(self, num):
        self._get_contents()
        
        if num > len(self.contents):
            return self.contents
        
        draw = list()

        while(num > 0):
            random_index = random.randrange(0, len(self.contents))
            random_content = self.contents.pop(random_index)
            draw.append(random_content)
            num -= 1
        
        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    success = 0

    for i in range(0, num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        test_success = True
        for i in drawn_balls:
            if i in expected_balls_copy and expected_balls_copy[i]:
                expected_balls_copy[i] -= 1

        for key, val in expected_balls_copy.items():
            if(val):
                test_success = False

        if(test_success):
            success += 1

        expected_balls_copy = copy.deepcopy(expected_balls)

    return float(success) / num_experiments