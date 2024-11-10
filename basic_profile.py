from faker import Faker
import pandas as pd
import numpy as np

global fake

class Profile():
    def __init__(self, num):
        global fake
        fake = Faker()
        np.random.seed(1)
        Faker.seed(1)
        self.num = num
        self.count=0
        self.profiles=self.gen_profiles()

    def gen_profiles(self):
        global fake

        genders = []
        first_name=[]
        last_name=[]
        emails=[]
        country=[]
        location_latitude=[]
        location_longitude=[]


        for i in range(self.num):
            gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
            genders.append(gender)
            first_name.append(fake.first_name_male() if "gender" == "M" else fake.first_name_female())
            last_name.append(fake.last_name())
            emails.append(fake.unique.email())
            country.append(fake.country())
            location_latitude.append(fake.latitude())
            location_longitude.append(fake.longitude())

        profiles = pd.DataFrame({
            'first_name': first_name,
            'last_name': last_name,
            'gender': genders,
            'emails': emails,
            'country': country,
            'location_latitude': location_latitude,
            'location_longitude': location_longitude
        })
        return profiles

    def gen_csv(self, filename):
        self.profiles.to_csv(f"{filename}.csv", index=True)

    def __iter__(self):
        self.count=0
        return self

    def __next__(self):
        x = self.profiles.loc[self.count]

        self.count+=1
        return x

if __name__ == '__main__':
    profiles=Profile(100)
    profiles.gen_csv("profiles")
    iter_profiles = iter(profiles)

    # # iteration example
    # for i in range(profiles.num):
    #     print(next(iter_profiles))