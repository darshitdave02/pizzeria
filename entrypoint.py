#!/usr/bin/env python3

import os
import subprocess

# Apply migrations
subprocess.run(["python3", "manage.py", "migrate"])

# Load seed data
subprocess.run(["python3", "manage.py", "loaddata", "orderApis/fixtures/cheese_seed.json"])
subprocess.run(["python3", "manage.py", "loaddata", "orderApis/fixtures/pizzabase_seed.json"])
subprocess.run(["python3", "manage.py", "loaddata", "orderApis/fixtures/topping_seed.json"])
subprocess.run(["python3", "manage.py", "loaddata", "orderApis/fixtures/pizza_seed.json"])
subprocess.run(["python3", "manage.py", "loaddata", "orderApis/fixtures/order_seed.json"])


# Start the Django app
os.system("python3 manage.py runserver 0.0.0.0:8000")
