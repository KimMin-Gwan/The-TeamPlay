def temp_gui(login_flag):
    menu = 0
    trigger = 'n'
    check = False

    print('-------------   choose the menu   -------------------')
    #로그인 여부 확인
    print('1. Explore Posts')
    print('2. Explore Teams')
    print('3. Explore Collabo Posts')
    if login_flag is False:
        print('3. sign in')
        print('9. Exit')
    else:
        print('3. See Profile')
        print('4. Make Team')
        print('5. Find Professor')
        print('9. Exit')
    print('Selected Menu : ', end='')
    input(menu)
    print('you choose {} ? (Y/N) : '.format(menu), end='')
    input(trigger)
    if trigger is 'N' or trigger is 'n':
        check = True
    
    return check, menu
