from car import Car


from car import Car

class CarFactory():

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage): 
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(current_date, last_service_date, warning_light_on: bool):
        return Car(current_date, last_service_date, warning_light_on)



