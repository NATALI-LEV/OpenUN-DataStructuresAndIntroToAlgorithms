class InputInts:
    
    def read_integers(file_path):
        """
        Read integers from a file and return a list of integers.

        Parameters:
        - file_path (str): Path to the file containing integers.

        Returns:
        - list of integers: List of integers read from the file.
        """
        integers = []

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    integers.append(int(line.strip()))
        except FileNotFoundError:
            print("error! File Is Not Found!")

        return integers

    
    def get_intput():
        """
        Read integers from a file and return a list of integers.

        Parameters:
        - file_path (str): Path to the file containing integers.

        Returns:
        - list of integers: List of integers read from the file.
        """
        while True:
            try:
                return int(input("Enter your d value: "))
            except ValueError:
                print("Please enter a valid integer value. Lets Try again.")
