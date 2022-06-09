import emp

def main():
    #three employee objects

    emp1 = emp.Employee('name', 'id', 'dept', 'title')
    emp2 = emp.Employee('name', 'id', 'dept', 'title')
    emp3 = emp.Employee('name', 'id', 'dept', 'title')


    #employee objects for each attribute
    emp1.set_name('Susan Meyers')
    emp1.set_id('47899')
    emp1.set_dept('Accounting')
    emp1.set_title('Vice President')

    emp2.set_name('Mark Jones')
    emp2.set_id('39119')
    emp2.set_dept('IT')
    emp2.set_title('Programmer')

    emp3.set_name('Joy Rogers')
    emp3.set_id('81774')
    emp3.set_dept('Manufacturing')
    emp3.set_title('Engineer')

main()
    
