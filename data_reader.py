def get_data():
    test_data = "23,85,800"

    values = test_data.split(",")

    temperature = values[0]
    humidity = values[1]
    light = values[2]

    return temperature, humidity, light