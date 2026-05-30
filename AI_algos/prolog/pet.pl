% PET 



:- dynamic yes/1, no/1. 
% Start point 
start :- 
write('PET RECOMMENDATION SYSTEM'), nl, 
write('Answer questions with yes. or no.'), nl, nl, 
recommend(Pet), 
nl, write('Recommended pet: '), write(Pet), nl, nl, 
give_tips(Pet), 
undo. 
% Recommendation rules 
recommend(dog)  :- prefers(active), has_space, likes_outdoor, !. 
recommend(cat)  :- prefers(independent), indoor_ok, !. 
recommend(fish) :- prefers(low_maintenance), small_space, !. 
recommend(bird) :- prefers(social), can_handle_noise, !. 
recommend(no_pet) :- prefers(no_pets), !. 
recommend(no_pet) :- write('No suitable pet recommendation.'), nl, fail. 
% Additional tips 
give_tips(dog)  :- write('Tips: Daily walks, training, vaccinations.'), nl. 
give_tips(cat)  :- write('Tips: Litter, scratching post, indoor play.'), nl. 
give_tips(fish) :- write('Tips: Tank maintenance, water quality checks.'), nl. 
give_tips(bird) :- write('Tips: Cage size, social time, toys.'), nl. 
give_tips(no_pet) :- write('Consider volunteering at shelters if you like animals.'), nl. 
% Preference predicates 
prefers(active)            
:- verify(wants_active_pet). 
prefers(independent)       
:- verify(wants_independent_pet). 
prefers(low_maintenance)   :- verify(wants_low_maintenance). 
prefers(social):- verify(wants_social_pet). 
prefers(no_pets):- verify(wants_no_pet). 
has_space     :- verify(has_large_space). 
small_space   :- verify(has_small_space). 
indoor_ok     :- verify(prefers_indoor). 
likes_outdoor :- verify(enjoys_outdoor_activity). 
can_handle_noise :- verify(can_handle_noise). 
% Question mechanism 
ask(Question) :- 
write('Does the person: '), write(Question), write('? (yes/no): '), 
read(Response), nl, 
( (Response == yes ; Response == y) -> assert(yes(Question)) ; assert(no(Question)), fail ). 
verify(S) :- (yes(S) -> true ; (no(S) -> fail ; ask(S))). 
% Undo assertions 
undo :- retract(yes(_)), fail. 
undo :- retract(no(_)), fail. 
undo. 
% Initialize when file loaded (optional) 
:- initialization(start).