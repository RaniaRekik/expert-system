from experta import Rule, Fact, KnowledgeEngine, AND, fact


class eyeDisease(KnowledgeEngine):
    #variables for answers
    diseases = ""
    description = ""
    photo = ""

    # Myopia
    @Rule(AND(Fact(itching='0'), Fact(blurring='1'), Fact(redness='0'), Fact(night='1'),
              Fact(mucus='0'), Fact(tear='0'), Fact(yellowing='0'), Fact(headache='1'),
              Fact(cough='0'), Fact(pain='0'), Fact(overstrain='1'), Fact(sensitivity='0'),
              Fact(rainbow='0'), Fact(double='0'), Fact(sightedness='1'), Fact(sight='0'),
              Fact(nausea='0'), Fact(dilated='0'), Fact(eyelid='1')))

    def Myopia(self):
        self.diseases = "Myopia"
        self.description = "Nearsightedness (myopia) is a common vision condition in which you can see objects near to you clearly, but objects farther away are blurry."
        self.photo = r".\photo\Myopia.jpg"


    #conjunctiva
    @Rule(AND(Fact(itching='1'), Fact(blurring='1'), Fact(redness='1'), Fact(night='0'),
              Fact(mucus='1'), Fact(tear='1'), Fact(yellowing='0'), Fact(headache='0'),
              Fact(cough='0'), Fact(pain='1'), Fact(overstrain='1'), Fact(sensitivity='1'),
              Fact(rainbow='0'), Fact(double='0'), Fact(sightedness='0'), Fact(sight='0'),
              Fact(nausea='0'), Fact(dilated='0'), Fact(eyelid='0')))
    def conjunctiva(self):
        self.diseases = "conjunctivitis"
        self.description = "Pink eye (conjunctivitis) is the inflammation or infection of the transparent membrane that lines your eyelid and eyeball. It's characterized by redness and a gritty sensation in your eye, along with itching. "
        self.photo = r".\photo\Conjunctivitis.jpg"

    #Ocular Allergy
    @Rule(AND(Fact(itching='1'), Fact(blurring='0'), Fact(redness='1'), Fact(night='1'),
              Fact(mucus='1'), Fact(tear='0'), Fact(yellowing='0'), Fact(headache='0'), Fact(cough='0'),
              Fact(pain='1'), Fact(overstrain='0'), Fact(sensitivity='1'), Fact(rainbow='0'), Fact(double='0'),
              Fact(sightedness='0'), Fact(sight='1'), Fact(nausea='0'), Fact(dilated='0'), Fact(eyelid='0'),
              ))
    def Allergy(self):
        self.diseases = "Ocular Allergy"
        self.description = "Ocular allergy is an inflammatory reaction of the surface of the eye to particles (allergens) in the environment."
        self.photo = r".\photo\ocular-allergy.jpg"

        #Glaucoma
    @Rule(AND(Fact(itching='0'), Fact(blurring='1'), Fact(redness='1'), Fact(night='1'),
              Fact(mucus='0'), Fact(tear='0'), Fact(yellowing='1'), Fact(headache='0'), Fact(cough='0'),
              Fact(pain='1'), Fact(overstrain='0'), Fact(sensitivity='0'), Fact(rainbow='1'), Fact(double='0'),
              Fact(sightedness='0'), Fact(sight='1'), Fact(nausea='1'), Fact(dilated='1'), Fact(eyelid='0'),

              ))
    def Glaucoma(self):
        self.diseases = "Glaucoma"
        self.description = "Glaucoma is a group of eye conditions that damage the optic nerve, the health of which is vital for good vision. "
        self.photo =r".\photo\Glaucoma.jpg"

    #Cataract
    @Rule(AND(Fact(itching='0'), Fact(blurring='1'), Fact(redness='0'), Fact(night='1'),
                  Fact(mucus='0'), Fact(tear='0'), Fact(yellowing='1'), Fact(headache='0'), Fact(cough='0'),
                  Fact(pain='0'), Fact(overstrain='0'), Fact(sensitivity='1'), Fact(rainbow='1'), Fact(double='1'),
                  Fact(sightedness='1'), Fact(sight='0'), Fact(nausea='0'), Fact(dilated='0'), Fact(eyelid='0'),

                  ))
    def Cataract(self):
        self.diseases = "Cataract"
        self.description = "cataract is a clouding of the normally clear lens of the eye. For people who have cataracts, seeing through cloudy lenses is a bit like looking through a frosty or fogged-up window. "
        self.photo = r".\photo\cataracts.png"
