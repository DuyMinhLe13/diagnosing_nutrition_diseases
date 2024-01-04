def collect_data():
    Habits = set()
    Symptoms = set()
    patient_name = ''
    patient_phone_number = ''
    print('Welcome to the consulting system for examination and treatment of nutritional diseases.!')


    ######################
    # HABITS
    ######################

    print('First, we want to survey your unhealthy eating habits and behaviors')
    while True:
        print('Below is a survey about your nutrition (Please enter the order number to choose):')
        print('1. Good, likes to eat salty foods (H05)')
        print("2. Don't care about the amount of salt in food (H06)")
        print('3. Eat less calcium-rich foods (H07)')
        print('4. Not conscious, concerned about getting enough vitamin D (H08)')
        print('5. Eat less foods rich in vitamin B12 (H09)')
        print('6. Eat less iron-rich foods (H16)')
        print('7. Eat a lot of foods that hinder iron absorption such as tea, coffee, ... (H17)')
        print('8. Eat less protein-rich foods (H19)')
        print('9. Not interested in nutritional mechanism (H23)')
        print('10. Skip')
        try:
            option = int(input())
            if option < 1 or option > 10:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Habits.add(5)
            elif option == 2: Habits.add(6)
            elif option == 3: Habits.add(7)
            elif option == 4: Habits.add(8)
            elif option == 5: Habits.add(9)
            elif option == 6: Habits.add(16)
            elif option == 7: Habits.add(17)
            elif option == 8: Habits.add(19)
            elif option == 9: Habits.add(23)
            elif option == 10: break
            print(f'The unhealthy habits you are having are H{sorted(list(Habits))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey about your daily eating habits (Please enter the order number to choose):')
        print('1. Not eating regularly and on time (H01)')
        print('2. Eat processed foods (H04)')
        print('3. Drink some water (H12)')
        print('4. Eat less vegetables or fruits (H14)')
        print('5. Eating food of unknown origin and quality (H20)')
        print('6. Diet (H21)')
        print('7. Eat less, lazy to eat (H22)')
        print('8. Skip')

        try:
            option = int(input())
            if option < 1 or option > 8:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Habits.add(1)
            elif option == 2: Habits.add(4)
            elif option == 3: Habits.add(12)
            elif option == 4: Habits.add(14)
            elif option == 5: Habits.add(20)
            elif option == 6: Habits.add(21)
            elif option == 7: Habits.add(22)
            elif option == 8: break
            print(f'The unhealthy habits you are having are H{sorted(list(Habits))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey about your physical health and sleep (Please enter the order number to choose):')
        print('1. Little, lazy physical activity (H02)')
        print('2. Sleep little, not enough sleep (H03)')
        print('3. Skip')

        try:
            option = int(input())
            if option < 1 or option > 3:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Habits.add(2)
            elif option == 2: Habits.add(3)
            elif option == 3: break
            print(f'The unhealthy habits you are having are H{sorted(list(Habits))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey about your habit of using stimulants and unhealthy foods (Please enter the order number to select):')
        print('1. Often drink alcoholic beverages (H10)')
        print('2. Smoking traditional cigarettes or e-cigarettes (H11)')
        print('3. Drink soft drinks or carbonated water (H13)')
        print('4. Skip')

        try:
            option = int(input())
            if option < 1 or option > 4:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Habits.add(10)
            elif option == 2: Habits.add(11)
            elif option == 3: Habits.add(13)
            elif option == 4: break
            print(f'The unhealthy habits you are having are H{sorted(list(Habits))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey about your habits of using functional foods (Please enter the order number to choose):')
        print('1. Use of diuretics (H15)')
        print('2. Using some drugs and functional foods without paying attention to the ingredients on the packaging (H18)')
        print('3. Skip')

        try:
            option = int(input())
            if option < 1 or option > 3:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Habits.add(15)
            elif option == 2: Habits.add(18)
            elif option == 3: break
            print(f'The unhealthy habits you are having are H{sorted(list(Habits))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')


    ######################
    # SYMPTOMS
    ######################

    print('Next, we want to survey the symptoms you have recently experienced.')

    while True:
        print('Below is a survey of your external symptoms (Please enter the order number to select):')
        print('1. Weight gain (S01)')
        print('2. Edema (S07)')
        print('3. Brittle, weak nails (S16)')
        print('4. Weak teeth (S17)')
        print('5. Hair loss (S24)')
        print('6. Dry, wrinkled skin (S26)')
        print('7. Weight loss (S27)')
        print('8. Skip')
        try:
            option = int(input())
            if option < 1 or option > 8:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Symptoms.add(1)
            elif option == 2: Symptoms.add(7)
            elif option == 3: Symptoms.add(16)
            elif option == 4: Symptoms.add(17)
            elif option == 5: Symptoms.add(24)
            elif option == 6: Symptoms.add(26)
            elif option == 7: Symptoms.add(27)
            elif option == 8: break
            print(f'The symptoms you are having are S{sorted(list(Symptoms))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey of your movement-related symptoms (Please enter a serial number to select):')
        print('1. Joint pain (S03)')
        print('2. Prone to bone fractures, or osteoporosis (S13)')
        print('3. Bone pain (S14)')
        print('4. Cramps (S15)')
        print('5. Reduced muscle mass (S25)')
        print('6. Skip')
        try:
            option = int(input())
            if option < 1 or option > 6:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Symptoms.add(3)
            elif option == 2: Symptoms.add(13)
            elif option == 3: Symptoms.add(14)
            elif option == 4: Symptoms.add(15)
            elif option == 5: Symptoms.add(25)
            elif option == 6: break
            print(f'The symptoms you are having are S{sorted(list(Symptoms))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey about symptoms related to your mental and neurological health (Please enter the order number to select):')
        print('1. Fatigue, weakness (S05)')
        print('2. Headache (S06)')
        print('3. Often nauseous (S08)')
        print('4. History of stroke (S10)')
        print('5. Difficulty concentrating (S22)')
        print('6. Dizziness (S23)')
        print('7. Skip')
        try:
            option = int(input())
            if option < 1 or option > 7:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Symptoms.add(5)
            elif option == 2: Symptoms.add(6)
            elif option == 3: Symptoms.add(8)
            elif option == 4: Symptoms.add(10)
            elif option == 5: Symptoms.add(22)
            elif option == 6: Symptoms.add(23)
            elif option == 7: break
            print(f'The symptoms you are having are S{sorted(list(Symptoms))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')


    while True:
        print('Below is a survey of your circulatory system symptoms (Please enter the order number to choose):')
        print('1. Hypertension (S09)')
        print('2. Heart failure (S11)')
        print('3. Numbness in limbs (S18)')
        print('4. Anemia (S19)')
        print('5. Skip')
        try:
            option = int(input())
            if option < 1 or option > 5:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Symptoms.add(9)
            elif option == 2: Symptoms.add(11)
            elif option == 3: Symptoms.add(18)
            elif option == 4: Symptoms.add(19)
            elif option == 5: break
            print(f'The symptoms you are having are S{sorted(list(Symptoms))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey about your respiratory symptoms (Please enter the order number to select):')
        print('1. Shortness of breath (S02)')
        print('2. Snoring (S04)')
        print('3. Skip')
        try:
            option = int(input())
            if option < 1 or option > 3:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Symptoms.add(2)
            elif option == 2: Symptoms.add(4)
            elif option == 3: break
            print(f'The symptoms you are having are S{sorted(list(Symptoms))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')

    while True:
        print('Below is a survey about symptoms related to your digestion and excretion (Please enter the order number to choose):')
        print('1. History of kidney stones (S12)')
        print('2. Indigestion, bloating, poor digestion (S20)')
        print('3. Frequent urination, frequent urination (S21)')
        print('4. Skip')
        try:
            option = int(input())
            if option < 1 or option > 4:
                print('There is no option with the number you just entered! Please enter again!')
                continue
            elif option == 1: Symptoms.add(12)
            elif option == 2: Symptoms.add(20)
            elif option == 3: Symptoms.add(21)
            elif option == 4: break
            print(f'The symptoms you are having are S{sorted(list(Symptoms))}')
            print('+++++++++++++++++++++++++')
        except: print('You entered the wrong syntax! Please enter again!')

    print('---------------------------------------------------------------------------')


    return sorted(list(Habits)), sorted(list(Symptoms))




