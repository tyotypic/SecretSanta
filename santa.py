import random

class Person(object):
    def __init__(self, my_name):
        self.name = my_name
        self.people_I_cant_get = [self]
        self.person_I_got = None
   
    def __repr__(self):
        return self.name
   
    def add_people_I_cant_get(self, *people):
        for person in people:
            self.people_I_cant_get.append(person)
            
class SecretSanta(object):
    def __init__(self, *all_the_people):
        self.people = list(all_the_people)
        
    def choose(self):
        self._bogo_choose()
        
    def _bogo_choose(self):
        """Not the most efficient way, but I like it better than choosing from an ever-decreasing pool. If conditions aren't too strict, it should work well. As the people_I_cant_get list becomes longer, this method will need more and more tries."""
        isFinished = False
        people = self.people
        results = list(people)
        
        count = 0
        while not isFinished:    
            random.shuffle(results)
            count += 1

            index = 0
            while index < len(people):
                if results[index] in people[index].people_I_cant_get:
                    break
                else:
                    index += 1
            
            if index == len(people):
                isFinished = True

                for (i, person) in enumerate(people):
                    person.person_I_got = results[i]
        
        return count
                
    def report(self):
        """This method is intended to keep the results secret from the programmer, too. Go email the file to whomever."""
        people = self.people
        for outfile_person in people:
            filename = outfile_person.name + ".txt"
            outfile = open(filename, "w")
            outfile.write("Your Secret Santa recipient is: %s\n\n" %outfile_person.person_I_got.name)
            outfile.write("These files have been generated by computer and the contents are secret even from the programmer.\n")
            outfile.write("Here are the conditions under which this program ran:\n")
            
            for person_Im_listing in people:
                for person_who_cant_be_gotten in person_Im_listing.people_I_cant_get:
                    if person_who_cant_be_gotten != person_Im_listing:
                        outfile.write("%s cannot get %s\n" %(person_Im_listing.name, person_who_cant_be_gotten.name))

            outfile.close()
            
    def test(self, numTests):
        count = 0
        for i in range(numTests):
            count += self._bogo_choose()
        print "total: %i, average: %f" %(count, count/float(numTests))        

    def pick_mark1():
        """Not even remotely valid code anymore. Kept for historic reasons"""
        results = {}
        isFinished = False
        while not isFinished:
            picked = set()
            for fromPerson in bigList:
                toPool = names[fromPerson].difference(picked)
                if len(toPool) == 0:
                    break
                toPerson = choice(list(toPool))
                
                picked.add(toPerson)
                results[fromPerson] = toPerson
                if len(results) == 7:
                    isFinished = True
        return results