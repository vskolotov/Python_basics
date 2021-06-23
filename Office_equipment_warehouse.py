class IsNotNumberError(Exception):
    def __str__(self):
        return 'Количество должно быть целым числом'


class NotPositiveNumberError(Exception):
    def __str__(self):
        return 'Количество должно быть целым положительным числом'


class Warehouse:

    def __init__(self, name):
        self.name = name
        self.shelf = {}
        self.dep = {}

    @staticmethod
    def valid_count(txt):
        if not isinstance(txt, int):
            raise IsNotNumberError
        if txt < 0:
            raise NotPositiveNumberError

    def put(self, equipment, count):
        self.valid_count(count)
        if equipment in self.shelf:
            self.shelf[equipment] += count
        self.shelf.setdefault(equipment, count)

    def send_department(self, department, equipment, count):
        self.valid_count(count)
        if department in self.dep:
            self.dep[department].append({equipment: count})
        else:
            self.dep.setdefault(department, [{equipment: count}])
        self.shelf[equipment] -= count

    def info(self):
        print(f'склад {self.name}')
        for k, v in self.shelf.items():
            t = k.type_equipment
            b = k.brand
            m = k.model
            p = k.price
            print(f'{t}: {b}-{m}, цена: {p} руб., количество: {v} шт.')

    def dep_info(self, department):
        print(f'в отделе {department}')
        for el in self.dep[department]:
            for k, v in el.items():
                t = k.type_equipment
                b = k.brand
                m = k.model
                print(f'\t {t}: {b}-{m}, {v} шт.')


class OfficeEquipment:
    def __init__(self, type_equipment=None, brand=None, model=None, price=None):
        self.type_equipment = type_equipment
        self.price = price
        self.brand = brand
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, brand=None, model=None, price=None, type_printer=None):
        type_equipment = 'принтер'
        super().__init__(type_equipment, brand, model, price)
        self.type_printer = type_printer


class Scanner(OfficeEquipment):
    def __init__(self, brand=None, model=None, price=None, type_scanner=None):
        type_equipment = 'сканер'
        super().__init__(type_equipment, brand, model, price)
        self.type_scanner = type_scanner


class CopyMachine(OfficeEquipment):
    def __init__(self, brand=None, model=None, price=None, copy_speed=None):
        type_equipment = 'копир'
        super().__init__(type_equipment, brand, model, price)
        self.copy_speed = copy_speed


printer_1 = Printer('HP', 'lg132', 150.9, 'laser')
scanner_1 = Scanner('Canan', 'l12', 100, type_scanner='Ручной')
warehouse_1 = Warehouse('#1')
warehouse_1.put(printer_1, 4)
warehouse_1.put(scanner_1, 5)
warehouse_1.info()
warehouse_1.put(printer_1, 4)
warehouse_1.info()
print()
warehouse_1.send_department('бух', printer_1, 2)
warehouse_1.info()
warehouse_1.send_department('бух', scanner_1, 2)
warehouse_1.info()
warehouse_1.dep_info('бух')
