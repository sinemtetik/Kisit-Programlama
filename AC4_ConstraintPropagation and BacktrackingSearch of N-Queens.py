'''

N-Queens problemi AC-4	algoritması ile	çözülmektedir. 
AC-4 algoritmasındaki temel amaç, tüm kısıtlar sağlanana kadar değişkenlerin domainlerindeki değerleri uygun şekilde kaldırmaktır.
N-Queens problemi için, bu algoritmanın	amacı, kısıtları yerinegetirerek herhangi iki kraliçenin birbirine saldırmamasını sağlamaktır.
arc_consistency fonksiyonu, değişkenlerin üzerinde kısıtları uygular. 
revise fonksiyonu, bir değişkenin alanından tutarsız değerleri kaldırır. 
satisfies_constraint fonksiyonu, bir değer atamasının verilen kısıtlamayı sağlayıp sağlamadığını kontrol eder. 
get_neighbors fonksiyonu, bir değişkenin komşularını elde eder. 
solve_nqueens fonksiyonu önce alan kısıtlılığını sağlar ve ardından geriye dönüş temelli çözüm yaklaşımına devam eder.
Son olarak, main fonksiyonunda kullanıcıdan input fonksiyonu ile n değeri alınır.
Bu değer, N-Queens problemi için satranç tahtasının boyutunu belirler. 
Sonrasında bu değer üzerinden NQueens sınıfının bir örneği oluşturuluyor ve çözüm yöntemi çağrılır.


'''

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]  # Satranç tahtası oluşturuluyor
        self.domains = [[set(range(n)) for _ in range(n)] for _ in range(n)]  # Her değişken için olası değerlerin kümeleri tutuluyor
        self.constraints = []  # Kısıtlamaların tutulacağı liste

    def setup_constraints(self):
        for row in range(self.n):
            for col in range(self.n):
                for i in range(self.n):
                    for j in range(self.n):
                        if (row != i or col != j) and \
                           (row == i or col == j or abs(row - i) == abs(col - j)):
                            self.constraints.append(((row, col), (i, j)))  # Her kraliçenin diğerine saldırmamasını sağlayan kısıtlamalar oluşturuluyor

    def arc_consistency(self):
        self.setup_constraints()
        queue = self.constraints[:]  # Kuyruk oluşturuluyor ve başlangıçta tüm kısıtlamalar kuyruğa ekleniyor
        while queue:
            (x, y) = queue.pop(0)
            if self.revise(x, y):
                if len(self.domains[x[0]][x[1]]) == 0:
                    return False  # Eğer bir değişkenin alanı boşsa (yani hiç olası değer kalmamışsa), bu durumun çözümü yoktur
                for z in self.get_neighbors(x):
                    if z != y:
                        queue.append((z, x))  # Eğer bir değişken güncellendiyse, bu değişkenin komşularını kuyruğa ekleyerek yayılma işlemi devam eder
        return True  # Eğer tüm kısıtlamaları geçebilirse, alan kısıtlılığı başarılıdır

    def revise(self, x, y):
        revised = False
        for value in list(self.domains[x[0]][x[1]]):
            if not any(self.satisfies_constraint(value, self.board[y[0]][y[1]], y_val) for y_val in self.domains[y[0]][y[1]]):
                self.domains[x[0]][x[1]].remove(value)
                revised = True  # Eğer bir değer belirli bir kısıtlamayı sağlamıyorsa, bu değer alanın kümesinden çıkarılır
        return revised

    def satisfies_constraint(self, x_val, y_val, y_val_other):
        return x_val != y_val_other and \
               (x_val, y_val) != (y_val_other, y_val) and \
               abs(x_val - y_val) != abs(x_val - y_val_other)  # Verilen kısıtlamanın sağlanıp sağlanmadığı kontrol edilir

    def get_neighbors(self, var):
        neighbors = []
        for c in self.constraints:
            if c[0] == var:
                neighbors.append(c[1])  # Verilen değişkenin kısıtlamalarından komşuları elde edilir
        return neighbors

    def solve_nqueens(self):
        if not self.arc_consistency():
            print("Tutarlı bir alan belirleme mümkün değil.")
            return False
        if not self.solve_nqueens_util(0):
            print("Çözüm bulunamadı.")
            return False
        self.print_solution()  # Arc consistency işlemi başarılı olduğunda ve N-queens problemi çözüldüğünde sonucu yazdırılır
        return True

    def solve_nqueens_util(self, col):
        if col >= self.n:
            return True
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                if self.solve_nqueens_util(col + 1):
                    return True
                self.board[i][col] = 0
        return False

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True  # Verilen pozisyona kraliçe yerleştirilip yerleştirilemeyeceği kontrol edilir

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()  # Sonuç yazdırılır


if __name__ == "__main__":
    while True:
        n = int(input("Satranç tahtasının boyutunu girin (0 çıkış yapar): "))  # Kullanıcıdan satranç tahtasının boyutunu alın
        if n == 0:
            print("Program sonlandırıldı.")
            break  # Kullanıcı 0 girerse programı sonlandır
        elif n < 0:
            print("Negatif bir değer giremezsiniz. Lütfen pozitif bir değer girin.")
            continue  # Negatif bir değer girerse kullanıcıya uyarı ver ve döngüyü tekrar başlat
        else:
            n_queens = NQueens(n)
            print(n, "kraliçe problemi çözümü:")
            n_queens.solve_nqueens()
