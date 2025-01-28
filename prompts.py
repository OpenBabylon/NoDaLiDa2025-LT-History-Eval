def prepare_input_text(question, choices):
    out = f"""Question:\n{question}\n\nAnswers:\n"""

    for choice_label in ["A", "B", "C", "D"]:
        choice_text = [x for x in choices if x["label"] == choice_label][0]["text"]
        out += choice_label + ") " + choice_text + "\n"
    return out


def get_messages(examples, system_prompt):
  messages = [{"role": "system", "content": system_prompt}]
  for example_dict in examples:
    messages.append(
      {
                "role": "user",
                "content": format_input(
                    question = example_dict["question"], 
                    choices=example_dict["choices"]
                )
            }
        )
    messages.append(
            {
                "role": "assistant",
                "content": example_dict["answerKey"]
            }
        )
    return messages


def get_ua_messages():
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""
  examples = [
    {
 "question": "У 2020 році в Литві відбулися вибори до Сейму. Яка політична партія отримала найбільше мандатів?", 
 "choices": [
 {
 "text": "Соціал-демократична партія Литви", "label": "A"
 },
 {

 "text": "Союз Вітчизни — Литовські християнські демократи", "label": "B",
 },
 {
 "text": "Лейбористська партія", "label": "C"
 },
 {
 "text": "Литовський республіканський ліберальний рух", "label": "D"
 }
 ],
 "answerKey": "B"
 },

{
 "question": "З приводу якого питання литовський уряд зіткнувся з напруженістю з Європейським Союзом у 2021 році?", 
 "choices": [
 {
 "text": "Торгові відносини з США", "label": "A"
 },
 {

 "text": "Угоди щодо кліматичної політики", "label": "B",
 },
 {
 "text": "Біженці та міграційна політика на кордоні Білорусі", "label": "C"
 },
 {
 "text": "Правила фінансової прозорості", "label": "D"
 }
 ],
 "answerKey": "C"
 },
    
   {
 "question":"У 2020 році Литва приєдналася до інших країн Балтії та заборонила імпорт електроенергії з нових атомних електростанцій якої країни?", 
 "choices": [
 {
 "text": "Росія", "label": "B"
 },
 {

 "text": "Білорусь", "label": "A",
 },
 {
 "text": "Польща", "label": "C"
 },
 {
 "text": "Україна", "label": "D"
 }
 ],
 "answerKey": "A"
 },
   {
 "question":  "У 2022 році Литва суттєво збільшила військові витрати. Яка головна причина цього збільшення?",
 "choices": [
 {
 "text": "загрози Китаю", "label": "A"
 },
 {

 "text": "відповідати вимогам НАТО щодо витрат на оборону", "label": "B",
 },
 {
 "text": "Внутрішня модернізація литовської армії", "label": "C"
 },
 {
 "text": "Зростання регіональної напруженості через українсько-російський конфлікт", "label": "D"
 }
 ],
 "answerKey": "D"
 }
]

  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]



def get_sw_messages():
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""
  examples = [
    {
 "question": "2020 hölls Seimas Valet i Litauen. Vilket politiskt parti fick flest mandat?",
 "choices": [
 {
 "text": "Litauens socialdemokratiska parti", "label": "A"
 },
 {

 "text": "Fosterlandsförbundet – Litauiska kristdemokrater", "label": "B",
 },
 {
 "text": "Darbo partija", "label": "C"
 },
 {
 "text": "Liberala rörelsen", "label": "D"
 }
 ],
 "answerKey": "B"
 },

{
 "question": "I vilken fråga stod den litauiska regeringen inför spänningar med Europeiska unionen 2021?",
 "choices": [
 {
 "text": "Handelsförbindelser med USA", "label": "A"
 },
 {

 "text": "Klimatpolitiska avtal", "label": "B",
 },
 {
 "text": "Flykting- och migrationspolitik vid gränsen till Vitryssland", "label": "C"
 },
 {
 "text": "Regler för finansiell insyn", "label": "D"
 }
 ],
 "answerKey": "C"
 },
    
   {
 "question": "2020 anslöt sig Litauen till de andra baltiska länderna och förbjöd import av el från vilket lands nya kärnkraftverk?",
 "choices": [
 {
 "text": "Ryssland", "label": "B"
 },
 {

 "text": "Vitryssland", "label": "A",
 },
 {
 "text": "Polen", "label": "C"
 },
 {
 "text": "Ukraina", "label": "D"
 }
 ],
 "answerKey": "A"
 },
   {
 "question":"År 2022 ökade Litauen avsevärt militärutgifterna. Vad var huvudorsaken till denna ökning?", 
 "choices": [
 {
 "text": "Kina hot", "label": "A"
 },
 {

 "text": "uppfyll Natos krav på försvarsutgifter", "label": "B",
 },
 {
 "text": "Intern modernisering av den litauiska armén", "label": "C"
 },
 {
 "text": "Stigande regionala spänningar på grund av konflikten mellan Ukraina och Ryssland", "label": "D"
 }
 ],
 "answerKey": "D"
 }
]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]


