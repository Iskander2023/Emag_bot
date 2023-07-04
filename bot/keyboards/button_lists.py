"""
списки для создания кнопок клавиатуры

"""
start_keyboard_menu = ["Каталог станков", "Каталог деталей", "О компании"]

list_of_emag_models = ["VL", "VM", "в меню =>>"]
list_of_dekay_models = ["V", "Y", "в меню =>>"]

machines_list_dekay_v = ["V-1160", "в меню =>>"]
machines_list_dekay_y = ["Y-3122", "в меню =>>"]

machines_list_vl = ["vl2", "vl4", "в меню =>>"]
machines_list_vm = ["vm9", "vm12", "в меню =>>"]

about_the_company = ["Контакты", "О нас", "Наши услуги", "в меню =>>"]
contacts_list = ["Технический отдел", "Отдел продаж", "Юридический отдел", "в меню =>>"]

part_type = ["Нефтедобдыча", "Машиностроение", "в меню =>>"]
oil_production_details = ["Муфта", "Трубы", "в меню =>>"]
mechanical_engineering_details = ["Подшипники", "Ступицы", "в меню =>>"]

coupling = ["OTTM", "BATRESS", "CENTUM", "в меню =>>"]
pipe_thread = ["OTTM", "BATRESS", "CENTUM", "в меню =>>"]
bearings = ["Кольцо подшипника внутреннее", "в меню =>>"]
hub = ["Ступица", "в меню =>>"]

"""
списки для минимизирования кода(используются для проверки в декораторе хэндлеров)
"""
dekay_or_emag = ["Dekay", "EMAG"]
list_of_models = ["VL", "VM", "V", "Y"]

e_d_list = ["vl2", "vl4", "vm9", "vm12", "V-1160", "Y-3122"]

parts_list = ["Муфта", "Трубы", "Подшипники", "Ступицы"]
details_list = ["OTTM", "BATRESS", "CENTUM", "Кольцо подшипника внутреннее", "Ступица"]