import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        try:
            assert brand != ""
            assert photo_file_name != ""
            assert carrying != ""
        except AssertionError:
            raise ValueError
        photo_file_name_ext = os.path.splitext(photo_file_name)[1]
        my_list = [".jpg", ".jpeg", ".png", ".gif"]
        if photo_file_name_ext not in my_list:
            raise ValueError
        self.photo_file_name = str(photo_file_name)
        self.brand = str(brand)
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        try:
            return os.path.splitext(self.photo_file_name)[1]
        except ValueError or IndexError:
            raise ValueError


class Car(CarBase):

    car_type = "car"

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            assert passenger_seats_count != ""
        except AssertionError:
            raise ValueError
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            assert body_whl != ""
            self.body_length, self.body_width, self.body_height = map(float, body_whl.split('x'))
        except (AssertionError, ValueError, IndexError):
            self.body_length = float(0)
            self.body_height = float(0)
            self.body_width = float(0)

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):

    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        try:
            assert extra != ""
        except AssertionError:
            raise ValueError
        self.extra = str(extra)


def get_car_list(file):
    car_list = []
    with open(file) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if row and row[0] == "car":
                try:
                    car_list += [Car(row[1], row[3], row[5], row[2])]
                except ValueError:
                    continue
            elif row and row[0] == "truck":
                try:
                    car_list += [Truck(row[1], row[3], row[5], row[4])]
                except ValueError:
                    continue
            elif row and row[0] == "spec_machine":
                try:
                    car_list += [SpecMachine(row[1], row[3], row[5], row[6])]
                except ValueError:
                    continue
    return car_list


if __name__ == "__main__":

    car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '10')
    print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep = '\n')

    truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
    print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep = '\n')

    spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'xff')
    print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep = '\n')

    spec_machine.get_photo_file_ext()

    cars = get_car_list('coursera_week3_cars.csv')

    print(len(cars))

    for car in cars:
        print(type(car))

    print(cars[0].passenger_seats_count)

    print(cars[1].get_body_volume())
