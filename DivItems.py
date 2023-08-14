import time
import funcs, styles

from rich.console import Console
from rich.style import Style
from rich.styled import Styled

console = Console()


class DivItem:
    def __init__(self):
        self.title = ""
        self.header = ""
        self.sign = ""
        self.family = ""
        self.aims = ""
        self.friends = ""
        self.enemies = ""
        self.guests = ""
        self.illness = ""
        self.evil_spirits = ""
        self.practice = ""
        self.lost = ""
        self.will_they = ""
        self.all_matters = ""

    def submenu(self):
        console.print('\n' + self.title + '\n', style=f'{funcs.primary_color[0]}', justify="center")
        time.sleep(1)
        console.print(Styled('\n' + self.header + '\n', styles.header), justify="center")
        console.print(Styled('\n' + self.sign + '\n', styles.regular), justify="center")


        while True:
            console.print(Styled(
                '[1] Family, property and life' + '\n' +
                '[2] Intentions and aims' + '\n' +
                '[3] Friends and wealth' + '\n' +
                '[4] Enemies' + '\n' +
                '[5] Guests' + '\n' +
                '[6] Illness' + '\n' +
                '[7] Evil spirits' + '\n' +
                '[8] Spiritual practice' + '\n' +
                '[9] Lost article' + '\n' +
                '[10] Will they come, and will the task be accomplished' + '\n' +
                '[0] All remaining matters' + '\n' +
                'Press [A] to print all' + '\n' +
                'Press [Q] to quit' + '\n'
            , styles.regular))

            choice = input()

            if choice == '1':
                console.print(Styled('\n' +self.family + '\n \n', styles.regular), justify="center")
            elif choice == '2':
                console.print(Styled('\n' +self.aims + '\n \n', styles.regular), justify="center")
            elif choice == '3':
                console.print(Styled('\n' +self.friends + '\n \n', styles.regular), justify="center")
            elif choice == '4':
                console.print(Styled('\n' +self.enemies + '\n \n', styles.regular), justify="center")
            elif choice == '5':
                console.print(Styled('\n' +self.guests + '\n \n', styles.regular), justify="center")
            elif choice == '6':
                console.print(Styled('\n' +self.illness + '\n \n', styles.regular), justify="center")
            elif choice == '7':
                console.print(Styled('\n' +self.evil_spirits + '\n \n', styles.regular), justify="center")
            elif choice == '8':
                console.print(Styled('\n' +self.practice + '\n \n', styles.regular), justify="center")
            elif choice == '9':
                console.print(Styled('\n' +self.lost + '\n \n', styles.regular), justify="center")
            elif choice == '10':
                console.print(Styled('\n' +self.will_they + '\n \n', styles.regular), justify="center")
            elif choice == '0':
                console.print(Styled('\n' +self.all_matters + '\n \n', styles.regular), justify="center")
            elif choice.lower() == 'a':
                self.print_all()
            elif choice.lower() == 'q':
                break
            else:
                print(" \n Choose a valid option and press Enter. \n")

    def print_all(self):
        print('\n')
        print(self.title + '\n')
        print(self.header + '\n')
        print(self.sign + '\n')
        print('FAMILY, PROPERTY AND LIFE' + '\n' + self.family + '\n')
        print('INTENTIONS AND AIMS' + '\n' + self.aims + '\n')
        print('FRIENDS AND WEALTH' + '\n' + self.friends + '\n')
        print('ENEMIES' + '\n' + self.enemies + '\n')
        print('GUESTS' + '\n' + self.guests + '\n')
        print('ILLNESS' + '\n' + self.illness + '\n')
        print('EVIL SPIRITS' + '\n' + self.evil_spirits + '\n')
        print('SPIRITUAL PRACTICE' + '\n' + self.practice + '\n')
        print('LOST ARTICLE' + '\n' + self.lost + '\n')
        print('WILL THEY COME, AND WILL THE TASK BE ACCOMPLISHED' + '\n' + self.will_they + '\n')
        print('ALL REMAINING MATTERS' + '\n' + self.all_matters + '\n')







AH_AH = DivItem()
AH_AH.title = 'The Stainless Sky'
AH_AH.header = 'If AH AH - the stainless sky - appears, then the inquirer should listen. Just as the sky is free from stains, so your mind should be completely purified and placed in equanimity.'
AH_AH.sign = 'The sign of this divination is "the sound of threefold emptiness."'
AH_AH.family = 'There is no harm to your family, property and life, and they will be very happy.'
AH_AH.aims = 'Since there is equanimity, there will be no obstructions to the fulfillment of your intentions and aims. This AH AH prediction is the most propitious for averting negative forces and bad omens. If you rely upon the Buddhas and Bodhisattvas, then obscurations will be cleared and results will be quickly obtained. If you had previous troubles or unhappiness, these will be righted.'
AH_AH.friends = 'Though you have friends and wealth, it will be difficult for them to remain with you in the future. If you desire to retain them, you should make offerings of flowers and the like to the Prajnaparamita Sutras-the discourses on the Perfection of Wisdom.'
AH_AH.enemies = 'There are no enemies.'
AH_AH.guests = 'There will be a smooth and comfortable journey for the guests that you are expecting.'
AH_AH.illness = 'It is seen that you are healthy, and there are no negative forces or evil spirits whatsoever bothering you.'
AH_AH.evil_spirits = 'There are no negative forces or evil spirits whatsoever bothering you.'
AH_AH.practice = 'There will be success in abandoning unwholesome tendencies and in accomplishing meditation. Faults and obscurations will be completely purified.'
AH_AH.lost = 'If it is still near the location where you left it, it will be found. Otherwise, it will be difficult to regain.'
AH_AH.will_they = 'There are equal chances either way. So things can be accomplished, but only slowly.'
AH_AH.all_matters = 'There is also only an average chance of success in regards to any other inquiry. In order to make the questioned matter possible and to make it successful, you should rely upon Vajrasattva as your special deity, recite the One Hundred Syllable Mantra of Vajrasattva, and recite any of the long, middle or short Prajnaparamita Sutras. Also, you can rely upon Akashagarbha as a special deity. \n This prediction is known as "the giving of fearlessness."'


AH_RA = DivItem()
AH_RA.title = 'The Flaming Rays of the Sun'
AH_RA.header = 'f AH RA the flaming rays of the sun - appears, then whatever the inquirer asks will be unreservedly settled like the clarity of the sun, and it will be very good.'
AH_RA.sign = 'The sign of this divination is known as dustless and clear."'
AH_RA.family = 'Your family, property and life will be good if you diligently engage in virtuous deeds.'
AH_RA.aims = 'If you cut the net of doubt enveloping yourself, then they will turn out well.'
AH_RA.friends = 'If you obtain shiny articles such as crystals, gems and the like, or red-colored articles, then there will be a slight improvement.'
AH_RA.enemies = 'There are no enemies'
AH_RA.guests = 'Your guests will journey with ease, and you will hear precise, pleasing news concerning them.'
AH_RA.illness = 'You will quickly recover from your illness, and there is no trouble from evil spirits.'
AH_RA.evil_spirits = 'There is no trouble from evil spirits.'
AH_RA.practice = 'Through practice, your intelligence, learning and contemplation will increase.'
AH_RA.lost = 'If you search in a southwesterly direction from where it has been lost, then it will be found. Someone will come to give you news about it.'
AH_RA.will_they = 'The meaning of this will be clearly known to you.'
AH_RA.all_matters = 'Although the prediction for all remaining questions are quite all right, nevertheless the outcome of work involving earth, houses, and objects which are used as supports-such as tables and so on - is slightly bad. If you rely upon wisdom deities such as Manjushri, offer butter lamps and prayer flags, and recite various sutras such as Dispelling the Darkness in the Ten Directions, then the work will turn out well. \n This prediction is known as "the departing of darkness."'


AH_PA = DivItem()
AH_PA.title = 'Nectar Rays of the Moon'
AH_PA.header = 'If AH PA - the good moon - appears, then just as the rays of nectar, the moon, illumine the sky, so the accomplishment ofpeaceful, increasing and virtuous activities is assured.'
AH_PA.sign = 'The sign of this divination is called "the enjoyment of sense-desire objects where there is no assemblage of obstacles."'
AH_PA.family = 'If you perform the rituals of cleansing pollutions and of washing, then you will be able to increase the number of your children.'
AH_PA.aims = 'There are no obstacles in regards to your intentions and aims. It is especially good to perform gentle, peaceful activities; a strong effect will not arise through power or violent activities.'
AH_PA.friends = 'All white colored objects, food and drink will increase.'
AH_PA.enemies = 'There are no enemies.'
AH_PA.guests = 'Your guests\' journeys will be comfortable, and they will arrive soon.'
AH_PA.illness = 'You will quickly recover from cold and digestive diseases.'
AH_PA.evil_spirits = 'There are no evil spirits bothering you whatsoever.'
AH_PA.practice = 'The virtuous mind is good and virtues will increase.'
AH_PA.lost = 'If you request a woman to investigate in a southern or northern direction, then the object will be found.'
AH_PA.will_they = 'It will be accomplished.'
AH_PA.all_matters = 'It is predicted that works involving women and any easy, non-strenuous activities are good. Any activity involving fire is slightly bad. Little things and happiness will increase by relying upon female deities such as White Tara and Ushnisha Vijaya. You should recite any sutra in which predictions for enlightenment are given to women. Perform the water-giving ritual and water-washing ritual to avoid punishment. It is very good if you perform offerings to nagas. Also, through relying upon any guru yoga practice, good results will arise. \n This prediction is known as "dense, good clouds."'


