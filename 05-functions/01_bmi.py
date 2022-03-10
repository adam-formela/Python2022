def calculate_bmi(weight, height):
    return round(weight / height ** 2, 2)

def get_state(bmi):
    if bmi < 18:
        return "niedowaga"
    elif bmi < 25:
        return "w normie"
    elif bmi < 30:
        return  "nadwaga"
    else:
        return "otyłość"

def check_health(w, h):
    bmi_result = calculate_bmi(w, h)
    bmi_status = get_state(bmi_result)
    return bmi_status

# --- reszta skrypu
# pyta uzytkownika
result = check_health(56, 1.6)
print('Twoje BMI ->', result)