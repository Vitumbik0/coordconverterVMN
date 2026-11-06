
def to_degrees(latitude, longitude):
    print("CONVERTING DECIMAL DEGREES TO GEOGRAPHIC COORDINATES")

    def convert(value, is_latitude):
        direction = "N" if is_latitude else "E"

        if value < 0:
            direction = "S" if is_latitude else "W"

        value = abs(value)

        degrees = int(value)
        minutes_decimal = (value - degrees) * 60
        minutes = int(minutes_decimal)
        seconds = (minutes_decimal - minutes) * 60

        return degrees, minutes, round(seconds, 4), direction

    lat_dms = convert(latitude, True)
    lon_dms = convert(longitude, False)

    result_formart=print(f"Geographic Coordinates: {lat_dms}, {lon_dms}")
    return result_formart



def to_decimal(latitude, longitude):
    print("CONVERTING GEOGRAPHIC COORDINATES TO DECIMAL DEGREES")

    def convert(degrees, minutes, seconds, direction):
        direction = direction.upper()

        if minutes < 0 or minutes >= 60 or seconds < 0 or seconds >= 60:
            raise ValueError("Minutes and seconds must be between 0 and 60.")

        if direction not in ("N", "S", "E", "W"):
            raise ValueError("Direction must be N, S, E, or W.")

        decimal_degrees = abs(degrees) + minutes / 60 + seconds / 3600

        if direction in ("S", "W"):
            decimal_degrees = -decimal_degrees

        return decimal_degrees

    lat_dd = convert(*latitude)
    lon_dd = convert(*longitude)

    result_format=print(f"Decimal Degrees: ({lat_dd:.3f}, {lon_dd:.3f})")
    return result_format

