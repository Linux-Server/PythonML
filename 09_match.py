current  = 150

match current:
    case 100 | 150:
        print("Hello 100")
    case 200:
        print("Hello 200")
    case _ :
        print("Go nothing")