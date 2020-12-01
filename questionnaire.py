allQuestions = [
    ('userID'      , "Hii! What is your User ID ? (1-50)"),
    ('tripType'    , "What is the type of trip you have ? \n\n1. Business \n2. Leisure\n\nEnter your choice ? (1\\2)"),
    ('companion'   , "How are you travelling ? \n\n1. Couple\n2. Family\n3. Friend\n4. Solo\n\nEnter your choice ? (1\\2\\3\\4)"),
    ('destination' , "What is your destination ? \n\n1. Singapore\n2. Tokyo\n\nEnter your choice ? (1\\2)"),
]

class User:
    def __init__(self, userID=None, tripType=None, companion=None, destination=None):
        self.data = {
            'userID'		: userID		,   # 1 - 50
            'tripType'	    : tripType	    ,   # business | leisure
            'companion'	    : companion		,   # couple | family | friend | solo
            'destination'	: destination       # singapore | tokyo | bankok
        }
    
    def nextQuestion(self):
        for param, question in allQuestions:
            if self.data[param] == None:
                return (param, question)
        else:
            return None, None
    
    def answer(self, param, ans):
        ans = ans.lower()
        if param == 'userID':
            if int(ans) in range(1,51):
                self.data['userID'] = 'user'+ans
                return True
            else:
                return False
        elif param == 'tripType':
            if   ans in ('1', 'business'):
                self.data[param] = 'business'
                return True
            elif ans in ('2', 'leisure'):
                self.data[param] = 'leisure'
                return True
            else:
                return False
        elif param == 'companion':
            if   ans in ('1', 'couple'):
                self.data[param] = 'couple'
                return True
            elif ans in ('2', 'family'):
                self.data[param] = 'family'
                return True
            elif ans in ('3', 'friend'):
                self.data[param] = 'friend'
                return True
            elif ans in ('4', 'solo'):
                self.data[param] = 'solo'
                return True
            else:
                return False
        elif param == 'destination':
            if   ans in ('1', 'singapore'):
                self.data[param] = 'singapore'
                return True
            elif ans in ('2', 'tokyo'):
                self.data[param] = 'tokyo'
                return True
            elif ans in ('3', 'bankok'):
                self.data[param] = 'bankok'
                return True
            else:
                return False
        else:
            return False

    def __str__(self) -> str:
        return '\n'.join([self.data[key] for key in self.data])

if __name__ == "__main__":
    tempUser = User()
    DONE = False

    while True:
        param, question = tempUser.nextQuestion()
        if question:
            correct = tempUser.answer(param, input(question+' : '))
            if not correct:
                print("I'm sorry,I did not Understand.?")
        else:
            break
    
    print("Successfull. Data :\n\n"+str(tempUser))

    from recommender import main
    output = main(
		location  = tempUser.data[  'destination'],
		target_id = tempUser.data[  'userID'     ],
		trip_type = tempUser.data[  'tripType'   ],
		companion = tempUser.data[  'companion'  ]
	)
    print("It's Workin, output is : ", output)


