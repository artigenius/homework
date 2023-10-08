# what time is it?
from datetime import datetime
current_datetime = datetime.now().time()
if current_datetime.hour <= 12:
    print('good morning!')
elif current_datetime.hour > 12 and current_datetime.hour <= 18:
    print('hello, good daytime!')
elif current_datetime.hour > 18 and current_datetime.hour <= 21:
    print('good evening!')
elif current_datetime.hour > 21:
    print('good night!')

# извините, я только перечитав задание, поняла
# что время мы должны были вводить сами :(


