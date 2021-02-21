import string
import time
import sys

### Defining a slow-typing Printing
def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

### Defining the Class of Tarot Cards
class TarotCard:
    def __init__(self, title, roll, event, outcome, person):
        #attributes
        self.title = title
        self.roll = roll
        self.event = event
        self.outcome = outcome
        self.person = person

### Defining a function to iterate through all 100 tarot cards and instantiate them all as members of the TarotCard class
def TarotIter(cards):
    cards = cards.split('\n')
    possiblecards = []
    for line in cards:
        card = line.split(',')
        possiblecards.append(TarotCard(card[0],card[1], card[2], card[3], card[4]))
    return possiblecards

###Defining Possible Cards, taken from Reddit User u/Bellociraptor's NPC Card Reader
tarotcards = """The Crimson King,1,unconvering dangerous secrets,knowledge at great cost, a powerful and dangerous man
The Scarlett Queen,2,dangerous bargains,victory only at great cost,a powerful and dangerous woman
The Cardinal Knight,3,violence or war,end reached through bloody conflict,andry or violent young man
The Azure King,4,a time of learning,knowledge will prove invaluable,a sage or scholar
The Cobalt Queen,5,something forgotten will return,forgetting a wrong or slight will cause it to happen again,someone you never thought you'd see again
The Cyan Knight,6,facing the consequences of ignorance,what you don't know will hurt you,an unexpected enemy
The Viridian King,7,consequences,someone you wronged will have their revenge,someone with a personal grudge
The Emerald Queen,8,conspiracies,a plot against you will play out,a jealous woman
The Jade Knight,9,rivalries,if you don't take them seriously enough, a rival will best you,a rivalries
The Obsidian King,10,a warned event will come to pass,success or failure will depend onhow warnings were heeded, a male practitioner of dark magic
The Onyx Queen,11,a change of forture,a reversal (either good or bad),a woman whose first impression matters
The Black Knight,12,a grudge,you will make an enduring enemy,a soldier from a defeated army
The Bone King,13,news of a death,final endings,a dying man
The Frost Queen,14,loss of someone powerful’s favor,fall from grace,a widow
The Pale Knight,15,return of a trouble thought over,recurring trouble,someone thought to be dead
The Herald of Sorrows,16,bad news,things will end poorly for someone close,a tragic youth
The King’s Assassin,17,a betrayal by someone powerful,make a powerful enemy,a traitor in a position of advantage
The Queen’s Thief,18,underhanded dealings,loss of something valuable,a charming rogue
The Conqueror,19,a shift in personal power,dramatic gain or loss of power,an ambitious man
The High Priest,20,a test of faith (Religious or otherwise),success or loss depends on the aid of others,someone of a devout or religious order
The Witch,21,a string of bad luck,something will have to be set right before luck can turn,a female practitioner of dark magic
The Gypsy,22,scams and false flattery,trust the wrong people and they will take you for a ride,someone young and charming
The Jester,23,loss or respect or jokes at your expense,you will be made a laughingstock,someone whose reputation has suffered
The Virgin,24,unfamiliar circumstances,you will be forced to navigate a challenge unprepared,an innocent
The Whore,25,a financial loss,may fall prey to excessive spending,an ambitious woman
The Alchemist,26,physical or Spiritual transition,irreversible personal change,a practitioner of strange sciences
The Physician,27,aid from another,slow healing of physical mental or spiritual wounds,someone you already put faith in (e.g. parent or teacher etc.)
The Occultist,28,painful Knowledge,something wicked comes,someone who should not be here
The Hunter,29,gains through long pursuit,the chase will yield it’s prizes,someone on a quest or mission
The Bleeding Man,30,pain,no matter the outcome the path will be suffering,a victim or persecution or torture
The Scarred Man,31,changed by suffering,painful events will have lasting ramifications,someone who carries the physical or mental marks of a great wrong
The Judge,32,decisions,positive outcomes only achieved if choices are made with reason instead of passion,older man in a position of authority
The Jury,33,judgement,outcome determined by others,a group of strangers
The Headsman,34,the Rule of Law,law upheld,a lawman
The Traveler,35,a journey,a change of locations,someone from far away
The Twins,36,a powerful bond,live or die for someone,someone with a powerful spiritual bond to the drawer or two people bonded to each other (e.g. identical twins or soul mates etc.)
Sacrifice,37,a willing loss,results for others worth personal cost,a man willingly suffering
Birth,38,pain that will change everything,someone or something will come into your life that will drastically alter it,a pregnant woman
Death,39,complete transition,irreversible change,someone in mourning
The Wedding,40,unification and bonds,formation of loves friendships or strong alliances,a new and close friend or ally
The Funeral,41,an ending or conclusion,bittersweet parting,someone who has come to you because of a mutual loss
The Tournament,42,an exciting challenge,a shot at glory,a friendly rival
Feast,43,joy and festicity,impressive but temporary gains,a wealthy and generous man
Famine,44,times of need,crushing but temporary losses,a miser
Reincarnation,45,new beginnings,the start of a new life,someone who has undergone a recent transition
The Ravens,46,aftermath of tragedy,profiting from loss,opportunist or profiteer
The White Wolf,47,spiritual awakening,a personal epiphany,a spiritualist
The Black Dog,48,misfortune,no way to get out unscathed,someone cursed
The Red Stallion,49,an adventure,a new and exciting experience,a bold adventurer
The Silver Stag,50,a chase or pursuit,chance at an elusive prize,an enigmatic stranger
The Bull,51,rapid progress,ends achieved through brute force and determination,a laborer or someone of similar origins
The Goat,52,overcoming obstacles,resilience and tenacity will win the day,someone from harsh circumstances
The Cat,53,you will overhear something,solutions will come through subtlety and discretion,someone frequently disregarded or underestimated
The Rat,54,subterfuge and underhanded dealings,the most clever will win,a spy or thief
The Two-Headed Serpent,55,flattery and false promises,grave consequences if you trust the wrong person,a charming liar
The Spider,56,beware of traps and snares,failure unless you spot all the complications,someone of few words and complex machinations
The Mermaid,57,seduction and risky affairs,heartbreak and tragic endings,a heartsick woman
The Manticore,58,close alliances and co-conspirators,your misdeeds will bind you to your partners in crime,a gang or party
The Viper,59,meddling in places you don't belong,there week be a cost for getting involved in matters that are not your place,a dangerous loner
The Leviathan,60,a natural or unavoidable disaster,outcome determined by circumstances beyond your control,someone linked to the Void
The Scorpion,61,someone will try and ruin you,you will be struck at at every turn,someone with a petty grudge
The Wasps,62,mass hysteria and mob rule,outcome will be decided by the crowd,a group or mob
The Bear,63,guarding that which you love,someone or something you care about will rely on you to aid them,protective older person
The Sword,64,strength,your strength will determine the outcome,a knight or military officer
The Spear,65,protection,your ability to protect someone or something will determine the outcom,a guard or soldier
The Axe,66,you will be the agent of justice,your judgement or actions will determine if justice is served,a vigilante
The Hammer,67,force,outcome will be determined by martial prowess,a ruffian or barbarian
The Knife,68,guile,outcome will be determined by cunning,a courtier or diplomat
The Rose,69,winning fame or favor,your success will earn you reputation and acclaim,a young and beautiful woman
The Broken Tower,70,calamity,failure of endeavors,someone who has suffered a recent failure.
The Bridge,71,joining together of two unlikely things,unexpected alliances,a foe turned friend
The Gallows Tree,72,punishment,making amends for your actions or words,a criminal
The Poisoned Cup,73,gift, reward or treasure will bring misfortune,even an apparent success will reap sorrow,someone who will try to ply you with false generosity
The Chalice,74,joy and reward,your endeavors will yield success and great gains,someone famous
The Sea,75,journey over water,cross a great physical distance,a fickle woman
The Lightning Struck Ship,76,a difficult journey,a life-or-death struggle,a sudden adversary
The Desert,77,loneliness and isolation,a struggle that must be faced alone,a wanderer or hermit
The Mountain,78,best of physical or mental endurance,toughness will win the day,an unusually large person
The Forest,79,confounding factors and unclear paths,a confusing journey during which it is easy to lose sight of the purpose,a woodsman or ranger
The Path,80,clarity of purpose,intent and purpose will be clear or obvious,a tracker or guide
The Stairway,81,opportunities,great things if you proceed carefully but a terrible slip and fall if you do not,an architect or builder
The Rising Sun,82,new beginnings and limitless potential,your actions in the immediate future will have long-lasting benefits or consequences,a young child
The Sun at Zenith,83,hard work will yield great benefits,you will sow and reap in equal measure,someone respected and established in their trade
The Setting Sun,84,rest and peaceful conclusions,the ending of a job or similar,a retired person
The New Moon,85,the unknown,unexpected event will change everything,a blind man
The Crescent Moon,86,half-truths and incomplete predictions,unsatisfactory conclusions and unfinished business,a restless youth
The Full Moon,87,true predictions,an unfolding of prophecy or fortunes,a seer
Wind,88,constant changes and reversals,no results (good or bad) will endure for long,a moody or unstable person
Snow,89,confusion and obfuscation,you will remain in ignorance or confusion,a mute
The Star,90,a quest or journey,the start of a new mission,a mentor or guide
The Demon,91,punishment,all sins punished,a torturer
The Devil,92,bargains and deals,an arrangement twisted against you,a drafter of contracts
The Fey,93,mysteries,inconclusive or strange endings,a mysterious or unknown person
The Dragon,94,a life-changing challenge,death or glory,a powerful adversary
Dreams,95,unlikely adventures or encounters with the uncanny,the ending will be a far cry from where you began,someone fae-touched
Nightmares,96,things long-feared will come to pass,things will appear far worse before they get better,a madman
Time,97,facing the inevitable,change that you are powerless to fight,someone important from your past
The Treasure Hoard,98,the prize at the end of the challenge,great reward after great challenge or suffering,someone you will have to fight for
DM’s Choice,99,whatever you want, whatever you want, whatever you want
Something that should not be,100,make up a card that isn’t in the deck,make up a card that isn't in the deck,make up a card that isn't in the deck"""

