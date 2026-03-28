import pymysql
from config import Config

def get_db_connection():
    """Create database connection"""
    try:
        connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def insert_questions():
    """Insert questions for Sales Executive, HR Manager, Finance Analyst"""
    connection = get_db_connection()
    if not connection:
        print("Failed to connect to database")
        return

    try:
        with connection.cursor() as cursor:
            # Get position IDs
            position_names = ['Sales Executive', 'HR Manager', 'Finance Analyst']
            position_ids = {}
            for name in position_names:
                cursor.execute("SELECT id FROM positions WHERE name = %s", (name,))
                pos = cursor.fetchone()
                if pos:
                    position_ids[name] = pos['id']
                else:
                    print(f"Warning: Position '{name}' not found")

            # ========== SALES EXECUTIVE ==========
            if 'Sales Executive' in position_ids:
                pos_id = position_ids['Sales Executive']
                print(f"\n📌 Inserting Sales Executive questions (ID: {pos_id})...")

                # English questions
                eng_q = [
                    {
                        'question': 'What is the sales funnel?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'The process customers go through from awareness to purchase', 'is_correct': True},
                            {'text': 'A tool for tracking sales calls', 'is_correct': False},
                            {'text': 'A type of discount structure', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'How do you handle customer objections?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Listen, acknowledge, and address the concern with value', 'is_correct': True},
                            {'text': 'Ignore them and continue pitching', 'is_correct': False},
                            {'text': 'Immediately offer a discount', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is CRM software used for?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Managing customer relationships and sales data', 'is_correct': True},
                            {'text': 'Creating invoices', 'is_correct': False},
                            {'text': 'Designing marketing materials', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What are the key skills for a sales executive?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Communication, negotiation, product knowledge, persistence', 'is_correct': True},
                            {'text': 'Coding, graphic design, accounting', 'is_correct': False},
                            {'text': 'Public speaking only', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'How do you build customer relationships?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Trust, regular follow-ups, understanding their needs', 'is_correct': True},
                            {'text': 'Only contacting them when you have a new product', 'is_correct': False},
                            {'text': 'Sending them daily emails', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a lead in sales?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'A potential customer who has shown interest', 'is_correct': True},
                            {'text': 'A customer who has already purchased', 'is_correct': False},
                            {'text': 'A sales manager', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the difference between a warm lead and a cold lead?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Warm leads have shown interest; cold leads haven\'t', 'is_correct': True},
                            {'text': 'Warm leads are from hot countries', 'is_correct': False},
                            {'text': 'Cold leads are better than warm leads', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the SPIN selling technique?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Situation, Problem, Implication, Need-payoff questions', 'is_correct': True},
                            {'text': 'A spinning presentation', 'is_correct': False},
                            {'text': 'A type of sales contest', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a sales pitch?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'A persuasive presentation to convince a prospect to buy', 'is_correct': True},
                            {'text': 'A type of sports equipment', 'is_correct': False},
                            {'text': 'A discount offer', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'How do you close a sale?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Ask for the order and handle final objections', 'is_correct': True},
                            {'text': 'Walk away from the customer', 'is_correct': False},
                            {'text': 'Lower the price repeatedly', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is upselling?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Encouraging customers to buy a more expensive item', 'is_correct': True},
                            {'text': 'Selling to customers on the phone', 'is_correct': False},
                            {'text': 'Giving a free gift', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is cross-selling?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Suggesting related products to complement a purchase', 'is_correct': True},
                            {'text': 'Selling across different countries', 'is_correct': False},
                            {'text': 'Selling in bulk', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a sales target?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'A specific goal for revenue or units sold', 'is_correct': True},
                            {'text': 'The target audience', 'is_correct': False},
                            {'text': 'A type of sales report', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the importance of product knowledge in sales?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'It builds credibility and helps address customer questions', 'is_correct': True},
                            {'text': 'It’s not important if you have good persuasion skills', 'is_correct': False},
                            {'text': 'It only matters for technical products', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a sales quota?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'A minimum performance target set for a salesperson', 'is_correct': True},
                            {'text': 'The maximum number of customers allowed', 'is_correct': False},
                            {'text': 'A type of sales territory', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'How do you handle a rejection?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Learn from it and move on to the next prospect', 'is_correct': True},
                            {'text': 'Take it personally and give up', 'is_correct': False},
                            {'text': 'Argue with the customer', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a sales pipeline?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Visual representation of prospects at different stages', 'is_correct': True},
                            {'text': 'A physical pipe for sales documents', 'is_correct': False},
                            {'text': 'A type of inventory system', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the difference between B2B and B2C sales?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'B2B sells to businesses, B2C sells to consumers', 'is_correct': True},
                            {'text': 'B2B is online only', 'is_correct': False},
                            {'text': 'B2C involves longer sales cycles', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is consultative selling?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Acting as an advisor to solve customer problems', 'is_correct': True},
                            {'text': 'Selling consulting services', 'is_correct': False},
                            {'text': 'Asking a lot of questions without listening', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'How do you prioritize prospects?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Based on potential value, urgency, and fit', 'is_correct': True},
                            {'text': 'By alphabetical order', 'is_correct': False},
                            {'text': 'By who calls first', 'is_correct': False}
                        ]
                    }
                ]

                for q_data in eng_q:
                    cursor.execute(
                        "INSERT INTO interview_questions (position_id, language, question_text, difficulty) VALUES (%s, %s, %s, %s)",
                        (pos_id, 'English', q_data['question'], q_data['difficulty'])
                    )
                    q_id = cursor.lastrowid
                    for ans in q_data['answers']:
                        cursor.execute(
                            "INSERT INTO question_answers (question_id, answer_text, is_correct) VALUES (%s, %s, %s)",
                            (q_id, ans['text'], ans['is_correct'])
                        )

                # Myanmar questions
                mya_q = [
                    {
                        'question': 'Sales funnel ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဖောက်သည်များ သိရှိခြင်းမှ ဝယ်ယူခြင်းအထိ ဖြတ်သန်းသည့် လုပ်ငန်းစဉ်', 'is_correct': True},
                            {'text': 'အရောင်းခေါ်ဆိုမှုများကိုခြေရာခံသည့်ကိရိယာ', 'is_correct': False},
                            {'text': 'လျှော့စျေးပေးသည့်ပုံစံ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'ဖောက်သည်ကန့်ကွက်မှုများကိုဘယ်လိုကိုင်တွယ်မလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'နားထောင်ပါ၊ အသိအမှတ်ပြုပါ၊ တန်ဖိုးနှင့်တုံ့ပြန်ပါ', 'is_correct': True},
                            {'text': 'လျစ်လျူရှုပြီး ဆက်ရောင်းပါ', 'is_correct': False},
                            {'text': 'ချက်ချင်းလျှော့စျေးပေးပါ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'CRM software ကိုဘာအတွက်သုံးသလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဖောက်သည်ဆက်ဆံရေးနှင့်အရောင်းဒေတာများကိုစီမံရန်', 'is_correct': True},
                            {'text': 'ငွေတောင်းခံလွှာများဖန်တီးရန်', 'is_correct': False},
                            {'text': 'စျေးကွက်ရှာဖွေရေးပစ္စည်းများဒီဇိုင်းဆွဲရန်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အရောင်းကိုယ်စားလှယ်တစ်ဦးအတွက် အဓိကကျွမ်းကျင်မှုများကားအဘယ်နည်း။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'ဆက်သွယ်ရေး၊ ညှိနှိုင်းရေး၊ ထုတ်ကုန်အသိပညာ၊ ဇွဲရှိမှု', 'is_correct': True},
                            {'text': 'ကုဒ်ရေးခြင်း၊ ဂရပ်ဖစ်ဒီဇိုင်း၊ စာရင်းကိုင်ခြင်း', 'is_correct': False},
                            {'text': 'လူထုဟောပြောခြင်းတစ်မျိုးတည်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'ဖောက်သည်ဆက်ဆံရေးကိုဘယ်လိုတည်ဆောက်မလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ယုံကြည်မှု၊ ပုံမှန်နောက်ဆက်တွဲဆက်သွယ်မှု၊ သူတို့၏လိုအပ်ချက်များကိုနားလည်ခြင်း', 'is_correct': True},
                            {'text': 'ထုတ်ကုန်အသစ်ရှိမှသာ ဆက်သွယ်ခြင်း', 'is_correct': False},
                            {'text': 'နေ့စဉ်အီးမေးလ်များပို့ခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အရောင်းမှာ lead ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'စိတ်ဝင်စားမှုပြထားသည့် အလားအလာရှိဖောက်သည်', 'is_correct': True},
                            {'text': 'ဝယ်ယူပြီးသားဖောက်သည်', 'is_correct': False},
                            {'text': 'အရောင်းမန်နေဂျာ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Warm lead နဲ့ cold lead ဘာကွာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Warm lead က စိတ်ဝင်စားမှုပြထား၊ cold lead က မပြထားဘူး', 'is_correct': True},
                            {'text': 'Warm lead က ပူတဲ့နိုင်ငံကလာတာ', 'is_correct': False},
                            {'text': 'Cold lead က warm lead ထက်ပိုကောင်းတယ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'SPIN ရောင်းချနည်းစနစ်ဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Situation, Problem, Implication, Need-payoff မေးခွန်းများ', 'is_correct': True},
                            {'text': 'လည်နေသည့်တင်ဆက်မှု', 'is_correct': False},
                            {'text': 'အရောင်းပြိုင်ပွဲအမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Sales pitch ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'အလားအလာရှိသူကိုဝယ်ရန်ဆွဲဆောင်သည့် ဆွဲဆောင်မှုရှိတင်ဆက်မှု', 'is_correct': True},
                            {'text': 'အားကစားပစ္စည်းအမျိုးအစား', 'is_correct': False},
                            {'text': 'လျှော့စျေးကမ်းလှမ်းမှု', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အရောင်းကိုဘယ်လိုပိတ်မလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'အော်ဒါကိုတောင်းပြီး နောက်ဆုံးကန့်ကွက်ချက်များကိုကိုင်တွယ်ပါ', 'is_correct': True},
                            {'text': 'ဖောက်သည်ဆီကထွက်သွားပါ', 'is_correct': False},
                            {'text': 'ထပ်ခါတလဲလဲစျေးချပါ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Upselling ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဖောက်သည်ကို ပိုစျေးကြီးသည့်ပစ္စည်းဝယ်ရန် အားပေးခြင်း', 'is_correct': True},
                            {'text': 'ဖုန်းဖြင့်ဖောက်သည်များကိုရောင်းခြင်း', 'is_correct': False},
                            {'text': 'လက်ဆောင်အခမဲ့ပေးခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Cross-selling ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဝယ်ယူမှုနှင့်ဆက်စပ်သည့်ထုတ်ကုန်များကိုအကြံပြုခြင်း', 'is_correct': True},
                            {'text': 'နိုင်ငံအမျိုးမျိုးသို့ရောင်းချခြင်း', 'is_correct': False},
                            {'text': 'အမြောက်အမြားရောင်းချခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Sales target ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဝင်ငွေ သို့မဟုတ် ရောင်းအားအတွက် သတ်မှတ်ထားသည့်ပန်းတိုင်', 'is_correct': True},
                            {'text': 'ပစ်မှတ်ပရိသတ်', 'is_correct': False},
                            {'text': 'အရောင်းအစီရင်ခံစာအမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အရောင်းမှာထုတ်ကုန်အသိပညာ၏အရေးပါမှုကဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ယုံကြည်စိတ်ချရမှုကိုတည်ဆောက်ပြီး ဖောက်သည်မေးခွန်းများကိုဖြေဆိုနိုင်သည်', 'is_correct': True},
                            {'text': 'ဆွဲဆောင်နိုင်စွမ်းရှိရင် အရေးမကြီးဘူး', 'is_correct': False},
                            {'text': 'နည်းပညာထုတ်ကုန်များအတွက်သာအရေးကြီးတယ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Sales quota ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'အရောင်းဝန်ထမ်းတစ်ဦးအတွက် သတ်မှတ်ထားသော အနည်းဆုံးစွမ်းဆောင်ရည်ပန်းတိုင်', 'is_correct': True},
                            {'text': 'ခွင့်ပြုထားသော ဖောက်သည်အများဆုံးအရေအတွက်', 'is_correct': False},
                            {'text': 'အရောင်းနယ်မြေအမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'ငြင်းပယ်ခံရခြင်းကိုဘယ်လိုကိုင်တွယ်မလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'သင်ခန်းစာယူပြီး နောက်အလားအလာရှိသူဆီဆက်သွားပါ', 'is_correct': True},
                            {'text': 'ကိုယ်ရေးကိုယ်တာယူပြီး အရှုံးပေးလိုက်ပါ', 'is_correct': False},
                            {'text': 'ဖောက်သည်နှင့်ငြင်းခုန်ပါ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Sales pipeline ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'အဆင့်အမျိုးမျိုးရှိ အလားအလာရှိသူများကို အမြင်အားဖြင့်ဖော်ပြချက်', 'is_correct': True},
                            {'text': 'အရောင်းစာရွက်စာတမ်းများအတွက်ရုပ်ပိုင်းပိုက်လိုင်း', 'is_correct': False},
                            {'text': 'စာရင်းစနစ်အမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'B2B နဲ့ B2C အရောင်းဘာကွာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'B2B က စီးပွားရေးလုပ်ငန်းများကိုရောင်း၊ B2C က စားသုံးသူများကိုရောင်း', 'is_correct': True},
                            {'text': 'B2B က အွန်လိုင်းတစ်မျိုးတည်းသာ', 'is_correct': False},
                            {'text': 'B2C က အရောင်းသံသရာပိုရှည်တယ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Consultative selling ဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'ဖောက်သည်ပြဿနာများဖြေရှင်းရန် အတိုင်ပင်ခံအဖြစ်ဆောင်ရွက်ခြင်း', 'is_correct': True},
                            {'text': 'အတိုင်ပင်ခံဝန်ဆောင်မှုများရောင်းခြင်း', 'is_correct': False},
                            {'text': 'နားမထောင်ဘဲမေးခွန်းများစွာမေးခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အလားအလာရှိသူများကိုဘယ်လိုဦးစားပေးမလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'အလားအလာတန်ဖိုး၊ အရေးတကြီးလိုအပ်မှုနှင့် ကိုက်ညီမှုအပေါ်မူတည်ပြီး', 'is_correct': True},
                            {'text': 'အက္ခရာစဉ်အလိုက်', 'is_correct': False},
                            {'text': 'ဘယ်သူအရင်ခေါ်လဲဆိုတာပေါ်မူတည်ပြီး', 'is_correct': False}
                        ]
                    }
                ]

                for q_data in mya_q:
                    cursor.execute(
                        "INSERT INTO interview_questions (position_id, language, question_text, difficulty) VALUES (%s, %s, %s, %s)",
                        (pos_id, 'Myanmar', q_data['question'], q_data['difficulty'])
                    )
                    q_id = cursor.lastrowid
                    for ans in q_data['answers']:
                        cursor.execute(
                            "INSERT INTO question_answers (question_id, answer_text, is_correct) VALUES (%s, %s, %s)",
                            (q_id, ans['text'], ans['is_correct'])
                        )
                print(f"✅ Sales Executive: 20 English + 20 Myanmar questions inserted")

            # ========== HR MANAGER ==========
            if 'HR Manager' in position_ids:
                pos_id = position_ids['HR Manager']
                print(f"\n📌 Inserting HR Manager questions (ID: {pos_id})...")

                # English questions
                eng_q = [
                    {
                        'question': 'What is the recruitment process?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Sourcing, screening, interviewing, and hiring candidates', 'is_correct': True},
                            {'text': 'Firing employees', 'is_correct': False},
                            {'text': 'Managing payroll only', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What are the types of employee interviews?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Structured, unstructured, behavioral, panel, etc.', 'is_correct': True},
                            {'text': 'Only one type: face-to-face', 'is_correct': False},
                            {'text': 'Phone interviews only', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is performance appraisal?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Systematic evaluation of employee performance', 'is_correct': True},
                            {'text': 'A type of salary increase', 'is_correct': False},
                            {'text': 'Employee\'s opinion of the company', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is employee onboarding?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Process of integrating new hires into the company', 'is_correct': True},
                            {'text': 'Firing new employees', 'is_correct': False},
                            {'text': 'Training existing employees', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is workplace diversity and inclusion?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Creating an environment where all employees feel valued', 'is_correct': True},
                            {'text': 'Hiring only people from different countries', 'is_correct': False},
                            {'text': 'Making everyone the same', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is an HR information system (HRIS)?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Software for managing HR data and processes', 'is_correct': True},
                            {'text': 'A type of employee survey', 'is_correct': False},
                            {'text': 'A recruitment agency', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the purpose of a job description?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Outline duties, responsibilities, and qualifications for a role', 'is_correct': True},
                            {'text': 'Describe the company history', 'is_correct': False},
                            {'text': 'A form for employee complaints', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is employee engagement?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'The level of commitment and involvement employees have', 'is_correct': True},
                            {'text': 'How many hours employees work', 'is_correct': False},
                            {'text': 'Employee salary satisfaction', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the difference between training and development?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Training is job-specific, development is career-focused', 'is_correct': True},
                            {'text': 'They are the same', 'is_correct': False},
                            {'text': 'Development is for managers only', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a 360-degree feedback?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Feedback from peers, subordinates, and supervisors', 'is_correct': True},
                            {'text': 'Feedback from 360 people', 'is_correct': False},
                            {'text': 'A type of performance review done once a year', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is talent management?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Attracting, developing, and retaining skilled employees', 'is_correct': True},
                            {'text': 'Managing employee salaries', 'is_correct': False},
                            {'text': 'Hiring temporary workers', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the role of HR in compliance?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Ensuring company follows labor laws and regulations', 'is_correct': True},
                            {'text': 'Writing company policies', 'is_correct': False},
                            {'text': 'Conducting employee performance reviews', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a performance improvement plan (PIP)?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'A document outlining steps for an underperforming employee', 'is_correct': True},
                            {'text': 'A plan to improve company profits', 'is_correct': False},
                            {'text': 'A type of bonus scheme', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is employee turnover?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'The rate at which employees leave the company', 'is_correct': True},
                            {'text': 'Employees working in shifts', 'is_correct': False},
                            {'text': 'Employee rotation between departments', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a stay interview?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'An interview to understand why employees stay', 'is_correct': True},
                            {'text': 'An interview with departing employees', 'is_correct': False},
                            {'text': 'A type of job interview', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the difference between HR and personnel management?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'HR is strategic; personnel management is administrative', 'is_correct': True},
                            {'text': 'They are the same', 'is_correct': False},
                            {'text': 'Personnel management is modern, HR is old', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a job evaluation?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Determining the relative worth of a job for pay purposes', 'is_correct': True},
                            {'text': 'Evaluating how well an employee does their job', 'is_correct': False},
                            {'text': 'A type of interview', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the purpose of an exit interview?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Gather feedback from departing employees', 'is_correct': True},
                            {'text': 'To convince them to stay', 'is_correct': False},
                            {'text': 'To finalize their last paycheck', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a competency framework?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'A set of skills and behaviors required for a role', 'is_correct': True},
                            {'text': 'A type of training program', 'is_correct': False},
                            {'text': 'An employee ranking system', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is HR analytics?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Using data to make HR decisions', 'is_correct': True},
                            {'text': 'Analyzing employee satisfaction', 'is_correct': False},
                            {'text': 'A software for payroll', 'is_correct': False}
                        ]
                    }
                ]

                for q_data in eng_q:
                    cursor.execute(
                        "INSERT INTO interview_questions (position_id, language, question_text, difficulty) VALUES (%s, %s, %s, %s)",
                        (pos_id, 'English', q_data['question'], q_data['difficulty'])
                    )
                    q_id = cursor.lastrowid
                    for ans in q_data['answers']:
                        cursor.execute(
                            "INSERT INTO question_answers (question_id, answer_text, is_correct) VALUES (%s, %s, %s)",
                            (q_id, ans['text'], ans['is_correct'])
                        )

                # Myanmar questions
                mya_q = [
                    {
                        'question': 'လူသစ်ငှားရမ်းခြင်းလုပ်ငန်းစဉ်ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ရှာဖွေခြင်း၊ စစ်ဆေးခြင်း၊ တွေ့ဆုံမေးမြန်းခြင်းနှင့်ခန့်အပ်ခြင်း', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းများကိုအလုပ်ဖြုတ်ခြင်း', 'is_correct': False},
                            {'text': 'လစာချက်လက်မှတ်ထုတ်ခြင်းသက်သက်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'ဝန်ထမ်းအင်တာဗျူးအမျိုးအစားများကဘာတွေလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'စနစ်ကျသော၊ စနစ်မကျသော၊ အပြုအမူဆိုင်ရာ၊ အဖွဲ့လိုက်စသည်', 'is_correct': True},
                            {'text': 'တစ်မျိုးတည်းသာရှိတယ်: မျက်နှာချင်းဆိုင်', 'is_correct': False},
                            {'text': 'ဖုန်းအင်တာဗျူးတစ်မျိုးတည်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'စွမ်းဆောင်ရည်အကဲဖြတ်ခြင်းဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'ဝန်ထမ်းစွမ်းဆောင်ရည်ကိုစနစ်တကျအကဲဖြတ်ခြင်း', 'is_correct': True},
                            {'text': 'လစာတိုးခြင်းအမျိုးအစား', 'is_correct': False},
                            {'text': 'ကုမ္ပဏီအပေါ်ဝန်ထမ်း၏ထင်မြင်ချက်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Employee onboarding ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဝန်ထမ်းအသစ်များကိုကုမ္ပဏီတွင်းသို့ပေါင်းစည်းခြင်းလုပ်ငန်းစဉ်', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းအသစ်များကိုအလုပ်ဖြုတ်ခြင်း', 'is_correct': False},
                            {'text': 'လက်ရှိဝန်ထမ်းများကိုလေ့ကျင့်ခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'လုပ်ငန်းခွင်မတူကွဲပြားမှုနှင့်ပါဝင်မှုဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ဝန်ထမ်းအားလုံးတန်ဖိုးထားခံရသည့်ပတ်ဝန်းကျင်ဖန်တီးခြင်း', 'is_correct': True},
                            {'text': 'နိုင်ငံခြားသားများကိုသာငှားရမ်းခြင်း', 'is_correct': False},
                            {'text': 'လူတိုင်းကိုတစ်မျိုးတည်းဖြစ်အောင်လုပ်ခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'HRIS ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'HR ဒေတာနှင့်လုပ်ငန်းစဉ်များစီမံရန်ဆော့ဝဲ', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းစစ်တမ်းအမျိုးအစား', 'is_correct': False},
                            {'text': 'အလုပ်အကိုင်အကျိုးဆောင်အေဂျင်စီ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အလုပ်ဖော်ပြချက်ရဲ့ရည်ရွယ်ချက်ကဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ရာထူးတစ်ခုအတွက်တာဝန်များ၊ လုပ်ငန်းဆောင်တာများနှင့်အရည်အချင်းများကိုဖော်ပြရန်', 'is_correct': True},
                            {'text': 'ကုမ္ပဏီသမိုင်းကိုဖော်ပြရန်', 'is_correct': False},
                            {'text': 'ဝန်ထမ်းတိုင်ကြားချက်များအတွက်ပုံစံ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Employee engagement ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ဝန်ထမ်းများ၏ကတိကဝတ်နှင့်ပါဝင်မှုအဆင့်', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းများအလုပ်ချိန်မည်မျှ', 'is_correct': False},
                            {'text': 'ဝန်ထမ်းလစာကျေနပ်မှု', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Training နဲ့ development ဘာကွာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Training က အလုပ်အတွက်သတ်သတ်မှတ်မှတ်၊ development က အသက်မွေးဝမ်းကျောင်းအတွက်', 'is_correct': True},
                            {'text': 'အတူတူပဲ', 'is_correct': False},
                            {'text': 'Development က မန်နေဂျာများအတွက်သာ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': '360-degree feedback ဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'လုပ်ဖော်ကိုင်ဖက်များ၊ လက်အောက်ငယ်သားများနှင့်အထက်အရာရှိများထံမှတုံ့ပြန်ချက်', 'is_correct': True},
                            {'text': 'လူ ၃၆၀ ထံမှတုံ့ပြန်ချက်', 'is_correct': False},
                            {'text': 'တစ်နှစ်တစ်ကြိမ်လုပ်သောစွမ်းဆောင်ရည်သုံးသပ်ချက်အမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Talent management ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ကျွမ်းကျင်ဝန်ထမ်းများကိုဆွဲဆောင်ခြင်း၊ ဖွံ့ဖြိုးတိုးတက်ခြင်းနှင့်ထိန်းသိမ်းခြင်း', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းလစာများကိုစီမံခြင်း', 'is_correct': False},
                            {'text': 'ယာယီဝန်ထမ်းများငှားရမ်းခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'လိုက်နာမှုတွင် HR ၏အခန်းကဏ္ဍကဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'ကုမ္ပဏီသည်အလုပ်သမားဥပဒေများကိုလိုက်နာကြောင်းသေချာစေခြင်း', 'is_correct': True},
                            {'text': 'ကုမ္ပဏီမူဝါဒများရေးသားခြင်း', 'is_correct': False},
                            {'text': 'ဝန်ထမ်းစွမ်းဆောင်ရည်သုံးသပ်ခြင်းများပြုလုပ်ခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Performance improvement plan (PIP) ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'စွမ်းဆောင်ရည်နိမ့်ဝန်ထမ်းအတွက်အဆင့်များဖော်ပြသည့်စာရွက်စာတမ်း', 'is_correct': True},
                            {'text': 'ကုမ္ပဏီအမြတ်တိုးရန်အစီအစဉ်', 'is_correct': False},
                            {'text': 'ဆုကြေးပေးစနစ်အမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Employee turnover ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဝန်ထမ်းများကုမ္ပဏီမှထွက်ခွာနှုန်း', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းများအဆိုင်းလိုက်အလုပ်လုပ်ခြင်း', 'is_correct': False},
                            {'text': 'ဌာနများအကြားဝန်ထမ်းလှည့်ခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Stay interview ဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'ဝန်ထမ်းများအဘယ်ကြောင့်ဆက်နေသည်ကိုနားလည်ရန်အင်တာဗျူး', 'is_correct': True},
                            {'text': 'ထွက်ခွာမည့်ဝန်ထမ်းများနှင့်အင်တာဗျူး', 'is_correct': False},
                            {'text': 'အလုပ်အင်တာဗျူးအမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'HR နဲ့ personnel management ဘာကွာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'HR က မဟာဗျူဟာကျ၊ personnel management က စီမံခန့်ခွဲရေးဆန်တယ်', 'is_correct': True},
                            {'text': 'အတူတူပဲ', 'is_correct': False},
                            {'text': 'Personnel management က ခေတ်မီ၊ HR က ခေတ်နောက်ကျ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Job evaluation ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'လစာသတ်မှတ်ရန်အတွက် အလုပ်၏တန်ဖိုးကိုဆုံးဖြတ်ခြင်း', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းတစ်ဦးအလုပ်ကောင်းကောင်းလုပ်သည်ကိုအကဲဖြတ်ခြင်း', 'is_correct': False},
                            {'text': 'အင်တာဗျူးအမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Exit interview ရဲ့ရည်ရွယ်ချက်ကဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ထွက်ခွာမည့်ဝန်ထမ်းထံမှတုံ့ပြန်ချက်စုဆောင်းရန်', 'is_correct': True},
                            {'text': 'သူတို့ကိုဆက်နေရန်ဆွဲဆောင်ရန်', 'is_correct': False},
                            {'text': 'နောက်ဆုံးလစာချက်လက်မှတ်အပြီးသတ်ရန်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Competency framework ဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'ရာထူးတစ်ခုအတွက်လိုအပ်သောကျွမ်းကျင်မှုနှင့်အပြုအမူများအစု', 'is_correct': True},
                            {'text': 'လေ့ကျင့်ရေးအစီအစဉ်အမျိုးအစား', 'is_correct': False},
                            {'text': 'ဝန်ထမ်းအဆင့်သတ်မှတ်ခြင်းစနစ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'HR analytics ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'HR ဆုံးဖြတ်ချက်များချရန်ဒေတာကိုအသုံးပြုခြင်း', 'is_correct': True},
                            {'text': 'ဝန်ထမ်းကျေနပ်မှုကိုခွဲခြမ်းစိတ်ဖြာခြင်း', 'is_correct': False},
                            {'text': 'လစာချက်လက်မှတ်အတွက်ဆော့ဝဲ', 'is_correct': False}
                        ]
                    }
                ]

                for q_data in mya_q:
                    cursor.execute(
                        "INSERT INTO interview_questions (position_id, language, question_text, difficulty) VALUES (%s, %s, %s, %s)",
                        (pos_id, 'Myanmar', q_data['question'], q_data['difficulty'])
                    )
                    q_id = cursor.lastrowid
                    for ans in q_data['answers']:
                        cursor.execute(
                            "INSERT INTO question_answers (question_id, answer_text, is_correct) VALUES (%s, %s, %s)",
                            (q_id, ans['text'], ans['is_correct'])
                        )
                print(f"✅ HR Manager: 20 English + 20 Myanmar questions inserted")

            # ========== FINANCE ANALYST ==========
            if 'Finance Analyst' in position_ids:
                pos_id = position_ids['Finance Analyst']
                print(f"\n📌 Inserting Finance Analyst questions (ID: {pos_id})...")

                # English questions
                eng_q = [
                    {
                        'question': 'What is financial statement analysis?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Evaluating financial statements to make decisions', 'is_correct': True},
                            {'text': 'Creating financial statements', 'is_correct': False},
                            {'text': 'Auditing financial statements', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the difference between cash flow and profit?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Cash flow is actual cash movement; profit is accounting measure', 'is_correct': True},
                            {'text': 'They are the same', 'is_correct': False},
                            {'text': 'Profit is cash flow minus expenses', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is ROI and how is it calculated?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Return on Investment: (Net Profit / Cost of Investment) × 100', 'is_correct': True},
                            {'text': 'Revenue minus expenses', 'is_correct': False},
                            {'text': 'Total assets divided by liabilities', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is budgeting?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Planning future income and expenses', 'is_correct': True},
                            {'text': 'Tracking past expenses', 'is_correct': False},
                            {'text': 'Calculating taxes', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What are the main financial ratios?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Liquidity, profitability, efficiency, solvency ratios', 'is_correct': True},
                            {'text': 'Only profitability ratios', 'is_correct': False},
                            {'text': 'Revenue and expense ratios', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a balance sheet?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Statement showing assets, liabilities, and equity', 'is_correct': True},
                            {'text': 'Statement of cash flows', 'is_correct': False},
                            {'text': 'Income statement', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is an income statement?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Reports revenue and expenses over a period', 'is_correct': True},
                            {'text': 'Shows company\'s net worth', 'is_correct': False},
                            {'text': 'Lists all assets', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a cash flow statement?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Shows inflows and outflows of cash', 'is_correct': True},
                            {'text': 'Same as income statement', 'is_correct': False},
                            {'text': 'Shows company\'s profit', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is working capital?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Current assets minus current liabilities', 'is_correct': True},
                            {'text': 'Total assets minus total liabilities', 'is_correct': False},
                            {'text': 'Cash on hand', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the time value of money?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Money today is worth more than same amount in future', 'is_correct': True},
                            {'text': 'Money value stays the same over time', 'is_correct': False},
                            {'text': 'Money loses value due to inflation only', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is NPV?',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Net Present Value: sum of future cash flows discounted', 'is_correct': True},
                            {'text': 'Net Profit Value', 'is_correct': False},
                            {'text': 'A type of ratio', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the difference between debt and equity?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Debt is borrowed money; equity is ownership', 'is_correct': True},
                            {'text': 'Both are the same', 'is_correct': False},
                            {'text': 'Debt is cheaper than equity', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is financial forecasting?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Predicting future financial outcomes', 'is_correct': True},
                            {'text': 'Analyzing past financial data', 'is_correct': False},
                            {'text': 'Creating financial statements', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a budget variance?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Difference between budgeted and actual amounts', 'is_correct': True},
                            {'text': 'A type of budget', 'is_correct': False},
                            {'text': 'The total budget amount', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a financial audit?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Independent examination of financial records', 'is_correct': True},
                            {'text': 'Internal review of expenses', 'is_correct': False},
                            {'text': 'Creating financial reports', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a break-even point?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Point where total revenue equals total costs', 'is_correct': True},
                            {'text': 'Point where profit is maximum', 'is_correct': False},
                            {'text': 'Point where company starts making profit', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is cost of goods sold (COGS)?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Direct costs attributable to production of goods sold', 'is_correct': True},
                            {'text': 'Total operating expenses', 'is_correct': False},
                            {'text': 'Marketing costs', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is a financial ratio analysis?',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Using ratios to evaluate company performance', 'is_correct': True},
                            {'text': 'Calculating percentages', 'is_correct': False},
                            {'text': 'Comparing two companies', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is liquidity?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Ability to meet short-term obligations', 'is_correct': True},
                            {'text': 'Profitability of the company', 'is_correct': False},
                            {'text': 'Total assets', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'What is the difference between fixed and variable costs?',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Fixed costs don’t change with output; variable costs do', 'is_correct': True},
                            {'text': 'Both change with output', 'is_correct': False},
                            {'text': 'Fixed costs are always higher', 'is_correct': False}
                        ]
                    }
                ]

                for q_data in eng_q:
                    cursor.execute(
                        "INSERT INTO interview_questions (position_id, language, question_text, difficulty) VALUES (%s, %s, %s, %s)",
                        (pos_id, 'English', q_data['question'], q_data['difficulty'])
                    )
                    q_id = cursor.lastrowid
                    for ans in q_data['answers']:
                        cursor.execute(
                            "INSERT INTO question_answers (question_id, answer_text, is_correct) VALUES (%s, %s, %s)",
                            (q_id, ans['text'], ans['is_correct'])
                        )

                # Myanmar questions
                mya_q = [
                    {
                        'question': 'Financial statement analysis ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဆုံးဖြတ်ချက်များချရန်အတွက် ဘဏ္ဍာရေးရှင်းတမ်းများကိုအကဲဖြတ်ခြင်း', 'is_correct': True},
                            {'text': 'ဘဏ္ဍာရေးရှင်းတမ်းများဖန်တီးခြင်း', 'is_correct': False},
                            {'text': 'ဘဏ္ဍာရေးရှင်းတမ်းများစစ်ဆေးခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Cash flow နဲ့ profit ဘာကွာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'Cash flow က ငွေအဝင်အထွက် အစစ်အမှန်၊ profit က စာရင်းရှင်းတွက်နည်း', 'is_correct': True},
                            {'text': 'အတူတူပဲ', 'is_correct': False},
                            {'text': 'Profit က cash flow အနှုတ်ကုန်ကျစရိတ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'ROI ဆိုတာဘာလဲ၊ ဘယ်လိုတွက်ချက်လဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Return on Investment: (အသားတင်အမြတ် / ရင်းနှီးမြှုပ်နှံမှုကုန်ကျစရိတ်) × ၁၀၀', 'is_correct': True},
                            {'text': 'ဝင်ငွေအနှုတ်ကုန်ကျစရိတ်', 'is_correct': False},
                            {'text': 'စုစုပေါင်းပိုင်ဆိုင်မှုများကိုတာဝန်ခံများနှင့်စား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Budgeting ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'အနာဂတ်ဝင်ငွေနှင့်ကုန်ကျစရိတ်များကိုစီမံခြင်း', 'is_correct': True},
                            {'text': 'အတိတ်ကုန်ကျစရိတ်များကိုခြေရာခံခြင်း', 'is_correct': False},
                            {'text': 'အခွန်များတွက်ချက်ခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အဓိကဘဏ္ဍာရေးအချိုးများကဘာတွေလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ငွေဖြစ်လွယ်မှု၊ အမြတ်အစွန်းရရှိမှု၊ ထိရောက်မှု၊ ကြွေးကျေနိုင်မှုအချိုးများ', 'is_correct': True},
                            {'text': 'အမြတ်အစွန်းအချိုးများသာ', 'is_correct': False},
                            {'text': 'ဝင်ငွေနှင့်ကုန်ကျစရိတ်အချိုးများ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Balance sheet ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ပိုင်ဆိုင်မှုများ၊ တာဝန်ခံများနှင့်ရှယ်ယာများကိုပြသည့်ရှင်းတမ်း', 'is_correct': True},
                            {'text': 'ငွေသားစီးဆင်းမှုရှင်းတမ်း', 'is_correct': False},
                            {'text': 'ဝင်ငွေရှင်းတမ်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Income statement ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ကာလတစ်ခုအတွင်းဝင်ငွေနှင့်ကုန်ကျစရိတ်များကိုဖော်ပြသည်', 'is_correct': True},
                            {'text': 'ကုမ္ပဏီ၏အသားတင်တန်ဖိုးကိုပြသည်', 'is_correct': False},
                            {'text': 'ပိုင်ဆိုင်မှုအားလုံးစာရင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Cash flow statement ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ငွေသားဝင်ရောက်မှုနှင့်ထွက်ရှိမှုများကိုပြသည်', 'is_correct': True},
                            {'text': 'ဝင်ငွေရှင်းတမ်းနှင့်အတူတူ', 'is_correct': False},
                            {'text': 'ကုမ္ပဏီ၏အမြတ်ကိုပြသည်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Working capital ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'လက်ရှိပိုင်ဆိုင်မှုများအနှုတ်လက်ရှိတာဝန်ခံများ', 'is_correct': True},
                            {'text': 'စုစုပေါင်းပိုင်ဆိုင်မှုများအနှုတ်စုစုပေါင်းတာဝန်ခံများ', 'is_correct': False},
                            {'text': 'လက်ထဲငွေသား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'ငွေ၏အချိန်တန်ဖိုးဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'ယနေ့ငွေသည် အနာဂတ်တူညီငွေပမာဏထက်တန်ဖိုးပိုကြီးသည်', 'is_correct': True},
                            {'text': 'ငွေတန်ဖိုးသည် အချိန်နှင့်အမျှအတူတူဖြစ်သည်', 'is_correct': False},
                            {'text': 'ငွေသည် ငွေကြေးဖောင်းပွမှုကြောင့်သာတန်ဖိုးကျသည်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'NPV ဆိုတာဘာလဲ။',
                        'difficulty': 'Hard',
                        'answers': [
                            {'text': 'Net Present Value: အနာဂတ်ငွေသားစီးဆင်းမှုများ၏ လက်ရှိတန်ဖိုး', 'is_correct': True},
                            {'text': 'Net Profit Value', 'is_correct': False},
                            {'text': 'အချိုးအမျိုးအစား', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'အကြွေးနဲ့ရှယ်ယာဘာကွာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'အကြွေးက ချေးထားတဲ့ငွေ၊ ရှယ်ယာက ပိုင်ဆိုင်မှု', 'is_correct': True},
                            {'text': 'နှစ်ခုလုံးအတူတူပဲ', 'is_correct': False},
                            {'text': 'အကြွေးက ရှယ်ယာထက်စျေးသက်သာတယ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Financial forecasting ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'အနာဂတ်ဘဏ္ဍာရေးရလဒ်များကိုခန့်မှန်းခြင်း', 'is_correct': True},
                            {'text': 'အတိတ်ဘဏ္ဍာရေးဒေတာကိုခွဲခြမ်းစိတ်ဖြာခြင်း', 'is_correct': False},
                            {'text': 'ဘဏ္ဍာရေးရှင်းတမ်းများဖန်တီးခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Budget variance ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ဘတ်ဂျက်နှင့်အမှန်တကယ်ပမာဏများအကြားကွာခြားချက်', 'is_correct': True},
                            {'text': 'ဘတ်ဂျက်အမျိုးအစား', 'is_correct': False},
                            {'text': 'စုစုပေါင်းဘတ်ဂျက်ပမာဏ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Financial audit ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ဘဏ္ဍာရေးမှတ်တမ်းများ၏လွတ်လပ်သောစစ်ဆေးခြင်း', 'is_correct': True},
                            {'text': 'ကုန်ကျစရိတ်များ၏အတွင်းပိုင်းသုံးသပ်ချက်', 'is_correct': False},
                            {'text': 'ဘဏ္ဍာရေးအစီရင်ခံစာများဖန်တီးခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Break-even point ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'စုစုပေါင်းဝင်ငွေနှင့်စုစုပေါင်းကုန်ကျစရိတ်တူညီသည့်အမှတ်', 'is_correct': True},
                            {'text': 'အမြတ်အများဆုံးဖြစ်သည့်အမှတ်', 'is_correct': False},
                            {'text': 'ကုမ္ပဏီအမြတ်စတင်ရရှိသည့်အမှတ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'ကုန်ပစ္စည်းရောင်းချရကုန်ကျစရိတ် (COGS) ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ရောင်းချသောကုန်ပစ္စည်းများထုတ်လုပ်မှုအတွက်တိုက်ရိုက်ကုန်ကျစရိတ်', 'is_correct': True},
                            {'text': 'စုစုပေါင်းလည်ပတ်ကုန်ကျစရိတ်', 'is_correct': False},
                            {'text': 'စျေးကွက်ရှာဖွေရေးကုန်ကျစရိတ်', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Financial ratio analysis ဆိုတာဘာလဲ။',
                        'difficulty': 'Medium',
                        'answers': [
                            {'text': 'ကုမ္ပဏီစွမ်းဆောင်ရည်ကိုအကဲဖြတ်ရန် အချိုးများကိုအသုံးပြုခြင်း', 'is_correct': True},
                            {'text': 'ရာခိုင်နှုန်းများတွက်ချက်ခြင်း', 'is_correct': False},
                            {'text': 'ကုမ္ပဏီနှစ်ခုကိုနှိုင်းယှဉ်ခြင်း', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Liquidity ဆိုတာဘာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'ရေတိုတာဝန်ခံများကိုကျေနိုင်စွမ်း', 'is_correct': True},
                            {'text': 'ကုမ္ပဏီ၏အမြတ်အစွန်းရရှိမှု', 'is_correct': False},
                            {'text': 'စုစုပေါင်းပိုင်ဆိုင်မှုများ', 'is_correct': False}
                        ]
                    },
                    {
                        'question': 'Fixed cost နဲ့ variable cost ဘာကွာလဲ။',
                        'difficulty': 'Easy',
                        'answers': [
                            {'text': 'Fixed cost က ထုတ်လုပ်မှုနှင့်မပြောင်းလဲ၊ variable cost က ပြောင်းလဲသည်', 'is_correct': True},
                            {'text': 'နှစ်ခုလုံးထုတ်လုပ်မှုနှင့်ပြောင်းလဲသည်', 'is_correct': False},
                            {'text': 'Fixed cost က အမြဲတမ်းပိုများသည်', 'is_correct': False}
                        ]
                    }
                ]

                for q_data in mya_q:
                    cursor.execute(
                        "INSERT INTO interview_questions (position_id, language, question_text, difficulty) VALUES (%s, %s, %s, %s)",
                        (pos_id, 'Myanmar', q_data['question'], q_data['difficulty'])
                    )
                    q_id = cursor.lastrowid
                    for ans in q_data['answers']:
                        cursor.execute(
                            "INSERT INTO question_answers (question_id, answer_text, is_correct) VALUES (%s, %s, %s)",
                            (q_id, ans['text'], ans['is_correct'])
                        )
                print(f"✅ Finance Analyst: 20 English + 20 Myanmar questions inserted")

            connection.commit()
            print("\n✅ All questions for Sales Executive, HR Manager, Finance Analyst inserted successfully!")

    except Exception as e:
        print(f"❌ Error inserting questions: {e}")
        connection.rollback()
    finally:
        connection.close()

if __name__ == '__main__':
    print("🚀 Starting to insert questions for Sales Executive, HR Manager, Finance Analyst...")
    insert_questions()