AH_TSA = DivItem()
AH_TSA.title = 'The Bright Star'
AH_TSA.header = 'If AH TSA - the very bright star - appears, then, if you work with steadfastness and carefulness of mind, there will be a good result.'
AH_TSA.sign = 'The sign of this divination is known as "the non-dispersion of the beautiful accumulation which has been gathered."'
AH_TSA.family = 'If you hang prayer flags and burn incense then all of these will turn out well.'
AH_TSA.aims = 'Any activity which involves going, travelling and movement, as well as acts of giving, will have good results.'
AH_TSA.friends = 'You will receive wooden articles,animals, green cloth and the like, in addition to news and letters.'
AH_TSA.enemies = 'There are no enemies.'
AH_TSA.guests = 'Your guests will have comfortable journeys and will arrive very, very soon.'
AH_TSA.illness = 'An air illness and agitation of the mind are present,but they are not very bad. It would be helpful if you were to worship your ancestors,make offerings to tree spirits,and the like.'
AH_TSA.evil_spirits = 'Though there are no evil spirits attacking you, there is the slight fault of having too many agitated, fickle thoughts. Through relying upon steadiness and firmness of mind, things will tum out well.'
AH_TSA.practice = 'Any type of spiritual practice will have a good result,especially if you do it in a location other than where you usually practice.'
AH_TSA.lost = 'Although it has been taken by another person, it is possible to find it should you search quickly in a northern or eastern direction from where it was lost.'
AH_TSA.will_they = 'It is said that it will be accomplished.'
AH_TSA.all_matters = 'These will be positive, although any activity involving water is slightly unfavorable. You should rely upon activity deities such as Green Tara. Perform ritual offerings to the Dharma Protectors, and hang as many prayer flags as possible. Perform circumambulations, prostrations and torma-throwing rituals. Recite any sutras, such as the Buddha Avatamsaka Sutra and those involving stories of the Buddhas and Bodhisattvas going to other lands. If green deities are relied upon, all activities will be quickly accomplished. \n Thus this prediction is known as increasing the power of air like the revolution of the energy currents in the sky.'


AH_NA = DivItem()
AH_NA.title = 'The Ground of Gold'
AH_NA.header = 'If AH NA - the ground of gold - appears, then steady work will be accomplished and have good results, just as the earth is good.'
AH_NA.sign = 'The sign of this divination is known as "the inability to guess accurately so that the answer will remain unresolved."'
AH_NA.family = 'Family, property and life are very stable and are in excellent condition.'
AH_NA.aims = 'Since your intention is firm , it is advisable to remain in your own location. Then your plan will not be aborted.'
AH_NA.friends = 'The long-term future is good, but it will take some time to obtain it.'
AH_NA.enemies = 'There are no enemies.'
AH_NA.guests = 'Generally their journey is good, but it will be some time before they arrive.'
AH_NA.illness = 'There is a slight phlegm disease, but it is not bad. It will be difficult to cure the disease immediately, so you should perform a fire ritual, erect "mani" prayer wheels that are turned by the wind, and hang many prayer flags.'
AH_NA.evil_spirits = 'There are no evil spirits bothering you.The blame for your trouble should be placed upon the unsuitableness of the earth and water in your locale.'
AH_NA.practice = 'The future is good, and this is especially true should you practice continually in one place.'
AH_NA.lost = 'It will be found by one of your own people. Otherwise, search in an eastern direction from where it was lost. If it isn\'t found quickly, then it will be difficult to find in the future.'
AH_NA.will_they = 'It will take some time, so don\'t be overly enthusiastic.'
AH_NA.all_matters = 'If done quickly, things will turn out well. However, any activity involving air, the sending of letters, news and the like, is unfavorable. It is good if you rely upon Vajra deities such as Shakyamuni, Achala, and so on, as well as on Quality or Jewel deities like Ratnasambhava. Also, it is good to perform wealth-propitiating rituals, make a hundred thousand small earth stupas, carve mantras upon rocks, erect images, and make offerings to earth gods. \n This prediction is known as "if you stay here, the basis will become firm."'


AH_DHIH = DivItem()
AH_DHIH.title = 'The Tone of the Vajra'
AH_DHIH.header = 'If AH DHI, Vajra Saraswati - the tone of the vajra - appears, then the happiness of mind will increase as it does when one hears good news, and all will be good.'
AH_DHIH.sign = 'The sign of this divination is known as "increasing the measureless intelligence by the goddess of mind." Generally speaking, this divination augurs well for the studies of science, arts and Buddhist scriptures.'
AH_DHIH.family = 'If you perform long-life meditations and rituals of female deities, then your life will be firm and stable.'
AH_DHIH.aims = 'You will achieve them.'
AH_DHIH.friends = 'There is quite a good chance of happiness.'
AH_DHIH.enemies = 'Enemies will not arise, and the gods will protect you.'
AH_DHIH.guests = 'Their journey will be happy and comfortable, and they will arrive quickly.'
AH_DHIH.illness = 'Illnesses will be allayed.'
AH_DHIH.evil_spirits = 'There are definitely no evil spirits bothering you. There is no cause for trouble even though the omens appear unpleasant, and so in actuality the situation is favorable. Pray to your special deity and this will clear your mind of the confusion.'
AH_DHIH.practice = 'If you practice the meditation of Vajra Saraswati then your intelligence will increase and this will be beneficial.'
AH_DHIH.lost = 'If you employ skillful means, it will be found.'
AH_DHIH.will_they = 'You will accomplish it just as you wish.'
AH_DHIH.all_matters = 'All of them are favorable. Perform peaceful activities; any activity involving women is especially good. For your own special deity, select any of the three Masters - Avalokiteshvara, Manjushri or Vajrapani - or any of the other Bodhisattvas. Also, it is good for you to rely upon the Mothers\' Mandala of the Heruka family, the Clear Light practice, and the Yoga of Desire. You should recite such Tantras as the Chakrasamvara and Vajra Dakini, and sutras such as the Samadhi Raja Sutra. Perform ritual offerings to the Mamos, and rely upon Dharma Protectors such as the Damchen pair, the five Tsering Chedma goddesses, and peaceful protectors who appear riding an animal. Especially pray to Makzerma and Reti. In this way, whatever you wish or strive for with your mind, you will achieve. \n This prediction is known as "that which moves to pleasantly increase and expand one\'s intelligence."'

RA_AH = DivItem()
RA_AH.title = 'The Bright Lamp'
RA_AH.header = 'If RA AH - the bright lamp - appears, then one\'s own mind is very clear and excels, just as a lamp excels in dispelling darkness.'
RA_AH.sign = 'The sign of this divination is known as "the bright lamp without wind".'
RA_AH.family = 'These are currently favorable.'
RA_AH.aims = 'You can do just as you wish; there will be success.'
RA_AH.friends = 'The current situation is good.'
RA_AH.enemies = 'None will arise. You may hear that your enemies are a long way off, but they will not be able to harm you.'
RA_AH.guests = 'You will hear clear news about them, and their journey will be comfortable.'
RA_AH.illness = 'Your illness will get worse.'
RA_AH.evil_spirits = 'There is no evil spirit bothering you. Your trouble is arising due to the power of previous deeds, but there will be no harm.'
RA_AH.practice = 'There will be no obstacles to your practicing by yourself.'
RA_AH.lost = 'If you search in a southwesterly direction from where it was lost you will find it.'
RA_AH.will_they = 'If you commence with diligence there will not be any obstacles and it will be accomplished.'
RA_AH.all_matters = 'No faults will be encountered in whatever activities you undertake. Read sutras such as the Kalpa Bhadra Sutra, and rely upon Lotus deities such as Amitayus, Kurukulle, Marichi, and the like. If you practice the meditation of Humkara Father-Mother and Red Garuda then you will have success. Rely upon suchDharma Protectors as the great deity Tsimar. Obstacles will be prevented from arising by clearing roads and walkways, performing fire rituals, and so on, and in this way you will accomplish your wishes. \n This prediction is known as "the one who helps oneself."'


RA_RA = DivItem()
RA_RA.title = 'Adding Butter to the Burning Flames'
RA_RA.header = 'If RA RA - the horse-headed deity Shri Hayagriva - appears, then all activities of power will be accomplished favorably and well.'
RA_RA.sign = 'The sign of this divination is known as to add butter again and again to the burning flames of desire.'
RA_RA.family = 'These will increase well. Also, the beauty of your body will be enhanced.'
RA_RA.aims = 'These will quickly be accomplished, and you will also hear some clear news concerning them. If you recite the proper number of mantras of any dakini practice, then your activities will expand and be in sharper focus.'
RA_RA.friends = 'Any articles which are dry by nature and of a red color will increase. Especially, by performing as many power fire rituals as you can do then your happiness will increase greatly.'
RA_RA.enemies = 'Though there are no enemies opposing you, if you wish to attack,there will soon be clear news that you\'ll be able to destroy the enemy through the east or in the center.'
RA_RA.guests = 'They will arrive soon and their journey will be comfortable.'
RA_RA.illness = 'In order to cure such diseases as heat, blood and contagious illnesses, you need treatment as well as the performance of rituals. Other types of diseases will be quickly cured.'
RA_RA.evil_spirits = 'There are no evil spirits attacking you. However,you are engaged in great works which are ill-planned,and so you are experiencing trouble. The attendants of the Wrathful Deities are not pleased with you,so if you make offerings to various types of worldly gods it will be good.'
RA_RA.practice = 'The performance of virtuous deeds and power activities will increase, and will be favorable for you.'
RA_RA.lost = 'It will be found in a southern or western direction from where it was lost.'
RA_RA.will_they = 'They will be accomplished quickly.'
RA_RA.all_matters = 'All are good, though any activities involving firm objects, earth and water are very bad. Engaging in them would be like water being exhausted through boiling or a summer pond being dried up You should rely upon wrathful deities of the Lotus-family, and power deities such as Hayagriva and Takkiraja. Recite sutras and tantras of Avalokiteshvara, such as Amoghapasha. If you depend upon power and wrathful deities, then your purposes will be quickly achieved and you will be happy like a fire that flames up. \n This prediction is known as "increasing the demonstration of joy."'


