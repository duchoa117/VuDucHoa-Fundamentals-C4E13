import mlab
from models.class_c4e_services import Service
mlab.connect()
infor_service = Service(
    image = "https://scontent.fhan2-3.fna.fbcdn.net/v/t1.0-9/29694924_370145806831621_4579098121071088843_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEBjJPc41gctC0Yl1kBHNQntUAQ0NViysYh59VNHQQx2ohVKadP7ZraOqKTdyaYKpBISDm3YfcdFKoA3DIQneBIBi05paxO81LxA81r9_Ncnw&oh=c698e9696714a225e2b92193d3f270a2&oe=5B639185",
    name = "Vũ Đức Hòa",
    gender = 1,
    yob = 1999,
    height = 175,
    phone_number = "01697223626",
    address = "210 Xã Đàn",
    description = "Hài hước, đẹp trai =)),....",
    measurements = [98,80,89]
    status = "Free"
)
infor_service.save()
