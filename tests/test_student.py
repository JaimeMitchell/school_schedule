from school_schedule.student import Student

def test_adding_one_class_increase():
    pass
    name ="Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name,grade,classes)
    
    ellis.add_class("Pottery")
    
    assert ellis.classes == ["Painting, Pottery"]