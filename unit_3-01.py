# Created by: Matthew Walsh
# Created on: oct 2017
# Created for: ICS3U
# This program shows how to use an if statement

import ui

MAXIMUM_NUMBER_OF_STUDENTS = 25

def number_of_students_button(sender):
    # check the number of students entered verses the constant above
    
    # input
    number_entered = int(view['number_of_students_textfield'].text)
    
    # process
    if number_entered > MAXIMUM_NUMBER_OF_STUDENTS:
        # output
        view['too_many_students_label'].text = "Too many students!"
    
view = ui.load_view()
view.present('full_sheet')
