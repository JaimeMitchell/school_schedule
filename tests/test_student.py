from school_schedule.student import Student

def test_adding_one_class_increase():
    
    name ="Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name,grade,classes)
    
    ellis.add_class("Pottery")
    
    assert ellis.classes == ["Painting", "Pottery"]
    assert len(ellis.classes) == 2
    
def test_student_class_attributes():
    name ="Ellis"
    grade = "junior"
    classes = ["Painting"]
    
    ellis = Student(name,grade,classes)
    
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    
# def test_student_class_invalid_input():
#     name = 456
#     grade = "junior"
#     classes = ["Painting"]
    
    
def test_classes_empty_list():
    
    name ="Ellis"
    grade = "junior"
    classes = []
    
    ellis = Student(name,grade,classes)
    
    assert ellis.classes == []
    
def test_get_num_classes():
    name ="Ellis"
    grade = "junior"
    classes = ["Painting","Choir","Math"]
    
    ellis = Student(name,grade,classes)
    result = ellis.get_num_classes()
    
    assert result == 3

def test_summary_returns_str():
    name ="Ellis"
    grade = "junior"
    classes = ["Painting","Choir","Math"]
    
    ellis = Student(name,grade,classes)
    result = ellis.summary()
    
    assert result == "Ellis is a junior enrolled in 3 classes : Painting, Choir, Math"
    