def TarotPull():
    ### Define Possible Cards for use in this function
    possiblecards = TarotIter(tarotcards)

    ###Printing the introduction and instructions
    print("Welcome to BranPap's DnD Tarot Reader, using the NPC Card Reader cards from Reddit user u/Bellociraptor.")
    print('')
    print('This iteration of the Tarot Reader will take you throught three readings:')
    print('1. The external and internal self of the character. (2 rolls)')
    print('2. The past/present and future of the character. (2 rolls)')
    print('3. Guidance on a specific question. (2 rolls)')
    print('')
    print("To use it, roll a D100 and input the roll number each time you see the prompt 'enter the roll'. If the player rolls the same number twice, have them reroll, but make note of the number; that card will have a stronger influence than ususal. ")
    print('')

    time.sleep(2)


    ### Beginning the first set of rolls
    slowprint("Let's begin with the external and internal self of the character:\n")
    print('')

    ###Input commands for the player's rolls
    num1 = int(input('Please enter the first roll: '))
    print('')
    num2 = int(input('Now please enter the second roll: '))


    ###Defining empty lists to append pulls into
    events = []
    outcomes = []
    persons = []
    names = []

    ###For loops:
    for card in possiblecards:
        if int(card.roll) == num1:
            events.append(str(card.event))
            names.append(str(card.title))
            outcomes.append(str(card.outcome))
            persons.append(str(card.person))

    for card in possiblecards:
        if int(card.roll) == num2:
            events.append(str(card.event))
            names.append(str(card.title))
            outcomes.append(str(card.outcome))
            persons.append(str(card.person))

    ##Printing the results
    print('')
    slowprint('You have pulled two cards\n')
    print('')
    slowprint(f'The first card is {names[0]}, representing the external self:\n')
    slowprint(f'Event: {events[0]}\n')
    slowprint(f'Outcomes: {outcomes[0]}\n')
    slowprint(f'Person: {persons[0]}\n')
    print('')
    slowprint(f'The second card is {names[1]}, representing the internal struggle:\n')
    slowprint(f'Event: {events[1]}\n')
    slowprint(f'Outcomes: {outcomes[1]}\n')
    slowprint(f'Person: {persons[1]}\n')
    print('')


    time.sleep(2)

    ###Beginning the second set of rolls
    slowprint("Now we pull for the past/present and future of the character:\n")
    print('')

    ###Input commands for the player's rolls
    num1 = int(input('Please enter the first roll: '))
    print('')
    num2 = int(input('Now please enter the second roll: '))


    ###Defining empty lists to append pulls into
    events = []
    outcomes = []
    persons = []
    names = []

    ###For loops:
    for card in possiblecards:
        if int(card.roll) == num1:
            events.append(str(card.event))
            names.append(str(card.title))
            outcomes.append(str(card.outcome))
            persons.append(str(card.person))

    for card in possiblecards:
        if int(card.roll) == num2:
            events.append(str(card.event))
            names.append(str(card.title))
            outcomes.append(str(card.outcome))
            persons.append(str(card.person))

    ##Printing the results
    print('')
    slowprint('You have pulled two cards\n')
    print('')
    slowprint(f'The first card is {names[0]}, representing the past/present:\n')
    slowprint(f'Event: {events[0]}\n')
    slowprint(f'Outcomes: {outcomes[0]}\n')
    slowprint(f'Person: {persons[0]}\n')
    print('')
    slowprint(f'The second card is {names[1]}, representing the future:\n')
    slowprint(f'Event: {events[1]}\n')
    slowprint(f'Outcomes: {outcomes[1]}\n')
    slowprint(f'Person: {persons[1]}\n')
    print('')

    time.sleep(2)

    ###Beginning the third set of rolls
    slowprint("Now we pull for the answers to the character's question:\n")
    print('')

    ###Input commands for the player's rolls
    num1 = int(input('Please enter the first roll: '))
    print('')
    num2 = int(input('Now please enter the second roll: '))

    ###Defining empty lists to append pulls into
    events = []
    outcomes = []
    persons = []
    names = []

    ###For loops:
    for card in possiblecards:
        if int(card.roll) == num1:
            events.append(str(card.event))
            names.append(str(card.title))
            outcomes.append(str(card.outcome))
            persons.append(str(card.person))

    for card in possiblecards:
        if int(card.roll) == num2:
            events.append(str(card.event))
            names.append(str(card.title))
            outcomes.append(str(card.outcome))
            persons.append(str(card.person))

    ##Printing the results
    print('')
    slowprint('You have pulled two cards\n')
    print('')
    slowprint(f'The first card is {names[0]}:\n')
    slowprint(f'Event: {events[0]}\n')
    slowprint(f'Outcomes: {outcomes[0]}\n')
    slowprint(f'Person: {persons[0]}\n')
    print('')
    slowprint(f'The second card is {names[1]}:\n')
    slowprint(f'Event: {events[1]}\n')
    slowprint(f'Outcomes: {outcomes[1]}\n')
    slowprint(f'Person: {persons[1]}\n')
    print('')

TarotPull()