def get_lt_messages():
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""
  examples = [
    {
        "question": "2020 metais Lietuvoje vyko Seimo rinkimai. Kuri politinė partija gavo daugiausiai mandatų?",
        "choices": [
            {
                "text": "Lietuvos socialdemokratų partija", "label": "A"
            },
            {
                
                "text": "Tėvynės sąjunga – Lietuvos krikščionys demokratai", "label": "B",
            },
            {
                "text": "Darbo partija", "label": "C"
            },
            {
                "text": "Liberalų sąjūdis", "label": "D"
            }
        ],
        "answerKey": "B"
    },

        {
        "question": "Kokiu klausimu 2021 metais Lietuvos vyriausybė susidūrė su įtampa su Europos Sąjunga?",
        "choices": [
            {
                "text": "Prekybos santykiai su JAV", "label": "A"
            },
            {
                
                "text": "Klimato politikos susitarimai", "label": "B",
            },
            {
                "text": "Pabėgėlių ir migracijos politika Baltarusijos pasienyje", "label": "C"
            },
            {
                "text": "Finansinio skaidrumo taisyklės", "label": "D"
            }
        ],
        "answerKey": "C"
    },
    
    {
        "question": "2020 metais Lietuva prisijungė prie kitų Baltijos šalių ir uždraudė elektros importą iš kurios šalies naujos atominės elektrinės?",
        "choices": [
            {
                "text": "Rusija", "label": "B"
            },
            {
                
                "text": "Baltarusija", "label": "A",
            },
            {
                "text": "Lenkija", "label": "C"
            },
            {
                "text": "Ukraina", "label": "D"
            }
        ],
        "answerKey": "A"
    },
    {
        "question": "2022 metais Lietuva smarkiai padidino karines išlaidas. Kokia buvo pagrindinė šio padidėjimo priežastis?",
        "choices": [
            {
                "text": "Kinijos grasinimai", "label": "A"
            },
            {
                
                "text": "atitikti NATO gynybos išlaidų reikalavimus", "label": "B",
            },
            {
                "text": "Vidinis Lietuvos kariuomenės modernizavimas", "label": "C"
            },
            {
                "text": "Auganti regioninė įtampa dėl Ukrainos ir Rusijos konflikto", "label": "D"
            }
        ],
        "answerKey": "D"
    }    
]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]


def get_lav_messages():
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""
  examples = [
    {
 "question": "2020. gadā Lietuvā notika Seima vēlēšanas. Kura politiskā partija saņēmusi visvairāk mandātu?",
 "choices": [
 {
 "text": "Lietuvas sociāldemokrātu partija", "label": "A"
 },
 {

 "text": "Tēvzemes savienība — Lietuvas kristīgie demokrāti", "label": "B",
 },
 {
 "text": "Darba partija", "label": "C"
 },
 {
 "text": "Liberalų sąjūdis", "label": "D"
 }
 ],
 "answerKey": "B"
 },

{
 "question": "Kādā jautājumā Lietuvas valdība saskārās ar spriedzi ar Eiropas Savienību 2021. gadā?",
 "choices": [
 {
 "text": "Tirdzniecības attiecības ar ASV", "label": "A"
 },
 {

 "text": "Klimata politikas līgumi", "label": "B",
 },
 {
 "text": "Bēgļu un migrācijas politika uz Baltkrievijas robežas", "label": "C"
 },
 {
 "text": "Finanšu pārredzamības noteikumi", "label": "D"
 }
 ],
 "answerKey": "C"
 },
    
   {
 "question": "2020. gadā Lietuva pievienojās pārējām Baltijas valstīm un aizliedza elektroenerģijas importu no kuras valsts jaunajām atomelektrostacijām?",
 "choices": [
 {
 "text": "Krievija", "label": "B"
 },
 {

 "text": "Baltkrievija", "label": "A",
 },
 {
 "text": "Polija", "label": "C"
 },
 {
 "text": "Ukraina", "label": "D"
 }
 ],
 "answerKey": "A"
 },
   {
 "question":"2022. gadā Lietuva būtiski palielināja militāros izdevumus. Kāds bija šī pieauguma galvenais iemesls?",
 "choices": [
 {
 "text": "Ķīnas draudi", "label": "A"
 },
 {

 "text": "atbilst NATO aizsardzības izdevumu prasībām", "label": "B",
 },
 {
 "text": "Lietuvas armijas iekšējā modernizācija", "label": "C"
 },
 {
 "text": "Pieaugošā reģionālā spriedze Ukrainas un Krievijas konflikta dēļ", "label": "D"
 }
 ],
 "answerKey": "D"
 }
]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]


