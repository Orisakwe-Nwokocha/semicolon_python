print("Welcome!!!")
print()
print(f"\tHome")
print()

print("1. Phone book\n2.Messages\n3.Chat\n4. Call Register\n5. Tones\n6. Settings\n7. Call Divert\n8. Games\n9. Speed dials\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM services")
print()
menu = int(input("Select an option: "))
print()

match (menu): 
	case 1:
		print("1. Search\n2. Service Nos\n3. Add name\n4. Erase\n5. Edit\n6. Assign tone\n7. Send b’card\n8. Options\n9. Speed dials\n10. Voice tags")
		print()
		phonebookMenu = int(input("Select an option: "))
		print()

		match phonebookMenu: 
			case 1:
				print("Search")
			case 2:
				print("Service Nos")
			case 3:
				print("Add name")
			case 4:
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Assign tone")
			case 7:
				print("Send b’card")
			case 8:
				print("1. Type of view2. Memory status")
				print()
				optionsPhonebookMenu = int(input("Select an option: "))
				print()
						
				if optionsPhonebookMenu == 1:
					print("Type of view")	
					 
				if optionsPhonebookMenu == 2:
					print("Memory status")					 

			case 9:
				print("Speed dials")
			case 10:
				print("Voice tags")		
	case 2:
		print("1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info service\n9. Voice mailbox number\n10. Service command editor")
		print()
		messagesMenu = int(input("Select an option: "))
		print()

		match messagesMenu: 
			case 1:
				print("Write messages")
			case 2:
				print("Inbox")
			case 3:
				print("Outbox")
			case 4:
				print("Erase")	
			case 5:
				print("Picture messages")
			case 6:
				print("Templates")
			case 7:
				print("1. Set 1\n2. Common")
				print()
				optionsMessagesMenu = int(input("Select an option: "))
				print()

				if optionsMessagesMenu == 1:
					print("1. Message centre number\n2. Messages sent as\n3. Message validity")
					print()
					moreOptions = int(input("Select an option: "))
					print()
	
					if moreOptions == 1: 
						print("Message centre number")
							 
					if moreOptions == 2: 
						print("Messages sent as")
							 
					if moreOptions == 3: 
						print("Message validity")
						 						 
				if optionsMessagesMenu == 2:
					print("1. Delivery reports\n2. Reply via same centre\n3. Character support")
					print()
					moreOptions2 = int(input("Select an option: "))
					print()

					if moreOptions2 == 1:
						print("Delivery reports")	 

					if moreOptions2 == 2: 
						print("Reply via same centre")
							 
					if moreOptions2 == 3: 
						print("Character support")

			case 8:
				print("Info service")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editorn")
						 	 
	case 3:
		print("Chat")
	case 4:
		print("1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call lists\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit")
		print()
		callRegisterMenu = int(input("Select an option: "))
		print()

		match callRegisterMenu: 
			case 1:
				print("Missed calls")
			case 2:
				print("Received calls")
			case 3:
				print("Dialled numbers")
			case 4:
				print("Erase recent call lists")	
			case 5:
				print("1. Last call duration\n2. All calls' duration\n3. Received calls' duration\n4. Dialled calls' duration\n5. Clear timers")
				print()
				showCallDuration = int(input("Select an option: "))
				print()			

				if showCallDuration == 1: 
					print("Last call duration")

				if showCallDuration == 2: 
					print("All calls' duration")
			 
				if showCallDuration == 3: 
					print("Received calls' duration")
						 
				if showCallDuration == 4: 
					print("Dialled calls' duration")					 

				if showCallDuration == 5: 
					print("Clear timers")

			case 6:
				print("1. Last call cost\n2. All calls' cost\n3. Clear counters")
				print()
				showCallCosts = int(input("Select an option: "))
				print()	
					
				if showCallCosts == 1: 
					print("Last call cost")
					 
				if showCallCosts == 2: 
					print("All calls' cost")
						 
				if showCallCosts == 3: 
					print("Clear counters")
						 
			case 7:
				print("1. Call cost limit\n2. Show costs in")
				print()			
				callCostSettings = int(input("Select an option: "))
				print()						
						
				if callCostSettings == 1: 
					print("Call cost limit")
					 
				if callCostSettings == 2: 
					print("Show costs in")				 
									
			case 8:
				print("Prepaid credit")
		
	case 5:
		print("1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Composer\n5. Message alert tone\n6. Keypad tones\n7. Warning and game tones\n8. Vibrating alert\n9. Screen saver")
		print()	
		tonesMenu = int(input("Select an option: "))
		print()	

		match tonesMenu: 
			case 1:
				print("Ringing tone")
			case 2:
				print("%Ringing volume")
			case 3:
				print("Incoming call alert")
			case 4:
				print("Composer")
			case 5:
				print("Message alert tone")
			case 6:
				print("Keypad tones")
			case 7:
				print("Warning and game tones")
			case 8:
				print("Vibrating alert")
			case 9:
				print("Screen saver")

	case 6:
		print("1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory settings")
		print()	
		settingsMenu = int(input("Select an option: "))
		print()	

		match settingsMenu: 
			case 1:
				print("1. Automatic redial\n2. Speed dialling\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer")
				print()	
				callSettings = int(input("Select an option: "))
				print()	
						
				if callSettings == 1: 
					print("Automatic redial")

				if callSettings == 2: 
					print("Speed dialling")
						 
				if callSettings == 3: 
					print("Call waiting options")
				 
				if callSettings == 4: 
					print("Own number sending")
						 
				if callSettings == 5: 
					print("Phone line in use")
						 
				if callSettings == 6: 
					print("Automatic answer")				 

			case 2:
				print("1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Lights\n6. Confirm SIM service actions")
				print()	
				phoneSettings = int(input("Select an option: "))
				print()	
						
				if phoneSettings == 1: 
					print("Language")
				 
				if phoneSettings == 2: 
					print("Cell info display")
					 
				if phoneSettings == 3: 
					print("Welcome note")
						 
				if phoneSettings == 4: 
					print("Network selection")
						 
				if phoneSettings == 5: 
					print("Lights")
						 
				if phoneSettings == 6: 
					print("Confirm SIM service actions")					 	
			
			case 3:
				print("1. PIN code request\n2. Call barring service\n3. Fixed dialling\n4. Closed user group\n5. Phone security\n6. Change access codes")
				print()	
				securitySettings = int(input("Select an option: "))
				print()	
						
				if securitySettings == 1: 
					print("PIN code request")
						 
				if securitySettings == 2: 
					print("Call barring service")
						 
				if securitySettings == 3: 
					print("Fixed dialling")
						 
				if securitySettings == 4: 
					print("Closed user group")
						 
				if securitySettings == 5: 
					print("Phone security")
						 
				if securitySettings == 6: 
					print("Change access codes")
						 
			case 4:
				print("Restore factory settings")
			

	case 7:
		print("Call divert")
	case 8:
		print("Games")		
	case 9:
		print("Calculator")
	case 10:
		print("Reminders")
	case 11:
		print("1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time")
		print()	
		clockMenu = int(input("Select an option: "))
		print()	

		match clockMenu: 
			case 1:
				print("Alarm clock")
			case 2:
				print("%Clock settings")
			case 3:
				print("Date settings")
			case 4:
				print("Stopwatch")
			case 5:
				print("Countdown timer")
			case 6:
				print("Auto update of date and time")
					 
	case 12:
		print("Profiles")
	case 13:
		print("SIM services")
			 
	 		




