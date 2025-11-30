import os
from dotenv import find_dotenv

print("Env before load:", repr(os.getenv("USERNAME")))
print("find_dotenv ->", repr(find_dotenv()))
