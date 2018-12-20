import webbrowser
search_term = "Google Test"
url = "https://www.google.com.tr/search?q={}".format(search_term)    
# new=0 open in same windwow, new=1 open in new window, new=2 open in new tab ** doesnt matter PM just opens new tab
webbrowser.open(url)



#https://stackoverflow.com/questions/14965946/script-for-opening-up-a-google-search-in-a-browser