def get_fn_messages():
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""
  examples = [
    {
 "question": "Vuonna 2020 Liettuassa pidettiin Seimas-vaalit. Mikä poliittinen puolue sai eniten mandaatteja?",
 "choices": [
 {
 "text": "Liettuan sosiaalidemokraattinen puolue", "label": "A"
 },
 {

 "text": "Kotimaan liitto – Liettuan kristillisdemokraatit", "label": "B",
 },
 {
 "text": "Työväenpuolue", "label": "C"
 },
 {
 "text": "Liettuan tasavallan liberaalien liike", "label": "D"
 }
 ],
 "answerKey": "B"
 },

{
 "question": "Mistä asioista Liettuan hallitus kohtasi jännitteitä Euroopan unionin kanssa vuonna 2021?",
 "choices": [
 {
 "text": "Kauppasuhteet Yhdysvaltojen kanssa", "label": "A"
 },
 {

 "text": "Ilmastopolitiikan sopimukset", "label": "B",
 },
 {
 "text": "Pakolais- ja maahanmuuttopolitiikka Valko-Venäjän rajalla", "label": "C"
 },
 {
 "text": "Taloudellisen avoimuuden säännöt", "label": "D"
 }
 ],
 "answerKey": "C"
 },
    
   {
"question": "Vuonna 2020 Liettua liittyi muiden Baltian maiden joukkoon ja kielsi sähkön tuonnin minkä maan uusista ydinvoimalaitoksista?",
 "choices": [
 {
 "text": "Venäjä", "label": "B"
 },
 {

 "text": "Valko-Venäjä", "label": "A",
 },
 {
 "text": "Puola", "label": "C"
 },
 {
 "text": "Ukraina", "label": "D"
 }
 ],
 "answerKey": "A"
 },
   {
 "question":"Vuonna 2022 Liettua lisäsi merkittävästi sotilasmenojaan. Mikä oli suurin syy tähän nousuun?", 
 "choices": [
 {
 "text": "Kiinan uhkaukset", "label": "A"
 },
 {

 "text": "Naton puolustusmenojen vuoksi", "label": "B",
 },
 {
 "text": "Liettuan armeijan sisäinen modernisointi", "label": "C"
 },
 {
 "text": "Ukrainan ja Venäjän välisen konfliktin aiheuttamat alueelliset jännitteet kasvavat", "label": "D"
 }
 ],
 "answerKey": "D"
 }
]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]


