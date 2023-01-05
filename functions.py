import pandas as pd

def extract_names(tag_lst):
    names_lst = []
    
    for name in tag_lst[3:]:
        names_lst.append(name.text)
    print(f"The number of names is {len(names_lst)}")
    
    return pd.Series(names_lst)

motor_lst = []
for motor in firm_motors:
    motor_lst.append(motor.text)

print(len(motor_lst))
# motor_lst