RA_PA = DivItem()
RA_PA.title = 'The Demon of Death'
RA_PA.header = 'If RA PA - the demon of death - appears, then the symbol is destruction. Just as a spark of fire is extinguished by a small amount of water, so whatever work you engage in is nonvirtuous and unsuccessful since it is clasped by the Lord of Death. The essence of this is that one departs through the outer southern door.'
RA_PA.sign = 'The sign of this divination is known as "killing, death and destruction."'
RA_PA.family = 'There is death and great obstacles. To overcome these, clean scriptural texts of dust and dirt, and perform a torma-throwing ritual of some wrathful deity.'
RA_PA.aims = 'As there are great hindrances and obstacles, these will not be accomplished. It is best to postpone efforts to fulfill them.'
RA_PA.friends = 'There are no friends or wealth, and you will have obstacles in trying to gain them.'
RA_PA.enemies = 'There are enemies about. Especially, you must refrain from going in a southern or northern direction.'
RA_PA.guests = 'They will encounter an uncomfortable journey with obstacles on the path. Perform a White Umbrella Deity ritual.'
RA_PA.illness = 'There is a great danger to the ill person. Those with cold diseases or where water has accumulated in the body will have a very difficult time. If you don\'t recite mantras and perform rituals to the Protectors quickly and diligently, then it will be difficult to cure the disease.'
RA_PA.evil_spirits = 'You are being harmed by impure drinking substances, round shaped articles which are dark blue in color, black articles such as certain types of food, wealth and ornaments of a widow, or pollutions arising from mixing your clothes together with the dirty clothes of a sick person or arising from the breaking of your vows. You should perform a releasing ritual (ched drob) of Tara or Vajrakilaya, and make offerings to the nagas. Even though the trouble comes from where you never suspect it, still you must protect yourself from unexpected troubles coming from water spirits, ghosts, and the like.'
RA_PA.practice = 'There are great obstacles. You should recite the Refuge Prayer to the Three Jewels one hundred thousand times. Also, perform the torma-throwing rituals and releasing rituals, and recite various sutras, and do other violent rituals directed towards the north. If these are not done, then it is very unfavorable. This divination shows great harm and obstacles to your life since it is like a flash fire which dies immediately. Recite the Amitayus Sutra and dharani as many times as possible.'
RA_PA.lost = 'Though it has been taken in a southern or northern direction, you won\'t be able to see it again even if you trace it.'
RA_PA.will_they = 'Since there is a wrong intention involved, it will be obstructed and so cannot be accomplished.'
RA_PA.all_matters = 'Though all inquiries will have a bad outcome, activities such as hunting, making poisons and acts of destruction will have favorable conclusions. \n This prediction is known as "the activity which accomplishes destruction."'


RA_TSA = DivItem()
RA_TSA.title = 'The King of Power'
RA_TSA.header = 'If RA TSA - the king ofpower - appears, then spontaneous strength arises from oneself, just as a forestfire is increased when s tirred by the wind. Here, activities of power and violence are endowed with sharp potential.'
RA_TSA.sign = 'According to the essence of the words of the consort of Yamantaka the Destroyer, the sign of this divination is known as "giving power to those who enter into this." This divination is also known as "the roar of brave tigers and lions."'
RA_TSA.family = 'As the strength of your power is increasing, nothing whatsoever can harm you.'
RA_TSA.aims = 'Being endowed with strength, whatever you wish will be achieved. It is excellent to perform activities of summoning and of violence. It is also good if you act in accordance with the essential practice of your special meditation deity.'
RA_TSA.friends = 'Your wealth will increase. Especially, green articles and those of oblong or oval shape will increase.'
RA_TSA.enemies = 'Since there are no enemies opposing you,you will be victorious over all classes of enemies.'
RA_TSA.guests = 'Guests and visitors will have a comfortable journey and will arrive quickly. Also, you will meet with benefit.'
RA_TSA.illness = 'Though your illness is acting up, there is no danger. You should make offerings to the Dharma Protectors.'
RA_TSA.evil_spirits = 'As the Protectors are guarding you,there are no evil spirits whatsoever troubling you. Though you think you have made great offerings to the Protectors, those are not enough and you must make even more offerings than before.'
RA_TSA.practice = 'Whatever aims you have, they will be well achieved.'
RA_TSA.lost = 'It will be obtained through force.'
RA_TSA.will_they = 'If you rely upon your special deity, they will come and all tasks will be accomplished.'
RA_TSA.all_matters = 'Though it is predicted that all remaining questions are favorable and your strength will be increased, know that any activity involving water, such as making rain, will have only mediocre results. Rely upon Vajrakilaya, the wrathful manifestation of Guru Padmasambhava, and your special meditation deity. By praising the power of theD harma Protectors, you will be protected. If you offer incense and hang prayer flags, then all activities you wish to perform will be endowed with great power and so will be successful. If you rely upon the Dharma Protectors, Ganapati, Mahakala and the planet-demon Rahula, you will gain the spiritual attainments. \n This prediction is known as "increasing power and strength."'

RA_NA = DivItem()
RA_NA.title = 'The Dried-up Tree'
RA_NA.header = 'If RA NA - the tree that is not wet - appears, then know that there will be no result whatsoever, just as no fruit will come from a dried-up tree.'
RA_NA.sign = 'The sign of this divination is proclaimed by the Gandharva (smell-eating being), the messenger of the demon Mara who resides in the southeast, who said, "Since one\'s mind is always afflicted, one\'s wishes are never achieved. So, this is suffering."'
RA_NA.family = 'Though there are no faults for the time being, in the future these matters will not go very well. Therefore, overall, the outlook is simply mediocre.'
RA_NA.aims = 'Being like a fire that suddenly flares up and then sputters out, they are difficult to accomplish.'
RA_NA.friends = 'There are none whatsoever.'
RA_NA.enemies = 'Although there are minor enemies, they are unable to cause you great harm.'
RA_NA.guests = 'Since the visitors will be tired and weary on their journey, there will be some delay in their arrival.'
RA_NA.illness = 'A lthough you will temporarily suffer from a bilious disorder, it will not be harmful to you.'
RA_NA.evil_spirits = 'Through attachment to ancestors or relatives who have died, trouble is arising, but no harm will result. Through compassion, you should perform some rituals to repay your debt of kindness to deceased relatives. Further, as you have broken your wealth relationship with the local and earth gods, you should recite the Suvama Prabha Sutra and various wealth propitiating rituals. It is good to accumulate merits, and also it is important to rectify disturbances caused by earth spirits whom you previously agitated.'
RA_NA.practice = 'Having too many wishes, it is hard for you to accomplish all of them - just as difficult as it is for a child to catch a rainbow.'
RA_NA.lost = 'It has been stolen and hidden by another, so it will be difficult to recover.'
RA_NA.will_they = 'Since your wishes are influenced by others, your activities are like dreams. So, it will be difficult to see the reults of achievement.'
RA_NA.all_matters = 'These are not good. Especially, any inquiry regarding the wish to obtain happiness or a special article has a very unfavorable prognosis. Postponing a task will bring benefit. Rituals which could be performed to alleviate the problem are the recitation of the Ten Wheels of Kshitigarbha, and mantras or dharanis for increasing wealth and livelihood such as the Suvarna Prabha Sutra. Recitation of the Manjushri Root Tantra and the like is also good. \n This prediction is known as "essenceless and inconceivable"'


RA_DHIH = DivItem()
RA_DHIH.title = 'The Door of Auspicious Visions'
RA_DHIH.header = 'If RA DHI - the guard of the south - appears, then it is good, as this is the door of auspicious visions. Further, the eye of transcendental wisdom will open.'
RA_DHIH.sign = 'The sign of this divination is known as "summoning the goddess of the west as a friend."'
RA_DHIH.family = 'Your fortune will increase, and the quality of your life is good.'
RA_DHIH.aims = 'If you follow the advice of a good friend, then there will be success. Various practices for seeing visions upon mirrors and the like will also be successful.'
RA_DHIH.friends = 'If these are cultivated with diligence, then achievements will be made.'
RA_DHIH.enemies = 'There are none.'
RA_DHIH.guests = 'Their journey will be comfortable and they will arrive soon.'
RA_DHIH.illness = 'Rituals done for the sick person will enhance chances of an immediate recovery.'
RA_DHIH.evil_spirits = 'There are none bothering you.'
RA_DHIH.practice = 'This is good. Especially, any practice which deals with the purification of precepts will be beneficial.'
RA_DHIH.lost = 'If you search in a southern or western direction from where it was lost, it will be found.'
RA_DHIH.will_they = 'It will be accomplished.'
RA_DHIH.all_matters = 'All are good, and you should quickly tum your mind from engaging in unsuitable, non-virtuous activities. It is advisable to rely upon Red Yamantaka. Further, your objectives and goals will increase and good signs will arise if you perform any religious practice involving voice goddesses, deities of the Lotus-family, goddesses such as Marichi, and Dharma Protectors such as Dorje Lekpa. Read various sutras and tantras, and if you burn many butter lamps and recite the prayer to Guru Padmasambhava as many times as possible, then your intentions will be achieved. \n This prediction is known as "advice from a beneficial friend."'


