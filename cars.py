# 10 car makes, 10 models for each make and price in USD
import random
import pandas as pd

car_make = [
    "Toyota",
    "BMW",
    "Mercedes-Benz",
    "Honda",
    "Ford",
    "Volkswagen",
    "Audi",
    "Porsche",
    "Tesla",
    "Ferrari"
]

car_data = {
    "Toyota": [
        {"model": "Camry", "price": 25000},
        {"model": "Corolla", "price": 20000},
        {"model": "RAV4", "price": 27000},
        {"model": "Highlander", "price": 35000},
        {"model": "4Runner", "price": 38000},
        {"model": "Tacoma", "price": 27000},
        {"model": "Tundra", "price": 36000},
        {"model": "Prius", "price": 25000},
        {"model": "Sienna", "price": 35000},
        {"model": "Avalon", "price": 36000}
    ],
    "BMW": [
        {"model": "3 Series", "price": 41000},
        {"model": "5 Series", "price": 54000},
        {"model": "7 Series", "price": 86000},
        {"model": "X3", "price": 43000},
        {"model": "X5", "price": 59000},
        {"model": "X7", "price": 74000},
        {"model": "M3", "price": 70000},
        {"model": "M5", "price": 103000},
        {"model": "i4", "price": 52000},
        {"model": "iX", "price": 84000}
    ],
    "Mercedes-Benz": [
        {"model": "C-Class", "price": 44000},
        {"model": "E-Class", "price": 56000},
        {"model": "S-Class", "price": 112000},
        {"model": "GLA", "price": 37000},
        {"model": "GLC", "price": 43000},
        {"model": "GLE", "price": 57000},
        {"model": "AMG GT", "price": 92000},
        {"model": "EQS", "price": 103000},
        {"model": "CLA", "price": 39000},
        {"model": "GLB", "price": 39000}
    ],
    "Honda": [
        {"model": "Civic", "price": 22000},
        {"model": "Accord", "price": 26000},
        {"model": "CR-V", "price": 27000},
        {"model": "Pilot", "price": 39000},
        {"model": "HR-V", "price": 24000},
        {"model": "Odyssey", "price": 33000},
        {"model": "Ridgeline", "price": 38000},
        {"model": "Passport", "price": 38000},
        {"model": "Insight", "price": 26000},
        {"model": "Fit", "price": 19000}
    ],
    "Ford": [
        {"model": "F-150", "price": 30000},
        {"model": "Mustang", "price": 27000},
        {"model": "Explorer", "price": 33000},
        {"model": "Escape", "price": 26000},
        {"model": "Edge", "price": 34000},
        {"model": "Bronco", "price": 30000},
        {"model": "Ranger", "price": 25000},
        {"model": "Expedition", "price": 51000},
        {"model": "Mach-E", "price": 44000},
        {"model": "Transit", "price": 38000}
    ],
    "Volkswagen": [
        {"model": "Golf", "price": 24000},
        {"model": "Jetta", "price": 19000},
        {"model": "Passat", "price": 27000},
        {"model": "Tiguan", "price": 26000},
        {"model": "Atlas", "price": 34000},
        {"model": "ID.4", "price": 41000},
        {"model": "Arteon", "price": 40000},
        {"model": "Taos", "price": 24000},
        {"model": "Atlas Cross Sport", "price": 31000},
        {"model": "GTI", "price": 30000}
    ],
    "Audi": [
        {"model": "A3", "price": 35000},
        {"model": "A4", "price": 40000},
        {"model": "A6", "price": 56000},
        {"model": "Q3", "price": 36000},
        {"model": "Q5", "price": 44000},
        {"model": "Q7", "price": 57000},
        {"model": "e-tron", "price": 66000},
        {"model": "RS6", "price": 109000},
        {"model": "TT", "price": 51000},
        {"model": "R8", "price": 143000}
    ],
    "Porsche": [
        {"model": "911", "price": 101000},
        {"model": "Cayenne", "price": 69000},
        {"model": "Macan", "price": 54000},
        {"model": "Panamera", "price": 88000},
        {"model": "Taycan", "price": 83000},
        {"model": "718 Cayman", "price": 61000},
        {"model": "718 Boxster", "price": 63000},
        {"model": "911 GT3", "price": 162000},
        {"model": "911 Turbo", "price": 174000},
        {"model": "Cayenne Coupe", "price": 77000}
    ],
    "Tesla": [
        {"model": "Model 3", "price": 43000},
        {"model": "Model Y", "price": 54000},
        {"model": "Model S", "price": 89000},
        {"model": "Model X", "price": 99000},
        {"model": "Model 3 Performance", "price": 55000},
        {"model": "Model Y Performance", "price": 61000},
        {"model": "Model S Plaid", "price": 125000},
        {"model": "Model X Plaid", "price": 119000},
        {"model": "Cybertruck", "price": 40000},
        {"model": "Roadster", "price": 200000}
    ],
    "Ferrari": [
        {"model": "F8 Tributo", "price": 276000},
        {"model": "SF90 Stradale", "price": 507000},
        {"model": "Roma", "price": 222000},
        {"model": "Portofino M", "price": 245000},
        {"model": "812 Superfast", "price": 340000},
        {"model": "296 GTB", "price": 322000},
        {"model": "SF90 Spider", "price": 558000},
        {"model": "F8 Spider", "price": 302000},
        {"model": "812 GTS", "price": 364000},
        {"model": "Daytona SP3", "price": 2200000}
    ]
}


class Cars():
    def __init__(self, num):

        random.seed(1)
        self.num = num
        self.count=0
        self.cars=self.gen_cars()

    def gen_cars(self):
        my_make = []
        my_model = []
        my_price = []

        for i in range(self.num):
            choice_make = random.choice(tuple(car_make))
            my_make.append(choice_make)
            choice = random.choice(tuple(car_data[choice_make]))
            choice_model, choice_price = choice["model"], choice["price"]
            my_model.append(choice_model)
            my_price.append(choice_price)

        df_car = pd.DataFrame({
            "make": my_make,
            "model": my_model,
            "price": my_price
        })

        return df_car

    def gen_csv(self, filename):
        self.cars.to_csv(f'{filename}.csv', index=True)

    def __iter__(self):
        self.count=0
        return self

    def __next__(self):
        x = self.profiles.loc[self.count]

        self.count+=1
        return x

if __name__ == '__main__':
    cars=Cars(100)
    cars.gen_csv("cars")
    iter_profiles = iter(cars)

    # # iteration example
    # for i in range(profiles.num):
    #     print(next(iter_profiles))
