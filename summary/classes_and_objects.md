*🐍 Python Learning — Classes & Objects*
*🎥 Format: YouTube Tutorial*

Hey everyone! In this session we moved on to *Classes and Objects* — one of the core building blocks for organizing code.

---

*📌 Topics Covered*

*1. Defining a Class*
Learned the `class` keyword and how variables and functions can live inside a class — no curly braces needed, just indentation.

*2. Creating an Object (Instance)*
Created an object by assigning `ClassName()` to a variable — no `new` keyword required, unlike Java/Swift.

*3. Accessing & Updating Variables*
Accessed class variables with `object.variable` and saw that updating the variable on one object doesn't affect another object of the same class.

*4. Calling Functions on an Object*
Defined a function inside a class and called it via `object.function()`. Every function inside a class must take `self` as its first parameter so it has access to the instance.

*5. The `__init__` Constructor*
Learned that `__init__` is a special function that runs automatically when an object is created, letting you set instance values (like a default) at initialization time instead of after.

*6. Exercise: Write It From Scratch*
Wrote `MyClass` with a `value` (default `10`), an `__init__(self, initialValue)` constructor, and a `printValue(self)` function. Hit a couple of classic beginner mistakes along the way — forgetting `self.` prefix and using the wrong string-format syntax (`%i` needs `self.value` after the `%`, not just `value`) — good reminder that writing code yourself (not copy-pasting) is what makes the syntax stick.

---

*💻 Files*
• `12_classes.py` — class definition, `__init__` constructor, instance method, creating & using an object

*🏠 Homework:*
There's an unfinished exercise from last time we still need to circle back to — stay tuned for the next video where we'll wrap that up and go further into classes (and maybe dictionaries too).

See you in the next video! 🚀
