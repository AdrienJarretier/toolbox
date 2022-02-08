def thousandSeparated(n):
    return "{:,}".format(n)

def sec2prettyTime(seconds):

    timeStr = ""

    if seconds < 0 :
        timeStr = "- "
        seconds *= -1

    timeStr += str(int(seconds/3600)) + " h "
    timeStr += str(int((seconds%3600)/60)) + " m "
    timeStr += str(int(seconds%60)) + " s "

    return timeStr

def time2sec(h,m,s):

    return h*3600+m*60+s

    
def hourToPretty(timeInHour):

    return str(int(timeInHour)) + ' h ' + str(int(timeInHour*60) % 60)