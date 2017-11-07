# Rota
Schedule generator for teams


/Flow/
main calls:
  staff_gen
    converts staff_list.csv into module(/json?)
  hours_gen
    converts hours_list.csv into module
  THEN uses list of conditions to assign people to shifts (possibly via calling other module?)
  exports module and csv (for easy import into excel)

important - double check input values; break flow if they don't match, print error; may need to refresh on regex (multiple regex options - list?)

rules:
  max hours allowed
  skills required
  not working on same day
  (optional/future version) - min hours rest
  respect days prev set as day off/never working those week days/holidays
  min 2 days off/week (potentially redudant with max hours allowed)
  
final check-through includes:
  all rules for each instance must be respected
  check for imbalance in hours worked (min and *submax* hour limits?)
  if any shifts are unassigned
    check for people off that day and assign if possible
    else think of system for minimum reassignment to cover gap (1 gets shift changed, so that 2 can fill void shift)
