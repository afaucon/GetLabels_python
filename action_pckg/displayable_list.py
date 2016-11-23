'''
Created on 7 avr. 2015

@author: e_afauco
'''

'''
Main Title
               [ Info_A    ;   Info_B    ;   Info_C    ;   Info_D  ]
(Item 1)      [[ Val A 1   ;   Val B 1   ;   Val C 1   ;   Val D 1 ];
(Item 2)       [ Val A 2   ;   Val B 2   ;   Val C 2   ;   Val D 2 ];
(Item 3)       [ Val A 3   ;   Val B 3   ;   Val C 3   ;   Val D 3 ];
(Item 4)       [ Val A 4   ;   Val B 4   ;   Val C 4   ;   Val D 4 ]]
'''

class displayable_list():
    
    def __init__(self, title, number_of_colomn):
        self.title              = title
        self.number_of_colomn   = number_of_colomn
        self.colomns_names_list = []
        self.items_list         = [[]]
        
        if self.number_of_colomn < 1:
            print("todo : error 1")
    
        
    def set_colomns_names_list(self, colomns_names_list):
        if self.number_of_colomn != len(colomns_names_list):
            print("todo : error 2")
            
        self.colomns_names_list = colomns_names_list
    
        
    def add_item(self, item):
        items_values_list = item
        
        if self.number_of_colomn != len(items_values_list):
            print("todo : error 3")
                       
        self.items_list.append(item)
    
    
    def get_title(self):
        return self.title
    
    