PA_AH = DivItem()
PA_AH.title = 'The Vase of Nectar'
PA_AH.header = 'If PA AH - the vase of nectar - appears, then activities of peace are accomplished, just as a vase is filled with nectar.'
PA_AH.sign = 'The sign of this divination is known as "drink nectar and gain immortality."'
PA_AH.family = 'The outlook for these is good.'
PA_AH.aims = 'There are no obstructions whatsoever, so you will achieve your aims. There is great benefit in fulfilling the wishes of the guru just as he desires.'
PA_AH.friends = 'Just as you can obtain whatever you desire from a wish-fulfilling vase, so you receive benefit from friends and wealth.'
PA_AH.enemies = 'There are no enemies since all are endowed with a peaceful mind.'
PA_AH.guests = 'Visitors will arrive safely and quickly, but a child may have some obstacles or troubles on the journey and thus will not arrive as soon as expected.'
PA_AH.illness = 'Medical treatment and performance of rituals will become like nectar, benefiting you quickly.'
PA_AH.evil_spirits = 'There are none bothering you whatsoever.'
PA_AH.practice = 'Performance of peaceful activities and the like is good. Further, it is favorable to rely upon deities that purify obscurations such as Vairochana (Sarva Vidya), the Medicine Buddha, Akshobhya and the like.'
PA_AH.lost = 'Search in a southern direction, or near a pond or stream.'
PA_AH.will_they = 'Having accomplished the task, you will be glad and without regret though you won\'t be as satisfied by it as you had anticipated.'
PA_AH.all_matters = 'All of these will tum out all right. However, any activities involving poison, and the like, will not be successful. All unfavorable conditions will be pacified if you perform washing rituals, rituals which lead beings to liberation at the time of death, confessions, and other purification rituals. This prediction is known as "the turbulent activities involving relatives and peaceful people."'


PA_RA = DivItem()
PA_RA.title = 'The Pool Without a Source of Water'
PA_RA.header = 'If PA RA - a pool without any source of water - appears, then wealth declines, just as a flow of water stops when its source is cut off'
PA_RA.sign = 'The sign of this divination is known as "the assembly of demons residing in the southwest who are the messengers of Mara, said, \'What is the use of building a castle on the sandy shore of an ocean?\' '
PA_RA.family = 'Though there is no problem for the immediate future, in the long run the outlook is slightly unfavorable. Therefore, you should accumulate merit.'
PA_RA.aims = 'The outlook for the accomplishment of your aims is only mediocre, and no benefit can come from friends.'
PA_RA.friends = 'Though something will be obtained, it will neither last nor be of benefit.'
PA_RA.enemies = 'Although there are many enemies who are greater than you think, they will not be able to actually harm you.'
PA_RA.guests = 'The visitors will have regret for their journey, but they will not face failure. They will also have difficulty in arriving on time.'
PA_RA.illness = 'There will be physical disturbances of the body and great unhealthiness. You should perform as many repayment rituals and substitute rituals as possible.'
PA_RA.evil_spirits = 'Although there is a little trouble arising from an article that was owned by a man and woman who separated and are resentful, still, since it cannot be identified, the harm will be minimal.'
PA_RA.practice = 'Good results will not be produced. You are undecided and confused. Furthermore, you have faulty and unwholesome intentions. Besides, the methods you are employing are not good. Therefore, you should recite confession prayers, the Prayer of Samantabhadra, the Avatamsaka Sutra, the Kalpabhadra Sutra, and other sutras. Also recite the Lalita Vistara Sutra; the reading of the Prajnaparamita Sutra in Eight Thousand Verses will be beneficial. Especially, recite the prayer and mantra of Guru Padmasambhava many times. The faithless must produce faith.'
PA_RA.lost = 'Since that lost article is unusable, even if it is found it will be of no benefit to you.'
PA_RA.will_they = 'Though you will commence the task, it will be difficult to gain a good result.'
PA_RA.all_matters = 'They are unfavorable. This is especially true for making relationships. Since destroying your goals is like destroying your work itself, it would be good to move to any other place, change your timings, and so on. Make many offerings of food and of other articles to the Sangha. Rely upon the dakinis such as Sang Ye and Simha Mukha. Also, it is good to perform burnt-food rituals, substitute rituals, and repayment rituals. \n This prediction is known as "decreasing of happiness."'


PA_PA = DivItem()
PA_PA.title = 'The Ocean of Nectar'
PA_PA.header = 'If PA PA - the ocean of nectar - appears, then wealth increases, just as the great ocean is filled with water'
PA_PA.sign = 'The sign of this divination is known as "the saying of Ushnisha Vijaya, \'the summer river increases.\' "'
PA_PA.family = 'They are currently good, and will increase.'
PA_PA.aims = 'You will obtain much wealth, prosperity and favorable conditions.'
PA_PA.friends = 'They will be inexhaustible like the water of a great ocean.'
PA_PA.enemies = 'No enemies will arise, and old ones will be reconciled.'
PA_PA.guests = 'Their journey will be comfortable and they will arrive on time.'
PA_PA.illness = 'If it is only a cold disease, then it is not bad. However, if it is a water disease, then the prospects of recovery are only fair.'
PA_PA.evil_spirits = 'There are none whatsoever that are bothering you. However, there is a danger of increasing attachment due to meeting with others.'
PA_PA.practice = 'It is very good. Through the practice of peaceful activities, the spiritual attainment of peaceful activities will be achieved.'
PA_PA.lost = 'It will be found either by a relative or by your searching in a northern or southern direction from where it was lost.'
PA_PA.will_they = 'All people involved are in harmony and so it will be accomplished effortlessly.'
PA_PA.all_matters = 'The outlook for all is favorable and good, and food and drink will increase. Especially, any activity involving water is good. However, engagements, marriage and so on, and works involving fire are not so good. You should recite the Avatamsaka Sutra and various dharanis. Through cleaning images and making offerings to nagas, the obtainment of the objects of your wishes will increase. Also, if diseases and other disturbances are not very great, they can be allayed. \n This prediction is known as "the washing that cleanses."'


PA_TSA = DivItem()
PA_TSA.title = 'The Demon of Afflictions'
PA_TSA.header = 'If PA TSA - the demon ofafflictions - appears, then happiness will be destroyed, just as the earth belaw the ocean is torn away by currents.'
PA_TSA.sign = 'The sign of this divination is known as "the vicious Yaksha demon who dwells at the outer gate of the north said, \'The ocean was agitated and muddied by the tail of the malicious naga.\'"'
PA_TSA.family = 'There are obstructions and great disturbances.'
PA_TSA.aims = 'For anything that you intend or aim, there are disturbance of mind and unhappiness.'
PA_TSA.friends = 'The outlook is unfavorable; they are like dust being carried away by the wind.'
PA_TSA.enemies = 'There is most probably an enemy. Especially, you will face harm from the east or north. There will most probably be a suit filed against you.'
PA_TSA.guests = 'Those on the journey will be endangered by getting lost, having something broken, or falling.'
PA_TSA.illness = 'There are air diseases and diseases of the veins and tendons that hamper movement. In order to remedy the pain you are experiencing from these, it is necessary to make torma offerings to the spirits and to perform the three parts ritual as many times as possible. Also, recite various sutras and the Prayer of Samantabhadra, release animals, and perform the Four Mandalas Ritual of Tara. It would be good to perform the meditation retreat of Achala as well.'
PA_TSA.evil_spirits = 'There is an attack of spirits belonging to the wood or green class. This is probably caused by a naga ritual or black magic being done against you. Also, you are being harmed by reciprocal fighting, people saying bad things against you, or by your having gone to gatherings where there is fighting and quarreling.'
PA_TSA.practice = 'Your mind will be disturbed, agitated and unhappy. You will break your vows. Therefore, you should rely upon Achala, perform torma-repelling rituals of a wrathful deity, hang prayer flags, and clean the dust from Dharma books.'
PA_TSA.lost = 'The article went into the wrong hands and will not be recovered.'
PA_TSA.will_they = 'Since your mind is very disturbed, it will be difficult to accomplish the task.'
PA_TSA.all_matters = 'They are unfavorable. Especially, the agitation of your mind and thoughts is great. However, there will be success in doing evil actions, such as causing people to separate, causing someone to leave you, and the like. There will be benefit by constructing small clay yellow stupas and other types of yellow stupas. \n This prediction is known as "the boiling of agitation."'


