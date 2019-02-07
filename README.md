# conditions_check
Checks conditions and raises an Exception if contition is False

An annoying part of coding are all those pre-condition checks on the beginning of most methods. 
To ease this pain, I wrote a small helper func to do those checks and raise an error if a check fails.

You pass a dict with all the conditions as keys you want to be True and as value the error-message. 
If any of the conditions is False, an Exception is raised with that message. 

You need at least Python3.6 to use f-strings ;), works with Python 3.7

Example:
```
checks = {
  hasattr(cls, "supported_types")        : f"{cls} needs supported_types-set",
  hasattr(cls, "supported_types_mapping"): f"{cls} needs supported_types_mapping",
  }

pre_condistions_check(checks)
```
