import datetime
 

current_time = datetime.datetime.now()
if(current_time.hour < 12 and current_time.hour > 4):
    print("Good morning, Your time is: ", current_time.hour,":",current_time.minute,"AM")
elif(current_time.hour >= 12 and current_time.hour < 16):
    print("Good Afternoon, Your time is: ",current_time.hour,":",current_time.minute,"PM")
elif(current_time.hour > 16):
    print("Good Evening, Your time is: ",current_time.hour,":",current_time.minute,"PM")
elif(current_time.hour >=0 and current_time.hour < 4):
    print("Its Dawn , Your time is: ",current_time.hour,":",current_time.minute,"PM")

