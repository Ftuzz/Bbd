banner_with_menu = """
                                                                                         
                                                                                         
___       ______    ,6P         ________                                                 
`MMb     dMM`MM'  6MM'          `MMMMMMMb.                  68b                          
 MMM.   ,PMM MM  6M'             MM    `Mb                  Y89                    /      
 M`Mb   d'MM MM 6M ____          MM     MM ___  __   _____  ___   ____     ____   /M     
 M YM. ,P MM MM MMMMMMMb         MM     MM `MM 6MM  6MMMMMb `MM  6MMMMb   6MMMMb./MMMMM  
 M `Mb d' MM MM MM'   `Mb        MM    .M9  MM69 " 6M'   `Mb MM 6M'  `Mb 6M'   Mb MM     
 M  YM.P  MM MM MM     MM        MMMMMMM9'  MM'    MM     MM MM MM    MM MM    `' MM     
 M  `Mb'  MM MM MM     MM        MM         MM     MM     MM MM MMMMMMMM MM       MM     
 M   YP   MM MM MM     MM        MM         MM     MM     MM MM MM       MM       MM     
 M   `'   MM MM YM.   ,M9        MM         MM     YM.   ,M9 MM YM    d9 YM.   d9 YM.  , 
_M_      _MM_MM_ YMMMMM9        _MM_       _MM_     YMMMMM9  MM  YMMMM9   YMMMM9   YMMM9 
                                                             MM                          
                                                         (8) M9                          
                                                          YMM9                           

┌─────────────────────────────────────────────────┐                                                 
│ 1. violence                                     │
│ 2. child abuse                                  │
│ 3. identity substitution                        │
│ 4. copyright                                    │
│ 5. irrelevant geogroup                          │
│ 6. spam                                         │
│ 7. other                                        │
└─────────────────────────────────────────────────┘
"""

def gradient_text(text):
    gradient_output = []
    for i in range(len(text)):
        ratio = i / len(text)
        color = (
            int(0 * (1 - ratio) + 0 * ratio),
            int(0 * (1 - ratio) + 0 * ratio),
            int(255 * (1 - ratio) + 128 * ratio),  
        )
        gradient_output.append(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text[i]}")
    return ''.join(gradient_output) + "\033[0m"

def print_banner():
    gradient_ban = gradient_text(banner_with_menu)
    print(gradient_ban)


print_banner()
