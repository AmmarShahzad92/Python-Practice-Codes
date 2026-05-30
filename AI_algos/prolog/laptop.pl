% LAPTOP 





:- dynamic yes/1, no/1. 
start :- 
write('LAPTOP DIAGNOSIS SYSTEM'), nl, 
write('Answer questions with yes. or no.'), nl, nl, 
diagnose(Issue), 
nl, write('Likely issue: '), write(Issue), nl, nl, 
suggest(Issue), 
undo. 
% Diagnosis rules 
diagnose(battery_issue)    :- battery_problems, !. 
diagnose(overheating)      :- overheating_symptoms, !. 
diagnose(software_crash)   :- software_crash_symptoms, !. 
diagnose(hardware_failure) :- hardware_failure_symptoms, !. 
diagnose(unknown) :- nl, fail. 
% Symptom groups 
battery_problems :- write('Unable to determine. Recommend professional check.'), 
verify(battery_drains_fast), 
verify(not_charging). 
overheating_symptoms :- 
verify(system_gets_hot), 
verify(fan_runs_loud). 
software_crash_symptoms :- 
verify(blue_screen) ; 
(verify(frequent_freeze), verify(software_updates_recently_failed)). 
hardware_failure_symptoms :- 
verify(beep_codes), 
verify(peripheral_not_detected). 
% Suggestions 
suggest(battery_issue) :- write('Check battery health, replace battery or charger, calibrate 
battery.'), nl. 
suggest(overheating)   :- write('Clean vents/fan, reapply thermal paste, check fan speed, 
avoid heavy load.'), nl. 
suggest(software_crash):- write('Boot in safe mode, check logs, uninstall recent updates, 
reinstall OS if necessary.'), nl. 
suggest(hardware_failure):- write('Check RAM seating, run diagnostics, consult repair 
center.'), nl. 
% Ask / verify / undo (same as before) 
ask(Question) :- 
write('Does the laptop have: '), write(Question), write('? (yes/no): '), 
read(Response), nl, 
( (Response == yes ; Response == y) -> assert(yes(Question)) ; assert(no(Question)), fail ). 
verify(S) :- (yes(S) -> true ; (no(S) -> fail ; ask(S))). 
undo :- retract(yes(_)), fail. 
undo :- retract(no(_)), fail. 
undo. 
:- initialization(start).