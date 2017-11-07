'''
This script creates a full schedule for a team. Accepts staff_list.csv and hours_list.csv as inputs (see below for details) and outputs rota.csv
'''

import staff_gen
import hours_gen

staff_gen.generate('staff_list.csv')
hours_gen.generate('hours_list.csv')







#from staff_dir import staff
#from hours_dir import hours

