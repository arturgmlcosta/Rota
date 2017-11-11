# Rota
Schedule generator for teams

Takes in csv files (export from excel)
	staff_list.csv
		First line: 'Name', 'Skills', 'Days off', etc
		Remaindeer: employee entries
	hours_list.csv
		First line: 'Shift', 'Day', 'Skills', 'From', 'To',etc
		Remainder: shift entries

Spits out csv files (import to excel)
	rota by day
	rota by employee
	daily allocations
		slice - day
	costings
		budgeted hours by hour
		total per day
		daily budget (hours) and people alocated per section


'''
Main:
	converts csv files into object lists and exports them to new module
		checks: break flow if input format != expected, write into txt file error message
	allocates staff to shifts following list of rules
	assesses result based on check
		apply changes as needed
	exports results

rules:
	max hours allowed
	skills required
	not working on same day
	(optional/future version) - min hours rest
	respect days prev set as day off/never working those week days/holidays
	min 2 days off/week (potentially redudant with max hours allowed)
  
final check-through includes:
	all rules for each instance must be respected
	check for imbalance in hours worked
		(*min* and *submax* hour limits?)
	if any shifts are unassigned
		check for people off that day and assign if possible
		else think of system for minimum reassignment to cover gap (1 gets shift changed, so that 2 can fill void shift)
