def banner() -> str:
    my_banner = """
        _  __                        
  _ __ (_)/ _| __ _ ___________ _ __ 
 | '_ \| | |_ / _` |_  /_  / _ \ '__|
 | | | | |  _| (_| |/ / / /  __/ |   
 |_| |_|_|_|  \__,_/___/___\___|_|   
                       # Version: 1.0                                     
    """
    return my_banner


def loading(stage: int, full: int) -> str:
    count_tube = int(stage / full * 10)
    count_points = 10 - count_tube
    loading_string = "[" + ("|" * count_tube) + ("." * count_points) + "]"
    return loading_string