# @title
def solution(disease):
    if disease == 1:
        print("""You may be overweight or obese. You need to improve your health by the following methods:
   - Diet: Elderly people need to build a healthy, balanced diet, reducing calorie intake.
   - Physical activity: Elderly people need to increase physical activity, at least 30 minutes a day.
   - Change lifestyle: Elderly people need to change some unhealthy living habits such as smoking, drinking alcohol,...
              """)
    if disease == 2:
        print("""You may have sodium overload. You need to improve your health by the following methods:
  - Limit eating processed foods: Processed foods often contain a lot of salt. Elderly people should replace processed foods with fresh foods.
  - Season foods with less salt: Elderly people should learn how to season foods with less salt. Instead of using salt for seasoning, elderly people can use alternative spices such as ginger, garlic, pepper,...
  - Check food labels: Elderly people should check food labels to know the amount of salt in the product.
              """)
    if disease == 3:
        print("""You may have calcium deficiency. You need to improve your health by the following methods:
- Increase calcium supplementation: Elderly people need to supplement calcium from foods and/or functional foods.
- Increase physical activity: Physical activity helps increase calcium absorption.
- Weight control: Being overweight or obese can increase the risk of osteoporosis.
- Don't smoke: Smoking reduces bone density.
- Limit alcohol consumption: Drinking alcohol reduces calcium absorption.
              """)
    if disease == 4:
        print("""You may have vitamin B2 deficiency. You need to improve your health by the following methods:
- Supplement through diet:

Elderly people can supplement vitamin B12 through their diet by eating lots of foods rich in vitamin B12, such as:

+ Meat: Beef, pork, chicken,...
+ Fish: Salmon, tuna, sardines,...
+ Eggs: Chicken eggs, duck eggs,...
+ Milk and dairy products: Fresh milk, yogurt, cheese,...
Elderly people should add these foods to their daily diet to ensure enough vitamin B12 is provided to the body.

- Oral supplementation:
If the elderly cannot supplement vitamin B12 through diet, they can supplement it orally. Currently, there are many types of functional foods supplemented with vitamin B12. Elderly people should consult a doctor before use.

In addition to vitamin B12 supplementation, elderly people also need to pay attention to the following issues to improve symptoms of vitamin B12 deficiency:

- Increase physical activity: Physical activity helps increase blood circulation and improve nerve function.
Get enough sleep: Getting enough sleep helps the body recover and regenerate energy.
Reduce stress: Stress can worsen symptoms of vitamin B12 deficiency.
              """)
    if disease == 5:
        print("""You may become dehydrated. You need to improve your health by the following methods:
- Drink water: This is the simplest and most effective solution to compensate for lost water. Elderly people should drink water regularly, especially when exercising, in hot weather and when sick.

- Drink fruit and vegetable juices: Fruits and vegetables contain a lot of water, helping to replenish water and nutrients for the body.

- Eat foods rich in water: Some foods rich in water include soup, porridge, milk,...

- Avoid drinking alcohol: Alcohol can increase the risk of dehydration.

- Increase physical activity: Physical activity helps the body retain water.
              """)

    if disease == 6:
        print("""You may have an iron deficiency. You need to improve your health by the following methods:
- Eat lots of iron-rich foods: Iron-rich foods include red meat, poultry, fish, eggs, beans, dark green leafy vegetables, etc. Elderly people should eat a variety of these foods to ensure Provide enough iron for the body.
- Limit eating foods that hinder iron absorption: Some foods can hinder iron absorption, such as tea, coffee, milk,... Elderly people should limit eating these foods. .
- Don't drink a lot of alcohol: Alcohol can reduce the body's ability to absorb iron.
- Iron supplementation as prescribed by the doctor: If the elderly have been diagnosed with iron deficiency, iron supplementation is required as prescribed by the doctor.
              """)

    if disease == 7:
        print("""You may have a protein deficiency. You need to improve your health by the following methods:
- Eat lean meat: Lean meat is a source of high quality protein. Elderly people should eat about 2-3 servings of lean meat per day.
- Eat fish: Fish is a source of high-quality protein and contains many healthy omega-3 fatty acids. Elderly people should eat about 2-3 servings of fish per week.
- Eat eggs: Eggs are a source of high-quality and inexpensive protein. Elderly people should eat about 2-3 eggs per day.
- Eat milk and dairy products: Milk and dairy products are a source of high quality protein. Elderly people should drink about 2-3 glasses of milk per day.
- Eat beans: Beans are a cheap and high-quality source of protein. Elderly people should eat about 2-3 servings of beans per day.

Additionally need:
- Eat lots of protein-rich foods: Protein-rich foods include meat, poultry, fish, eggs, milk, beans, etc. Elderly people should eat a variety of these foods to ensure adequate supply. protein for the body.
- Limit eating foods containing poor quality protein: Some foods contain poor quality protein, such as processed meat, fast food,... Elderly people should limit eating these foods. .
- Don't drink a lot of alcohol: Alcohol can reduce the body's ability to absorb protein.
- Supplement protein as prescribed by the doctor: If the elderly have been diagnosed with protein deficiency, they need to supplement protein as prescribed by the doctor.
              """)

    if disease == 8:
        print("""You may be malnourished. You need to improve your health by the following methods:
- Balanced, diverse diet: Elderly people need to eat lots of fruits, vegetables, whole grains, lean meats, fish, and eggs. Elderly people should eat many small meals a day for easy digestion and absorption.

- Drink enough water: Elderly people need to drink enough water to maintain health and help the body absorb nutrients.

- Participate in regular physical activities: Physical activities can help improve appetite and enhance overall health.

- Regular health check-ups: Regular health checks can help detect and treat diseases that can increase the risk of malnutrition.

Below are some specific solutions to help the elderly improve malnutrition:

- Eat lots of fruits and vegetables: Fruits and vegetables are rich sources of vitamins, minerals, and fiber. Seniors should eat at least 5 servings of fruits and vegetables every day.
- Eat lean meats: Lean meat is a source of high quality protein. Elderly people should eat about 2-3 servings of lean meat per day.
- Eat fish: Fish is a source of high-quality protein and healthy omega-3 fatty acids. Elderly people should eat about 2-3 servings of fish per week.
- Eat eggs: Eggs are a source of high-quality and inexpensive protein. Elderly people should eat about 2-3 eggs per day.
- Eat milk and dairy products: Milk and dairy products are a source of protein, calcium, and vitamin D. Elderly people should drink about 2-3 glasses of milk a day.
- Eat beans: Beans are a cheap and high-quality source of protein. Elderly people should eat about 2-3 servings of beans per day.
              """)