def get_est_messages():
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""
  examples = [
    {
 "question": "2020. aastal toimusid Leedus Seimi valimised. Milline erakond sai kõige rohkem mandaate?",
 "choices": [
 {
 "text": "Leedu Sotsiaaldemokraatlik Partei", "label": "A"
 },
 {

 "text": "Isamaaliit – Leedu Kristlikud Demokraadid", "label": "B",
 },
 {
 "text": "Tööpartei", "label": "C"
 },
 {
 "text": "Liberaalne Liikumine", "label": "D"
 }
 ],
 "answerKey": "B"
 },

{
 "question": "Millises küsimuses tekkis Leedu valitsusel 2021. aastal pinge Euroopa Liiduga?",
 "choices": [
 {
 "text": "Kaubandussuhted USA-ga", "label": "A"
 },
 {

 "text": "Kliimapoliitika kokkulepped", "label": "B",
 },
 {
 "text": "Pagulas- ja migratsioonipoliitika Valgevene piiril", "label": "C"
 },
 {
 "text": "Finantsläbipaistvuse eeskirjad", "label": "D"
 }
 ],
 "answerKey": "C"
 },
    
   {
"question":"2020. aastal ühines Leedu teiste Balti riikidega ja keelas mis riigi uutest tuumajaamadest elektri impordi?", 
 "choices": [
 {
 "text": "Venemaa", "label": "B"
 },
 {

 "text": "Valgevene", "label": "A",
 },
 {
 "text": "Poola", "label": "C"
 },
 {
 "text": "Ukraina", "label": "D"
 }
 ],
 "answerKey": "A"
 },
   {
 "question": "2022. aastal suurendas Leedu oluliselt sõjalisi kulutusi. Mis oli selle kasvu peamine põhjus?",
 "choices": [
 {
 "text": "Hiina ähvardused", "label": "A"
 },
 {

 "text": "NATO kaitsekulutuste nõuete tõttu", "label": "B",
 },
 {
 "text": "Leedu sõjaväe sisemine moderniseerimine", "label": "C"
 },
 {
 "text": "Kasvavad piirkondlikud pinged Ukraina-Vene konflikti tõttu", "label": "D"
 }
 ],
 "answerKey": "D"
 }
]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]


def get_en_messages(prepared_input_text):
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""

  examples = [
    {
 "question": "In 2020, the Seimas elections were held in Lithuania. Which political party received the most mandates?",
 "choices": [
 {
 "text": "Lithuanian Social Democratic Party", "label": "A"
 },
 {

 "text": "Homeland Union – Lithuanian Christian Democrats leadership ", "label": "B",
 },
 {
 "text": "Labor party", "label": "C"
 },
 {
 "text": "Liberal Movement", "label": "D"
 }
 ],
 "answerKey": "B"
 },

{
 "question": "On what issue did the Lithuanian government face tension with the European Union in 2021?",
 "choices": [
 {
 "text": "Trade relations with the USA", "label": "A"
 },
 {

 "text": "Climate Policy Agreements", "label": "B",
 },
 {
 "text": "Refugee and migration policy at the border of Belarus", "label": "C"
 },
 {
 "text": "Financial Transparency Rules", "label": "D"
 }
 ],
 "answerKey": "C"
 },
    
   {
 "question": "In 2020, Lithuania joined the other Baltic countries and banned the import of electricity from which country's new nuclear power plants?",
 "choices": [
 {
 "text": "Russia", "label": "B"
 },
 {

 "text": "Belarus", "label": "A",
 },
 {
 "text": "Poland", "label": "C"
 },
 {
 "text": "Ukraine", "label": "D"
 }
 ],
 "answerKey": "A"
 },
   {
 "question": "In 2022, Lithuania significantly increased military spending. What was the main reason for this increase?",
 "choices": [
 {
 "text": "China threats", "label": "A"
 },
 {

 "text": "meet NATO defense spending requirements", "label": "B",
 },
 {
 "text": "Internal modernization of the Lithuanian army", "label": "C"
 },
 {
 "text": "Rising regional tensions due to Ukraine-Russia conflict", "label": "D"
 }
 ],
 "answerKey": "D"
 }
]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]

def get_ar_messages(prepared_input_text):
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""

  examples = [
      {
   "question": "في عام 2020، أجريت انتخابات مجلس النواب في ليتوانيا. أي حزب سياسي حصل على أكبر عدد من المقاعد؟",
   "choices": [
   {
   "text": "هو حزب سياسي ليتواني، أسس", "label": "A"
   },
   {

   "text": "اتحاد الوطن – الديمقراطيون المسيحيون الليتوانيون", "label": "B",
   },
   {
   "text": "حزب العمل", "label": "C"
   },
   {
   "text": "الحركة الليبرالية", "label": "D"
   }
   ],
   "answerKey": "B"
   },

  {
   "question": "في أي قضية واجهت الحكومة الليتوانية التوتر مع الاتحاد الأوروبي في عام 2021؟",
   "choices": [
   {
   "text": "العلاقات التجارية مع الولايات المتحدة", "label": "A"
   },
   {

   "text": "اتفاقيات سياسة المناخ", "label": "B",
   },
   {
   "text": "سياسة اللاجئين والهجرة على حدود بيلاروسيا", "label": "C"
   },
   {
   "text": "قواعد الشفافية المالية", "label": "D"
   }
   ],
   "answerKey": "C"
   },
      
     {
  "question": "في عام 2020، انضمت ليتوانيا إلى دول البلطيق الأخرى وحظرت استيراد الكهرباء من محطات الطاقة النووية الجديدة في أي دولة؟",
   "choices": [
   {
   "text": "روسيا", "label": "B"
   },
   {

   "text": "بيلاروسيا", "label": "A",
   },
   {
   "text": "بولندا", "label": "C"
   },
   {
   "text": "أوكرانيا", "label": "D"
   }
   ],
   "answerKey": "A"
   },
     {
             "question": "في عام 2022، زادت ليتوانيا الإنفاق العسكري بشكل كبير. ما هو السبب الرئيسي وراء هذه الزيادة؟",
   "choices": [
   {
   "text": "تهديدات الصين", "label": "A"
   },
   {

   "text": "متطلبات الإنفاق الدفاعي لحلف شمال الأطلسي", "label": "B",
   },
   {
   "text": "التحديث الداخلي للجيش الليتواني", "label": "C"
   },
   {
   "text": "تصاعد التوترات الإقليمية بسبب الصراع بين أوكرانيا وروسيا", "label": "D"
   }
   ],
   "answerKey": "D"
   },
   {}
  ]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]


