import logging

logging.basicConfig(level=logging.INFO)
def add(a , b):
    logging.info("Additon operation performed")
    return a + b

if __name__=="__main__":
    print(add(2,5))