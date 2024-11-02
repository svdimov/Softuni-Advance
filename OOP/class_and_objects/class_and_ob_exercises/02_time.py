class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def set_time(self, hours, minutes, seconds) -> None:
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def get_time(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0

        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())
print('================')
time = Time(10, 59, 59)
print(time.next_second())
print('=================')
time = Time(23, 59, 59)
print(time.next_second())