def get_dn_messages(prepared_input_text):
  system = """You are answering questions from Lithuanian history. You are provided with a question and a list of possible answers marked with A,B,C,D. Generate the correct answer to the provided question. Output only a letter that corresponds to a correct answer!"""

  examples = [
    {
 "question": "I 2020 blev Seimas-valget afholdt i Litauen. Hvilket politisk parti fik flest mandater?",
 "choices": [
 {
 "text": "Socialdemokraterne", "label": "A"
 },
 {

 "text": "Homeland Union - litauiske kristne demokraters ledelse", "label": "B",
 },
 {
 "text": "Arbejderpartiet", "label": "C"
 },
 {
 "text": "Liberalernes Bevægelse", "label": "D"
 }
 ],
 "answerKey": "B"
 },

{
 "question": "På hvilket spørgsmål stod den litauiske regering over for spændinger med EU i 2021?", 
 "choices": [
 {
 "text": "Handelsforbindelser med USA", "label": "A"
 },
 {

 "text": "Klimapolitiske aftaler", "label": "B",
 },
 {
 "text": "Flygtninge- og migrationspolitik ved grænsen til Hviderusland", "label": "C"
 },
 {
 "text": "Regler for finansiel gennemsigtighed", "label": "D"
 }
 ],
 "answerKey": "C"
 },
    
   {
"question": "I 2020 sluttede Litauen sig til de øvrige baltiske lande og forbød import af elektricitet fra hvilket lands nye atomkraftværker?",
 "choices": [
 {
 "text": "Rusland", "label": "B"
 },
 {

 "text": "Hviderusland", "label": "A",
 },
 {
 "text": "Polen", "label": "C"
 },
 {
 "text": "Ukraine", "label": "D"
 }
 ],
 "answerKey": "A"
 },
   {
 "question":"I 2022 øgede Litauen militærudgifterne markant. Hvad var hovedårsagen til denne stigning?",
 "choices": [
 {
 "text": "Kina trusler", "label": "A"
 },
 {

 "text": "NATOs forsvarsudgifter", "label": "B",
 },
 {
 "text": "Intern modernisering af den litauiske hær", "label": "C"
 },
 {
 "text": "Stigende regionale spændinger på grund af konflikten mellem Ukraine og Rusland", "label": "D"
 }
 ],
 "answerKey": "D"
 }
]
  return get_messages(examples, system) + [{"role": "user", "content": prepared_input_text}]


def get_prompts(lang):
    if lang == "ar":
      return [(get_ar_messages, "ar_few_shot")]
    if lang=="dn":
      return [(get_dn_messages, "dn_few_shot")]
    if lang == "en":
      return [(get_en_messages, "en_few_shot")]
    if lang == "est":
      return [(get_est_messages, "est_few_shot")]
    if lang=="fn":
      return [(get_fn_messages, "fn_few_shot")]
    if lang=="lav":
      return [(get_lav_messages, "lav_few_shot")]
    if lang=="lt":
      return [(get_lt_messages, "lt_few_shot")]
    if lang=="sw":
      return [(get_sw_messages, "sw_few_shot")]
    if lang=="ua":
      return [(get_ua_messages, "ua_few_shot")]




