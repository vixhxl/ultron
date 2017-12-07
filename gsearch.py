import webbrowser

def search(word):
    url="http://www.google.com/?#q="
    webbrowser.open_new_tab(url+word)


