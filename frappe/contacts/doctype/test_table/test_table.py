# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TestTable(Document):
	def validate(self):
		name = self.name1
		if(name):
			if (not(name_validate(name))):
				frappe.throw("Please Enter Valid Name")
			
		
		cnic = self.cnic
		if(cnic):
			if (not(cnic_validate(cnic))):
				frappe.throw("Please Enter Valid CNIC")
			
		
		num = self.mobile_no
		if(num):
			if (not(phone_validate(num))):
				frappe.throw("Please Enter Valid Mobile no")
				
		
		email = self.email
		if(email):
			if (not(email_validate(email))):
				frappe.throw("Please Enter Valid Email")
			


def  cnic_validate(cnic):
	regex_cnic = '/^([0-9]{5}[\-][0-9]{7}[\-][0-9]{1})$/'
	if (not(cnic.match(regex_cnic)) or cnic.length != 15):
		return False
	else: 
		return True


def  name_validate(name):
	is_text_valid = False
	if (len(name) >= 3):
		pattern = '/^[a-zA-Z. ]+$/g'
		if(name.match(pattern) != null):
			is_text_valid = True
		
		
		return is_text_valid

def email_validate(email):
	pattern =  '/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/'
	is_email_valid = False
	if(email.match(pattern) != null):
		is_email_valid = True
		return is_email_valid
		
	if (not(email.match(mailformat))):
		return False
	else:
		return True
    



def phone_validate(phone):
    regex_phone = '/^0[0-9]{3}-[0-9]{7}$/'
  
    if (not(phone.match(regex_phone)) or phone.length != 12):
        
        return False
    else: 
        return True
    


def phone(phone):
    regex_phone = '/^0[0-9]{2}-[0-9]{7}$/'
  
    if (not(phone.match(regex_phone)) or phone.length != 11):
       
        return False
    else:
        return True