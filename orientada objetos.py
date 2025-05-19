class Exercise:
    def __init__(self, name, type, muscle_group, equipment, difficulty):
        self.name = name
        self.type = type
        self.muscle_group = muscle_group
        self.equipment = equipment
        self.difficulty = difficulty

    def perform(self):
        print(f"Doing {self.name} for {self.muscle_group} muscles")

bench_press = Exercise("Bench Press", "Strength", "Chest", "Barbell", "Intermediate")
print(f"Bench Press: {bench_press.name}, {bench_press.type}, {bench_press.muscle_group}, {bench_press.equipment}, {bench_press.difficulty}")

squat = Exercise("Squat", "Strength", "Legs", "Barbell", "Intermediate")
print(f"Squat: {squat.name}, {squat.type}, {squat.muscle_group}, {squat.equipment}, {squat.difficulty}")

deadlift = Exercise("Deadlift", "Strength", "Back", "Barbell", "Advanced")
print(f"Deadlift: {deadlift.name}, {deadlift.type}, {deadlift.muscle_group}, {deadlift.equipment}, {deadlift.difficulty}")

pull_up = Exercise("Pull-up", "Bodyweight", "Back", "Bar", "Intermediate")
print(f"Pull-up: {pull_up.name}, {pull_up.type}, {pull_up.muscle_group}, {pull_up.equipment}, {pull_up.difficulty}")

bicep_curl = Exercise("Bicep Curl", "Isolation", "Biceps", "Dumbbells", "Beginner")
print(f"Bicep Curl: {bicep_curl.name}, {bicep_curl.type}, {bicep_curl.muscle_group}, {bicep_curl.equipment}, {bicep_curl.difficulty}")


class Supplement:
    def __init__(self, name, purpose, form, flavor, price):
        self.name = name
        self.purpose = purpose
        self.form = form
        self.flavor = flavor
        self.price = price

    def consume(self):
        print(f"Taking {self.name} for {self.purpose}")

whey = Supplement("Whey Protein", "Muscle Recovery", "Powder", "Chocolate", "40$")
print(f"Whey: {whey.name}, {whey.purpose}, {whey.form}, {whey.flavor}, {whey.price}")

creatine = Supplement("Creatine", "Strength & Power", "Powder", "Unflavored", "25$")
print(f"Creatine: {creatine.name}, {creatine.purpose}, {creatine.form}, {creatine.flavor}, {creatine.price}")

bcaa = Supplement("BCAA", "Muscle Retention", "Powder", "Watermelon", "30$")
print(f"BCAA: {bcaa.name}, {bcaa.purpose}, {bcaa.form}, {bcaa.flavor}, {bcaa.price}")

preworkout = Supplement("Pre-Workout", "Energy Boost", "Powder", "Blue Raspberry", "35$")
print(f"Preworkout: {preworkout.name}, {preworkout.purpose}, {preworkout.form}, {preworkout.flavor}, {preworkout.price}")

multivitamin = Supplement("Multivitamin", "Overall Health", "Tablet", "None", "15$")
print(f"Multivitamin: {multivitamin.name}, {multivitamin.purpose}, {multivitamin.form}, {multivitamin.flavor}, {multivitamin.price}")

class WorkoutPlan:
    def __init__(self, name, focus, days_per_week, duration, coach):
        self.name = name
        self.focus = focus
        self.days_per_week = days_per_week
        self.duration = duration
        self.coach = coach

    def start(self):
        print(f"Starting the {self.name} plan designed by {self.coach}")

plan1 = WorkoutPlan("Mass Builder", "Hypertrophy", 5, "8 weeks", "Coach Mike")
print(f"Plan1: {plan1.name}, {plan1.focus}, {plan1.days_per_week} days, {plan1.duration}, {plan1.coach}")

plan2 = WorkoutPlan("Shred Phase", "Cutting", 6, "6 weeks", "Coach Laura")
print(f"Plan2: {plan2.name}, {plan2.focus}, {plan2.days_per_week} days, {plan2.duration}, {plan2.coach}")

plan3 = WorkoutPlan("Strength Camp", "Strength", 4, "10 weeks", "Coach Dan")
print(f"Plan3: {plan3.name}, {plan3.focus}, {plan3.days_per_week} days, {plan3.duration}, {plan3.coach}")

plan4 = WorkoutPlan("Full Body Burn", "General Fitness", 3, "4 weeks", "Coach Nina")
print(f"Plan4: {plan4.name}, {plan4.focus}, {plan4.days_per_week} days, {plan4.duration}, {plan4.coach}")

plan5 = WorkoutPlan("Leg Mastery", "Leg Hypertrophy", 2, "6 weeks", "Coach Rob")
print(f"Plan5: {plan5.name}, {plan5.focus}, {plan5.days_per_week} days, {plan5.duration}, {plan5.coach}")
