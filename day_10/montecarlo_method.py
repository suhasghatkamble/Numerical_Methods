import random
from datetime import datetime

# Passing the current time as the seed value
dt = datetime.now()
random.seed(int(dt.strftime('%Y%m%d%H%M%S%f')))
# random.seed(1)
for i in range(10):
    print(random.randint ( 0, 30), end="\t")