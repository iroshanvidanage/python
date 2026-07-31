import pytz
from datetime import datetime, timedelta

def calculate_fd_time(start_date, duration, timezone_str='UTC'):
    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    timezone = pytz.timezone(timezone_str)
    start_date = timezone.localize(start_date)
    end_date = start_date + timedelta(days=duration)
    return end_date.strftime('%Y-%m-%d %H:%M:%S %Z%z')


if __name__ == "__main__":
    start_date = '2025-06-23 10:00:00'
    duration = 200  # days
    timezone_str = 'Asia/Colombo'
    fd_time = calculate_fd_time(start_date, duration, timezone_str)
    print(f'Fixed Deposit Maturity Date and Time: {fd_time}')
