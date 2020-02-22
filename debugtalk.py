import os
import random
import alert
def gen_name():
    val = random.randint(0x4e00, 0x9fbf)
    return "TEST"+chr(val)+chr(val)


def gen_contact():
    val = random.randint(0x4e00, 0x9fbf)
    return "TEST"+chr(val)


def gen_mobile():
    prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
    return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))


def hook_print(any):
    print(any)
    
if __name__ == '__main__':
    gen_mobile()