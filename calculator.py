"""
Simple Tkinter calculator.

Usage:
	python calculator.py

Buttons: digits 0-9, ., +, -, *, /, C (clear), = (evaluate).
Keyboard: type numbers/operators, Enter to evaluate, Backspace to delete, C to clear.

This file provides a small GUI for basic arithmetic. The evaluator blocks '**' and '//' and only allows digits,
operators, parentheses and decimal points.
"""

import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Calculator")
		self.resizable(False, False)
		self._create_widgets()
		self._bind_keys()

	def _create_widgets(self):
		self.display_var = tk.StringVar(value="0")

		display = ttk.Entry(self, textvariable=self.display_var, font=(None, 20), justify='right', state='readonly')
		display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

		btn_specs = [
			('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
			('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
			('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
			('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
		]

		for (text, r, c) in btn_specs:
			action = (lambda char=text: self._on_button(char))
			ttk.Button(self, text=text, command=action).grid(row=r, column=c, sticky='nsew', padx=3, pady=3)

		eq_button = ttk.Button(self, text='=', command=self._evaluate)
		eq_button.grid(row=5, column=0, columnspan=4, sticky='nsew', padx=3, pady=(0,5))

		# configure grid weights
		for i in range(6):
			self.rowconfigure(i, weight=1)
		for j in range(4):
			self.columnconfigure(j, weight=1)

	def _bind_keys(self):
		for key in '0123456789.+-*/':
			self.bind(key, lambda e, k=key: self._on_button(k))
		self.bind('<Return>', lambda e: self._evaluate())
		self.bind('<KP_Enter>', lambda e: self._evaluate())
		self.bind('<BackSpace>', lambda e: self._backspace())
		self.bind('c', lambda e: self._clear())
		self.bind('C', lambda e: self._clear())

	def _on_button(self, char: str):
		cur = self.display_var.get()
		if cur == '0' and char not in '.+-*/':
			new = char
		elif cur == '0' and char in '.+-*/':
			new = cur + char
		else:
			if cur.endswith('='):
				# last was result, start new input unless operator
				cur = cur.rstrip('=')
				if char in '+-*/':
					new = cur + char
				else:
					new = char
			else:
				new = cur + char

		self.display_var.set(new)

	def _clear(self):
		self.display_var.set('0')

	def _backspace(self):
		cur = self.display_var.get()
		if len(cur) <= 1:
			self.display_var.set('0')
		else:
			self.display_var.set(cur[:-1])

	def _safe_eval(self, expression: str):
		# Allow only digits, operators, dot and parentheses
		allowed = set('0123456789+-*/.() ')
		if not set(expression) <= allowed:
			raise ValueError('Invalid characters in expression')
		# Prevent accidental double operators like '**' or '//' if undesired
		if '**' in expression or '//' in expression:
			raise ValueError('Unsupported operator')
		# Evaluate in a minimal namespace
		return eval(expression, {'__builtins__': None}, {})

	def _evaluate(self):
		expr = self.display_var.get()
		try:
			result = self._safe_eval(expr)
			self.display_var.set(str(result) + '=')
		except Exception:
			self.display_var.set('Error')


def main():
	app = Calculator()
	app.mainloop()


if __name__ == '__main__':
	main()

