# Endless Sky Mission Builder Style Guide

All code should adhere to PEP8, and [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) 

In addition to this, the are two types of extensions to consider, CRITICAL and Quality of Life (QoL). Any PR that does not conform to the CRITICAL section of this style guide will not be accepted. Expect me to ask you to add it if your PR does not include the QoL extensions.

---
## Critical

### 1) Importing ESMB code
Inconsistent imports can cause failure to build, which means I or M\*C\*O have to spend hours futzing with the build tool to figure out what is wrong. We have determined that the following will work 100% of the time.

If you need a single module from a single package, and you don't need any other packages, do the following:
```python
from src.path.to.module import my_module
```

Example from current source:
```python
from src.model.model_data_parsers import MissionParser
```

If you need to import a package to use many of the modules inside, do the following

```python
# the import
import src.path.to.package as package

# using something from the module
module_instance = package.my_module(args)
```

Example from current source:
```python
import src.gui.editor as editor

self.option_pane = editor.OptionPane(self.gui)
```

---

## QoL
These things make the code easier to read, so I'm gonna ask that any code added to this project includes this