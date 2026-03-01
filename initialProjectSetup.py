import tkinter as tk
import heapq, math, random, time

ROWS, COLS, CELL = 15, 20, 30
E, W, S, G, F, V, P, A = range(8)

COLOR = { E:"#1e1e2e", W:"#585b70", S:"#89b4fa", G:"#f38ba8",
          F:"#f9e2af",  V:"#3b82f6", P:"#a6e3a1", A:"#cba6f7" }
