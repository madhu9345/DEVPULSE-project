import pandas as pd
import numpy as np
import random

def generate_fake_data(n=300):
    data = []
    for _ in range(n):
        state = random.choice(['Focused', 'Tired', 'Needs Break'])

        if state == 'Focused':
            typing_speed = np.random.normal(5, 0.5)
            pause_time = np.random.normal(3, 1)
            errors = np.random.randint(1, 4)
        elif state == 'Tired':
            typing_speed = np.random.normal(3, 0.7)
            pause_time = np.random.normal(7, 2)
            errors = np.random.randint(5, 10)
        else:
            typing_speed = np.random.normal(2, 0.5)
            pause_time = np.random.normal(15, 4)
            errors = np.random.randint(10, 20)

        data.append({
            'typing_speed': round(typing_speed, 2),
            'pause_time': round(pause_time, 2),
            'errors': errors,
            'label': state
        })

    return pd.DataFrame(data)

# Generate and save
df = generate_fake_data()
df.to_csv("developer_productivity.csv", index=False)
print("✅ Data Generated and Saved.")
