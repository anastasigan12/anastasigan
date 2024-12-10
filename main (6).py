import math
import matplotlib.pyplot as plt

class Point12:
    instance_count = 0  # Лічильник створених екземплярів

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point12.instance_count += 1

    def __del__(self):
        Point12.instance_count -= 1
        print(f"Point {self.__x, self.__y} destroyed")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value if -100 <= value <= 100 else 0

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value if -100 <= value <= 100 else 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count


# Створюємо список точок
points = [Point12(10, 10), Point12(20, 30), Point12(15, 25), Point12(40, 50)]

# Обчислюємо відстань між другою та четвертою точками
distance_2_4 = Point12.distance(points[1], points[3])
print(f"Відстань між другою і четвертою точками: {distance_2_4:.2f}")

# Переміщуємо третю крапку на 36 вправо
points[2].move(36, 0)

# Візуалізація точок до і після зміни
x_coords_before = [10, 20, 15, 40]
y_coords_before = [10, 30, 25, 50]

x_coords_after = [p.x for p in points]
y_coords_after = [p.y for p in points]

plt.figure(figsize=(10, 5))

# До зміни
plt.subplot(1, 2, 1)
plt.scatter(x_coords_before, y_coords_before, color="blue", label="До зміни")
plt.title("До зміни")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.legend()

# Після зміни
plt.subplot(1, 2, 2)
plt.scatter(x_coords_after, y_coords_after, color="red", label="Після зміни")
plt.title("Після зміни")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Збереження координат у файл
with open("coordinates.txt", "w") as f:
    for i, p in enumerate(points):
        f.write(f"{i + 1}) {p.x}:{p.y}\n")
