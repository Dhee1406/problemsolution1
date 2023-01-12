#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Newspaper:
    def __init__(self, name: str, monday: float, tuesday: float, wednesday: float,
               thursday: float, friday: float, saturday: float, sunday: float):
        self.name = name
        self.prices = {
            "Monday": monday,
            "Tuesday": tuesday,
            "Wednesday": wednesday,
            "Thursday": thursday,
            "Friday": friday,
            "Saturday": saturday,
            "Sunday": sunday
        }

    def get_weekly_price(self) -> float:
        return sum(self.prices.values())


class SubscriptionCalculator:
    def __init__(self, budget: float, newspapers: list[Newspaper]):
        self.budget = budget
        self.newspapers = newspapers

    def get_possible_combinations(self) -> list[tuple[str, str]]:
        combinations = []
        for newspaper1 in self.newspapers:
            for newspaper2 in self.newspapers:
                if newspaper1 == newspaper2:
                    continue
                total_price = newspaper1.get_weekly_price() + newspaper2.get_weekly_price()
                if total_price <= self.budget:
                    combinations.append((newspaper1.name, newspaper2.name))
        return combinations



toi = Newspaper("TOI", 3, 3, 3, 3, 3, 5, 6)
hindu = Newspaper("Hindu", 2.5, 2.5, 2.5, 2.5, 2.5, 4, 4)
et = Newspaper("ET", 4, 4, 4, 4, 4, 4, 10)
bm = Newspaper("BM", 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5)
ht = Newspaper("HT", 2, 2, 2, 2, 2, 4, 4)

calculator = SubscriptionCalculator(int(input()), [toi, hindu, et, bm, ht])
combinations = calculator.get_possible_combinations()
print(combinations)

calculator = SubscriptionCalculator(int(input()), [toi, hindu, et, bm, ht])
combinations = calculator.get_possible_combinations()
print(combinations)


# In[ ]:




