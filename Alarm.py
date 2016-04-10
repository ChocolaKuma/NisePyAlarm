"""
import time

print('How many hours would you like to sleep?')
a = int(input())

b = a * 60
c = b * 60  #hours

print('How many minutes would you like to sleep? (In addition)?')
m = int(input())

n = m * 60
z = c + n
j = z / 60
h = j / 60
print('Okay then. You will sleep for about', h,'Hours')
print('thats a wopping', z, 'Secs')

print('Starting')

"""


def clock():
    """Pulls in current time and converts it to est"""
    from time import gmtime, strftime
    from datetime import datetime, timedelta

    timedate = datetime.now()
    current_time_in_utc = datetime.utcnow()
    global time
    time = current_time_in_utc + timedelta(hours=-5)

##    print(timedate) #time in utc
##    print("The current time is:",time,"in EST") #time in est


def alarmsound(OPTION):
    """What alarms user"""
    opt = OPTION
    import webbrowser,os
    if opt == 1:
        '''opens pandora'''
        webbrowser.open_new("http://www.pandora.com/")
        webbrowser.open_new_tab("https://www.google.com/search?q=weather+48042&rlz=1C1EODB_enUS570US570&oq=weather+48042&aqs=chrome.0.69i59l3.6079j0j4&sourceid=chrome&es_sm=122&ie=UTF-8")
    if opt == 2:
        """J-ROCK PLAY LIST"""
        webbrowser.open_new("https://www.youtube.com/watch?v=Rehz5z0uuWA&index=4&list=PLu07vtOK7KLF4O3SWGkJnhoRsvnRz6O45")
    if opt == 3:
        webbrowser.open_new("")
    if opt == 4:
        '''opens mp3'''
        os.startfile('alarm.mp3')


def calc(HOURS,MINUTES):
    """Calc:
        Basicly it turns input into secounds"""
    b = HOURS * 60  
    c = b * 60      
    n = MINUTES * 60
    z = c + n


def timer_loop(z):
    """counts down the secounds then breaks"""
    import time
    timeout = 10
    target = time.time() + z   #### Put number In seconds here

    while True:
        diff = target - time.time()
        if diff < timeout:
            if diff > 0:  # highly unlikely that diff will go below 0 but just in case
                time.sleep(diff)
            break
        
        else:
            time.sleep(timeout)
    print('Good Morining!')
    alarmsound(4)

def alarm(z):
    """Alarm"""
    clock()
    currentTime = time
    print(currentTime)
    timeFormat = "2015-01-26 16:56:39.593000"
    print("What time would you like to wake up")
    print("Example:", timeFormat)
    Wake = input()
    print(Wake)
    NUM = 1
    while NUM == 1:
        #print("Start of loop")
##        clock()
##        currentTime = time        
        if Wake == time:
            print("Time to wake up")
            NUM==0
            #print("End of loop")
    


def interface():
    print('How many hours would you like to sleep?')
    global HOURS
    HOURS = int(input())
    print('How many minutes would you like to sleep? (In addition)?')
    global MINUTES
    MINUTES = int(input())


def main():
    z= 21600
    #18000
    timer_loop(z)





main()
