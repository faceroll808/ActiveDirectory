import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("activedirectory:///?User=cn=Bob F,ou=Employees,dc=Domain&Password=bob123&Server=10.0.1.2&Port=389")