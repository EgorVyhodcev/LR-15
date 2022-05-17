#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polynom:
    def __init__(self, degree):
        self.__degree = degree
        self.__size = degree + 1
        self.__idx_list = []

    def get_size(self):
        return self.__size

    def get_idx_list(self):
        print(self.__idx_list[-1])
        return self.__idx_list

    def print_coef(self):
        print(self.__idx_list)

    def read_coef(self):
        for i in range(self.__size):
            c = float(input("Enter the coef: "))
            self.__idx_list.append(c)

    def count_x(self, x):
        res = sum(elem * x ** idx for idx, elem in enumerate(self.__idx_list))
        return res

    def sum_polynom(self, pol_deg, idx_list2):
        if self.__degree > pol_deg:
            res_idx = [0] * self.__size
            index = 0
            for idx, elem in enumerate(idx_list2):
                res_idx[idx] = elem + self.__idx_list[idx]
                index = idx
            for index in range(index + 1, self.__size):
                res_idx[index] = self.__idx_list[index]
            return res_idx
        else:
            res_idx = [0] * (pol_deg + 1)
            index = 0
            for idx, elem in enumerate(self.__idx_list):
                res_idx[idx] = elem + idx_list2[idx]
                index = idx
            for index in range(index + 1, pol_deg + 1):
                res_idx[index] = idx_list2[index]
            return res_idx

    def pol_subtraction(self, pol_deg, idx_list2):
        for idx in range(len(idx_list2)):
            idx_list2[idx] *= -1
        # print(idx_list2)
        res = self.sum_polynom(pol_deg, idx_list2)
        return res

    def multiply_pol(self, pol_deg, idx_list2):
        res_idx = [0] * (self.__degree + pol_deg + 1)
        for idx1, elem1 in enumerate(self.__idx_list):
            for idx2, elem2 in enumerate(idx_list2):
                res_idx[idx1 + idx2] += elem1 * elem2
        return res_idx

    def multiply_by_num(self, num):
        for idx in range(len(self.__idx_list)):
            self.__idx_list[idx] *= num
        return self.__idx_list

    def __eq__(self, val):
        if isinstance(val, Polynom):
            return self.__idx_list == val.__idx_list
        else:
            return len(self.__idx_list) == 1 and self.__idx_list[0] == val

    def __gt__(self, val):
        if isinstance(val, Polynom):
            return self.__idx_list[-1] > val.__idx_list[-1]
        else:
            return len(self.__idx_list) == 1 and self.__idx_list[0] > val

    def __lt__(self, val):
        if isinstance(val, Polynom):
            if len(self.__idx_list) <= len(val.__idx_list):
                return self.__idx_list[-1] < val.__idx_list[-1]
        else:
            return len(self.__idx_list) == 1 and self.__idx_list[0] > val

    def __ne__(self, val):
        if isinstance(val, Polynom):
            return not self.__idx_list == val.__idx_list
        else:
            return not len(self.__idx_list) == 1 and self.__idx_list[0] == val

    def differentiation(self):
        res = []
        for idx, elem in enumerate(self.__idx_list):
            if idx > 0:
                res.append(elem * idx)
        return res

    def integrate(self):
        res = [0] * (self.__size + 1)
        for idx, elem in enumerate(self.__idx_list):
            res[idx + 1] = elem / (idx + 1)
        return res

    def __getitem__(self, item):
        return self.__idx_list[item]


if __name__ == '__main__':
    pol = Polynom(4)
    pol.print_coef()
    pol.read_coef()
    pol.print_coef()
    print(f"Index overload: {pol[0]}, {pol[-1]}")
    print(f"Polynom value: {pol.count_x(3)}")
    pol2 = Polynom(5)
    pol2.read_coef()
    pol2.print_coef()
    print(f"Sum of polynoms: {pol.sum_polynom(5, pol2.get_idx_list())}")
    print(f"Polynom substract: {pol.pol_subtraction(5, pol2.get_idx_list())}")
    print(
        f"Polynom multiplication: {pol.multiply_pol(5, pol2.get_idx_list())}"
          )
    print(f"Polynom mult. by number: {pol.multiply_by_num(5)}")
    pol3 = Polynom(4)
    pol3.read_coef()
    pol3.print_coef()
    print(f"pol == pol3: {pol == pol3}")
    print(f"pol > pol3: {pol > pol3}")
    print(f"pol < pol3: {pol < pol3}")
    print(f"pol != pol3: {pol != pol3}")
    print(f"Polynom differentiation: {pol.differentiation()}")
    print(f"Polynom integration: {pol.integrate()}")
