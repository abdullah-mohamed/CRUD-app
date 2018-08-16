"""
 project : Database for MIS subject CIE200 lvl200
 written by : ...
 date : 12/ 11 / 2017
 version : 1
 Info :
	- start at user_interface function if you are reading the code.
    - There will be 2 major classes: Student, Database
	- The Database will allow Adding, Removing(Using a password, Dertermined at the making of a new Database),
		Updating(Using password also), Reading and printing a database in a file.
	- To find unfinished parts, search for todo
"""
from sys import exit

# check_for_type function
string_val = 1
int_val = 2
float_val = 3

class Student(object):
	""" Class for grouping each student related information """
	
	def __init__(self, name, ID, subjects, degrees, GPA, num_of_hours, fees_per_hour):
		""" For giving each student his particular information """
		self.name = name                                          	# name of student
		self.ID = ID 												# ID of student
		self.subjects = subjects								  	# list of registered subjects		
		self.degrees  = degrees										# list of degrees of registered subjects 
		self.gpa = GPA												# student GPA
		self.fees_flag = 0        									# flag indicating whether student paid his fees or not. 0 ----> fees not paid, 1 ----> fees paid
		if (self.gpa >= 3.6):
			self.fees = num_of_hours * fees_per_hour * 0.75			# students with high GPA get a 25% discount on their fees
		else:
			self.fees = num_of_hours * fees_per_hour
		