PA_NA = DivItem()
PA_NA.title = 'The Golden Lotus'
PA_NA.header = 'If PA NA - the golden lotus - appears, then any aim whatsoever will be successful, just as green crops ripen into yellow kernels. Also, this is called "the unploughed harvest. "'
PA_NA.sign = 'The sign of this divination is known as "from the speech of the very pleasing consort of White Manjushri who said, \'A garden of mandara flowers moistened by the rain of nectar is very beautiful.\'"'
PA_NA.family = 'There are excellent conditions, so these are very good.'
PA_NA.aims = 'They will become better and better.'
PA_NA.friends = 'These will increase and benefit you greatly. Especially, if you perform wealth-propitiating rituals of Vasudharani, Vaishravana, and Jambhala your wealth will increase. You should also rely upon the Dharma Protector Men Tsun.'
PA_NA.enemies = 'There are none against you.'
PA_NA.guests = 'Their journey will be comfortable and their purpose will be accomplished. However, the journey will be a little slow.'
PA_NA.illness = 'The disease will be cured gradually.'
PA_NA.evil_spirits = 'There are none bothering you. Since many people look up to you, you can be of benefit to them.'
PA_NA.practice = 'Your good intentions will increase, and your teaching of the Dharma will gather people like bees and benefit them. It would be good to make an image of a Dharma Protector, and also to rely upon peaceful deities such as White Vajra Varahi and Vajra Devi. If you recite the Lalita Vistara Sutra and the Bodhisattva Pitaka Sutra, it will bring happiness and good luck in the future.'
PA_NA.lost = 'It will be found. Even if it isn\'t found immediately, there is a good chance to find it in the future.'
PA_NA.will_they = 'It will be accomplished gradually.'
PA_NA.all_matters = 'Though the outlook is not so positive for the present time, gradually it will become good. \n This prediction that possesses beauty is known as "increasing happiness."'

PA_DHIH = DivItem()
PA_DHIH.title = 'The Nectar-like Medicine'
PA_DHIH.header = 'If PA DHI, the doorman of the north - appears, then it is through the door of nectar-like medicine that benefit will arise. This is also called "the gathering of the clouds of the essence of gold."'
PA_DHIH.sign = 'The sign of this divination is known as "arriving at the happy stream in the golden south."'
PA_DHIH.family = 'All these matters are good.'
PA_DHIH.aims = 'Whatever you wish for will be accomplished just as you envision. Furthermore, you will be nourished by the fulfillment of your plans. If you rely upon deities such as Pratisara, your wishes will be achieved.'
PA_DHIH.friends = 'Your gains and wealth will increase greatly.'
PA_DHIH.enemies = 'There are none against you.'
PA_DHIH.guests = 'They will have a comfortable journey and will arrive on time.'
PA_DHIH.illness = 'If you act according to the doctor\'s advice the disease will be cured.'
PA_DHIH.evil_spirits = 'There are none now, since the one that was bothering you has left.'
PA_DHIH.practice = 'Your character and behavior is pleasing, and so you will accomplish your practice in accordance with whatever you wish.'
PA_DHIH.lost = 'If you search in a southern or northern direction from where it was lost, you will definitely find it.'
PA_DHIH.will_they = 'They will come, and the task will be accomplished.'
PA_DHIH.all_matters = 'Just as the above answers have augured success, so likewise any other matter about which you may inquire will be successful. Assisting others to give up their bad intentions is good. If you practice peaceful activities through relying upon deities such as Akshobhya, White Sita Vajra Vidarana, and Amrita Kundali, then your good fortune and happiness will increase like the gems found in the ocean. Moreover, rely upon Guru Padmasambhava, deities of the Jewel family, wealth deities, and deities of the increasing class. Also, it will be beneficial to rely upon peaceful Dharma Protectors. Make praises and offerings to White Mahakala and hang blue prayer flags. If you place the Prajnaparamita Sutra in water, and the like, then your relatives will say beneficial and nice things to you, and you will be well received when you arrive at a place. \n This prediction is therefore known as "similar goodness."'


TSA_AH = DivItem()
TSA_AH.title = 'The White Umbrella of Good Fortune'
TSA_AH.header = 'If TSA AH - the great umbrella of good fortune - appears, then good fortune increases, just as the white umbrella flutters.'
TSA_AH.sign = 'The sign of this divination is known as "the flower garden that ripens on time."'
TSA_AH.family = 'These matters are in good condition.'
TSA_AH.aims = 'They will be fulfilled. Performing the meditation and recitation of Simha Mukha is beneficial. Especially, you will hear good news. However, your decisions will sometimes have no effect and others\' promises will not have any results, like the imprint of a bird\'s feet in the sky.'
TSA_AH.friends = 'If you make offerings to the wealth deities, good news will most probably come.'
TSA_AH.enemies = 'There are none, so you do not need to be apprehensive.'
TSA_AH.guests = 'They will have a comfortable journey and will arrive soon.'
TSA_AH.illness = 'You will recover quickly.'
TSA_AH.evil_spirits = 'You are bothered, not by evil spirits, but rather only by your mental imputations. There is no reason for your troubles other than the propensities of your own conceptualizations.'
TSA_AH.practice = 'This will be successful.'
TSA_AH.lost = 'There is an average chance of finding it.'
TSA_AH.will_they = 'There is an obstruction, so the undertaking will not occur whatsoever.'
TSA_AH.all_matters = 'The prediction is called "giving breath." Therefore, you should rely upon deities such as Dhvaja Devi, Tashi Lhamo, and Maha Mayuri. It is also good for you to hang prayer flags and construct prayer wheels. If you pray to protectors like Pehar it is good. This prediction is known as "whatever path one desires to travel upon, one will arrive safely."'

TSA_RA = DivItem()
TSA_RA.title = 'The Great, Fiery Weapon'
TSA_RA.header = 'If TSA RA - the great fiery weapon - appears, then one is successful, just as one receives a reward for bravery, having been victorious over all.'
TSA_RA.sign = 'The sign of this divination is known from the words of Yamantaka, the chief of the wrathful army who destroys the enemy, the destroyer of those with wrong understanding, who roared, "Defeat the enemy, subdue Mara."'
TSA_RA.family = 'Diligently and continually perform rituals to the protectors. Then things will be very good.'
TSA_RA.aims = 'Being victorious over every direction leads to success. Especially, there is great success for the Dharma activity of wrathfulness, such as subduing others, and the like. Just by the recitation of wrathful mantras, and so on, there will be success.'
TSA_RA.friends = 'Wealth, food, drink and the like will be obtained through force.'
TSA_RA.enemies = 'All enemies will be destroyed, and you will be victorious over others.'
TSA_RA.guests = 'They will come quickly and will be victorious over others.'
TSA_RA.illness = 'Illness will be cured.'
TSA_RA.evil_spirits = 'They don\'t have the chance to look at you, let alone to trouble you. You are so strong that you have the ability to keep the mind of others under your control, so you should produce compassion for them.'
TSA_RA.practice = 'Power and violent activities will produce clear results.'
TSA_RA.lost = 'It will be found.'
TSA_RA.will_they = 'It is certain to be accomplished.'
TSA_RA.all_matters = 'This prediction deals with the act of showing strength in all matters. Generally, the performance of works involving earth and water will encounter difficulty. Such activities as causing thunderbolts, hail, and the like will be accomplished. Rely upon the meditation deities with wrathful mantras, and Yamantaka. If you rely upon the meditations and practices involving fire and air, such as the path of inner heat and the melting of the Bodhichitta to produce bliss, then you will have an excellent ability to accomplish power and violent activities. You should rely upon Yamantaka, Hayagriva, Mahakala, and male deities of the Activity - family such as Amoghasiddhi. By relying upon Vajrakilaya, you will gain power. It is specially good to rely upon Maning, Mahakala, Leshin or Vajrapani.\n This prediction is known as "subduing all others by being endowed."'


TSA_PA = DivItem()
TSA_PA.title = 'Empty of Intelligence'
TSA_PA.header = 'If TSA PA - empty of intelligence - appears, then thoughts are empty, just as the wind moves through an empty valley.'
TSA_PA.sign = 'The sign of this divination is known from the town-dwelling evil spirits and ghosts, the messengers of Mara that wander in the northwest, who said, "It is very difficult to catch a white piece of paper carried away by the wind; who is capable of catching it?"'
TSA_PA.family = 'Though they meet with unfavorable conditions and there is great danger of their being separated, scattered and destroyed, still the performance of rituals will be of benefit.'
TSA_PA.aims = 'You are becoming too worried and mentally aggravated for such a small purpose.'
TSA_PA.friends = 'Even if wealth is held in your hand, it will seep through like water leaking from cupped hands.'
TSA_PA.enemies = 'Though the nature of this enemy was first friendly and then later hateful, still there wouldn\'t be any greater harm than to have a disputation with him. It is best to stay away from him and give some money that will benefit him.'
TSA_PA.guests = 'They will tum back empty-handed or will have difficulty in fulfilling their desired purpose.'
TSA_PA.illness = 'There will be a slight cold or air disease, and your body\'s elements are out of balance. The reason for the increase in your mental afflictions is due to the power of your relationship with bad friends and bad attendants. Separating from them will bring happiness. Your activities will most probably be polluted.'
TSA_PA.evil_spirits = 'Though there is no great harm from them, still you should perform a substitute ritual.'
TSA_PA.practice = 'As your mind is very agitated, it will be difficult to accomplish your wishes.'
TSA_PA.lost = 'It will be difficult to recover.'
TSA_PA.will_they = 'As this is the divination "empty of intelligence," it is difficult to accomplish.'
TSA_PA.all_matters = 'It is predicted that they won\'t be achieved as you wish. Most probably, people will not listen to your advice. Make your mind steady, accumulate merit, read the Vinaya, and recite collections of sutras. This prediction is known as "scattering the mind into pieces."'


