# Table Seperators
row_seperator = "_"
column_seperator = "|"

#Table Selectors
left_selector = "【"

# Distance of Output From L.H.S
tab = "\t"

# Input indicator for menu options (Why Does it exist)
get_input_menu = tab + ":)"

################
# USER VARIABLES
################
user = "\n\n" + tab +"Who Are You ?\n\n"

user_list = [
				"Admin",
				"Customer",
				"Exit"
			]

tries_done = "You Have Entered Wrong Entry Three Times"
tries_remaining = "Tries Remaining : "

#################
# ADMIN VARIABLES
#################
get_admin_name = "\n\n" + tab + "Admin Id :: "
get_admin_pswd = "\n\n" + tab + "Password :: "

admin_ids = ["Vinayak","CEO","t"]
admin_pswd = ["LinusTorvaldsOP","rob_my_shop","t"]

admin_name_found = "Admin Username found, Now Enter Password"

try_again_admin_name = "User name not found, Try Again !"
try_again_admin_pswd = "Wrong Password, Try Again !"

admin_menu_0 = [
					"Show Products",
					"Manage Products",
					"Show Employee Info",
					"Edit Employee Info",
					"Show Sales (Graphs)",
					"Show Complaints",
					"Back"
				]

admin_menu_0_1 = [
					"Show All Products",
					"Search Product by ID",
					"Search Product by Name",
					"Back"
				]

admin_menu_0_2 = [
					"Manage Products (Spreadsheet Mode)",
					"Manage Products (by ID)",
					"Manage Products (by Name))",
					"Back"]

admin_menu_0_3 = [
					"Show all Employees",
					"Search Employee by ID",
					"Search Employee by Name",
					"Back"
				]
admin_menu_0_6 = [
					"Show All Complaints",
					"Back"
				]

####################
# CUSTOMER VARIABLES
####################

customer_menu_0 = [
					"Buy Product",
					"Show All Products",
					"Return Product",
					"Feedback/Complaint",
					"Back"
				  ]
#################
# Stock Variables
#################

enter_pid = tab + "Product ID :: "
enter_pname = tab + "Product Name :: "
enter_eid = tab + "Employee ID :: "
enter_ename = tab + "Employee Name :: "



# Message Titles
mssg_title_default = "MESSAGE BOX"
mssg_title_error = "ERROR"
mssg_title_dir = "DIRECTORY"


# Error Messages
err_01 = "Invalid Input"
err_02 = "Input out of range"
err_03 = "ID not found"
err_04 = "Name not found"
err_05 = "ID's are integer"

msg_01 = "All Complaints have been Deleted ."
confirm_msg = "Are Your sure (Y/n) :: "



valid_inputs = ["A","B","C","D"]

# lolcat
wait = tab + "Press Enter to Continue"
yes = ["y","Y","Yes","yes"]
admin = "Admin"
customer = "Customer"

