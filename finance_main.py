def calculate_pay(hours_worked, hourly_rate):
        if hours_worked<=40:
            return hours_worked*hourly_rate
        else:
            return hourly_rate*40+(hours_worked-40)*hourly_rate*1.5
       