TSA_TSA = DivItem()
TSA_TSA.title = 'The Streamer of Fame'
TSA_TSA.header = 'If TSA TSA - the streamer of fame - appears, then one\'s renown and fame will increase, just as the king of the gods resounds the drum when victorious in war. This is the divination of Garuda\'s son flying in the sky.'
TSA_TSA.sign = 'The sign of this divination is known from the words of Amrita Kundali who said, "This is the time for proclamations in every direction, just as one hoists a flag at the summit of a mountain."'
TSA_TSA.family = 'Generally speaking, the current situation of your family, property and life is positive, and your good fortune will increase. Nonetheless, when excessiveness surpasses excessiveness, you will need to catch in small pieces only (i.e., only small things will be accomplished).'
TSA_TSA.aims = 'There will be success in fulfilling your wishes. If you diligently perform rituals to the Dharma Protectors, then any activity you have begun will be accomplished.'
TSA_TSA.friends = 'Most probably you will obtain them quickly.'
TSA_TSA.enemies = 'Though there will be fighting, you will be victorious.'
TSA_TSA.guests = 'The journey will be comfortable and they will return quickly. Also, you will hear news of them.'
TSA_TSA.illness = 'Although the body is out of balance due to an air disease, there is no danger or cause for concern.'
TSA_TSA.evil_spirits = 'There are none that are bothering you.'
TSA_TSA.practice = 'There will be great success in fulfilling your aims. Also, you will obtain great renown.'
TSA_TSA.lost = 'You will most probably find it quickly by searching in a northeasterly direction from where it was lost.'
TSA_TSA.will_they = 'It is predicted that they will come.'
TSA_TSA.all_matters = 'They are successful and stable. However, you will face difficulties with activities involving earth and water. You should rely upon making offerings, reciting praises and performing rituals against curses. Rely upon the meditation practice of wrathful Niladanda, the goddess Tsanti, and also upon the Dharma Protectors such as Chittapati and Ngen Nerna, as well as activity deities. Such activities as traveling, flying in the sky, walking with fast feet, and so on, will meet with success. Success will also be experienced in any activity of expelling, such as expelling ghosts from a certain locale. It is good to make various types of offerings, such as tea, scarves, and the like. \n This prediction is known as " quick settlement and fame."'


TSA_NA = DivItem()
TSA_NA.title = 'The Mara Demon of Aggregates'
TSA_NA.header = 'If TSA NA, the Mara of the aggregates appears, then matters pertaining to family, property, life, friends, and wealth are not positive whatsoever, just as a tree is cut down in the middle.'
TSA_NA.sign = 'The sign of this divination is known from the words of the "slaughterer of breath" who resides at the outer eastern gate who said, "Cut plants with a sickle." \n You must recite mantras for a long time and perform torma throwing rituals.'
TSA_NA.family = 'The outlook is unfavorable.'
TSA_NA.aims = 'There is a great obstruction. The "air horse" (i.e., good luck) won\'t run on the path. Recite the prayer of Guru Padmasambhava, Removing Obstacles from the Path, and also the Sutra of Tara Which Dispels the Darkness in the Ten Directions.'
TSA_NA.friends = 'The outlook for both having beneficial friends and gathering wealth is not good.'
TSA_NA.enemies = 'Most probably you will encounter an enemy. Especially if you remain in the eastern or central part of your country, you will be suppressed. Perform a ritual for subduing enemies, such as that of Ta Mar or King Kang. Since you may be scolded and berated by your superiors, you should think ahead in order to prevent this from happening.'
TSA_NA.guests = 'There will be obstacles on the journey. It will be difficult for them to arrive on schedule, and they will have remorse for having undertaken the journey.'
TSA_NA.illness = 'There is a strong phlegm disease, and there will be difficulty in breathing. Rituals are needed to overcome this.'
TSA_NA.evil_spirits = 'You are being harmed by earth spirits and local spirits. Also, you are experiencing trouble caused by a yellow article, and a square house, square room, or any square object. You may also be harmed by a "king evil spirit" who is following an article given to you from the house or from the hand of a Buddhist or Bon priest. The cause of this is your desire to compete with the people who originally inhabited that place or with great non-humans, or your harming of images, and the like. There is also a great danger of being afflicted by impurities and pollutions, so the washing ritual should be performed.'
TSA_NA.practice = 'Though you think about the Dharma path, you are diverted to wrong directions. In order to overcome this, you should clean roads, build paths nicely, and rely upon obstacle-clearing deities such as Tara.'
TSA_NA.lost = 'As the meat has already entered the mouth of the lion, it is difficult to recover.'
TSA_NA.will_they = 'Although there is much commotion, it won\'t be accomplished.'
TSA_NA.all_matters = 'They are not favorable. However, acts of instigation or deception will meet with success. \n This prediction is known as "being pressed down by a large hill."'


TSA_DHIH = DivItem()
TSA_DHIH.title = 'The House of Good Tidings'
TSA_DHIH.header = 'If TSA DHI - the gatekeeper of the east appears, then good works are accomplished, just as the house of good tidings is seen. Also, this is called the wish-fulfilling tree.'
TSA_DHIH.sign = 'The sign of this divination is known as to adorn yourwork with the streamers of transcendental activity."'
TSA_DHIH.family = 'All of these matters will have good and sudden results. The work of informing others is especially good.'
TSA_DHIH.aims = 'These will be successful, with quick results. Relations with others are good.'
TSA_DHIH.friends = 'There will be success with immediate results. Relaying news is especially good.'
TSA_DHIH.enemies = 'There are none, and you will experience a pleasant time.'
TSA_DHIH.guests = 'They will have a comfortable journey, meet with good friends and will arrive soon.'
TSA_DHIH.illness = 'Your disease will be cured.'
TSA_DHIH.evil_spirits = 'There are none that are bothering you.'
TSA_DHIH.practice = 'Good intentions are involved and so your spiritual activities will increase.'
TSA_DHIH.lost = 'It will be found in an eastern or northern direction from where it was lost.'
TSA_DHIH.will_they = 'It will be successfully completed, and you will be able to settle matters.'
TSA_DHIH.all_matters = 'In accordance with your desires, you will find success. Rely upon Activity family deities such as Mahabala, Parna Shavari, Ushnisha Vijaya, and Tara. Make offerings to the four-armed Mahakala and other Dharma Protectors. It is also good to rely upon Ma Gyal and Yaksha family deities. Recite sutras from the Ratna Kuta Collection. It is good to study and teach the Dharma. There will be benefit in having conch shells blown and making adornments of streamers. \n This prediction is known as "dissemination of joyful news and arrival at the summit of the mountain."'


NA_AH = DivItem()
NA_AH.title = 'The Golden Mountain'
NA_AH.header = 'If NA AH - the golden mountain - appears, then firmness and stability are seen, just as the golden mountain reaching high is seen.'
NA_AH.sign = 'The sign of this divination is known as "the unchanging auspicious symbol."'
NA_AH.family = 'These matters are firm and steady.'
NA_AH.aims = 'These are excellent and will bring stability to your life in the future.'
NA_AH.friends = 'The possessions and friends obtained earlier are stable, and they will remain due to the power of steadiness.'
NA_AH.enemies = 'There are none whatsoever, and your power is steady.'
NA_AH.guests = 'Though they are neither lost nor harmed, they will take a little time to arrive.'
NA_AH.illness = 'There is none.'
NA_AH.evil_spirits = 'There are none whatsoever bothering you.'
NA_AH.practice = 'It is firm and good through strength and steadiness.'
NA_AH.lost = 'It has not gone into another\'s hands.'
NA_AH.will_they = 'Though there may be a delay of your present project in favor of another, that project which has already been started will meet with a successful outcome.'
NA_AH.all_matters = 'Generally, all of these are successful. However, any activity involving traveling to another place will encounter some delay. Read the Avatamsaka Sutra and Vinaya Sutras. Rely upon deities of the Vajra-family and mother deities of the Destroyer-family. Hold Kshitigarbha as your special deity. Your good fortune will increase if you rely upon the mantras of Lochani, Vaishravana and Jambhala. Erect images and stupas and perform activities, which are steady. \n Since this prediction is known as "holding one\'s own place and not moving," it represents the excellence of all activities performed on a stable foundation.'

