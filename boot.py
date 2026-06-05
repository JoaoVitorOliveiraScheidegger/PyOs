


def start_machine():
    print("Ligando PC")
    from kernel import Kernel
    with Kernel() as kernel:

        kernel.start_system()



if __name__ == "__main__":
    start_machine()