class Database(object):
	""" Class for making a new Database """
	
	def __init__(self, name):
		self.name = name					# name of the database
		self.password = 0
		self.list = []						# list of Student instances 
	
	def add(self):
		""" 
		Inputs needed data(comments in parenthesis is the start of an input process), makes
		a new student instance then add it to the database instance list of Student instances
		"""
		
		# Input 7 values and check them (name, ID, subjects, degrees, GPA, num_of_hours, fees_per_hour)
		# all of these variables have the name student_variable
		
		
		# (name input) check for its type and check if its a duplicate
		student_name = raw_input("Enter the name of a student >> ")
		
		# check for type
		student_name = check_for_type(student_name, string_val)	
		
		# check if input already exists in the list 
		if(self.check_duplicate(student_name, "name")):
			# (ID input) and check for its type
			student_ID = raw_input("Enter %s's ID number? >> " % student_name)
			
			# check for type
			student_ID = check_for_type(student_ID, int_val)
			
			# casting into integer
			student_ID = int(student_ID)
			
			# check if another student has the same ID
			check = self.check_duplicate(student_ID, "ID")
			if (not check):
				print "Another student in %s database has the same ID." % self.name
				print "Operation unsuccessful!!"
				return 0
			
			# check for value(greater then 0)
			msg = "ID can't be 0 or negative number."
			student_ID = check_for_value(msg, student_ID, "ID", "SOE", 0)		
			
			
			# (subjects input)
			num_of_subjects = raw_input("How many subjects did student %s register? >> " % student_name)
			
			# check for type
			num_of_subjects = check_for_type(num_of_subjects, int_val)
			
			# casting into integer
			num_of_subjects = int(num_of_subjects)
			
			# check for value(greater than 0)
			msg =  "num_of_subjects can't be 0 or negative number."
			num_of_subjects = check_for_value(msg, num_of_subjects, "number of subjects", "SOE", 0)		
			
			# list for student subjects
			student_subjects = []			
			
			# loop to enter subjects
			for i in range(0, num_of_subjects):
				subject = raw_input("Enter name of subject number %d >> "  % (i + 1))
				
				# check for type
				subject = check_for_type(subject, string_val)
					
				# adding to student_subjects
				student_subjects.append(subject)
			
			# list for student degrees
			student_degrees = []
			
			# (degrees input)
			for i in range(0, num_of_subjects):
				degree = raw_input("Enter degree of %s subject >> " % student_subjects[i])
				
				# check for type
				degree = check_for_type(degree, float_val)
				
				# casting into integer
				degree = int(degree)
				
				# check for value(greater than 0)
				msg = "degree can't be a negative number."
				degree = check_for_value(msg, degree, "degree", "S", 0)
				
				# adding to student_degrees
				student_degrees.append(degree)
			
			
			# (GPA input)
			student_gpa = raw_input("Enter %s gpa >> " % student_name)
			
			# check for type
			student_gpa = check_for_type(student_gpa, float_val)
			
			# cast into integer
			student_gpa = int(student_gpa)
			
			# check for value (GPA 0 --> 4)    --> didn't use the check_for_value function because of 2 conditions
			while (student_gpa <= 0 or student_gpa >= 4):
				print "GPA valid values 0~4."
				student_gpa = raw_input("Enter valid GPA >> ")
				
				# check for type
				student_gpa = check_for_type(student_gpa, int_val)
				
				# casting into integer
				student_gpa = int(student_gpa)			
			
			
			# (num of registered hours input)
			student_num_of_hours = raw_input("Enter number of student %s registered hours >> " % student_name)
			
			# check for type
			student_num_of_hours = check_for_type(student_num_of_hours, int_val)
				
			# cast into integer
			student_num_of_hours = int(student_num_of_hours)
			
			#  check for value
			msg = "registered hours must be at least double the number of subjects."
			student_num_of_hours = check_for_value(msg, student_num_of_hours, "number of hours", "S", (num_of_subjects * 2))
			
			
			# (fees per hour input)
			student_fees_per_hour = raw_input("Enter fees/hour for student %s >> " % student_name)
			
			# check for type
			student_fees_per_hour = check_for_type(student_fees_per_hour, float_val)
			
			# casting into integer
			student_fees_per_hour = int(student_fees_per_hour)
			
			# check for value
			# note: fees can be 0 for full funded scholarships
			msg = "fees/hour can't be a negative value"
			student_fees_per_hour = check_for_value(msg, student_fees_per_hour, "price/hour", "S", 0)
			
			
			# make a student instance (self, name, ID, subjects, degrees, GPA, num_of_hours, fees_per_hour_ID)
			student = Student(student_name, student_ID, student_subjects, student_degrees, student_gpa, student_num_of_hours, student_fees_per_hour)
			self.list.append(student)
			
			print "Operation successful."
		else:
			print "Another student in %s database has the same name." % self.name
			print "Operation unsuccessful!!"
	
	def check_duplicate(self, charactristic, thing):
		""" checks if a student already has the entered name or ID return 0 --> student exist, 1 --> not exist """
		ret = 1
		if (thing == "ID"):
			for i in self.list:
				if (i.ID == charactristic):
					ret = 0
		else:
			for i in self.list:
				if (i.name == charactristic):
					ret = 0
		return ret
		
	def check_duplicate_index(self, charactristic, thing):
		""" returns index if a student already has the entered name or ID """
		count = 0
		if (thing == "ID"):
			for i in self.list:
				if (i.ID == charactristic):
					return count
				count += 1
		else:
			for i in self.list:
				if (i.name == charactristic):
					return count
				count += 1
	
	def remove(self):
		""" removes a student instance from a database """
		
		# check password to make sure he has permission
		password = raw_input("Enter %s database password >> " % self.name)
		
		if (password == self.password):
			print "Access granted!!"
			print "You can access students using name or ID."
			print "Enter ID or Name."
			
			# determine accessing method
			access = raw_input("How would you like to access the student ? >> ")
			
			# check for type
			access = check_for_type(access, string_val)
			
			# check for value
			if (access == 'ID' or access == 'Name'):
				if (access == 'ID'):
					# ID input
					student_id = raw_input("Enter student ID to remove him from the Database >> ")
					
					# check for type
					student_id = check_for_type(student_id, int_val)
					
					# check for value
					msg = "ID can't be 0 or negative number."
					student_id = check_for_value(msg, student_id, "ID", "SOE", 0)	
					
					# check if student exists or not
					check = self.check_duplicate(student_id, access)
					if (check):
						print "No student in %s database has such ID." % self.name
						print "Process Terminated!!"
						return 0
						
					# find Student instance with the same ID
					student_instance_index = self.check_duplicate_index(student_id, access)
					
					# pop the student out of the Database list of Student instances using his index
					self.list.pop(student_instance_index)
					
					print "Process successful."
					print "Student %d no longer exists in %s Database." % (student_id, self.name)
					
				else:
					# name input
					student_name = raw_input("Enter student name to remove him from the Database >> ")
					
					# check for type
					student_name = check_for_type(student_name, string_val)
					
					# check if student exists or not
					check = self.check_duplicate(student_id, access)
					if (check):
						print "No student in %s database has such name." % self.name
						print "Process Terminated!!"
						return 0
					
					# find Student instance with the same name
					student_instance_index = self.check_duplicate_index(student_name, access)
					
					# pop the student out of the Database list of Student instances using his index
					self.list.pop(student_instance_index)
					
					print "Process successful."
					print "Student %s no longer exists in %s Database." % (student_name, self.name)
					
			else:
				print "Invalid Access method, enter 'ID' or 'Name' only."
				print "Process Terminated!!"
				return 0			
		else:
			print "Wrong password, Access denied!!"
			print "Process Terminated!!"
	
	def update(self):
		""" updates information os student, Password required """
		
		# check password to make sure he has permission
		password = raw_input("Enter %s database password >> " % self.name)
		
		if (password == self.password):
			print "Access granted!!"
			print "You can access students using name or ID."
			print "Enter ID or Name."
			
			# determine accessing method
			access = raw_input("How would you like to access the student ? >> ")
			
			# check for type
			access = check_for_type(access, string_val)
			
			# check for value
			if (access == 'ID' or access == 'Name'):
				if (access == 'ID'):
					# ID input
					student_id = raw_input("Enter student ID to update his information >> ")
					
					# check for type
					student_id = check_for_type(student_id, int_val)
					
					# check for value
					msg = "ID can't be 0 or negative number."
					student_id = check_for_value(msg, student_id, "ID", "SOE", 0)	
					
					# check if student exists or not
					check = self.check_duplicate(student_id, access)
					if (check):
						print "No student in %s database has such ID." % self.name
						print "Process Terminated!!"
						return 0
						
					# find Student instance with the same ID
					student_instance_index = self.check_duplicate_index(student_id, access)
					
					# print the possible commands for user
					print "\tYou are updating %d info." % student_id					# todo : if Student object is updated with more details, this will change
					print "\tTo update his name, enter name."
					print "\tTo update his ID, enter ID."
					print "\tTo update his Subjects, enter subjects."
					print "\tTo update his Degrees, enter degrees."
					print "\tTo update his GPA, enter gpa."
					print "\tTo update his fees condition, enter fees"
					
					# atrribute that user want to change in a specific instance
					attr = raw_input("Which info would you like to update ? >> ")
					
					# check for type
					attr = check_for_type(attr, string_val)
					
					# variable for the updates
					new_update = "BOO"
					
					# check for attribute to be updated
					if (attr == 'name'):
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %d >> " % (attr, student_id)) 
						
						# check for type
						new_update = check_for_type(new_update, string_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					elif (attr == 'ID'):
						# Getting the specific attribute of the insatance
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %d >> " % (attr, student_id)) 
						
						# check for type
						new_update = check_for_type(new_update, int_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					elif (attr == 'subjects'):									
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update_num_of_sub = raw_input("Enter the updated number of %s of %d >> " % (attr, student_id)) 
						
						# check for type
						new_update_num_of_sub = check_for_type(new_update_num_of_sub, int_val)
						
						# check for value
						msg = "Number of subjects must be greater than 0."
						new_update_num_of_sub = check_for_value(msg, new_update_num_of_sub, "Number of subjects", "SOE", 0)
						
						# empty the previous subject list
						for i in range(0, len(student_instance_name)):
							student_instance_name.pop(i)
						
						# refill the subject list with new subjects
						for i in range(0, new_update_num_of_sub):
							# subject input
							subject = raw_input("Enter subject number %d >> " % (i + 1))
							
							# check for type
							subject = check_for_type(subject, string_val)
							
							# add to instance subjects list
							student_instance_name.append(subject)
						
					elif (attr == 'degrees'):								
						student_instance_name = getattr(self.list[student_instance_index], 'subjects')   # we want to find the index then change it in attribute degrees
						
						# new update input
						print "\tstudent %d is enrolled in:" % student_id
						for i in (student_instance_name):
							print "\t\t- %s" % i
						new_update_subject = raw_input("Which subject do you want to update ? >> ") 
						
						#check for type
						new_update_subject = check_for_type(new_update_subject, string_val)
						
						# check if subject exists
						subject_update_index = -1
						count = 0
						for i in (student_instance_name):
							if (i == new_update_subject):
								subject_update_index = count
							count += 1
						if (subject_update_index == -1):
							print "student %d isn't enrolled in %s." % (student_id, new_update_subject)
							print "Process Terminated"
							return 0
					
						# get degrees specific attribute
						student_instance_name = getattr(self.list[student_instance_index], attr)
						
						# get the update value
						new_update = raw_input("Enter %d's subject %s new Degree? >> " % (student_id, new_update_subject))
						
						# check for type
						new_update = check_for_type(new_update, int_val)
						
						# check for value
						msg = "Degree can't be less than 0."
						new_update = check_for_value(msg, new_update, "Student Degree", "SOE", 0)
						
						# update the checked value in the instance
						student_instance_name[subject_update_index] = new_update							# syntax : Is it right?
						
					elif (attr == 'gpa'):
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %d >> " % (attr, student_id)) 
						
						# check for type
						new_update = check_for_type(new_update, int_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					elif (attr == 'fees'):
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %d >> "% (attr, student_id))
						
						# check for type
						new_update = check_for_type(new_update, float_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					else:
						print "Invalid update input."
						print "Process Terminated!!"
						return 0
						
					print "Process successful."
					print "Student %d's %s is updated to %r." % (student_id, attr, new_update)
					
				else:
					# name input
					student_name = raw_input("Enter student name to update his information >> ")
					
					# check for type
					student_name = check_for_type(student_name, string_val)
					
					# check if student exists or not
					check = self.check_duplicate(student_name, access)
					if (check):
						print "No student in %s database has such name." % self.name
						print "Process Terminated!!"
						return 0
						
					# find Student instance with the same name
					student_instance_index = self.check_duplicate_index(student_name, access)
					
					# print the possible commands for user
					print "\tYou are updating %s info." % student_name					# todo : if Student object is updated with more details, this will change
					print "\tTo update his name, enter name."
					print "\tTo update his ID, enter ID."
					print "\tTo update his Subjects, enter subjects."
					print "\tTo update his Degrees, enter degrees."
					print "\tTo update his GPA, enter gpa."
					print "\tTo update his fees condition, enter fees"
					
					# atrribute that user want to change in a specific instance
					attr = raw_input("Which info would you like to update ? >> ")
					
					# check for type
					attr = check_for_type(attr, string_val)
					
					#variable for new updates
					new_update = "FOO"
					
					# check for attribute to be updated
					if (attr == 'name'):
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %s >> " % (attr, student_name)) 
						
						# check for type
						new_update = check_for_type(new_update, string_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					elif (attr == 'ID'):
						# Getting the specific attribute of the instance
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %s >> " % (attr, student_name)) 
						
						# check for type
						new_update = check_for_type(new_update, int_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					elif (attr == 'subjects'):									
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update_num_of_sub = raw_input("Enter the updated number of %s of %s >> " % (attr, student_name)) 
						
						# check for type
						new_update_num_of_sub = check_for_type(new_update_num_of_sub, int_val)
						
						# check for value
						msg = "Number of subjects must be greater than 0."
						new_update_num_of_sub = check_for_value(msg, new_update_num_of_sub, "Number of subjects", "SOE", 0)
						
						# empty the previous subject list
						for i in range(0, len(student_instance_name)):
							student_instance_name.pop(i)
						
						# refill the subject list with new subjects
						for i in range(0, new_update_num_of_sub):
							# subject input
							subject = raw_input("Enter subject number %d >> " % (i + 1))
							
							# check for type
							subject = check_for_type(subject, string_val)
							
							# add to instance subjects list
							student_instance_name.append(subject)
						
					elif (attr == 'degrees'):								
						student_instance_name = getattr(self.list[student_instance_index], 'subjects')   # we want to find the index then change it in attribute degrees
						
						# new update input
						print "\tstudent %s is enrolled in:" % student_name
						for i in (student_instance_name):
							print "\t\t- %s" % i
						new_update_subject = raw_input("Which subject do you want to update ? >> ") 
						
						#check for type
						new_update_subject = check_for_type(new_update_subject, string_val)
						
						# check if subject exists
						subject_update_index = -1
						count = 0
						for i in (student_instance_name):
							if (i == new_update_subject):
								subject_update_index = count
							count += 1
						if (subject_update_index == -1):
							print "student %s isn't enrolled in %s." % (student_name, new_update_subject)
							print "Process Terminated"
							return 0
					
						# get the specific attribute
						student_instance_name = getattr(self.list[student_instance_index], attr)
						
						# get the update value
						new_update = raw_input("Enter %s's subject %s new Degree? >> " % (student_name, new_update_subject))
						
						# check for type
						new_update = check_for_type(new_update, int_val)
						
						# check for value
						msg = "Degree can't be less than 0."
						new_update = check_for_value(msg, new_update, "Student Degree", "SOE", 0)
						
						# put the new value
						student_instance_name[subject_update_index] = new_update							# syntax : Is it right?    --> yes
						
					elif (attr == 'gpa'):
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %s >> " % (attr, student_name)) 
						
						# check for type
						new_update = check_for_type(new_update, int_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					elif (attr == 'fees'):
						student_instance_name = getattr(self.list[student_instance_index],attr)
						
						# new update input
						new_update = raw_input("Enter the updated %s of %s >> "% (attr, student_name))
						
						# check for type
						new_update = check_for_type(new_update, float_val)
						
						# update the specific attribute
						student_instance_name = new_update
						
					else:
						print "Invalid update input."
						print "Process Terminated!!"
						return 0
						
					print "Process successful."
					print "Student %s's %s is updated to %r." % (student_name, attr, new_update)
					
			else:
				print "Invalid Access method, enter 'ID' or 'Name' only."
				print "Process Terminated!!"
				return 0
		else:
			print "Wrong password, Access denied!!"
			print "Process Terminated!!"
		
	def read(self):
		""" prints information about a specific student using his name or ID. """
		
		print "You can access students using name or ID."
		print "Enter ID or Name."
			
		# determine accessing method
		access = raw_input("How would you like to access the student ? >> ")
			
		# check for type
		access = check_for_type(access, string_val)
			
		# check for value
		if (access == 'ID' or access == 'Name'):
			if (access == 'ID'):
				# ID input
				student_id = raw_input("Enter student ID to read his information >> ")
					
				# check for type
				student_id = check_for_type(student_id, int_val)
					
				# check for value
				msg = "ID can't be 0 or negative number."
				student_id = check_for_value(msg, student_id, "ID", "SOE", 0)	
					
				# check if student exists or not
				check = self.check_duplicate(student_id, access)
				if (check):
					print "No student in %s database has such ID." % self.name
					print "Process Terminated!!"
					return 0
						
				# find Student instance with the same ID
				student_instance_index = self.check_duplicate_index(student_id, access)
				
				print "\tYou are viewing %d info." % student_id					# todo : if Student object is updated with more details, this will change
				print "\t\tName    : %s" % ((self.list[student_instance_index]).name)
				print "\t\tID      : %d" % ((self.list[student_instance_index]).ID)
				print "\t\tSubjects: %s" % ((self.list[student_instance_index]).subjects)
				print "\t\tDegrees : %s" % ((self.list[student_instance_index]).degrees)
				print "\t\tGPA     : %f" % ((self.list[student_instance_index]).gpa)
				print "\t\tFees    : %d" % ((self.list[student_instance_index]).fees)
				
			else:				# access by name
				# name input
				student_name = raw_input("Enter student name to remove him from the Database >> ")
					
				# check for type
				student_name = check_for_type(student_name, string_val)
					
				# check if student exists or not
				check = self.check_duplicate(student_name, access)
				if (check):
					print "No student in %s database has such name." % self.name
					print "Process Terminated!!"
					return 0
					
				# find Student instance with the same name
				student_instance_index = self.check_duplicate_index(student_name, access)
				
				print "\tYou are viewing %s info." % student_name					# todo : if Student object is updated with more details, this will change
				print "\t\tName    : %s" % ((self.list[student_instance_index]).name)
				print "\t\tID      : %d" % ((self.list[student_instance_index]).ID)
				print "\t\tSubjects: %s" % ((self.list[student_instance_index]).subjects)
				print "\t\tDegrees : %s" % ((self.list[student_instance_index]).degrees)
				print "\t\tGPA     : %f" % ((self.list[student_instance_index]).gpa)
				print "\t\tFees    : %d" % ((self.list[student_instance_index]).fees)
		else:
			print "Invalid Access method, enter 'ID' or 'Name' only."
			print "Process Terminated!!"
			return 0
				
	def print_infile(self):
		""" prints the contents of a database in a Text file named after the database. """
		
		# check password to make sure he has permission
		password = raw_input("Enter %s database password >> " % (self.name))
		
		if (password == self.password):
			print "Access granted!!"
			
			# open a file and name it after the database
			database_file = open("%s.txt" % (self.name), 'w')
			
			# print the Database name in the file
			database_file.write("This file contains %s Database\n------------------------------\n\n" % (self.name))
			
			# Access students and print them in the file 
			for i in self.list:										# todo : if Student object is updated with more details, this will change
				database_file.write("\t\tName    : %s\n" % (i.name))
				database_file.write("\t\tID      : %d\n" % (i.ID))
				database_file.write("\t\tSubjects: %s\n" % (i.subjects))
				database_file.write("\t\tDegrees : %s\n" % (i.degrees))
				database_file.write("\t\tGPA     : %f\n" % (i.gpa))
				database_file.write("\t\tFees    : %d\n" % (i.fees))
				database_file.write("\n-----\n")
			
			# close the file
			database_file.close()
			
		else:
			print "Wrong password, Access denied!!"
			print "Process Terminated!!"
	
	def help(self):
		""" prints all commands available, Yasser takes credit for it. """
		print "\tCommands:"
		print "\t\tadd   :\tAdd new students."
		print "\t\tremove:\tremove a student(Password required)."
		print "\t\tupdate:\tupdate a student's information(Password required)."
		print "\t\tread  :\tread a specific student's information using his ID or name."
		print "\t\tprint :\tprint the whole database in a file and save it(Password required)."
		print "\t\tnew   :\tmake another database(clears a database if exists)."
		print "\t\tswitch:\tswitch between databases."
		print "\t\tquit  :\tTerminates the program."
		print "\t\thelp  :\tprint all the commands available."

def user_interface(databases_list):
	"""
	Welcome to Database control program.
	This program can :
		- Make a new database for students.
		- After making your database, you can:
			- Add new students.									 command  --->  add
			- remove a student(Password required).							 command  --->  remove
			- update a student's information(Password required).					 command  --->  update
			- read a specific student's information using his ID or name.				 command  --->  read
			- print the whole database in a file and save it(Password required).			 command  --->  print
			- make another database(clears a database if exists).					 command  --->  new
			- switch between databases.								 command  --->  switch 
			- print all the commands available.                       				 command  --->  help
			- Terminate the program.    						         command  --->  quit
 		- As this is the first time you run the program, your first command
		 must be making a new database.
		- To terminate the program, enter quit (Be sure of printing your work in a file).
	"""
	
	print user_interface.__doc__
	new_name = raw_input("What is the name of your database? >> ")
	
	# check if entered value is valid
	new_name = check_for_type(new_name, string_val)
			
	# make a new class Database
	new_database = Database(new_name)
		
	# password for database
	new_password = raw_input("What is the password of %s database? >> " % new_name)
	
	# check for type
	new_password = check_for_type(new_password, string_val)
	
	# append the password to the database
	new_database.password = new_password
	
	# store the database in the databases_list to access later if needed
	databases_list.append(new_database)
	
	while 1 :
		print "\n-------\n"
		print "\tYou are now commanding %s Database." % new_database.name
		action = raw_input("What do you want to do ? >> ")
		
		# different commands that can be entered by user, check user_interface documentation! 
		if (action == "add"):
			new_database.add()
			
		elif (action == "remove"):
			new_database.remove()
			
		elif (action == "update"):
			new_database.update()
			
		elif (action == "read"):
			new_database.read()
			
		elif (action == "print"):
			new_database.print_infile()
			
		elif (action == "switch"):
			new_database = choose_data_base()
			
		elif (action == "new"):
			print "\n------\n"
			new_name = raw_input("What is the name of your new database? >> ")
			
			# check if entered value is a string
			new_name = check_for_type(new_name, string_val)
			
			# check if database exits to clear it 
			for i in range (0, len(databases_list)):
				if (databases_list[i].name == new_name):
					databases_list.pop(i)													# syntax: databases_list.pop(i)
					databases_list[i].list = []												# todo : do I need to distroy the old instance first?
			
			# make a new Database instance 
			new_database = Database(new_name)
			
			# password for database
			new_password = raw_input("What is the password of %s database? >> " % new_name)
	
			# check for type
			new_password = check_for_type(new_password, string_val)
	
			# append the password to the database
			new_database.password = new_password
			
			# store it in databases_list
			databases_list.append(new_database)
		
		elif (action == "help"):
			new_database.help()
		
		elif (action == "quit"):
			print "Goodbye !!"
			exit()
			
		else:
			print "command invalid, please refer to the list of available commands above."

def check_for_type(var, check_value):
	""" variable to check its type, value of type according to check_input function """
	
	if (check_value == 1): 				# check if string
		while True:
			if (type(var) == str):
				return var
			else:
				print "Invalid Input, enter a valid alphabetical value."
	elif (check_value == 2):			# check if integer
		while True:
			try:
				var = int(var)
				return var
			except ValueError:
				print "Invalid Input."
				var = raw_input("Enter a valid non-alphabetical numeric value >> ")
	else:								# check for float
		while True:
			try:
				var = float(var)
				return var
			except ValueError:
				print "Invalid Input."
				var = raw_input("Enter a valid non-alphabetical numeric value >> ")

def check_for_value(message, var, var_name, comparison_sign, comparison_value):
	""" compares 2 values and takes input from user until a valid value is entered"""
	if (comparison_sign == "G"):	    # greater than
		while(var > comparison_value):
			var = rest(message, var, var_name)
			
	elif (comparison_sign == "S"):		# smaller than
		while(var < comparison_value):
			var = rest(message, var, var_name)
			
	elif (comparison_sign == "GOE"):    # greater than or equal
		while (var >= comparison_value):
			var = rest(message, var, var_name)
			
	elif (comparison_sign == "SOE"):	# smaller than or equal
		while (var <= comparison_value):
			var = rest(message, var, var_name)
			
	else:								# equal
		while (var == comparison_value):
			var = rest(message, var, var_name)
	return var

def rest(message, var, var_name):
	print message
	var = raw_input("Enter valid %s >> " % var_name)
				
	# check for type
	var = check_for_type(var, 2)
			
	# cast into integer
	var = int(var)
	return var
	
def choose_data_base():
	""" returns which database to do work on """
	db_name = raw_input("Which database do you want to work on ? >> ")
	flag_exist = 0 											# determine whether a database of such name exists or not, 0 --> doesn't exist,1 --> exists
	
	# sweep the list looking for the database
	for i in range(0, len(databases_list)):
		if (databases_list[i].name == db_name):
			flag_exist = 1
			return databases_list[i]
			
	# recurse until you get a valid name from user
	if (flag_exist == 0):
		print "No database of such name!"
		choose_data_base()

# a list containing all databases instances made		
databases_list = []
		
# calling the UI at the beginning of the program
user_interface(databases_list)