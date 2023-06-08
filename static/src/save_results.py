from db import add_pred

def save_results(text, filename):
    add_pred(filename, text)