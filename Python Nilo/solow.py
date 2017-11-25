# -*- coding: utf-8 -*-
# Modelo de Solow
import numpy as np


class Solow():
    def __init__(self, k_inicial=0.0, depreciacao=0.0, poupanca=0.0, tech0=0.0, alpha=0.0, pop_delta=0.0):
        self.define(k_inicial, depreciacao, poupanca, tech0, alpha, pop_delta)

    def define(self, k_inicial, depreciacao, poupanca, tech0, alpha, pop_delta):
        self.k_inicial = k_inicial
        self.depreciacao = depreciacao
        self.poupanca = poupanca
        self.tech0 = tech0
        self.alpha = alpha
        self.pop_delta = pop_delta
        self.k = self.k_inicial
        self.last_k = self.k

    def show_states(self):
        print()
        print("%25s" % "---- Modelo de Solow -----")
        print("%20s %5.2f" % ("Capital Inicial:", self.k_inicial))
        print("%20s %5.2f" % ("Depreciação:", self.depreciacao))
        print("%20s %5.2f" % ("Poupança:", self.poupanca))
        print("%20s %5.2f" % ("Tech. Inicial:", self.tech0))
        print("%20s %5.2f" % ("Alpha:", self.alpha))
        print("%20s %5.2f" % ("Cresc. Pop.:", self.pop_delta))
        print("%20s %5.2f" % ("Capital:", self.k))
        print()

    def next_k(self):
        return ((1 - self.depreciacao) * self.k + self.poupanca * self.k ** self.alpha)/(1 + self.pop_delta)

    def refresh_k(self):
        self.last_k = self.k
        self.k = self.next_k()

    def delta_k(self):
        return self.k - self.last_k

while True:

    print("\nIniciando o modelo")

    model = Solow()

    k = float(input(" Capital Inicial: "))
    d = float(input(" Depreciação: "))
    p = float(input(" Poupança: "))
    t = float(input(" Tech. Inicial: "))
    a = float(input(" Alpha: "))
    c = float(input(" Cresc. Pop.: "))
    model.define(k, d, p, t, a, c)
    n = 0

    model.show_states()

    print(" t  |  k    | delta(k)%")

    while (model.delta_k() >= 0.001 or n == 0):
        print("%2d  | %5.2f | %5.3f" % (n, model.k, model.delta_k()))
        model.refresh_k()
        n += 1

    print("\nEstado estacionário: k = %5.2f\n" % model.k)

