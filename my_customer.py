# Your code goes here
class customer:
    no_of_customers = 0 
    
class get_discount(customer):
    max (11 - customer.no_of_customers, 5)
            
    def __init__ (self, cid):
        self.cust_id = cid 
        customer.no_of_customers += 1 

    def apply_discount (self, price):
        return (int) (price * (1 - self.discount / 100.))