NA_RA = DivItem()
NA_RA.title = 'The Demon of the Heavenly Son'
NA_RA.header = 'If NA RA - the Mara demon of the heavenly son appears - then this fall of the dice augurs ill, just as a fire burns a good house.'
NA_RA.sign = 'The sign of this divination is known from the words of the deceiver, the great leader of wrong views, who dwells at the outer gate in the west, who said, "If the fire of desire blazes, oneself is burnt."'
NA_RA.family = 'There is instability and great obstruction.'
NA_RA.aims = 'The result of completion is empty.'
NA_RA.friends = 'They are similar to the ashes of burnt silk and silken brocades.'
NA_RA.enemies = 'There are enemies, and harm will especially arise from the southwest.'
NA_RA.guests = 'There is a great danger for both man and property.'
NA_RA.illness = 'You are suffering from a disease such as a hot disease, blood disease, or contagious disease, and it is bad.'
NA_RA.evil_spirits = 'A red article, a triangular article, or flesh and blood from the west is causing you harm. There is danger of being harmed by spirits if you burn things in the kitchen or displease them in other ways.'
NA_RA.practice = 'To avert a great obstacle, perform peaceful fire rituals and washing rituals many times. Make medicines and recite various prayers and mantras of Guru Padmasambhava many times.'
NA_RA.lost = 'It will not be found.'
NA_RA.will_they = 'There is a danger of not accomplishing the task, since there is a great obstacle.'
NA_RA.all_matters = 'They are not successful. However, the prospects are excellent for non-virtuous activities such as setting fire to a city. It is good to do "cutting rituals," and the like. \n This prediction is known as "the aggregates of the person being harmed by suffering."'


NA_PA = DivItem()
NA_PA.title = 'The Overflowing Jewelled Vessel'
NA_PA.header = 'If NA PA the golden vessel filled with grains - appears, then prosperity increases, just as the jewelled vessel is filled with food. This is also called the wish-fulfilling cow.'
NA_PA.sign = 'The sign of this divination is known from the words of White Manjushri, whose body causes deterioration to be allayed, who said, "The concurrence of the golden vase and the ingredient of nectar is very beautiful."'
NA_PA.family = 'They are in positive states and are endowed with happiness.'
NA_PA.aims = 'The happiness of mind increases.'
NA_PA.friends = 'Food, wealth and friends, in particular, return and increase.'
NA_PA.enemies = 'There are no thieves and enemies.'
NA_PA.guests = 'Their purpose will be successful. Though a little late, they will arrive happily.'
NA_PA.illness = 'It will be cured and you will gain happiness.'
NA_PA.evil_spirits = 'There are none that are bothering you. Though it appears like an attack from an evil spirit, it is actually a favorable condition.'
NA_PA.practice = 'It is good and will meet with success.'
NA_PA.lost = 'Either it will be found in the eastern part or central area of your locale, or it will be found in a southern direction from where it was lost.'
NA_PA.will_they = 'If they have not yet come to your place or not yet begun the work, there will be some regret but the endeavor will be accomplished in the future just as they had wished.'
NA_PA.all_matters = 'You should remain happy and contented . Receive empowerments and initiations, and rely upon wealth deities and deities of the jewel-family. If you practice the yoga technique of extracting the essence of food and the process of creation, you will meet with success. Perform consecrated food offerings and rituals to the Dharma. Protectors, and make offerings to the nagas. Recite the Vairochana Tantra. Also, relying upon Ganapati is good. \n This prediction is known as "the good field which increases happiness."'


NA_TSA = DivItem()
NA_TSA.title = 'The Scattered Mountain of Sand'
NA_TSA.header = 'If NA TSA - the mountain of sand - appears, then the results of your aims are spoiled and thrown about, just as dust is scattered by the wind.'
NA_TSA.sign = 'The sign of this divination is known from the speech of the mind-stealing spirits, the messengers of the demon Mara who dwell in the northeast, who said, "The golden house is gradually levelled into dust."'
NA_TSA.family = 'They will be diminished more and more.'
NA_TSA.aims = 'There will b e great changes, and finally you will experience deterioration.'
NA_TSA.friends = 'Nothing new will arise, and your previously accumulated possessions will greatly diminish.'
NA_TSA.enemies = 'Since your prosperity will suddenly be harmed by enemies, you must perform suppressing rituals.'
NA_TSA.guests = 'You will be happy to see them, but the news they bring will cause repentance and sorrow.'
NA_TSA.illness = 'It doesn\'t appear to be an illness that causes great harm; this slight illness can be cured through religious rituals.'
NA_TSA.evil_spirits = 'Though there is not a great evil spirit, still your mental perceptions have been agitated and disturbed. You should perform a peaceful fire ritual. The cause of this disturbance is that you have accumulated propensities for faulty activities and decisions. A burying ritual should be performed. Request members of the Sangha to recite verses of auspiciousness.'
NA_TSA.practice = 'Since the future is not good, it will be difficult to achieve your goals.'
NA_TSA.lost = 'It will be more difficult to find it as time passes.'
NA_TSA.will_they = 'It will be difficult to accomplish. Even if it is accomplished, there will be no benefit derived from it.'
NA_TSA.all_matters = 'There will be no meaningful result of your activities. However, works involving destruction will be successful. As this prediction is unfavorable, you should recite the Ratna Kuta Sutra, the Mangala Sutra, and prayers to Guru Padmasambhava many times, and build a golden bridge. It is also beneficial to perform a burying ritual and have scriptures written with gold lettering. \n This prediction is known as "dwindling the mountain into dust."'


NA_NA = DivItem()
NA_NA.title = 'The Mansion of Gold'
NA_NA.header = 'If NA NA - the mansion of gold - appears, then all things are good, vast, and s table, just as a celestial mansion is endowed with vast wealth.'
NA_NA.sign = 'The sign of this divination is known as "where the jewelled mountain is set upon a ground of gold there is great astonishment. "'
NA_NA.family = 'Since the present conditions are like an inexhaustible treasure, these matters are seen to be excellent through great steadfastness.'
NA_NA.aims = 'Just as the earth and mountains are very firm, so these are good. However, there is a chance of delay. If you propitiate wealth deities and earth deities, your aims will be achieved.'
NA_NA.friends = 'These resources will be very vast in the future.'
NA_NA.enemies = 'They do not exist for you.'
NA_NA.guests = 'Their arrival will be delayed, but since they arrive safely, their trip is well accomplished.'
NA_NA.illness = 'Though you will suffer for a long time from a serious illness, no lasting harm will arise from it. Furthermore, it is difficult for another illness to arise.'
NA_NA.evil_spirits = 'There is no cause for any evil spirit to harm you.'
NA_NA.practice = 'You will be steadfast in keeping vows and the like, and your wishes will be fulfilled.'
NA_NA.lost = 'It has not moved from the place where it was lost. If, by chance, it has been moved, then it will be difficult to recover.'
NA_NA.will_they = 'Unless the matter is settled quickly, there is a chance of delay.'
NA_NA.all_matters = 'If they are not delayed, they will tum out well. It will be difficult to accomplish unsteady activities such as giving up your job, moving, going to new places, making requests to officials, and the like. Also, activities involving destruction are not favorable. Activities involving wealth rituals, binding, hastily done works, and so on, are excellent. Erect shrines for wealth deities, such as Vasudharani, and also erect stupas. Bury a wealth vase in your house. To practice increasing activities is very good. Recite the mantras of Buddha Lochani and Kshitigarbha. Rituals performed for Ber Nag Chen Mahakala are also beneficial. This prediction is known as "the placing of some great thing upon another great thing."'


NA_DHIH = DivItem()
NA_DHIH.title = 'The Treasury of Jewels'
NA_DHIH.header = 'If NA DHI the gatekeeper of the west appears, then there is perfect prosperity, similar to the opening of a treasury of jewels.'
NA_DHIH.sign = 'The sign of this divination is known as " opening the door of the treasury of jewels in the east." It is also known as "obtaining butter from milk and gems from the ocean."'
NA_DHIH.family = 'As there will be no changes, prospects are good.'
NA_DHIH.aims = 'They are excellent and firm, and so the outlook for the future is positive.'
NA_DHIH.friends = 'Whatever you wish will b e fulfilled.'
NA_DHIH.enemies = 'None will arise.'
NA_DHIH.guests = 'They will have a successful and comfortable journey.'
NA_DHIH.illness = 'It will gradually clear up.'
NA_DHIH.evil_spirits = 'There are none whatsoever bothering you.'
NA_DHIH.practice = 'It is very good. It is recommended that you rely upon deities of the Vajra-family and the three masters of the Tathagata-family. Also, rely upon Mahakala.'
NA_DHIH.lost = 'It must be near to the place where it was originally lost.'
NA_DHIH.will_they = 'In the long run, it will be accomplished.'
NA_DHIH.all_matters = 'They are successful. It is especially advisable to seek the blessings of the Jewel-family. If you rely upon nagas and other spirits, there will be success. Make offerings to earth deities and local deities so that good luck will arise. \n This prediction is known as "a building of many stories."'

DHIH_AH = DivItem()
DHIH_AH.title = 'Manjushri Appears'
DHIH_AH.header = 'If DHI AH - the brave Manjushri - appears, then whatever is wished for will be fulfilled, like a gem falling into one\'s hand.'
DHIH_AH.sign = 'The sign of this divination is known from the speech of the Transcendental Being of Mind\'s Great Bliss who said, "The agility of the great primordial wisdom of pure awareness increases without regard to directions."'
DHIH_AH.family = 'Since they are firm and without obstructions, conditions are good'
DHIH_AH.aims = 'Have no doubts concerning the situation, since an authority that i s not involved with deception is present here. It is advisable to listen to, study and contemplate the general Buddhist teachings, especially those of the mantra teachings.'
DHIH_AH.friends = 'They will continue to increase.'
DHIH_AH.enemies = 'All enemies will come to you with respect.'
DHIH_AH.guests = 'Their journey will be comfortable and successful.'
DHIH_AH.illness = 'It will be cured naturally.'
DHIH_AH.evil_spirits = 'There are none whatsoever that are disturbing you now, nor will any arise. The situation is good, and there is no cause whatsoever to be harmed, so do not worry.'
DHIH_AH.practice = 'It is good, and the happiness of your mind will increase. Whatever you wish will be fulfilled.'
DHIH_AH.lost = 'It will be found.'
DHIH_AH.will_they = 'They will come and it will be accomplished.'
DHIH_AH.all_matters = 'All your goals will be fulfilled. Rely upon meditation deities such as Manjushri, Padmasambhava, Kalachakra, and the like. Meditate upon the path of the Illusory Body and the Six Applications of the Great Completion. Also rely upon Thang Lha and Mahakala as your Dharma Protectors. If you erect the three supports of images, scriptures and stupas, then most probably you will encounter prosperity. \n This prediction is known as the "principal owner of the thirty-six cities" or "increasing transcendental wisdom and accomplishing excellence."'


