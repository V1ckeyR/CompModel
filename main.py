import random
import numpy as np
from scipy import stats
import seaborn
import matplotlib.pyplot as plt


class Lab1:
    def __init__(self):
        self.size = 10000
        self._generate_random_numbers()
        self.draw_hist()
        self.check()

    def _generate_random_numbers(self):
        # Згенерувати 10000 випадкових чисел способом, указаним у варіанті.
        self.sigma = random.random()
        self.alpha = random.random()
        self.mu = [sum(np.random.uniform(size=12)) - 6 for _ in range(self.size)]

        self.randoms = [self.sigma * self.mu[i] + self.alpha for i in range(self.size)]

        # Знайти середнє і дисперсію цих випадкових чисел.
        self.mean = np.mean(self.randoms)
        self.dispersion = np.std(self.randoms)
        print(f'mean: {self.mean} \ndispersion: {self.dispersion}')

    def draw_hist(self):
        # Побудувати гістограму частот. По виду гістограми частот визначити вид закону розподілу -> нормальний (Гауса)
        gaussian_distribution = np.random.normal(size=self.size, loc=self.mean, scale=self.dispersion)
        seaborn.displot(gaussian_distribution, kind='kde', color='g')
        plt.show()
        seaborn.histplot(self.randoms, kde=True)
        plt.show()

    def check(self):
        # Відповідність заданому закону розподілу перевірити за допомогою критерію згоди ксі^2.
        _, p = stats.normaltest(self.randoms)
        approved = '' if p < 0.05 else 'not '
        print(f'Distribution is { approved }normal')

    def __repr__(self):
        return f'sigma: {self.sigma} \nalpha: {self.alpha}'


if __name__ == '__main__':
    print(Lab1())

