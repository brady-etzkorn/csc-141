def car_build(manufacturer,model,**extra_info):
    extra_info['manufacturer'] = manufacturer
    extra_info['model'] = model
    return extra_info

car_info = car_build('kia','soul',color = 'black',drive = 'four wheel')
print(car_info)