DHIH_RA = DivItem()
DHIH_RA.title = 'The Endless Auspicious Knot'
DHIH_RA.header = 'If DHI RA - the auspicious knot - appears,then a mind-pleasing scene will be witnessed, just as when one arrives at a flower garden.'
DHIH_RA.sign = 'The sign of this divination is known as "O intelligent one, look at that wonderful scene with your eyes."'
DHIH_RA.family = 'The outlook is not merely good, but is excellent.'
DHIH_RA.aims = 'Your intentions are appropriate and will meet with success. In relation to people, your dwelling and events happening at your present residence, good fortune will occur. Whatever your decisions may be, only harmony will arise. For this reason, plans and aims will meet with success and happiness and be well accomplished.'
DHIH_RA.friends = 'You will gain both, along with joy.'
DHIH_RA.enemies = 'There are none.'
DHIH_RA.guests = 'Their journey is comfortable and they will arrive soon.'
DHIH_RA.illness = 'It will be cured soon.'
DHIH_RA.evil_spirits = 'There do not appear to be any bothering you. There is no cause for any to trouble you, so your mind should be at ease and happy.'
DHIH_RA.practice = 'Your wishes will be fulfilled and advancements will begin to appear.'
DHIH_RA.lost = 'It will be found quickly.'
DHIH_RA.will_they = 'It will be accomplished and they will come.'
DHIH_RA.all_matters = 'It is best for you to do what you think is right. Rely upon auspicious deities such as Nivarana Vikshambhi, Ushnisha Vijaya, Sita Tapatra, and the like. If you rely upon Chakrasamvara, Vajrasattva and Mahajala it is especially good, and you will fulfill your wishes. Reciting the prayer of Spontaneously Fulfilling Wishes of Guru Padmasambhava is certain to bring success. Simply practicing the meditation deities which you previously relied upon, and propitiating the Dharma Protectors that you cherished in your heart, will bring good fortune. \n This prediction is known as "friendly desire."'


DHIH_PA = DivItem()
DHIH_PA.title = 'The Golden Female Fish'
DHIH_PA.header = 'If DHI PA - the golden female fish - appears, then physical agility and good luck will increase, like the swift movements of a female fish in the ocean.'
DHIH_PA.sign = 'The sign of this divination is known as "because one bathes in nectar, one\'s happiness increases."'
DHIH_PA.family = 'Their prospects are good.'
DHIH_PA.aims = 'These are favorable and successful.'
DHIH_PA.friends = 'They will arise in great number.'
DHIH_PA.enemies = 'They have no chance to harm you.'
DHIH_PA.guests = 'Their journey will be comfortable and they will arrive quickly.'
DHIH_PA.illness = 'It will be cured.'
DHIH_PA.evil_spirits = 'There are none to bother you.'
DHIH_PA.practice = 'It is good and progress will be made.'
DHIH_PA.lost = 'It will be recovered.'
DHIH_PA.will_they = 'They will come to fruition in time.'
DHIH_PA.all_matters = 'They will be smooth, good, and will succeed. Studying medicine is positive. Recite the Ratna Kuta Sutra, the Smirityupasthana Sutra, and other short sutras. If you do peaceful and increasing fire rituals, you will meet with good results. Also, holding Maitreya as your special deity is good. \n This prediction is known as "to endeavor in accordance with one\'s intentions, wishes and aims."'


DHIH_TSA = DivItem()
DHIH_TSA.title = 'The White Conch'
DHIH_TSA.header = 'If DHI TSA the white conch of Dharma appears, then fame and fortune increase, like the pleasant sound of the conch.'
DHIH_TSA.sign = 'The sign of this divination is known as "one\'s thoughts become renowned like a pleasing tune."'
DHIH_TSA.family = 'The outlook is positive, and you will hear good news.'
DHIH_TSA.aims = 'These will be successful, and you will hear good tidings. If you teach languages, debate, logic and the like, it is good.'
DHIH_TSA.friends = 'You will hear some very clear news.'
DHIH_TSA.enemies = 'There are none.'
DHIH_TSA.guests = 'They will arrive with good news.'
DHIH_TSA.illness = 'Though there is no danger or harm to the ill person\'s life, agitation and disturbance of the mind will occur.'
DHIH_TSA.evil_spirits = 'There are none to bother you.'
DHIH_TSA.practice = 'Fame will come to you.'
DHIH_TSA.lost = 'There will be clear news about it.'
DHIH_TSA.will_they = 'They will come, and it will be accomplished.'
DHIH_TSA.all_matters = 'They will succeed, so do as you wish. You should hold Arya Samantabhadra as your special deity. Recite the Dhvajagra Sutra and various dharanis. Rely upon Chaturmukha and Yaksha-family deities for Dharma Protectors. As others will agree with you, you will accomplish your desires. \n This prediction is known as "increasing good news and fame."'


DHIH_NA = DivItem()
DHIH_NA.title = 'The Golden Wheel'
DHIH_NA.header = 'If DHI NA - the golden wheel - appears, then there is prosperity and well-being, like the obtaining ofa kingdom by a prince. There is prosperity and well-being.'
DHIH_NA.sign = 'The sign of this divination is known as "the amazement of obtaining a treasure without effort."'
DHIH_NA.family = 'They are stable and good.'
DHIH_NA.aims = 'Because they are steady in the long run, the prospects are good. Especially, you will be foremost in worldly customs and manners.'
DHIH_NA.friends = 'They will increase.'
DHIH_NA.enemies = 'They will come under your control.'
DHIH_NA.guests = 'They will be victorious and happy.'
DHIH_NA.illness = 'Though there is definitely no danger to the sick person, since some god is displeased with this person, he or she will take a little while to recover.'
DHIH_NA.evil_spirits = 'There are none bothering you.'
DHIH_NA.practice = 'There will be good luck and it will succeed.'
DHIH_NA.lost = 'There is a possibility of finding it at another time.'
DHIH_NA.will_they = 'There will be some delay, but the future is good.'
DHIH_NA.all_matters = 'In the long run there will be success. Rely upon meditation deities such as Yamantaka, the unsurpassable Heruka, Vairochana, and the like. Also, rely upon Ushnisha Chakravartin as your special deity. Recite the Mara Vijaya Dharani. Also, it is advisable to rely upon Panj ara Mahakala and Chaturmukha as your Dharma Protectors. \n This prediction is known as "climbing upon a throne."'


DHIH_DHIH = DivItem()
DHIH_DHIH.title = 'The Jewelled Banner of Victory'
DHIH_DHIH.header = 'If DHI DHI - the hoisted banner of victory - appears, then you are victorious and excel, like the raising of the banner of victors over every direction. You are able to accomplish whatever activity you wish to do.'
DHIH_DHIH.sign = 'The sign of this divination is known as, "If one relies upon the powerful wish-fulfilling king, then greater and greater results are obtained. This is truly amazing."'
DHIH_DHIH.family = 'Since your family and property do not diminish, it is good. As your life force is very stable, it is hard like a diamond, so there is no present worry about sickness or death.'
DHIH_DHIH.aims = 'These will be very well fulfilled. It is good to make nectar pills and perform the meditation practice of deities who hold swords and other similar objects.'
DHIH_DHIH.friends = 'They will be gathered. Your desires are fulfilled by the wish-fulfilling jewel so that your aims and wishes are accomplished in a way exceeding your expectations.'
DHIH_DHIH.enemies = 'There are none.'
DHIH_DHIH.guests = 'They will have a comfortable journey and will arrive safely.'
DHIH_DHIH.illness = 'It will be cured naturally.'
DHIH_DHIH.evil_spirits = 'There is neither an evil spirit troubling you nor a cause for one to trouble you.'
DHIH_DHIH.practice = 'It is clear and bright like the moon outshining the stars. If you diligently meditate upon your special deity, you will gain great attainments. If you study logic, you will be particularly successful.'
DHIH_DHIH.lost = 'If you do as a close friend advises you, then it will be found.'
DHIH_DHIH.will_they = 'All your tasks will work out smoothly, and there will be success.'
DHIH_DHIH.all_matters = 'All these matters will meet with success, so you should do as you wish to do. Through accumulatiIlg more virtues and relying upon meditation derties such as Vajrakilaya, Hevajra, Guhyasamaja, Vajrapani, and the like, you will meet with much good luck and good fortune. If you make offerings to the six-armed Mahakala it is good. You should recite the texts of the Great Completion and the Manjushri Nama Samgiti. Also, rely upon the Dharma Protector King Gesar as Werma. \n This prediction is known as "hoisting the jewelled banner of victory."'
