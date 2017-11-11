'''
This script creates a full schedule for a team. Accepts staff_list.csv and hours_list.csv as inputs (see below for details) and outputs rota.csv
'''

import gen

staff = staff_gen.generate('staff_list.csv')
hours = hours_gen.generate('hours_list.csv')

criteria = [
	member['week'][shift['week day']] == '',		#staff member not working that day
	member['max hours'] - member['current hours'] <= shift['end'] - shift['begin'],
													#enough hours left to do shift
	len([i for i in member['week'] if member['week'][i] != 0]) <5,
													#maximum 5 working days per week
	shift['week day'] not in member['days off']
]

def allocate (staff,hours,criteria):
  for member in staff:
    for shift in hours:
      if all(criteria):
        #allocate



